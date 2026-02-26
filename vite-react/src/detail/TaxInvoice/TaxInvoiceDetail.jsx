import TaxInvoiceNavigation from './TaxInvoiceNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function TaxInvoiceDetail({ document, onBack, onClose, onToCreateOn }){
    const date = new Date();
    const order = document || {number: "ДО0000000022", date: date.toLocaleString()};
    return (
        <>
            <Header name="Податкова накладна" document={order} onBack={onBack} onClose={onClose}/>
            <TaxInvoiceNavigation onBack={onBack} onToCreateOn={onToCreateOn} />
            <DocumentDetailTab canEdit={false}/>
        </>
    )
}

export default TaxInvoiceDetail;