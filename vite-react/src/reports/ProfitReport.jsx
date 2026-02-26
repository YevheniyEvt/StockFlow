import React, { useState } from 'react';
import { Form, Button, Table, Row, Col, Card } from 'react-bootstrap';

function ProfitReport() {
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
            // Заглушка для демонстрації згідно зі схемою ProfitReportResponseSchema
            const mockData = {
                start_date: startDate,
                end_date: endDate,
                total_revenue: 50000.00,
                total_purchase_cost: 35000.00,
                total_profit: 15000.00,
                items: [
                    { product_id: 1, product_name: "Товар 1", revenue: 20000.00, purchase_cost: 14000.00, profit: 6000.00 },
                    { product_id: 2, product_name: "Товар 2", revenue: 30000.00, purchase_cost: 21000.00, profit: 9000.00 }
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
                            <Row className="text-center g-3">
                                <Col md={4}>
                                    <div className="p-3 bg-light rounded border">
                                        <div className="text-muted small">Загальний дохід</div>
                                        <div className="h5 mb-0 text-primary">{reportData.total_revenue.toLocaleString()} грн</div>
                                    </div>
                                </Col>
                                <Col md={4}>
                                    <div className="p-3 bg-light rounded border">
                                        <div className="text-muted small">Загальна собівартість</div>
                                        <div className="h5 mb-0 text-danger">{reportData.total_purchase_cost.toLocaleString()} грн</div>
                                    </div>
                                </Col>
                                <Col md={4}>
                                    <div className="p-3 bg-light rounded border">
                                        <div className="text-muted small">Загальний прибуток</div>
                                        <div className="h5 mb-0 text-success">{reportData.total_profit.toLocaleString()} грн</div>
                                    </div>
                                </Col>
                            </Row>
                        </div>
                        <Table striped bordered hover responsive>
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Назва продукту</th>
                                    <th>Дохід</th>
                                    <th>Собівартість</th>
                                    <th>Прибуток</th>
                                </tr>
                            </thead>
                            <tbody>
                                {reportData.items.map((item) => (
                                    <tr key={item.product_id}>
                                        <td>{item.product_id}</td>
                                        <td>{item.product_name}</td>
                                        <td>{item.revenue.toLocaleString()}</td>
                                        <td>{item.purchase_cost.toLocaleString()}</td>
                                        <td>{item.profit.toLocaleString()}</td>
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

export default ProfitReport;