

import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Table from 'react-bootstrap/Table';

function BankAccounts({ document }){
    const companyAccounts = document.organization?.bank_accounts || [];
    const counterpartyAccounts = document.counterparty?.bank_accounts || [];

    return (
        <Row>
            <Col md={6}>
                <h6 className="fw-bold mb-3">Банківські рахунки організації</h6>
                <Table bordered hover size="sm" className="small">
                    <thead>
                        <tr>
                            <th>Назва</th>
                            <th>Рахунок</th>
                            <th>Банк</th>
                            <th>Валюта</th>
                        </tr>
                    </thead>
                    <tbody>
                        {companyAccounts.length > 0 ? companyAccounts.map(acc => (
                            <tr key={acc.id}>
                                <td>{acc.name}</td>
                                <td>{acc.checking_account}</td>
                                <td>{acc.bank}</td>
                                <td>{acc.currency?.name}</td>
                            </tr>
                        )) : (
                            <tr>
                                <td colSpan="4" className="text-center text-muted">Дані відсутні</td>
                            </tr>
                        )}
                    </tbody>
                </Table>
            </Col>
            <Col md={6}>
                <h6 className="fw-bold mb-3">Банківські рахунки контрагента</h6>
                <Table bordered hover size="sm" className="small">
                    <thead>
                        <tr>
                            <th>Назва</th>
                            <th>Рахунок</th>
                            <th>Банк</th>
                            <th>Валюта</th>
                        </tr>
                    </thead>
                    <tbody>
                        {counterpartyAccounts.length > 0 ? counterpartyAccounts.map(acc => (
                            <tr key={acc.id}>
                                <td>{acc.name}</td>
                                <td>{acc.checking_account}</td>
                                <td>{acc.bank}</td>
                                <td>{acc.currency?.name}</td>
                            </tr>
                        )) : (
                            <tr>
                                <td colSpan="4" className="text-center text-muted">Дані відсутні</td>
                            </tr>
                        )}
                    </tbody>
                </Table>
            </Col>
        </Row>
    )
}

export default BankAccounts;