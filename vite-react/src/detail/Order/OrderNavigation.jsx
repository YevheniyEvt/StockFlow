import { useState } from 'react';
import axios from 'axios';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import Dropdown from 'react-bootstrap/Dropdown';
import ButtonGroup from 'react-bootstrap/ButtonGroup';


function OrderNavigation({ document, onToCreateOn, onBack, counterparts, organizations, onUpdate  }){
    const [formData, setFormData] = useState({
        document_date: new Date(document.document_date).toISOString().split('T')[0],
        counterparty_id: document.counterparty_id || "",
        organization_id: document.organization_id || "",
        comment: document.comment || ""
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSave = async () => {
        try {
            const dataToSave = {
                ...formData,
                counterparty_id: formData.counterparty_id === "" ? null : formData.counterparty_id,
                organization_id: formData.organization_id === "" ? null : formData.organization_id
            };
            const response = await axios.patch(`/api/documents/orders/${document.id}/update`, dataToSave);
            alert("Замовлення збережено");
            if (onUpdate) onUpdate(response.data);
            console.log("Saved order:", response.data);
        } catch (error) {
            console.error("Error saving order:", error);
            alert("Помилка при збереженні замовлення");
        }
    };

    const handleConfirm = async (closeAfter = false) => {
        try {
            const response = await axios.patch(`/api/documents/orders/${document.id}/update-status`, {
                status: 'confirmed_by_client'
            });
            alert("Замовлення підтверджено");
            if (onUpdate) onUpdate(response.data);
            if (closeAfter && onBack) {
                onBack();
            }
        } catch (error) {
            console.error("Error confirming order:", error);
            alert("Помилка при підтвердженні замовлення");
        }
    };

    return (
        <div className="detail-navigation p-3 bg-white border-bottom shadow-sm">
            <div className="d-flex flex-wrap gap-2 mb-4">
                <Button variant="primary" size="sm" className="btn-icon" onClick={handleSave}>
                    <i className="bi bi-save"></i> Записати
                </Button>
                <Button variant="success" size="sm" className="btn-icon" onClick={() => handleConfirm(false)}>
                    <i className="bi bi-check-circle"></i> Підтвердити
                </Button>
                <Button variant="outline-primary" size="sm" className="btn-icon" onClick={() => handleConfirm(true)}>
                    Підтвердити та закрити
                </Button>
                <Dropdown as={ButtonGroup} size="sm">
                  <Dropdown.Toggle variant="outline-secondary" id="dropdown-basic">
                    <i className="bi bi-file-earmark-plus"></i> Створити на підставі
                  </Dropdown.Toggle>
                  <Dropdown.Menu>
                    <Dropdown.Item onClick={() => onToCreateOn(document)}>Рахунок на оплату</Dropdown.Item>
                  </Dropdown.Menu>
                </Dropdown>
            </div>

             <Form className="document-form">
                 <Row className="g-3">
                   <Col md={3}>
                      <Form.Group controlId="orderNumber">
                        <Form.Label className="small fw-bold text-muted mb-1">Номер</Form.Label>
                        <Form.Control size="sm" type="text" value={document.id} disabled className="bg-light" />
                      </Form.Group>
                  </Col>
                  <Col md={3}>
                      <Form.Group controlId="orderDate">
                        <Form.Label className="small fw-bold text-muted mb-1">Дата</Form.Label>
                        <Form.Control 
                            size="sm" 
                            type="date" 
                            name="document_date"
                            value={formData.document_date} 
                            onChange={handleChange}
                        />
                      </Form.Group>
                  </Col>
                  <Col md={6}></Col>

                  <Col md={6}>
                      <Form.Group controlId="counterparty">
                        <Form.Label className="small fw-bold text-muted mb-1">Контрагент</Form.Label>
                        <Form.Select 
                            aria-label="Контрагент" 
                            size="sm"
                            name="counterparty_id"
                            value={formData.counterparty_id}
                            onChange={handleChange}
                        >
                                <option value="">Виберіть контрагент...</option>
                                {counterparts.map((counterpart) => (
                                    <option key={counterpart.id} value={counterpart.id}>
                                        {counterpart.name}
                                    </option>
                                ))}
                        </Form.Select>
                      </Form.Group>
                  </Col>
                  <Col md={6}>
                      <Form.Group controlId="organization">
                        <Form.Label className="small fw-bold text-muted mb-1">Організація</Form.Label>
                        <Form.Select 
                            aria-label="Організація" 
                            size="sm"
                            name="organization_id"
                            value={formData.organization_id}
                            onChange={handleChange}
                        >
                                <option value="">Виберіть організацію...</option>
                                {organizations.map((organization) => (
                                    <option key={organization.id} value={organization.id}>
                                        {organization.name}
                                    </option>
                                ))}
                        </Form.Select>
                      </Form.Group>
                  </Col>
                  <Col md={12}>
                      <Form.Group controlId="comment">
                        <Form.Label className="small fw-bold text-muted mb-1">Коментар</Form.Label>
                        <Form.Control 
                            size="sm" 
                            as="textarea" 
                            rows={2}
                            name="comment"
                            value={formData.comment}
                            onChange={handleChange}
                        />
                      </Form.Group>
                  </Col>
                </Row>
            </Form>
        </div>
    )
}

export default OrderNavigation