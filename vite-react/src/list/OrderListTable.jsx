import Table from 'react-bootstrap/Table';

function OrderListTable({ elements, onRowDoubleClick }) {
    return (
        <div className="table-container m-3">
            <Table hover responsive className="custom-table mb-0">
              <thead>
                <tr>
                  <th>Дата</th>
                  <th>Номер</th>
                  <th>Вид операції</th>
                  <th className="text-end">Сума</th>
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
                        onClick={() => {}} // Можна додати одинарний клік для виділення
                        onDoubleClick={() => onRowDoubleClick(element)}
                        style={{ cursor: 'pointer' }}
                    >
                        <td>{element.date}</td>
                        <td><span className="fw-bold">{element.number}</span></td>
                        <td>{element.typeOperation}</td>
                        <td className="text-end fw-bold">{element.amount.toLocaleString('uk-UA', { minimumFractionDigits: 2 })}</td>
                        <td><small className="text-muted">{element.curency}</small></td>
                        <td>{element.countparty}</td>
                        <td>{element.warhouse}</td>
                        <td>{element.organization}</td>
                    </tr>
                ))}
              </tbody>
            </Table>
        </div>
    )
}
export default OrderListTable;





















