from datetime import datetime, timedelta
from flaskr.database import db
from flaskr.directory.models import Organization, Counterparty, OperationType, Warehouse, Contract, UnitsOfMeasurement
from flaskr.nomenclature.models import Product
from flaskr.documents.models import Order, Invoice, GoodsReceivedNote, GoodsDeliveryNote, TaxInvoice, DocumentItem
from flaskr.documents.models.document_enum import OrderStatus, InvoiceStatus

def setup_all_entities(app):
    with app.app_context():
        org = Organization(name="Org", address="Addr", additional_data="Data")
        db.session.add(org)
        db.session.flush()

        cp = Counterparty(organization_id=org.id, name="CP", address="CP Addr", additional_data="CP Data")
        op = OperationType(organization_id=org.id, name="Op", additional_data="Op Data")
        wh = Warehouse(organization_id=org.id, name="Wh", address="Wh Addr", additional_data="Wh Data")
        ct = Contract(organization_id=org.id, name="Ct", additional_data="Ct Data")
        uom = UnitsOfMeasurement(organization_id=org.id, name="pcs", additional_data="units")
        
        db.session.add_all([cp, op, wh, ct, uom])
        db.session.flush()

        prod = Product(
            name="Prod", organization_id=org.id, units_of_measurement_id=uom.id,
            article=1, selling_price=10.0
        )
        db.session.add(prod)
        db.session.commit()

        return {
            "org_id": org.id,
            "cp_id": cp.id,
            "op_id": op.id,
            "wh_id": wh.id,
            "ct_id": ct.id,
            "uom_id": uom.id,
            "prod_id": prod.id
        }

def test_order_views(client, app):
    entities = setup_all_entities(app)
    # Create
    response = client.post("/documents/orders/create", json={
        "organization_id": entities["org_id"],
        "counterparty_id": entities["cp_id"],
        # "operation_type_id": entities["op_id"],
        # "warehouse_id": entities["wh_id"],
        # "contract_id": entities["ct_id"],
        # "amount": 0
    })
    assert response.status_code == 201
    order_id = response.json["id"]

    # List
    response = client.get("/documents/orders", json={"organization_id": entities["org_id"]})
    assert response.status_code == 200
    assert any(item["id"] == order_id for item in response.json)

    # Update Status
    response = client.patch(f"/documents/orders/{order_id}/update-status", json={"status": "confirmed_by_client"})
    assert response.status_code == 200
    assert response.json["status"] == "confirmed_by_client"

def test_invoice_views(client, app):
    entities = setup_all_entities(app)
    with app.app_context():
        order = Order(
            organization_id=entities["org_id"], counterparty_id=entities["cp_id"],
            operation_type_id=entities["op_id"], warehouse_id=entities["wh_id"],
            contract_id=entities["ct_id"], amount=0
        )
        db.session.add(order)
        db.session.commit()
        order_id = order.id

    # Create
    due_date = (datetime.now() + timedelta(days=7)).isoformat()
    response = client.post("/documents/invoices/create", json={
        "organization_id": entities["org_id"],
        "counterparty_id": entities["cp_id"],
        "order_id": order_id,
        # "operation_type_id": entities["op_id"],
        # "warehouse_id": entities["wh_id"],
        # "contract_id": entities["ct_id"],
        # "amount": 0,
        # "payment_final_date": due_date
    })
    assert response.status_code == 201
    invoice_id = response.json["id"]

    # List
    response = client.get("/documents/invoices", json={"organization_id": entities["org_id"]})
    assert response.status_code == 200
    assert any(item["id"] == invoice_id for item in response.json)

def test_goods_received_note_views(client, app):
    entities = setup_all_entities(app)
    # Create
    response = client.post("/documents/goods_received_notes/create", json={
        "organization_id": entities["org_id"],
        "counterparty_id": entities["cp_id"],
        # "operation_type_id": entities["op_id"],
        # "warehouse_id": entities["wh_id"],
        # "contract_id": entities["ct_id"],
        # "amount": 0
    })
    assert response.status_code == 201
    grn_id = response.json["id"]

    # List
    response = client.get("/documents/goods_received_notes", json={"organization_id": entities["org_id"]})
    assert response.status_code == 200
    assert any(item["id"] == grn_id for item in response.json)

def test_held_goods_received_note(client, app):
    entities = setup_all_entities(app)
    # Create GRN
    response = client.post("/documents/goods_received_notes/create", json={
        "organization_id": entities["org_id"],
        "counterparty_id": entities["cp_id"],
    })
    grn_id = response.json["id"]
    
    # Update GRN to add warehouse_id (required for movements)
    client.patch(f"/documents/goods_received_notes/{grn_id}/update", json={
        "warehouse_id": entities["wh_id"]
    })

    # Add item
    client.post("/documents/document_item/create", json={
        "document_id": grn_id,
        "product_id": entities["prod_id"],
        "quantity": 10
    })

    # Held GRN
    response = client.post(f"/documents/goods_received_notes/{grn_id}/held", json={})
    assert response.status_code == 200
    assert response.json["status"] == "held"
    
    # Verify movement and stock
    from flaskr.accounting.models import ProductMovement, ProductStockLot
    with app.app_context():
        movement = db.session.scalar(db.select(ProductMovement).where(ProductMovement.document_id == grn_id))
        assert movement is not None
        assert float(movement.quantity) == 10.0
        
        lot = db.session.scalar(db.select(ProductStockLot).where(ProductStockLot.product_id == entities["prod_id"]))
        assert lot is not None
        assert float(lot.quantity_remaining) == 10.0

def test_goods_delivery_note_views(client, app):
    entities = setup_all_entities(app)
    with app.app_context():
        order = Order(
            organization_id=entities["org_id"], counterparty_id=entities["cp_id"],
            operation_type_id=entities["op_id"], warehouse_id=entities["wh_id"],
            contract_id=entities["ct_id"], amount=0
        )
        db.session.add(order)
        db.session.flush()
        invoice = Invoice(
            organization_id=entities["org_id"], counterparty_id=entities["cp_id"],
            operation_type_id=entities["op_id"], warehouse_id=entities["wh_id"],
            contract_id=entities["ct_id"], amount=0, order_id=order.id,
            payment_final_date=datetime.now() + timedelta(days=1)
        )
        db.session.add(invoice)
        db.session.commit()
        invoice_id = invoice.id

    # Create
    response = client.post("/documents/goods_delivery_notes/create", json={
        "organization_id": entities["org_id"],
        "counterparty_id": entities["cp_id"],
        # "operation_type_id": entities["op_id"],
        # "warehouse_id": entities["wh_id"],
        # "contract_id": entities["ct_id"],
        # "amount": 0,
        "invoice_id": invoice_id
    })
    assert response.status_code == 201
    gdn_id = response.json["id"]

    # List
    response = client.get("/documents/goods_delivery_notes", json={"organization_id": entities["org_id"]})
    assert response.status_code == 200
    assert any(item["id"] == gdn_id for item in response.json)

def test_goods_delivery_note_change_status(client, app):
    entities = setup_all_entities(app)
    # 1. Provide stock via GRN
    grn_res = client.post("/documents/goods_received_notes/create", json={
        "organization_id": entities["org_id"], "counterparty_id": entities["cp_id"]
    })
    grn_id = grn_res.json["id"]
    client.patch(f"/documents/goods_received_notes/{grn_id}/update", json={
        "warehouse_id": entities["wh_id"]
    })
    client.post("/documents/document_item/create", json={
        "document_id": grn_id, "product_id": entities["prod_id"], "quantity": 20
    })
    client.post(f"/documents/goods_received_notes/{grn_id}/held", json={})

    # 2. Create Order -> Invoice -> GDN
    order_res = client.post("/documents/orders/create", json={
        "organization_id": entities["org_id"], "counterparty_id": entities["cp_id"]
    })
    order_id = order_res.json["id"]
    client.patch(f"/documents/orders/{order_id}/update", json={
        "warehouse_id": entities["wh_id"]
    })
    client.post("/documents/document_item/create", json={
        "document_id": order_id, "product_id": entities["prod_id"], "quantity": 5
    })
    
    inv_res = client.post("/documents/invoices/create", json={
        "organization_id": entities["org_id"], "counterparty_id": entities["cp_id"], "order_id": order_id
    })
    invoice_id = inv_res.json["id"]
    
    gdn_res = client.post("/documents/goods_delivery_notes/create", json={
        "organization_id": entities["org_id"], "counterparty_id": entities["cp_id"], "invoice_id": invoice_id
    })
    gdn_id = gdn_res.json["id"]
    client.patch(f"/documents/goods_delivery_notes/{gdn_id}/update", json={"warehouse_id": entities["wh_id"]})

    # 3. Change status to HELD (triggers selling movement)
    response = client.patch(f"/documents/goods_delivery_notes/{gdn_id}/update-status", json={"status": "held"})
    assert response.status_code == 200
    assert response.json["status"] == "held"

    # 4. Verify stock
    from flaskr.accounting.models import ProductStockLot
    with app.app_context():
        lot = db.session.scalar(db.select(ProductStockLot).where(ProductStockLot.product_id == entities["prod_id"]))
        # Original 20, sold 5 -> remaining 15
        assert float(lot.quantity_remaining) == 15.0

def test_tax_invoice_views(client, app):
    entities = setup_all_entities(app)
    with app.app_context():
        order = Order(
            organization_id=entities["org_id"], counterparty_id=entities["cp_id"],
            operation_type_id=entities["op_id"], warehouse_id=entities["wh_id"],
            contract_id=entities["ct_id"], amount=0
        )
        db.session.add(order)
        db.session.flush()
        invoice = Invoice(
            organization_id=entities["org_id"], counterparty_id=entities["cp_id"],
            operation_type_id=entities["op_id"], warehouse_id=entities["wh_id"],
            contract_id=entities["ct_id"], amount=0, order_id=order.id,
            payment_final_date=datetime.now() + timedelta(days=1)
        )
        db.session.add(invoice)
        db.session.flush()
        gdn = GoodsDeliveryNote(
            organization_id=entities["org_id"], counterparty_id=entities["cp_id"],
            operation_type_id=entities["op_id"], warehouse_id=entities["wh_id"],
            contract_id=entities["ct_id"], amount=0, invoice_id=invoice.id
        )
        db.session.add(gdn)
        db.session.commit()
        gdn_id = gdn.id

    # Create
    response = client.post("/documents/tax_invoices/create", json={
        "organization_id": entities["org_id"],
        "counterparty_id": entities["cp_id"],
        # "operation_type_id": entities["op_id"],
        # "warehouse_id": entities["wh_id"],
        # "contract_id": entities["ct_id"],
        # "amount": 0,
        "goods_delivery_note_id": gdn_id
    })
    assert response.status_code == 201
    ti_id = response.json["id"]

    # List
    response = client.get("/documents/tax_invoices", json={"organization_id": entities["org_id"]})
    assert response.status_code == 200
    assert any(item["id"] == ti_id for item in response.json)

def test_document_item_create(client, app):
    entities = setup_all_entities(app)
    with app.app_context():
        order = Order(
            organization_id=entities["org_id"], counterparty_id=entities["cp_id"],
            operation_type_id=entities["op_id"], warehouse_id=entities["wh_id"],
            contract_id=entities["ct_id"], amount=0
        )
        db.session.add(order)
        db.session.commit()
        order_id = order.id

    response = client.post("/documents/document_item/create", json={
        "document_id": order_id,
        "product_id": entities["prod_id"],
        "quantity": 5
    })
    assert response.status_code == 201
    assert float(response.json["quantity"]) == 5.0
    assert float(response.json["amount"]) == 50.0
