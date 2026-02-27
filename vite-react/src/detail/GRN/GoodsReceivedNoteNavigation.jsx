import { useState } from 'react';
import axios from 'axios';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import Dropdown from "react-bootstrap/Dropdown";
import ButtonGroup from "react-bootstrap/ButtonGroup";


function GoodsReceivedNoteNavigation({ document, onBack, onToCreateOn, counterparts, organizations, contracts, warehouses, operationTypes, onUpdate }){
    const [formData, setFormData] = useState({
        document_date: new Date(document.document_date).toISOString().split('T')[0],
        operation_type_id: document.operation_type_id || "",
        counterparty_id: document.counterparty_id || "",
        organization_id: document.organization_id || "",
        contract_id: document.contract_id || "",
        warehouse_id: document.warehouse_id || "",
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
                organization_id: formData.organization_id === "" ? null : formData.organization_id,
                operation_type_id: formData.operation_type_id === "" ? null : formData.operation_type_id,
                contract_id: formData.contract_id === "" ? null : formData.contract_id,
                warehouse_id: formData.warehouse_id === "" ? null : formData.warehouse_id,
            };
            const response = await axios.patch(`/api/documents/goods_received_notes/${document.id}/update`, dataToSave);
            alert("Надходження збережено");
            if (onUpdate) onUpdate(response.data);
            console.log("Saved GRN:", response.data);
        } catch (error) {
            console.error("Error saving GRN:", error);
            alert("Помилка при збереженні надходження");
        }
    };

    const handleHeld = async (closeAfter = false) => {
        try {
            const response = await axios.post(`/api/documents/goods_received_notes/${document.id}/held`);
            alert("Надходження проведено");
            if (onUpdate) onUpdate(response.data);
            if (closeAfter && onBack) {
                onBack();
            }
        } catch (error) {
            console.error("Error holding GRN:", error);
            alert("Помилка при проведенні надходження");
        }
    };

    return (
         <div className="detail-navigation p-3 bg-white border-bottom shadow-sm">
            <div className="d-flex flex-wrap gap-2 mb-4">
                <Button variant="primary" size="sm" className="btn-icon" onClick={handleSave}>
                    <i className="bi bi-save"></i> Записати
                </Button>
                <Button variant="success" size="sm" className="btn-icon" onClick={() => handleHeld(false)}>
                    <i className="bi bi-check-circle"></i> Провести
                </Button>
                <Button variant="outline-primary" size="sm" className="btn-icon" onClick={() => handleHeld(true)}>
                    Провести та закрити
                </Button>
            </div>

             <Form className="document-form">
                 <Row className="g-3">
                   <Col md={3}>
                      <Form.Group controlId="orderNumber">
                        <Form.Label className="small fw-bold text-muted mb-1">Номер</Form.Label>
                        <Form.Control size="sm" type="text"  value={document.id} className="bg-light" disabled/>
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
                  <Col md={6}>
                     <Form.Group controlId="operationType">
                        <Form.Label className="small fw-bold text-muted mb-1">Вид операції</Form.Label>
                        <Form.Select 
                            aria-label="Вид операції" 
                            size="sm"
                            name="operation_type_id"
                            value={formData.operation_type_id}
                            onChange={handleChange}
                        >
                            <option value="">Виберіть вид операції...</option>
                            {operationTypes.map((operationType) => (
                                <option key={operationType.id} value={operationType.id}>
                                    {operationType.name}
                                </option>
                            ))}
                        </Form.Select>
                     </Form.Group>
                  </Col>

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

                  <Col md={6}>
                      <Form.Group controlId="contract">
                        <Form.Label className="small fw-bold text-muted mb-1">Договір:</Form.Label>
                          <Form.Select 
                            aria-label="Договір" 
                            size="sm"
                            name="contract_id"
                            value={formData.contract_id}
                            onChange={handleChange}
                          >
                            <option value="">Виберіть договір...</option>
                            {contracts.map((contract) => (
                                <option key={contract.id} value={contract.id}>
                                    {contract.name}
                                </option>
                            ))}
                          </Form.Select>
                      </Form.Group>
                  </Col>
                  <Col md={6}>
                      <Form.Group controlId="warehouse">
                        <Form.Label className="small fw-bold text-muted mb-1">Склад:</Form.Label>
                          <Form.Select 
                            aria-label="Склад" 
                            size="sm"
                            name="warehouse_id"
                            value={formData.warehouse_id}
                            onChange={handleChange}
                          >
                            <option value="">Виберіть склад...</option>
                            {warehouses.map((warehouse) => (
                                <option key={warehouse.id} value={warehouse.id}>
                                    {warehouse.name}
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

export default GoodsReceivedNoteNavigation