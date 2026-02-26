import React, { useState } from 'react';
import DocumentList from "./list/DocumentList.jsx";
import DocumentDetail from "./detail/DocumentDetail.jsx";
import Home from './Home.jsx';
import Reports from "./reports/Reports.jsx";

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

  const handleToCreateOn = (document) => {
    let createdDocument;
    switch (documentType) {
        case 'order':
            createdDocument = 'invoice';
            break;
        case 'invoice':
            createdDocument = 'goodsDelivery';
            break;
        case 'goodsDelivery':
            createdDocument = 'taxInvoice';
            break;
        default:
            createdDocument = documentType;
    }
    setDocumentType(createdDocument)
    setSelectedDocument(document);
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
