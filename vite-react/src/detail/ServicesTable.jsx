import Button from "react-bootstrap/Button";
import Table from "react-bootstrap/Table";


function ServicesTable(props) {
    const buttonClass = props.canEdit === false ? 'd-none' : "ms-4 mb-2 mt-2"
    return (
        <>
            <div className={buttonClass}>
                <Button variant="outline-secondary shadow me-2" size="sm" >
                    Додати
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
                  <th>Сума з ПДВ</th>
                  <th>% ПДВ</th>
                  <th>Сума ПДВ</th>
                  <th>Всього</th>
                  <th>Рахунок</th>
                </tr>
              </thead>
              <tbody className="text-nowrap">
                {props.services.map((product, index) => (
                    <tr
                        key={product.id}
                        id={product.id}
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

export default ServicesTable;