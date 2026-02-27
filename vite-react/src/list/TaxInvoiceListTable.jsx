import Table from 'react-bootstrap/Table';

function TaxInvoiceListTable({ elements, onRowDoubleClick }) {
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
                    <td><span className="fw-bold">{element.id}</span></td>
                    <td>{element.operation_type?.name}</td>
                    <td>{element.amount.toFixed(2)}</td>
                    <td><small className="text-muted">-----</small></td>
                    <td>{element.counterparty?.name}</td>
                    <td>{element.warehouse?.name}</td>
                    <td>{element.organization?.name}</td>
                </tr>
            ))}
          </tbody>
        </Table>
    )
}
export default TaxInvoiceListTable;





















