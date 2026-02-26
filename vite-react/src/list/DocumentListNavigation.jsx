import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import { InputGroup } from 'react-bootstrap';

function DocumentListNavigation(){
    return (
        <div className="nav-toolbar border-bottom shadow-sm">
            <Form className="mb-3">
                <Row className="g-3 align-items-center">
                    <Col xs={12} md={5}>
                        <InputGroup size="sm">
                            <InputGroup.Text id="partner-check">
                                <Form.Check type="checkbox" id="check-partner" />
                            </InputGroup.Text>
                            <InputGroup.Text className="bg-white border-end-0">Контрагент</InputGroup.Text>
                            <Form.Select aria-label="Вибір контрагента" className="border-start-0">
                                <option>Виберіть контрагента...</option>
                                <option value="1">ТОВ "Альфа"</option>
                                <option value="2">ФОП Петренко</option>
                                <option value="3">ТОВ "Бета"</option>
                            </Form.Select>
                        </InputGroup>
                    </Col>
                    <Col xs={12} md={5}>
                        <InputGroup size="sm">
                            <InputGroup.Text id="org-check">
                                <Form.Check type="checkbox" id="check-org" />
                            </InputGroup.Text>
                            <InputGroup.Text className="bg-white border-end-0">Організація</InputGroup.Text>
                            <Form.Select aria-label="Вибір організації" className="border-start-0">
                                <option>Виберіть організацію...</option>
                                <option value="1">ПП "Моя Компанія"</option>
                            </Form.Select>
                        </InputGroup>
                    </Col>
                </Row>
            </Form>
            
            <Row className="g-2 align-items-center">
                <Col xs="auto">
                    <Button variant="primary" size="sm" className="btn-icon">
                        <i className="bi bi-plus-lg"></i> Створити
                    </Button>
                </Col>
                <Col className="ms-auto" xs={12} sm={6} md={4}>
                    <InputGroup size="sm">
                        <InputGroup.Text className="bg-white border-end-0">
                            <i className="bi bi-search text-muted"></i>
                        </InputGroup.Text>
                        <Form.Control 
                            type="text" 
                            placeholder="Пошук документів..." 
                            className="border-start-0"
                        />
                    </InputGroup>
                </Col>
            </Row>
        </div>
    );
}

export default DocumentListNavigation;