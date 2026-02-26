import DocumentListNavigation from "./DocumentListNavigation.jsx";
import Header from "../Header.jsx";
import GoodsReceivedNoteListTable from "./GoodsReceivedNoteListTable.jsx";
import GoodsDeliveryNoteListTable from "./GoodsDeliveryNoteListTable.jsx";
import TaxInvoiceListTable from "./TaxInvoiceListTable.jsx";
import OrderListTable from "./OrderListTable.jsx";
import InvoiceListTable from "./InvoiceListTable.jsx";

const elements = [
    {
        id: 1,
        date: '2026-02-20',
        number: 'TN-000001',
        typeOperation: 'Продаж',
        amount: 1500.50,
        curency: 'UAH',
        countparty: 'ТОВ "Альфа"',
        warhouse: 'Основний склад',
        organization: 'ПП "Моя Компанія"'
    },
    {
        id: 2,
        date: '2026-02-21',
        number: 'TN-000002',
        typeOperation: 'Продаж',
        amount: 2300.00,
        curency: 'UAH',
        countparty: 'ФОП Петренко',
        warhouse: 'Склад №2',
        organization: 'ПП "Моя Компанія"'
    },
    {
        id: 3,
        date: '2026-02-22',
        number: 'TN-000003',
        typeOperation: 'Повернення',
        amount: 450.75,
        curency: 'UAH',
        countparty: 'ТОВ "Бета"',
        warhouse: 'Основний склад',
        organization: 'ПП "Моя Компанія"'
    }
]

function DocumentList({ onRowDoubleClick, onForward, documentType, onBack, onClose }) {
    let TableComponent;
    let title = "";

    switch (documentType) {
        case 'taxInvoice':
            TableComponent = TaxInvoiceListTable;
            title = "Податкова накладна";
            break;
        case 'order':
            TableComponent = OrderListTable;
            title = "Замовлення покупця";
            break;
        case 'invoice':
            TableComponent = InvoiceListTable;
            title = "Рахунок на оплату";
            break;
        case 'goodsReceived':
            TableComponent = GoodsReceivedNoteListTable;
            title = "Надходження товарів та послуг";
            break;
        case 'goodsDelivery':
            TableComponent = GoodsDeliveryNoteListTable;
            title = "Видаткова накладна";
            break;
        default:
            TableComponent = OrderListTable;
            title = "Документи";
    }

    return (
        <div className="d-flex flex-column h-100">
            <Header name={title} onForward={onForward} onBack={onBack} onClose={onClose}/>
            <DocumentListNavigation />
            <TableComponent elements={elements} onRowDoubleClick={onRowDoubleClick} />
        </div>
    )
}

export default DocumentList