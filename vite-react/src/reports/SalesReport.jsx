import React, { useState } from 'react';
import { Form, Button, Table, Row, Col, Card } from 'react-bootstrap';

function SalesReport() {
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [reportData, setReportData] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleFetchReport = async () => {
        if (!startDate || !endDate) {
            alert("Будь ласка, виберіть обидві дати");
            return;
        }
        setLoading(true);
        try {
            // Тут буде запит до сервера
            // const response = await fetch(`/api/reports/sales?start_date=${startDate}&end_date=${endDate}`);
            // const data = await response.json();
            
            // Заглушка для демонстрації згідно зі схемою SalesReportResponseSchema
            const mockData = {
                start_date: startDate,
                end_date: endDate,
                total_quantity: 150,
                total_amount: 45000.50,
                items: [
                    { product_id: 1, product_name: "Товар 1", quantity: 50, amount: 15000.00 },
                    { product_id: 2, product_name: "Товар 2", quantity: 100, amount: 30000.50 }
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
                        <Col md={4}>
                            <Form.Group controlId="startDate">
                                <Form.Label>Початкова дата</Form.Label>
                                <Form.Control 
                                    type="date" 
                                    value={startDate} 
                                    onChange={(e) => setStartDate(e.target.value)} 
                                />
                            </Form.Group>
                        </Col>
                        <Col md={4}>
                            <Form.Group controlId="endDate">
                                <Form.Label>Кінцева дата</Form.Label>
                                <Form.Control 
                                    type="date" 
                                    value={endDate} 
                                    onChange={(e) => setEndDate(e.target.value)} 
                                />
                            </Form.Group>
                        </Col>
                        <Col md={4}>
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
                            <h5>Результати за період з {reportData.start_date} по {reportData.end_date}</h5>
                            <Row>
                                <Col md={6}>
                                    <div className="p-3 bg-light rounded">
                                        <strong>Загальна кількість:</strong> {reportData.total_quantity}
                                    </div>
                                </Col>
                                <Col md={6}>
                                    <div className="p-3 bg-light rounded">
                                        <strong>Загальна сума:</strong> {reportData.total_amount.toLocaleString()} грн
                                    </div>
                                </Col>
                            </Row>
                        </div>
                        <Table striped bordered hover responsive>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Назва продукту</th>
                                    <th>Кількість</th>
                                    <th>Сума</th>
                                </tr>
                            </thead>
                            <tbody>
                                {reportData.items.map((item) => (
                                    <tr key={item.product_id}>
                                        <td>{item.product_id}</td>
                                        <td>{item.product_name}</td>
                                        <td>{item.quantity}</td>
                                        <td>{item.amount.toLocaleString()}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </Table>
                    </div>
                ) : (
                    <div className="text-center py-5 text-muted">
                        Виберіть період та натисніть "Сформувати звіт"
                    </div>
                )}
            </Card.Body>
        </Card>
    );
}

export default SalesReport;