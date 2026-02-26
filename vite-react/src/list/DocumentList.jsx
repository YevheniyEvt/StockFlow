import DocumentListNavigation from "./DocumentListNavigation.jsx";
import Header from "../Header.jsx";
import GoodsReceivedNoteListTable from "./GoodsReceivedNoteListTable.jsx";
import GoodsDeliveryNoteListTable from "./GoodsDeliveryNoteListTable.jsx";
import TaxInvoiceListTable from "./TaxInvoiceListTable.jsx";
import OrderListTable from "./OrderListTable.jsx";
import InvoiceListTable from "./InvoiceListTable.jsx";

import axios from "axios";
import {useState} from "react";
import { useEffect } from 'react';

function DocumentList({ onRowDoubleClick, onForward, documentType, onBack, onClose }) {
    let TableComponent;
    let title = "";
    let listUrl
    let createNewObject


    const [newObject, setNewObject] = useState(null);

    const createNewOrder = async () => {
        setLoading(true);

        axios.post("/api/documents/orders/create", {
            organization_id: selectedOrganization.id
        })
          .then(response => {
            fetchTableData()
            setNewObject(response.data);
          })
          .catch(error => {
            console.error(error);
          }).then(()=>setLoading(false));
    };

    const createNewGoodsReceivedNote = async () => {
        setLoading(true);
        axios.post("/api/documents/goods_received_notes/create", {
            organization_id: selectedOrganization.id
        })
          .then(response => {
            fetchTableData()
            setNewObject(response.data);
          })
          .catch(error => {
            console.error(error);
          }).then(()=>setLoading(false));
    };


    switch (documentType) {
        case 'taxInvoice':
            TableComponent = TaxInvoiceListTable;
            title = "Податкова накладна";
            listUrl='/api/documents/tax_invoices'
            break;
        case 'order':
            TableComponent = OrderListTable;
            title = "Замовлення покупця";
            createNewObject=createNewOrder
            listUrl='/api/documents/orders'
            break;
        case 'invoice':
            TableComponent = InvoiceListTable;
            title = "Рахунок на оплату";
            listUrl='/api/documents/invoices'
            break;
        case 'goodsReceived':
            TableComponent = GoodsReceivedNoteListTable;
            title = "Надходження товарів та послуг";
            createNewObject=createNewGoodsReceivedNote
            listUrl='/api/documents/goods_received_notes'
            break;
        case 'goodsDelivery':
            TableComponent = GoodsDeliveryNoteListTable;
            title = "Видаткова накладна";
            listUrl='/api/documents/goods_delivery_notes'
            break;
        default:
            TableComponent = OrderListTable;
            title = "Документи";
            listUrl='/api/documents/orders'
    }

    const [loading, setLoading] = useState(false);
    const [selectedOrganization, setSelectedOrganization] = useState(null);
    const [selectedCounterpart, setSelectedCounterpart] = useState(null);


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
    useEffect(() => {
        fetchOrganizations()
        fetchCounterpartys()
    }, []);


    const [objects, setObjects] = useState([]);
    const fetchTableData = async () => {
        axios.get(listUrl, {
        })
          .then(response => {
            setObjects(response.data);
          })
          .catch(error => {
            console.error(error);
          });
    }
    useEffect(() => {
        fetchTableData()
    }, []);


    return (
        <div className="d-flex flex-column h-100">
            <Header name={title} onForward={onForward} onBack={onBack} onClose={onClose}/>
            <DocumentListNavigation
                counterparts={counterparts}
                setSelectedCounterpart={setSelectedCounterpart}
                organizations={organizations}
                setSelectedOrganization={setSelectedOrganization}
                createNewObject={createNewObject}
                loading={loading}
                selectedOrganization={selectedOrganization}

            />
            <TableComponent
                elements={objects}
                onRowDoubleClick={onRowDoubleClick} />
        </div>
    )
}

export default DocumentList