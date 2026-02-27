import { useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';

import ProductsTable from './ProductsTable.jsx';
import ServicesTable from "./ServicesTable.jsx";
import BankAccounts from "./BankAccounts.jsx";

    // const products = [
    //     { id: 1, name: "Брус квадратний 40*40", quantity: 10, unit: "шт.", factor: 1, price: 120.00, amount: 1200.00, DiscountAmount: 1200, discount: 0, vatRate: "20%", vatAmount: 200.00, total: 3600.00, account: 203 },
    //     { id: 2, name: "Брус квадратний 50*50", quantity: 5, unit: "шт.", factor: 1, price: 150.00, amount: 750.00, DiscountAmount: 1200, discount: 0, vatRate: "20%", vatAmount: 150.00, total: 900.00, account: 203 },
    //     { id: 3, name: "Брус квадратний 50*50", quantity: 5, unit: "шт.", factor: 1, price: 150.00, amount: 750.00, DiscountAmount: 1200, discount: 0, vatRate: "20%", vatAmount: 150.00, total: 900.00, account: 203 },
    // ];
    //
    // const services = [
    //     { id: 1, name: "Брус квадратний 40*40", quantity: 10, unit: "шт.", factor: 1, price: 120.00, amount: 1200.00, vatRate: "20%", vatAmount: 200.00, total: 3600.00, account: 203 },
    //     { id: 2, name: "Брус квадратний 50*50", quantity: 5, unit: "шт.", factor: 1, price: 150.00, amount: 750.00, vatRate: "20%", vatAmount: 150.00, total: 900.00, account: 203 },
    // ];

function DocumentDetailTab({document, canEdit, onUpdate, documentType }) {
    const products = document.items.filter(item => item.product);
    const services = document.items.filter(item => item.service);
    const [key, setKey] = useState('products');
    const productTitle = key==="products" ?`Товари(${products.length})`: "Товари"
    const servicesTitle = key==="services" ?`Послуги(${services.length})`: "Послуги"

  return (
    <div className="bg-white m-3 rounded shadow-sm">
        <Tabs
          id="controlled-tab-example"
          activeKey={key}
          onSelect={(k) => setKey(k)}
          className="custom-tabs px-3 pt-2 border-bottom-0"
        >
          <Tab eventKey="products" title={productTitle}>
            <div className="p-3">
                <ProductsTable 
                    canEdit={canEdit} 
                    products={products} 
                    onUpdate={onUpdate}
                    documentId={document.id}
                    documentType={documentType}
                    organizationId={document.organization_id}
                />
            </div>
          </Tab>
          <Tab eventKey="services" title={servicesTitle}>
            <div className="p-3">
                <ServicesTable 
                    canEdit={canEdit} 
                    services={services} 
                    onUpdate={onUpdate}
                    documentId={document.id}
                    documentType={documentType}
                    organizationId={document.organization_id}
                />
            </div>
          </Tab>
          <Tab eventKey="bank" title="Реквізити">
            <div className="p-3">
                <BankAccounts document={document}/>
            </div>
          </Tab>
        </Tabs>
    </div>
  );
}

export default DocumentDetailTab;