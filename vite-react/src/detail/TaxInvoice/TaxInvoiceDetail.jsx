import { useState, useEffect } from 'react';
import TaxInvoiceNavigation from './TaxInvoiceNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function TaxInvoiceDetail({ document, onBack, onClose, onToCreateOn, counterparts, organizations, contracts, warehouses, operationTypes }){
    const [currentDocument, setCurrentDocument] = useState(document);

    useEffect(() => {
        setCurrentDocument(document);
    }, [document]);

    const handleDocumentUpdate = (updatedDocument) => {
        setCurrentDocument(updatedDocument);
    };

    return (
        <>
            <Header name="Податкова накладна" document={currentDocument} onBack={onBack} onClose={onClose}/>
            <TaxInvoiceNavigation 
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
            <DocumentDetailTab document={currentDocument} canEdit={false}/>
        </>
    )
}

export default TaxInvoiceDetail;