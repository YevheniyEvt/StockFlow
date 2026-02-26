import OrderNavigation from './OrderNavigation.jsx';
import DocumentDetailTab from "../DocumentDetailTab.jsx";
import Header from "../../Header.jsx"

function OrderDetail({document, onBack, onClose, onToCreateOn, counterparts, organizations }){
    return (
        <>
            <Header name="Замовлення" document={document} onBack={onBack} onClose={onClose}/>
            <OrderNavigation
                document={document}
                onToCreateOn={onToCreateOn}
                onBack={onBack}
                counterparts={counterparts}
                organizations={organizations}
            />
            <DocumentDetailTab document={document} canEdit={true} />
        </>
    )
}

export default OrderDetail;