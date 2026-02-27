import React, {useEffect, useState} from 'react';
import { Form, Button, Table, Row, Col, Card } from 'react-bootstrap';
import axios from "axios";

function ProfitReport() {
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [reportData, setReportData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [organizations, setOrganizations] = useState([]);

    const [selectedOrganization, setSelectedOrganization] = useState(null);
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
    }, []);

    const handleFetchReport = async () => {
        if (!startDate || !endDate) {
            alert("Будь ласка, виберіть обидві дати");
            return;
        }
        setLoading(true);
        if (!selectedOrganization) {
            alert("Будь ласка, виберіть оргарізацію");
            setLoading(false);
            return;
        }
        axios.get(`/api/reports/profit-report/${selectedOrganization?.id}`,{
            params: { start_date: startDate, end_date: endDate }
            })
              .then(response => {
                  console.log(response.data)
                setReportData(response.data);
              })
              .catch(error => {
                console.error(error);
          });
        setLoading(false);
    };

    return (
        <Card className="shadow-sm">
            <Card.Header className="bg-white py-3">
                <Form>
                    <Row className="align-items-end">
                        <Col md={3}>
                            <Form.Group controlId="startDate">
                                <Form.Label>Початкова дата</Form.Label>
                                <Form.Control 
                                    type="date" 
                                    value={startDate} 
                                    onChange={(e) => setStartDate(e.target.value)} 
                                />
                            </Form.Group>
                        </Col>
                        <Col md={3}>
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
                          <Form.Group controlId="organization">
                            <Form.Label className="small fw-bold text-muted mb-1">Організація</Form.Label>
                            <Form.Select
                                aria-label="Організація"
                                size="sm"
                                name="organization_id"
                            >
                                    <option onClick={() => setSelectedOrganization(null)} value="">Виберіть організацію...</option>
                                    {organizations.map((organization) => (
                                        <option
                                            key={organization.id}
                                            value={organization.id}
                                            onClick={() => setSelectedOrganization(organization)}
                                        >
                                            {organization.name}
                                        </option>
                                    ))}
                            </Form.Select>
                          </Form.Group>
                      </Col>
                        <Col md={2}>
                            <Button 
                                variant="primary" 
                                onClick={handleFetchReport} 
                                disabled={loading}
                                className="w-100"
                            >
                                {loading ? 'Завантаження...' : 'Сформувати  '}
                            </Button>
                        </Col>
                    </Row>
                </Form>
            </Card.Header>
            <Card.Body>
                {reportData ? (
                    <div>
                        <div className="mb-4">
                            <h5>Результати за період з {new Date(reportData.start_date).toLocaleDateString('uk-UA')}  по {new Date(reportData.end_date).toLocaleDateString('uk-UA')}</h5>
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