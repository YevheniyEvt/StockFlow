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
                        <td><span className="fw-bold">{element.id}</span></td>
                        <td>{element.operation_type?.name}</td>
                        <td>{element.amount.toFixed(2)}</td>
                        <td>{element.counterparty?.bank_accounts?.[0]?.currency?.name || <small className="text-muted">-----</small>}</td>
                        <td>{element.counterparty?.name}</td>
                        <td>{element.warehouse?.name}</td>
                        <td>{element.organization?.name}</td>
                        <td>{element.contract?.name}</td>
                    </tr>
                ))}
              </tbody>
            </Table>
        </div>
    )
}
export default OrderListTable;





















