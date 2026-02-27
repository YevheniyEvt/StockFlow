import { useState, useEffect } from 'react';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import axios from 'axios';

function ItemModal({ show, onHide, onSave, item, documentId, type, organizationId, documentType }) {
    const [formData, setFormData] = useState({
        quantity: 1,
        product_id: "",
        service_id: "",
        selling_price: ""
    });
    const [options, setOptions] = useState([]);

    useEffect(() => {
        if (show) {
            fetchOptions();
            if (item) {
                setFormData({
                    quantity: item.quantity,
                    product_id: item.product?.id || "",
                    service_id: item.service?.id || "",
                    selling_price: item.selling_price || ""
                });
            } else {
                setFormData({
                    quantity: 1,
                    product_id: "",
                    service_id: "",
                    selling_price: ""
                });
            }
        }
    }, [show, item, type, organizationId]);

    const fetchOptions = async () => {
        try {
            const endpoint = type === 'product' ? '/api/nomenclature/products' : '/api/nomenclature/services';
            const response = await axios.get(endpoint, {
                params: { organization_id: organizationId }
            });
            setOptions(response.data);
        } catch (error) {
            console.error(`Error fetching ${type}s:`, error);
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));

        if ((name === 'product_id' || name === 'service_id') && value !== "") {
            const selectedOption = options.find(o => o.id === parseInt(value));
            if (selectedOption) {
                setFormData(prev => ({
                    ...prev,
                    selling_price: selectedOption.selling_price
                }));
            }
        }
    };

    const handleSave = async () => {
        try {
            if (item) {
                // Update existing item
                const response = await axios.patch(`/api/documents/document_item/${item.id}/update`, {
                    quantity: parseFloat(formData.quantity),
                    selling_price: documentType !== 'goods_received_note' ? parseFloat(formData.selling_price) : null,
                    purchase_price: documentType === 'goods_received_note' ? parseFloat(formData.selling_price): null
                });
                onSave(response.data);
            } else {
                // Create new item
                const data = {
                    document_id: documentId,
                    quantity: parseFloat(formData.quantity),
                    selling_price: documentType !== 'goods_received_note' ? parseFloat(formData.selling_price) : null,
                    purchase_price: documentType === 'goods_received_note' ? parseFloat(formData.selling_price): null
                };
                if (type === 'product') {
                    data.product_id = parseInt(formData.product_id);
                } else {
                    data.service_id = parseInt(formData.service_id);
                }
                const response = await axios.post('/api/documents/document_item/create', data);
                onSave(response.data);
            }
            onHide();
        } catch (error) {
            console.error("Error saving item:", error);
            alert("Помилка при збереженні");
        }
    };

    return (
        <Modal show={show} onHide={onHide}>
            <Modal.Header closeButton>
                <Modal.Title>{item ? 'Редагувати' : 'Додати'} {type === 'product' ? 'товар' : 'послугу'}</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Group className="mb-3">
                        <Form.Label>{type === 'product' ? 'Товар' : 'Послуга'}</Form.Label>
                        <Form.Select 
                            name={type === 'product' ? 'product_id' : 'service_id'}
                            value={type === 'product' ? formData.product_id : formData.service_id}
                            onChange={handleChange}
                            disabled={!!item}
                        >
                            <option value="">Виберіть...</option>
                            {options.map(opt => (
                                <option key={opt.id} value={opt.id}>{opt.name}</option>
                            ))}
                        </Form.Select>
                    </Form.Group>
                    <Row>
                        <Col md={6}>
                            <Form.Group className="mb-3">
                                <Form.Label>Кількість</Form.Label>
                                <Form.Control 
                                    type="number" 
                                    name="quantity"
                                    value={formData.quantity}
                                    onChange={handleChange}
                                />
                            </Form.Group>
                        </Col>
                        <Col md={6}>
                            <Form.Group className="mb-3">
                                <Form.Label>Ціна</Form.Label>
                                <Form.Control 
                                    type="number" 
                                    name="selling_price"
                                    value={formData.selling_price}
                                    onChange={handleChange}
                                />
                            </Form.Group>
                        </Col>
                    </Row>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={onHide}>Скасувати</Button>
                <Button variant="primary" onClick={handleSave}>Зберегти</Button>
            </Modal.Footer>
        </Modal>
    );
}

export default ItemModal;
