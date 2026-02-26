import React, { useState } from 'react';
import { Form, Button, Table, Row, Col, Card } from 'react-bootstrap';

function ProductStockReport() {
    const [date, setDate] = useState('');
    const [reportData, setReportData] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleFetchReport = async () => {
        if (!date) {
            alert("Будь ласка, виберіть дату");
            return;
        }
        setLoading(true);
        try {
            // Заглушка для демонстрації згідно зі схемою RemainingProductsReportResponseSchema
            const mockData = {
                date: date,
                total_quantity: 250,
                total_cost: 75000.00,
                items: [
                    { product_id: 1, product_name: "Товар 1", quantity_remaining: 100, total_cost: 30000.00, average_cost: 300.00 },
                    { product_id: 2, product_name: "Товар 2", quantity_remaining: 150, total_cost: 45000.00, average_cost: 300.00 }
                ]
            };
            setReportData(mockData);
        } catch (error) {
            console.error("Помилка при завантаженні звіту:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Card className="shadow-sm">
            <Card.Header className="bg-white py-3">
                <Form>
                    <Row className="align-items-end">
                        <Col md={6}>
                            <Form.Group controlId="reportDate">
                                <Form.Label>Дата залишків</Form.Label>
                                <Form.Control 
                                    type="date" 
                                    value={date} 
                                    onChange={(e) => setDate(e.target.value)} 
                                />
                            </Form.Group>
                        </Col>
                        <Col md={6}>
                            <Button 
                                variant="primary" 
                                onClick={handleFetchReport} 
                                disabled={loading}
                                className="w-100"
                            >
                                {loading ? 'Завантаження...' : 'Сформувати звіт'}
                            </Button>
                        </Col>
                    </Row>
                </Form>
            </Card.Header>
            <Card.Body>
                {reportData ? (
                    <div>
                        <div className="mb-4">
                            <h5>Залишки товарів станом на {reportData.date}</h5>
                            <Row>
                                <Col md={6}>
                                    <div className="p-3 bg-light rounded border text-center">
                                        <div className="text-muted small">Загальна кількість</div>
                                        <div className="h5 mb-0">{reportData.total_quantity}</div>
                                    </div>
                                </Col>
                                <Col md={6}>
                                    <div className="p-3 bg-light rounded border text-center">
                                        <div className="text-muted small">Загальна вартість</div>
                                        <div className="h5 mb-0">{reportData.total_cost.toLocaleString()} грн</div>
                                    </div>
                                </Col>
                            </Row>
                        </div>
                        <Table striped bordered hover responsive>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Назва продукту</th>
                                    <th>Залишок</th>
                                    <th>Ср. ціна</th>
                                    <th>Загальна вартість</th>
                                </tr>
                            </thead>
                            <tbody>
                                {reportData.items.map((item) => (
                                    <tr key={item.product_id}>
                                        <td>{item.product_id}</td>
                                        <td>{item.product_name}</td>
                                        <td>{item.quantity_remaining}</td>
                                        <td>{item.average_cost.toLocaleString()}</td>
                                        <td>{item.total_cost.toLocaleString()}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </Table>
                    </div>
                ) : (
                    <div className="text-center py-5 text-muted">
                        Виберіть дату та натисніть "Сформувати звіт"
                    </div>
                )}
            </Card.Body>
        </Card>
    );
}

export default ProductStockReport;