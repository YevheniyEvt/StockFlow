import { useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';

import ProductsTable from './ProductsTable.jsx';
import ServicesTable from "./ServicesTable.jsx";
import BankAccounts from "../BankAccounts.jsx";

    const products = [
        { id: 1, name: "Брус квадратний 40*40", quantity: 10, unit: "шт.", factor: 1, price: 120.00, amount: 1200.00, vatRate: "20%", vatAmount: 200.00, total: 3600.00, account: 203 },
        { id: 2, name: "Брус квадратний 50*50", quantity: 5, unit: "шт.", factor: 1, price: 150.00, amount: 750.00, vatRate: "20%", vatAmount: 150.00, total: 900.00, account: 203 },
        { id: 3, name: "Брус квадратний 50*50", quantity: 5, unit: "шт.", factor: 1, price: 150.00, amount: 750.00, vatRate: "20%", vatAmount: 150.00, total: 900.00, account: 203 },
    ];

    const services = [
        { id: 1, name: "Брус квадратний 40*40", quantity: 10, unit: "шт.", factor: 1, price: 120.00, amount: 1200.00, vatRate: "20%", vatAmount: 200.00, total: 3600.00, account: 203 },
        { id: 2, name: "Брус квадратний 50*50", quantity: 5, unit: "шт.", factor: 1, price: 150.00, amount: 750.00, vatRate: "20%", vatAmount: 150.00, total: 900.00, account: 203 },
    ];

function DocumentDetailTab() {
    const [key, setKey] = useState('products');
    const productTitle = key==="products" ?`Товари(${products.length})`: "Товари"
    const servicesTitle = key==="services" ?`Послуги(${services.length})`: "Послуги"

  return (
    <Tabs
      id="controlled-tab-example"
      activeKey={key}
      onSelect={(k) => setKey(k)}
      className="m-3"
    >
      <Tab eventKey="products" title={productTitle} className="m-3">
        <ProductsTable products={products}/>
      </Tab>
      <Tab eventKey="services" title={servicesTitle} className="m-3">
        <ServicesTable services={services}/>
      </Tab>
      <Tab eventKey="bank" title="Реквізити" className="m-3">
        <BankAccounts/>
      </Tab>
    </Tabs>
  );
}

export default DocumentDetailTab;