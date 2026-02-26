import React, { useState } from 'react';
import DocumentList from "./list/DocumentList.jsx";
import DocumentDetail from "./detail/DocumentDetail.jsx";
import Home from './Home.jsx';
import Reports from "./reports/Reports.jsx";
import axios from "axios";

function App() {
  const [view, setView] = useState('home');
  const [selectedDocument, setSelectedDocument] = useState(null);
  const [documentType, setDocumentType] = useState(null);

  const handleSelectDocumentType = (type) => {
    setDocumentType(type);
    if (type === 'reports') {
      setView('reports');
    } else {
      setView('list');
    }
  };

  const handleRowDoubleClick = (document) => {
    setSelectedDocument(document);
    setView('detail');
  };

  const handleBackToList = () => {
    setView('list');
  };

  const handleBackToHome = () => {
    setView('home');
    setDocumentType(null);
    setSelectedDocument(null);
  };

  const handleForwardToDetail = () => {
    if (selectedDocument) {
      setView('detail');
    }
  };
  const createNewInvoice = async (document) => {
    try {
      const response = await axios.post("/api/documents/invoices/create", {
        order_id: document.id,
        organization_id: document.organization_id,
        counterparty_id: document.counterparty_id,
      });
      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

    const createNewGoodsDeliveryNote = async (document) => {
        try {
          const response = await axios.post("/api/documents/goods_delivery_notes/create", {
            invoice_id: document.id,
            organization_id: document.organization_id,
            counterparty_id: document.counterparty_id,
          });
          return response.data;
        } catch (error) {
          console.error(error);
          throw error;
        }
  };

    const createNewTaxInvoice = async (document) => {
        try {
          const response = await axios.post("/api/documents/tax_invoices/create", {
            goods_delivery_note_id: document.id,
            organization_id: document.organization_id,
            counterparty_id: document.counterparty_id,
          });
          return response.data;
        } catch (error) {
          console.error(error);
          throw error;
        }
  };

  const handleToCreateOn = async (document) => {
    let createdDocumentType;
    let newSelectedDocument = document;

    switch (documentType) {
      case 'order':
        createdDocumentType = 'invoice';
        newSelectedDocument = await createNewInvoice(document);
        break;
      case 'invoice':
        createdDocumentType = 'goodsDelivery';
        newSelectedDocument = await createNewGoodsDeliveryNote(document);
        break;
      case 'goodsDelivery':
        createdDocumentType = 'taxInvoice';
        newSelectedDocument = await createNewTaxInvoice(document);
        break;
      default:
        createdDocumentType = documentType;
    }

    setDocumentType(createdDocumentType);
    setSelectedDocument(newSelectedDocument);
    setView('detail');
  };
  return (
    <div className='min-vh-100 bg-light'>
      {view === 'home' && (
        <Home onSelectDocumentType={handleSelectDocumentType} />
      )}
      {view === 'list' && (
        <DocumentList
          documentType={documentType}
          onRowDoubleClick={handleRowDoubleClick}
          onForward={handleForwardToDetail}
          onBack={handleBackToHome}
          onClose={handleBackToHome}
        />
      )}
      {view === 'detail' && (
        <DocumentDetail
          document={selectedDocument}
          documentType={documentType}
          onBack={handleBackToList}
          onClose={handleBackToHome}
          onToCreateOn={handleToCreateOn}
        />
      )}
      {view === 'reports' && (
        <Reports onBack={handleBackToHome} />
      )}
    </div>
  )
}




export default App
