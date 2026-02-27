import { useState, useEffect } from 'react';
import GoodsDeliveryNoteNavigation from './GoodsDeliveryNoteNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function GoodsDeliveryNoteDetail({ document, onBack, onClose, onToCreateOn, counterparts, organizations, contracts, warehouses }){
    const [currentDocument, setCurrentDocument] = useState(document);

    useEffect(() => {
        setCurrentDocument(document);
    }, [document]);

    const handleDocumentUpdate = (updatedDocument) => {
        setCurrentDocument(updatedDocument);
    };

    return (
        <>
            <Header name="Видаткова накладна" document={currentDocument} onBack={onBack} onClose={onClose}/>
            <GoodsDeliveryNoteNavigation
                document={currentDocument}
                onBack={onBack}
                onToCreateOn={onToCreateOn}
                counterparts={counterparts}
                organizations={organizations}
                contracts={contracts}
                warehouses={warehouses}
                onUpdate={handleDocumentUpdate}
            />
            <DocumentDetailTab document={currentDocument} canEdit={true}/>
        </>
    )
}

export default GoodsDeliveryNoteDetail;