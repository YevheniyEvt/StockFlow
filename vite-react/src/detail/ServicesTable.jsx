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
                        style={{ cursor: 'pointer' }}
                    >
                        <td>{index + 1}</td>
                        <td>{item.product.name}</td>
                        <td>{item.quantity}</td>
                        <td>{item.product.units_of_measurement_id}</td>
                        <td>{item.product.multiplicity}</td>
                        <td>{item.selling_price.toFixed(2)}</td>
                        <td>{(item.amount * (item.discount/100)).toFixed(2)}</td>
                        <td>{item.discount.toFixed(0)}</td>
                        <td>{(item.amount - (item.amount * (item.discount/100))).toFixed(2)}</td>
                        <td>{((item.amount - (item.amount * (item.discount/100)))*0.2).toFixed(2)}</td>
                    </tr>
                ))}
              </tbody>
        </Table>
        </>

    )
}

export default ServicesTable;