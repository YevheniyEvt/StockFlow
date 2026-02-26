from __future__ import annotations

import random
from decimal import Decimal

from flaskr import init_app
from flaskr.database import db

# directory models
from flaskr.directory.models import (
    Organization,
    Counterparty,
    Warehouse,
    OperationType,
    UnitsOfMeasurement,
    Contract,
)

# nomenclature models
from flaskr.nomenclature.models import Product, Service


def get_or_create(model, defaults=None, **kwargs):
    obj = model.query.filter_by(**kwargs).first()
    if obj:
        return obj, False
    params = dict(kwargs)
    if defaults:
        params.update(defaults)
    obj = model(**params)
    db.session.add(obj)
    return obj, True


def seed_directory():
    # Organizations
    org_data = [
        {"name": "ТОВ 'Промтехнології'", "address": "Київ, вул. Хрещатик, 1", "additional_data": "ЄДРПОУ-38472910"},
        {"name": "ПП 'Захід-Ресурс'", "address": "Львів, пл. Ринок, 10", "additional_data": "ЄДРПОУ-42109567"},
        {"name": "АТ 'ДніпроЕнерго'", "address": "Дніпро, пр. Яворницького, 50", "additional_data": "ЄДРПОУ-29384756"},
        {"name": "ФОП Ковальчук О.В.", "address": "Харків, вул. Сумська, 15", "additional_data": "ІПН-3029485761"},
        {"name": "ТОВ 'Одеська Логістика'", "address": "Одеса, вул. Дерибасівська, 5", "additional_data": "ЄДРПОУ-45123490"},
    ]
    organizations: list[Organization] = []
    for data in org_data:
        org, _ = get_or_create(
            Organization,
            name=data["name"],
            defaults={
                "address": data["address"],
                "additional_data": data["additional_data"],
            },
        )
        organizations.append(org)

    # Units of Measurement
    uom_names = ["шт", "кг", "м", "л", "послуга"]
    uoms: list[UnitsOfMeasurement] = []
    for i, name in enumerate(uom_names):
        uom, _ = get_or_create(
            UnitsOfMeasurement,
            organization_id=organizations[i % len(organizations)].id,
            name=name,
            defaults={"additional_data": f"код-{i+1}"},
        )
        uoms.append(uom)

    # Counterparties
    cp_data = [
        {"name": "ФОП Іваненко В.М.", "address": "Київ, вул. Васильківська, 20", "data": "ІПН-2938475610"},
        {"name": "ТОВ 'БудМастер'", "address": "Київ, вул. Будівельників, 5", "data": "ЄДРПОУ-39485761"},
        {"name": "ПАТ 'Київстар'", "address": "Київ, вул. Дегтярівська, 53", "data": "ЄДРПОУ-21673832"},
        {"name": "ТОВ 'Нова Пошта'", "address": "Полтава, вул. Європейська, 187", "data": "ЄДРПОУ-33547528"},
        {"name": "ФОП Петренко С.П.", "address": "Вінниця, вул. Соборна, 44", "data": "ІПН-3129485702"},
    ]
    counterparties: list[Counterparty] = []
    for i, data in enumerate(cp_data):
        cp, _ = get_or_create(
            Counterparty,
            organization_id=organizations[i % len(organizations)].id,
            name=data["name"],
            defaults={
                "additional_data": data["data"],
                "address": data["address"],
            },
        )
        counterparties.append(cp)

    # Warehouses
    wh_data = [
        {"name": "Центральний склад", "address": "Київ, вул. Промислова, 10"},
        {"name": "Склад №2 (Західний)", "address": "Львів, вул. Городоцька, 200"},
        {"name": "Склад готової продукції", "address": "Дніпро, вул. Робоча, 45"},
        {"name": "Магазин 'Електроніка'", "address": "Харків, вул. Свободи, 2"},
        {"name": "Регіональний хаб", "address": "Одеса, вул. Транспортна, 15"},
    ]
    warehouses: list[Warehouse] = []
    for i, data in enumerate(wh_data):
        wh, _ = get_or_create(
            Warehouse,
            organization_id=organizations[i % len(organizations)].id,
            name=data["name"],
            defaults={
                "additional_data": f"WH-{i+1}",
                "address": data["address"],
            },
        )
        warehouses.append(wh)

    # Operation Types
    op_names = ["Закупівля", "Продаж", "Списання", "Переміщення", "Повернення"]
    operation_types: list[OperationType] = []
    for i, name in enumerate(op_names):
        op, _ = get_or_create(
            OperationType,
            organization_id=organizations[i % len(organizations)].id,
            name=name,
            defaults={"additional_data": f"OP-CODE-{i+1}"},
        )
        operation_types.append(op)

    # Contracts
    contract_names = [
        "Договір купівлі-продажу №1/24",
        "Договір оренди №15",
        "Генеральна угода про партнерство",
        "Контракт на поставку №45",
        "Рамковий договір №99",
    ]
    contracts: list[Contract] = []
    for i, name in enumerate(contract_names):
        ct, _ = get_or_create(
            Contract,
            organization_id=organizations[i % len(organizations)].id,
            name=name,
            defaults={"additional_data": f"дата-{i+1}.01.2024"},
        )
        contracts.append(ct)

    return {
        "organizations": organizations,
        "uoms": uoms,
        "counterparties": counterparties,
        "warehouses": warehouses,
        "operation_types": operation_types,
        "contracts": contracts,
    }


def seed_nomenclature(organizations, uoms, counterparties):
    # 20 Products
    product_names = [
        "Ноутбук Dell Latitude 5540",
        "Монітор Samsung 27\"",
        "Клавіатура Logitech MX Keys",
        "Миша Apple Magic Mouse",
        "Принтер HP LaserJet Pro",
        "Wi-Fi Роутер MikroTik",
        "SSD накопичувач 1TB Samsung",
        "Оперативна пам'ять 16GB DDR4",
        "Блок живлення 750W",
        "Корпус Fractal Design",
        "Материнська плата ASUS ROG",
        "Процесор Intel Core i7",
        "Відеокарта NVIDIA RTX 4070",
        "Зовнішній диск 2TB WD",
        "USB-хаб Baseus",
        "Навушники Sony WH-1000XM5",
        "Веб-камера Logitech C920",
        "Джерело безперебійного живлення",
        "Мережевий кабель 5м (патч-корд)",
        "Сумка для ноутбука 15.6\"",
    ]
    for i, name in enumerate(product_names):
        org = organizations[i % len(organizations)]
        uom = uoms[0]  # шт
        cp = counterparties[i % len(counterparties)] if i % 3 != 0 else None
        get_or_create(
            Product,
            organization_id=org.id,
            units_of_measurement_id=uom.id,
            counterparty_id=cp.id if cp else None,
            article=1000 + i,
            defaults={
                "name": name,
                "multiplicity": Decimal("1.00"),
                "selling_price": Decimal(str(500 + (i * 100))),
                "minimum_stock": Decimal(str(5 + (i % 5))),
            },
        )

    # 5 Services
    service_names = [
        "Консультація ІТ-спеціаліста",
        "Встановлення ПЗ",
        "Налаштування мережі",
        "Ремонт обладнання",
        "Кур'єрська доставка",
    ]
    for i, name in enumerate(service_names):
        org = organizations[i % len(organizations)]
        uom = uoms[4]  # послуга
        cp = counterparties[i % len(counterparties)] if i % 2 == 0 else None
        get_or_create(
            Service,
            organization_id=org.id,
            units_of_measurement_id=uom.id,
            counterparty_id=cp.id if cp else None,
            article=2000 + i,
            defaults={
                "name": name,
                "multiplicity": Decimal("1.00"),
                "selling_price": Decimal(str(300 + (i * 200))),
            },
        )


def main():
    app = init_app()
    with app.app_context():
        # ensure tables exist (init_app already calls create_all)
        payload = seed_directory()
        seed_nomenclature(
            payload["organizations"], payload["uoms"], payload["counterparties"]
        )
        db.session.commit()
        print("Seed completed successfully.")


if __name__ == "__main__":
    main()
