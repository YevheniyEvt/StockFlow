import React, {useEffect, useState} from 'react';
import {Form, Button, Table, Row, Col, Card, InputGroup} from 'react-bootstrap';
import axios from 'axios';

function ProductStockReport() {
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

    const [date, setDate] = useState('');
    const fetchReport = async () => {
        if (!date) {
            alert("Будь ласка, виберіть дату");
            return;
        }
        if (!selectedOrganization) {
            alert("Будь ласка, виберіть оргарізацію");
            return;
        }
        setLoading(true);
        axios.get(`/api/reports/remaining-products-report/${selectedOrganization?.id}`,{
            params: { date: date }
            })
              .then(response => {
                  console.log(response.data)
                setReportData(response.data);
              })
              .catch(error => {
                console.error(error);
          });
        setLoading(false);
    }
    useEffect(() => {
        fetchOrganizations()
    }, []);

    return (
        <Card className="shadow-sm">
            <Card.Header className="bg-white py-3">
                <Form className="document-form">
                    <Row className="align-items-end">
                        <Col md={3}>
                            <Form.Group controlId="reportDate">
                                <Form.Label className="small fw-bold text-muted mb-1">Дата залишків</Form.Label>
                                <Form.Control 
                                    type="date" 
                                    value={date} 
                                    onChange={(e) => setDate(e.target.value)} 
                                />
                            </Form.Group>
                        </Col>
                      <Col md={6}>
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
                        <Col md={3}>
                            <Button
                                variant="primary"
                                onClick={fetchReport}
                                disabled={loading}
                                className="w-100"
                            >
                                {loading ? 'Завантаження...' : 'Сформувати'}
                            </Button>
                        </Col>
                </Row>
                </Form>
            </Card.Header>
            <Card.Body>
                {reportData ? (
                    <div>
                        <div className="mb-4">
                            <h5>Залишки товарів станом на {new Date(reportData.date).toLocaleDateString('uk-UA')}</h5>
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