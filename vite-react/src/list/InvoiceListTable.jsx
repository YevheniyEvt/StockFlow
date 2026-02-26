import Table from 'react-bootstrap/Table';

function InvoiceListTable({ elements, onRowDoubleClick }) {
    return (
            <Table striped bordered hover responsive className="border m-2">
              <thead>
                <tr>
                  <th>Дата</th>
                  <th>Номер</th>
                  <th>Вид операції</th>
                  <th>Сума</th>
                  <th>Валюта</th>
                  <th>Контрагент</th>
                  <th>Склад</th>
                  <th>Організація</th>
                </tr>
              </thead>
              <tbody className="text-nowrap">
                {elements.map((element) => (
                    <tr
                        key={element.id}
                        id={element.id}
                        style={{ cursor: 'pointer' }}
                        onDoubleClick={() => onRowDoubleClick(element)}
                    >
                        <td>{element.date}</td>
                        <td>{element.number}</td>
                        <td>{element.typeOperation}</td>
                        <td>{element.amount.toFixed(2)}</td>
                        <td>{element.curency}</td>
                        <td>{element.countparty}</td>
                        <td>{element.warhouse}</td>
                        <td>{element.organization}</td>
                    </tr>
                ))}
              </tbody>
            </Table>
    )
}
export default InvoiceListTable;





















