import GoodsReceivedNoteNavigation from './GoodsReceivedNoteNavigation.jsx';
import DocumentDetailTab from "./DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function GoodsReceivedNoteDetail({ document, onBack, onClose, onToCreateOn }){
    const date = new Date();
    const order = document || {number: "ДО0000000022", date: date.toLocaleString()};
    return (
        <>
            <Header name="Прибуткова накладна" document={order} onBack={onBack} onClose={onClose}/>
            <GoodsReceivedNoteNavigation onBack={onBack} onToCreateOn={onToCreateOn} />
            <DocumentDetailTab />
        </>
    )
}

export default GoodsReceivedNoteDetail;