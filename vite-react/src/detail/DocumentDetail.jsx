import GoodsReceivedNoteDetail from "./GRN/GoodsReceivedNoteDetail.jsx";
import GoodsDeliveryNoteDetail from "./GDN/GoodsDeliveryNoteDetail.jsx";
import OrderDetail from "./Order/OrderDetail.jsx";
import InvoiceDetail from "./Invoice/InvoiceDetail.jsx";
import TaxInvoiceDetail from "./TaxInvoice/TaxInvoiceDetail.jsx";

function DocumentDetail({document, documentType, onBack, onClose, onToCreateOn }){
    if (!document) return null;

    let DetailComponent;
    switch (documentType) {
        case 'taxInvoice':
            DetailComponent = TaxInvoiceDetail;
            break;
        case 'order':
            DetailComponent = OrderDetail;
            break;
        case 'invoice':
            DetailComponent = InvoiceDetail;
            break;
        case 'goodsReceived':
            DetailComponent = GoodsReceivedNoteDetail;
            break;
        case 'goodsDelivery':
            DetailComponent = GoodsDeliveryNoteDetail;
            break;
        default:
            DetailComponent = OrderDetail;
    }

    return (
        <div>
            <DetailComponent document={document} onBack={onBack} onClose={onClose} onToCreateOn={onToCreateOn}/>
        </div>
    )
}

export default DocumentDetail;