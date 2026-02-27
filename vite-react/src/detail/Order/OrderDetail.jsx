import { useState, useEffect } from 'react';
import OrderNavigation from './OrderNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function OrderDetail({document, onBack, onClose, onToCreateOn, counterparts, organizations, contracts, warehouses, operationTypes }){
    const [currentDocument, setCurrentDocument] = useState(document);

    useEffect(() => {
        setCurrentDocument(document);
    }, [document]);

    const handleDocumentUpdate = (updatedDocument) => {
        setCurrentDocument(updatedDocument);
    };

    return (
        <>
            <Header name="Замовлення" document={currentDocument} onBack={onBack} onClose={onClose}/>
            <OrderNavigation
                document={currentDocument}
                onToCreateOn={onToCreateOn}
                onBack={onBack}
                counterparts={counterparts}
                organizations={organizations}
                contracts={contracts}
                warehouses={warehouses}
                operationTypes={operationTypes}
                onUpdate={handleDocumentUpdate}
            />
            <DocumentDetailTab document={currentDocument} canEdit={true} />
        </>
    )
}

export default OrderDetail;