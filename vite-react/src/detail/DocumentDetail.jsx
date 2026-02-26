import GoodsReceivedNoteDetail from "./GRN/GoodsReceivedNoteDetail.jsx";
import GoodsDeliveryNoteDetail from "./GDN/GoodsDeliveryNoteDetail.jsx";
import OrderDetail from "./Order/OrderDetail.jsx";
import InvoiceDetail from "./Invoice/InvoiceDetail.jsx";
import TaxInvoiceDetail from "./TaxInvoice/TaxInvoiceDetail.jsx";
import {useEffect, useState} from "react";
import axios from "axios";

function DocumentDetail({document, documentType, onBack, onClose, onToCreateOn }){

    const [counterparts, setCounterparts] = useState([]);
    const fetchCounterpartys = async () => {
        axios.get('/api/directory/counterparts', {
        })
          .then(response => {
            setCounterparts(response.data);
          })
          .catch(error => {
            console.error(error);
          });
    }

    const [organizations, setOrganizations] = useState([]);
    const fetchOrganizations = async () => {
        axios.get('/api/directory/organizations')
          .then(response => {
            setOrganizations(response.data);
          })
          .catch(error => {
            console.error(error);
          });
    }

    const [contracts, setContracts] = useState([]);
    const fetchContracts = async () => {
        axios.get('/api/directory/contracts')
          .then(response => {
            setContracts(response.data);
          })
          .catch(error => {
            console.error(error);
          });
    }

    const [warehouses, setWarehouses] = useState([]);
    const fetchWarehouses = async () => {
        axios.get('/api/directory/warehouses')
          .then(response => {
            setWarehouses(response.data);
          })
          .catch(error => {
            console.error(error);
          });
    }

    const [operationTypes, setOperationTypes] = useState([]);
    const fetchOperationTypes = async () => {
        axios.get('/api/directory/operation_types')
          .then(response => {
            setOperationTypes(response.data);
          })
          .catch(error => {
            console.error(error);
          });
    }

    useEffect(() => {
        fetchOrganizations()
        fetchCounterpartys()
        fetchContracts()
        fetchWarehouses()
        fetchOperationTypes()
    }, []);

    let DetailComponent;
    switch (documentType) {
        case 'taxInvoice':
            DetailComponent = TaxInvoiceDetail;
            break;
        case 'order':
            DetailComponent = OrderDetail;
            break;
        case 'invoice':
            DetailComponent = InvoiceDetail;
            break;
        case 'goodsReceived':
            DetailComponent = GoodsReceivedNoteDetail;
            break;
        case 'goodsDelivery':
            DetailComponent = GoodsDeliveryNoteDetail;
            break;
        default:
            DetailComponent = OrderDetail;
    }

    return (
        <div>
            <DetailComponent
                document={document}
                onBack={onBack}
                onClose={onClose}
                onToCreateOn={onToCreateOn}
                counterparts={counterparts}
                organizations={organizations}
                contracts={contracts}
                warehouses={warehouses}
                operationTypes={operationTypes}
            />
        </div>
    )
}

export default DocumentDetail;