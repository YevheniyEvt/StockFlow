import Table from 'react-bootstrap/Table';

function InvoiceListTable({ elements, onRowDoubleClick }) {
    console.log(elements)
    return (
          <Table striped bordered hover responsive className="border m-2">
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
                    id={element.id}
                    style={{ cursor: 'pointer' }}
                    onDoubleClick={() => onRowDoubleClick(element)}
                >
                    <td>{new Date(element.document_date).toLocaleString('uk-UA')}</td>
                    <td><span className="fw-bold">ДО0000{element.id}</span></td>
                    <td>{element.operation_type_id}</td>
                    <td>{element.amount.toFixed(2)}</td>
                    <td><small className="text-muted">-----</small></td>
                    <td>{element.counterparty_id}</td>
                    <td>{element.warehouse_id}</td>
                    <td>{element.organization_id}</td>
                </tr>
            ))}
          </tbody>
        </Table>
    )
}
export default InvoiceListTable;





















