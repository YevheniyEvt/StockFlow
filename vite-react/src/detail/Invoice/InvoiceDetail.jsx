import { useState, useEffect } from 'react';
import InvoiceNavigation from './InvoiceNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function InvoiceDetail({ document, onBack, onClose, onToCreateOn, counterparts, organizations, contracts, warehouses, operationTypes}){
    const [currentDocument, setCurrentDocument] = useState(document);

    useEffect(() => {
        setCurrentDocument(document);
    }, [document]);

    const handleDocumentUpdate = (updatedDocument) => {
        setCurrentDocument(updatedDocument);
    };

    return (
        <>
            <Header name="Рахунок фактура" document={currentDocument} onBack={onBack} onClose={onClose}/>
            <InvoiceNavigation
                document={currentDocument}
                onBack={onBack}
                onToCreateOn={onToCreateOn}
                counterparts={counterparts}
                organizations={organizations}
                contracts={contracts}
                warehouses={warehouses}
                operationTypes={operationTypes}
                onUpdate={handleDocumentUpdate}
            />
            <DocumentDetailTab document={currentDocument} canEdit={true} onUpdate={handleDocumentUpdate} documentType="invoice" />
        </>
    )
}

export default InvoiceDetail;