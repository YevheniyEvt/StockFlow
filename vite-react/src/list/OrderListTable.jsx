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
                  <th>Контракт</th>
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
                        <td>{new Date(element.document_date).toLocaleString('uk-UA')}</td>
                        <td><span className="fw-bold">ДО0000{element.id}</span></td>
                        <td>{element.operation_type_id}</td>
                        <td>{element.amount.toFixed(2)}</td>
                        <td><small className="text-muted">-----</small></td>
                        <td>{element.contract_id}</td>
                        <td>{element.warehouse_id}</td>
                        <td>{element.organization_id}</td>
                        <td>{element.contract_id}</td>
                    </tr>
                ))}
              </tbody>
            </Table>
        </div>
    )
}
export default OrderListTable;





















