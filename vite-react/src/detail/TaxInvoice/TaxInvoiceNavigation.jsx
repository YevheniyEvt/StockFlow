import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import Dropdown from "react-bootstrap/Dropdown";
import ButtonGroup from "react-bootstrap/ButtonGroup";


function TaxInvoiceNavigation({onBack, onToCreateOn}){
    return (
        <div className="detail-navigation p-3 bg-white border-bottom shadow-sm">
            <div className="d-flex flex-wrap gap-2 mb-4">
                <Button variant="primary" size="sm" className="btn-icon">
                    <i className="bi bi-save"></i> Записати
                </Button>
                <Button variant="success" size="sm" className="btn-icon">
                    <i className="bi bi-check-circle"></i> Підтвердити
                </Button>
                <Button variant="outline-primary" size="sm" className="btn-icon" onClick={onBack}>
                    Підтвердити та закрити
                </Button>
            </div>

             <Form className="document-form">
                 <Row className="g-3">
                   <Col md={3}>
                      <Form.Group controlId="orderNumber">
                        <Form.Label className="small fw-bold text-muted mb-1">Номер</Form.Label>
                        <Form.Control size="sm" type="text" value="ДО0000000020" disabled className="bg-light" />
                      </Form.Group>
                  </Col>
                  <Col md={3}>
                      <Form.Group controlId="orderDate">
                        <Form.Label className="small fw-bold text-muted mb-1">Дата</Form.Label>
                        <Form.Control size="sm" type="date" defaultValue={new Date().toISOString().split('T')[0]} disabled/>
                      </Form.Group>
                  </Col>
                  <Col md={6}></Col>

                  <Col md={6}>
                      <Form.Group controlId="counterparty">
                        <Form.Label className="small fw-bold text-muted mb-1">Контрагент</Form.Label>
                        <Form.Select aria-label="Контрагент" size="sm" disabled>
                            <option value="1">ТОВ "Альфа"</option>
                        </Form.Select>
                      </Form.Group>
                  </Col>
                  <Col md={6}>
                      <Form.Group controlId="organization">
                        <Form.Label className="small fw-bold text-muted mb-1">Організація</Form.Label>
                        <Form.Select aria-label="Організація" size="sm" disabled>
                            <option value="1">ПП "Моя Компанія"</option>
                        </Form.Select>
                      </Form.Group>
                  </Col>

                  <Col md={6}>
                      <Form.Group controlId="exampleForm.ControlInput1">
                        <Form.Label className="small fw-bold text-muted mb-1">Договір:</Form.Label>
                          <Form.Select aria-label="Договір" size="sm" disabled>
                            <option value="1">203-12</option>
                          </Form.Select>
                      </Form.Group>
                  </Col>
                  <Col md={6}>
                      <Form.Group controlId="exampleForm.ControlInput1">
                        <Form.Label className="small fw-bold text-muted mb-1">Склад:</Form.Label>
                          <Form.Select aria-label="Склад" size="sm" disabled>
                            <option value="1">Київський</option>
                          </Form.Select>
                      </Form.Group>
                  </Col>
                </Row>
            </Form>
        </div>
    )
}

export default TaxInvoiceNavigation