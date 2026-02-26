import GoodsDeliveryNoteNavigation from './GoodsDeliveryNoteNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function GoodsDeliveryNoteDetail({ document, onBack, onClose, onToCreateOn }){
    const date = new Date();
    const order = document || {number: "ДО0000000022", date: date.toLocaleString()};
    return (
        <>
            <Header name="Видаткова накладна" document={order} onBack={onBack} onClose={onClose}/>
            <GoodsDeliveryNoteNavigation onBack={onBack} onToCreateOn={onToCreateOn} />
            <DocumentDetailTab canEdit={true}/>
        </>
    )
}

export default GoodsDeliveryNoteDetail;