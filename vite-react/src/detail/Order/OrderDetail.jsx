import OrderNavigation from './OrderNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function OrderDetail({document, onBack, onClose, onToCreateOn }){
    const date = new Date();
    const order = document || {number: "ДО0000000020", date: date.toLocaleString()};
    return (
        <>
            <Header name="Замовлення" document={order} onBack={onBack} onClose={onClose}/>
            <OrderNavigation onToCreateOn={onToCreateOn} onBack={onBack} />
            <DocumentDetailTab canEdit={true} />
        </>
    )
}

export default OrderDetail;