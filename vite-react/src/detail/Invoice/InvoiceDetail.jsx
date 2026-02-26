import InvoiceNavigation from './InvoiceNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function InvoiceDetail({ document, onBack, onClose, onToCreateOn }){
    const date = new Date();
    const order = document || {number: "ДО0000000022", date: date.toLocaleString()};
    return (
        <>
            <Header name="Рахунок фактура" document={order} onBack={onBack} onClose={onClose}/>
            <InvoiceNavigation onBack={onBack} onToCreateOn={onToCreateOn} />
            <DocumentDetailTab canEdit={true} />
        </>
    )
}

export default InvoiceDetail;