from flaskr.database import db
from flaskr.directory.models import (
    Organization, Counterparty, Warehouse, OperationType, UnitsOfMeasurement, Contract
)

def setup_org(app):
    with app.app_context():
        org = Organization(name="Test Org", additional_data="Some data")
        db.session.add(org)
        db.session.commit()
        org_id = org.id
    return org_id

def test_organization_create(client, app):
    response = client.post("/directory/organizations/create", json={
        "name": "New Org",
        "address": "123 Main St",
        "additional_data": "Some data"
    })
    assert response.status_code == 201
    assert response.json["name"] == "New Org"
    assert "id" in response.json

def test_organization_list(client, app):
    setup_org(app)
    response = client.get("/directory/organizations", json={})
    assert response.status_code == 200
    assert len(response.json) >= 1

def test_organization_detail(client, app):
    org_id = setup_org(app)
    response = client.get(f"/directory/organizations/{org_id}")
    assert response.status_code == 200
    assert response.json["name"] == "Test Org"

def test_counterparty_views(client, app):
    org_id = setup_org(app)
    # Create
    response = client.post("/directory/counterparts/create", json={
        "organization_id": org_id,
        "name": "CP1",
        "address": "CP Address",
        "additional_data": "CP Data"
    })
    assert response.status_code == 201
    cp_id = response.json["id"]

    # List
    response = client.get("/directory/counterparts", json={"organization_id": org_id})
    assert response.status_code == 200
    assert any(item["name"] == "CP1" for item in response.json)

    # Detail
    response = client.get(f"/directory/counterparts/{cp_id}")
    assert response.status_code == 200
    assert response.json["name"] == "CP1"

def test_warehouse_views(client, app):
    org_id = setup_org(app)
    # Create
    response = client.post("/directory/warehouses/create", json={
        "organization_id": org_id,
        "name": "WH1",
        "address": "WH Address",
        "additional_data": "WH Data"
    })
    assert response.status_code == 201
    wh_id = response.json["id"]

    # List
    response = client.get("/directory/warehouses", json={"organization_id": org_id})
    assert response.status_code == 200
    assert any(item["name"] == "WH1" for item in response.json)

def test_operation_type_views(client, app):
    org_id = setup_org(app)
    # Create
    response = client.post("/directory/operation_types/create", json={
        "organization_id": org_id,
        "name": "OP1",
        "additional_data": "OP Data"
    })
    assert response.status_code == 201
    op_id = response.json["id"]

    # List
    response = client.get("/directory/operation_types", json={"organization_id": org_id})
    assert response.status_code == 200
    assert any(item["name"] == "OP1" for item in response.json)

def test_uom_views(client, app):
    org_id = setup_org(app)
    # Create
    response = client.post("/directory/units_of_measurements/create", json={
        "organization_id": org_id,
        "name": "pcs",
        "additional_data": "pieces"
    })
    assert response.status_code == 201
    uom_id = response.json["id"]

    # List
    response = client.get("/directory/units_of_measurements", json={"organization_id": org_id})
    assert response.status_code == 200
    assert any(item["name"] == "pcs" for item in response.json)

def test_contract_views(client, app):
    org_id = setup_org(app)
    # Create
    response = client.post("/directory/contracts/create", json={
        "organization_id": org_id,
        "name": "Contract 1",
        "additional_data": "Data"
    })
    assert response.status_code == 201
    contract_id = response.json["id"]

    # List
    response = client.get("/directory/contracts", json={"organization_id": org_id})
    assert response.status_code == 200
    assert any(item["name"] == "Contract 1" for item in response.json)
