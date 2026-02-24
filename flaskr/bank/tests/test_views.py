import pytest
from flaskr.database import db
from flaskr.directory.models import Organization, Counterparty
from flaskr.bank.models import Currency, BankAccountCompany, BankAccountCounterparty

def setup_org_and_currency(app):
    with app.app_context():
        org = Organization(name="Test Org", additional_data="Some data")
        db.session.add(org)
        db.session.commit()
        org_id = org.id

        curr = Currency(organization_id=org_id, name="USD")
        db.session.add(curr)
        db.session.commit()
        curr_id = curr.id
    return org_id, curr_id

def test_currency_create(client, app):
    org_id, _ = setup_org_and_currency(app)

    response = client.post("/bank/currency/create", json={
        "organization_id": org_id,
        "name": "USD_NEW"
    })
    assert response.status_code == 201
    assert response.json["name"] == "USD_NEW"
    assert response.json["organization_id"] == org_id

def test_currency_list(client, app):
    org_id, _ = setup_org_and_currency(app)

    response = client.get("/bank/currency", json={"organization_id": org_id})
    assert response.status_code == 200
    assert any(item["name"] == "USD" for item in response.json)

def test_currency_detail(client, app):
    _, curr_id = setup_org_and_currency(app)

    response = client.get(f"/bank/currency/{curr_id}")
    assert response.status_code == 200
    assert response.json["name"] == "USD"

def test_bank_account_company_create(client, app):
    org_id, curr_id = setup_org_and_currency(app)

    payload = {
        "organization_id": org_id,
        "name": "Main Account",
        "checking_account": "123456789",
        "mfi": 123456,
        "edrpou": 98765432,
        "bank": "Big Bank",
        "currency_id": curr_id
    }
    response = client.post("/bank/bank_account_company/create", json=payload)
    assert response.status_code == 201
    assert response.json["name"] == "Main Account"

def test_bank_account_company_list(client, app):
    org_id, curr_id = setup_org_and_currency(app)
    with app.app_context():
        acc = BankAccountCompany(
            organization_id=org_id,
            name="List Account",
            checking_account="987654321",
            mfi=654321,
            edrpou=23456789,
            bank="Small Bank",
            currency_id=curr_id
        )
        db.session.add(acc)
        db.session.commit()

    response = client.get("/bank/bank_account_company", json={"organization_id": org_id})
    assert response.status_code == 200
    assert any(item["name"] == "List Account" for item in response.json)

def test_bank_account_counterparty_create(client, app):
    org_id, curr_id = setup_org_and_currency(app)
    with app.app_context():
        cp = Counterparty(organization_id=org_id, name="CP1", additional_data="CP Data")
        db.session.add(cp)
        db.session.commit()
        cp_id = cp.id

    payload = {
        "counterparty_id": cp_id,
        "name": "CP Account",
        "checking_account": "111222333",
        "mfi": 111111,
        "edrpou": 22222222,
        "bank": "CP Bank",
        "currency_id": curr_id
    }
    response = client.post("/bank/bank_account_counterparty/create", json=payload)
    assert response.status_code == 201
    assert response.json["name"] == "CP Account"

def test_bank_account_counterparty_list(client, app):
    org_id, curr_id = setup_org_and_currency(app)
    with app.app_context():
        cp = Counterparty(organization_id=org_id, name="CP2", additional_data="CP Data")
        db.session.add(cp)
        db.session.flush()
        cp_id = cp.id
        
        acc = BankAccountCounterparty(
            counterparty_id=cp_id,
            name="CP List Account",
            checking_account="444555666",
            mfi=444444,
            edrpou=55555555,
            bank="CP Bank 2",
            currency_id=curr_id
        )
        db.session.add(acc)
        db.session.commit()

    response = client.get("/bank/bank_account_counterparty", json={"counterparty_id": cp_id})
    assert response.status_code == 200
    assert any(item["name"] == "CP List Account" for item in response.json)
