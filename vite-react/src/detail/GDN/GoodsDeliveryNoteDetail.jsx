import GoodsDeliveryNoteNavigation from './GoodsDeliveryNoteNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function GoodsDeliveryNoteDetail({ document, onBack, onClose, onToCreateOn, counterparts, organizations, contracts, warehouses }){
    const date = new Date();
    const order = document || {number: "ДО0000000022", date: date.toLocaleString()};

    return (
        <>
            <Header name="Видаткова накладна" document={order} onBack={onBack} onClose={onClose}/>
            <GoodsDeliveryNoteNavigation
                document={document}
                onBack={onBack}
                onToCreateOn={onToCreateOn}
                counterparts={counterparts}
                organizations={organizations}
                contracts={contracts}
                warehouses={warehouses}
            />
            <DocumentDetailTab document={document} canEdit={true}/>
        </>
    )
}

export default GoodsDeliveryNoteDetail;