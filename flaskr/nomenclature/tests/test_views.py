from flaskr.database import db
from flaskr.directory.models import Organization, UnitsOfMeasurement
from flaskr.nomenclature.models import Product, Service

def setup_org_and_uom(app):
    with app.app_context():
        org = Organization(name="Test Org", additional_data="Data")
        db.session.add(org)
        db.session.commit()
        org_id = org.id
        
        uom = UnitsOfMeasurement(organization_id=org_id, name="pcs", additional_data="units")
        db.session.add(uom)
        db.session.commit()
        uom_id = uom.id
    return org_id, uom_id

def test_product_create(client, app):
    org_id, uom_id = setup_org_and_uom(app)

    response = client.post("/nomenclature/products/create", json={
        "name": "Widget",
        "organization_id": org_id,
        "units_of_measurement_id": uom_id,
        "article": 123,
        "selling_price": "19.99"
    })
    assert response.status_code == 201
    assert response.json["name"] == "Widget"
    assert float(response.json["selling_price"]) == 19.99

def test_product_list(client, app):
    org_id, uom_id = setup_org_and_uom(app)
    with app.app_context():
        prod = Product(
            name="Gadget", 
            organization_id=org_id, 
            units_of_measurement_id=uom_id, 
            article=456, 
            selling_price=29.99
        )
        db.session.add(prod)
        db.session.commit()

    response = client.get("/nomenclature/products", json={"organization_id": org_id})
    assert response.status_code == 200
    assert any(item["name"] == "Gadget" for item in response.json)

def test_service_views(client, app):
    org_id, uom_id = setup_org_and_uom(app)
    # Create
    response = client.post("/nomenclature/services/create", json={
        "name": "Repair",
        "organization_id": org_id,
        "units_of_measurement_id": uom_id,
        "article": 789,
        "selling_price": "50.00"
    })
    assert response.status_code == 201
    service_id = response.json["id"]

    # List
    response = client.get("/nomenclature/services", json={"organization_id": org_id})
    assert response.status_code == 200
    assert any(item["name"] == "Repair" for item in response.json)

    # Detail
    response = client.get(f"/nomenclature/services/{service_id}")
    assert response.status_code == 200
    assert response.json["name"] == "Repair"
