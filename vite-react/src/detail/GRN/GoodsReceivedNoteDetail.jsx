import { useState, useEffect } from 'react';
import GoodsReceivedNoteNavigation from './GoodsReceivedNoteNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function GoodsReceivedNoteDetail({ document, onBack, onClose, onToCreateOn, counterparts, organizations, contracts, warehouses, operationTypes }){
    const [currentDocument, setCurrentDocument] = useState(document);

    useEffect(() => {
        setCurrentDocument(document);
    }, [document]);

    const handleDocumentUpdate = (updatedDocument) => {
        setCurrentDocument(updatedDocument);
    };

    return (
        <>
            <Header name="Прибуткова накладна" document={currentDocument} onBack={onBack} onClose={onClose}/>
            <GoodsReceivedNoteNavigation
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
            <DocumentDetailTab document={currentDocument} canEdit={true} onUpdate={handleDocumentUpdate} documentType="goods_received_note" />
        </>
    )
}

export default GoodsReceivedNoteDetail;