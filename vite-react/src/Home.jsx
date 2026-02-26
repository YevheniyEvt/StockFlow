import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';

function Home({ onSelectDocumentType }) {
    const documentTypes = [
        { id: 'goodsReceived', name: 'Надходження товарів та послуг', icon: 'bi-box-seam' },
        { id: 'order', name: 'Замовлення покупця', icon: 'bi-cart-check' },
        { id: 'invoice', name: 'Рахунок на оплату', icon: 'bi-cash-stack' },
        { id: 'goodsDelivery', name: 'Видаткова накладна', icon: 'bi-truck' },
        { id: 'taxInvoice', name: 'Податкова накладна', icon: 'bi-file-earmark-spreadsheet' },
        { id: 'reports', name: 'Звіти', icon: 'bi-file-earmark-spreadsheet' },

    ];

    return (
        <Container className="py-5">
            <header className="text-center mb-5">
                <h2 className="fw-bold text-primary">Система керування документами</h2>
                <p className="text-muted">Виберіть розділ для роботи з документами</p>
            </header>
            <Row className="g-4">
                {documentTypes.map((type) => (
                    <Col key={type.id} xs={12} sm={6} lg={4}>
                        <Card 
                            className="document-card h-100 shadow-sm" 
                            onClick={() => onSelectDocumentType(type.id)}
                        >
                            <Card.Body>
                                <div className="icon-wrapper mb-3">
                                    <i className={`bi ${type.icon}`}></i>
                                </div>
                                <Card.Title className="h5 mb-0 text-center">{type.name}</Card.Title>
                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>
        </Container>
    );
}

export default Home;
