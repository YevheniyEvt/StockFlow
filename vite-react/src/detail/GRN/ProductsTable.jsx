import { useState } from "react";
import Table from "react-bootstrap/Table";
import Button from "react-bootstrap/Button";


function ProductsTable({products}){
    const [selectedId, setSelectedId] = useState(null);



    const handleRowClick = (id) => {
        setSelectedId(id);
    };

    const handleEdit = () => {
        if (selectedId) {
            console.log("Редагувати рядок з ID:", selectedId);
            alert(`Редагувати рядок з ID: ${selectedId}`);
        } else {
            alert("Будь ласка, виберіть рядок для редагування");
        }
    };

    const handleDelete = () => {
        if (selectedId) {
            console.log("Видалити рядок з ID:", selectedId);
            alert(`Видалити рядок з ID: ${selectedId}`);
        } else {
            alert("Будь ласка, виберіть рядок для видалення");
        }
    };

    return (
        <>
            <div className="ms-4 mb-2 mt-2">
                <Button variant="outline-secondary shadow me-2" size="sm" >
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
              <thead>
                <tr>
                  <th>№</th>
                  <th>Назва</th>
                  <th>Кількість</th>
                  <th>Од. вим.</th>
                  <th>Кратність</th>
                  <th>Ціна з ПДВ</th>
                  <th>Сума з ПДВ</th>
                  <th>% ПДВ</th>
                  <th>Сума ПДВ</th>
                  <th>Всього</th>
                  <th>Рахунок</th>
                </tr>
              </thead>
              <tbody>
                {products.map((product, index) => (
                    <tr 
                        key={product.id} 
                        id={product.id}
                        onClick={() => handleRowClick(product.id)}
                        className={selectedId === product.id ? "table-active" : ""}
                        style={{ cursor: 'pointer' }}
                    >
                        <td>{index + 1}</td>
                        <td>{product.name}</td>
                        <td>{product.quantity}</td>
                        <td>{product.unit}</td>
                        <td>{product.factor}</td>
                        <td>{product.price.toFixed(2)}</td>
                        <td>{product.amount.toFixed(2)}</td>
                        <td>{product.vatRate}</td>
                        <td>{product.vatAmount.toFixed(2)}</td>
                        <td>{product.total.toFixed(2)}</td>
                        <td>{product.account}</td>
                    </tr>
                ))}
              </tbody>
        </Table>
        </>

    )
}

export default ProductsTable;