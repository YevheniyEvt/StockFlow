import React, { useState } from 'react';
import { Container, Nav, Button } from 'react-bootstrap';
import ProfitReport from "./ProfitReport.jsx";
import SalesReport from "./SalesReport.jsx";
import ProductStockReport from "./ProductStockReport.jsx";

function Reports({ onBack }) {
  const [activeTab, setActiveTab] = useState('sales');

  const renderReport = () => {
    switch (activeTab) {
      case 'sales':
        return <SalesReport />;
      case 'profit':
        return <ProfitReport />;
      case 'stock':
        return <ProductStockReport />;
      default:
        return <SalesReport />;
    }
  };

  return (
    <Container className="py-4">
      <div className="d-flex align-items-center mb-4">
        <Button variant="outline-secondary" onClick={onBack} className="me-3">
          <i className="bi bi-arrow-left"></i> Назад
        </Button>
        <h2 className="mb-0">Звіти</h2>
      </div>

      <Nav variant="tabs" activeKey={activeTab} onSelect={(k) => setActiveTab(k)} className="mb-4">
        <Nav.Item>
          <Nav.Link eventKey="sales">Продажі</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="profit">Прибуток</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="stock">Залишки товарів</Nav.Link>
        </Nav.Item>
      </Nav>

      <div className="report-content">
        {renderReport()}
      </div>
    </Container>
  );
}

export default Reports;