import { useState } from "react";
import Button from "react-bootstrap/Button";
import Table from "react-bootstrap/Table";
import axios from 'axios';
import ItemModal from "./ItemModal.jsx";


function ServicesTable(props) {
    const [selectedId, setSelectedId] = useState(null);
    const [showModal, setShowModal] = useState(false);
    const [editingItem, setEditingItem] = useState(null);

    const handleRowClick = (id) => {
        setSelectedId(id);
    };

    const handleAdd = () => {
        setEditingItem(null);
        setShowModal(true);
    };

    const handleEdit = () => {
        if (selectedId) {
            const item = props.services.find(s => s.id === selectedId);
            setEditingItem(item);
            setShowModal(true);
        } else {
            alert("Будь ласка, виберіть рядок для редагування");
        }
    };

    const handleDelete = async () => {
        if (selectedId) {
            if (window.confirm("Ви впевнені, що хочете видалити цей рядок?")) {
                try {
                    await axios.delete(`/api/documents/document_item/${selectedId}/delete`);
                    if (props.onUpdate) {
                        const response = await axios.get(`/api/documents/${props.documentType}s/${props.documentId}`);
                        props.onUpdate(response.data);
                    }
                    setSelectedId(null);
                } catch (error) {
                    console.error("Error deleting item:", error);
                    alert("Помилка при видаленні");
                }
            }
        } else {
            alert("Будь ласка, виберіть рядок для видалення");
        }
    };

    const handleSaveItem = async (updatedItem) => {
        if (props.onUpdate) {
            try {
                const response = await axios.get(`/api/documents/${props.documentType}s/${props.documentId}`);
                props.onUpdate(response.data);
            } catch (error) {
                console.error("Error refreshing document:", error);
            }
        }
    };

    const buttonClass = props.canEdit === false ? 'd-none' : "ms-4 mb-2 mt-2"
    return (
        <>
            <div className={buttonClass}>
                <Button variant="outline-secondary shadow me-2" size="sm" onClick={handleAdd}>
                    Додати
                </Button>
                <Button 
                    variant="outline-secondary shadow me-2" 
                    size="sm"
                    onClick={handleEdit}
                    disabled={!selectedId}
                >
                    Змінити
                </Button>
                <Button 
                    variant="outline-secondary shadow me-2" 
                    size="sm"
                    onClick={handleDelete}
                    disabled={!selectedId}
                >
                    Видалити
                </Button>
            </div>
            <Table bordered hover responsive className="border m-2">
              <thead className="text-nowrap">
                <tr>
                  <th>№</th>
                  <th>Назва</th>
                  <th>Кількість</th>
                  <th>Од. вим.</th>
                  <th>Кратність</th>
                  <th>Ціна з ПДВ</th>
                  <th>Знижка</th>
                  <th>% Знижки</th>
                  <th>Сума з ПДВ</th>
                  <th>Сума ПДВ</th>
                </tr>
              </thead>
              <tbody className="text-nowrap">
                {props.services.map((item, index) => (
                    <tr
                        key={item.id}
                        id={item.id}
                        onClick={() => handleRowClick(item.id)}
                        className={selectedId === item.id ? "table-active" : ""}
                        style={{ cursor: 'pointer' }}
                    >
                        <td>{index + 1}</td>
                        <td>{item.service?.name}</td>
                        <td>{item.quantity}</td>
                        <td>{item.service?.units_of_measurement?.name}</td>
                        <td>{item.service?.multiplicity}</td>
                        <td>{item.selling_price.toFixed(2)}</td>
                        <td>{(item.amount * (item.discount/100)).toFixed(2)}</td>
                        <td>{item.discount.toFixed(0)}</td>
                        <td>{(item.amount - (item.amount * (item.discount/100))).toFixed(2)}</td>
                        <td>{((item.amount - (item.amount * (item.discount/100)))*0.2).toFixed(2)}</td>
                    </tr>
                ))}
              </tbody>
        </Table>

        <ItemModal 
            show={showModal}
            onHide={() => setShowModal(false)}
            onSave={handleSaveItem}
            item={editingItem}
            documentId={props.documentId}
            type="service"
            organizationId={props.organizationId}
        />
        </>

    )
}

export default ServicesTable;