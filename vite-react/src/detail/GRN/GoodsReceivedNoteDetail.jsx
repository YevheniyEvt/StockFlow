import GoodsReceivedNoteNavigation from './GoodsReceivedNoteNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function GoodsReceivedNoteDetail({ document, onBack, onClose, onToCreateOn, counterparts, organizations, contracts, warehouses, operationTypes }){
    const date = new Date();
    const order = document || {number: "ДО0000000022", date: date.toLocaleString()};
    return (
        <>
            <Header name="Прибуткова накладна" document={order} onBack={onBack} onClose={onClose}/>
            <GoodsReceivedNoteNavigation
                document={document}
                onBack={onBack}
                onToCreateOn={onToCreateOn}
                counterparts={counterparts}
                organizations={organizations}
                contracts={contracts}
                warehouses={warehouses}
                operationTypes={operationTypes}
            />
            <DocumentDetailTab document={document} canEdit={true} />
        </>
    )
}

export default GoodsReceivedNoteDetail;