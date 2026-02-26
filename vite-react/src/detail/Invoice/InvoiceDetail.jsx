import InvoiceNavigation from './InvoiceNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function InvoiceDetail({ document, onBack, onClose, onToCreateOn, counterparts, organizations, contracts, warehouses}){
    return (
        <>
            <Header name="Рахунок фактура" document={document} onBack={onBack} onClose={onClose}/>
            <InvoiceNavigation
                document={document}
                onBack={onBack}
                onToCreateOn={onToCreateOn}
                counterparts={counterparts}
                organizations={organizations}
                contracts={contracts}
                warehouses={warehouses}
            />
            <DocumentDetailTab document={document} canEdit={true} />
        </>
    )
}

export default InvoiceDetail;