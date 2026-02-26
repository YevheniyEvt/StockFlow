import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import Dropdown from 'react-bootstrap/Dropdown';
import ButtonGroup from 'react-bootstrap/ButtonGroup';


function GoodsDeliveryNoteNavigation({document, onBack, onToCreateOn, counterparts, organizations, contracts, warehouses }){
    return (
         <div className="detail-navigation p-3 bg-white border-bottom shadow-sm">
            <div className="d-flex flex-wrap gap-2 mb-4">
                <Button variant="primary" size="sm" className="btn-icon">
                    <i className="bi bi-save"></i> Записати
                </Button>
                <Button variant="success" size="sm" className="btn-icon">
                    <i className="bi bi-check-circle"></i> Провести
                </Button>
                <Button variant="outline-primary" size="sm" className="btn-icon" onClick={onBack}>
                    Провести та закрити
                </Button>
                <Dropdown as={ButtonGroup} size="sm">
                  <Dropdown.Toggle variant="secondary" id="dropdown-basic" >
                    Створити на підставі
                  </Dropdown.Toggle>
                  <Dropdown.Menu>
                    <Dropdown.Item onClick={() => onToCreateOn(document)}>Податкова накладна</Dropdown.Item>
                  </Dropdown.Menu>
                </Dropdown>
            </div>

             <Form className="document-form">
                 <Row className="g-3">
                   <Col md={3}>
                      <Form.Group controlId="orderNumber">
                        <Form.Label className="small fw-bold text-muted mb-1">Номер</Form.Label>
                        <Form.Control size="sm" type="text" value={document.id} className="bg-light" disabled/>
                      </Form.Group>
                  </Col>
                  <Col md={3}>
                      <Form.Group controlId="orderDate">
                        <Form.Label className="small fw-bold text-muted mb-1">Дата</Form.Label>
                        <Form.Control size="sm" type="date" defaultValue={new Date(document.document_date).toISOString().split('T')[0]} />
                      </Form.Group>
                  </Col>
                  <Col md={6}></Col>

                  <Col md={6}>
                      <Form.Group controlId="counterparty">
                        <Form.Label className="small fw-bold text-muted mb-1">Контрагент</Form.Label>
                        <Form.Select aria-label="Контрагент" size="sm">
                                <option>Виберіть контрагент...</option>
                                {counterparts.map((counterpart) => (
                                    <option key={counterpart.id}
                                            value={counterpart.id}
                                            selected={counterpart.id === document.counterparty_id}
                                    >
                                        {counterpart.name}
                                    </option>
                                ))}
                        </Form.Select>
                      </Form.Group>
                  </Col>
                  <Col md={6}>
                      <Form.Group controlId="organization">
                        <Form.Label className="small fw-bold text-muted mb-1">Організація</Form.Label>
                        <Form.Select aria-label="Організація" size="sm">
                            {organizations.map((organization) => (
                                <option key={organization.id}
                                        value={organization.id}
                                        selected={organization.id === document.organization_id}
                                >
                                    {organization.name}
                                </option>
                            ))}
                        </Form.Select>
                      </Form.Group>
                  </Col>

                  <Col md={6}>
                      <Form.Group controlId="exampleForm.ControlInput1">
                        <Form.Label className="small fw-bold text-muted mb-1">Договір:</Form.Label>
                          <Form.Select aria-label="Договір" size="sm">
                            <option value="">Оберіть договір...</option>
                            {contracts.map((contract) => (
                                <option key={contract.id}
                                        value={contract.id}
                                        selected={contract.id === document.contract_id}
                                >
                                    {contract.name}
                                </option>
                            ))}
                          </Form.Select>
                      </Form.Group>
                  </Col>
                  <Col md={6}>
                      <Form.Group controlId="exampleForm.ControlInput1">
                        <Form.Label className="small fw-bold text-muted mb-1">Склад:</Form.Label>
                          <Form.Select aria-label="Склад" size="sm">
                            <option value="">Оберіть склад...</option>
                            {warehouses.map((warehouse) => (
                                <option key={warehouse.id}
                                        value={warehouse.id}
                                        selected={warehouse.id === document.warehouse_id}
                                >
                                    {warehouse.name}
                                </option>
                            ))}
                          </Form.Select>
                      </Form.Group>
                  </Col>
                </Row>
            </Form>
        </div>
    )
}

export default GoodsDeliveryNoteNavigation