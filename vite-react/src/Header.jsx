import CloseButton from 'react-bootstrap/CloseButton';

function Header({ name, document, onBack, onForward, onClose }) {
    let date = document ? document.document_date : '';
    let displayDate = date ? `від ${new Date(date).toLocaleDateString('uk-UA')}` : '';
    let number = document ? document.id : '';
    let displayNumber = number ? `№${number}` : '';

    const getStatusDisplay = (status) => {
        if (!status) return null;
        
        const statusMap = {
            'confirmed_by_client': { text: 'Підтверджено', color: 'text-success' },
            'held': { text: 'Проведено', color: 'text-success' },
            'paid': { text: 'Оплачено', color: 'text-success' },
            'registered': { text: 'Зареєстровано', color: 'text-success' },
            'draft': { text: 'Чернетка', color: 'text-muted' }
        };

        const display = statusMap[status.toLowerCase()] || { text: status, color: 'text-secondary' };
        return <span className={`${display.color} ms-2 small fw-normal`}>({display.text})</span>;
    };

    return (
        <div className="app-header d-flex justify-content-between align-items-center px-3 border-bottom">
            <div className="d-flex align-items-center">
                <div className="nav-arrows me-3">
                    <button 
                        className="btn btn-link p-0 text-dark me-2" 
                        onClick={onBack}
                        title="Назад"
                    >
                        <i className="bi bi-arrow-left-short fs-3"></i>
                    </button>
                    <button 
                        className="btn btn-link p-0 text-dark" 
                        onClick={onForward}
                        title="Вперед"
                    >
                        <i className="bi bi-arrow-right-short fs-3"></i>
                    </button>
                </div>
                <h5 className="mb-0 fw-bold">
                    {name} <span className="text-primary mx-1">{displayNumber}</span> {displayDate}
                    {document && getStatusDisplay(document.status)}
                </h5>
            </div>
            <div className="d-flex align-items-center gap-2">
                {/*<button className="btn btn-sm btn-outline-secondary d-none d-md-inline-block me-2">*/}
                {/*    <i className="bi bi-printer me-1"></i> Друк*/}
                {/*</button>*/}
                <CloseButton onClick={onClose} className="ms-2" />
            </div>
        </div>
    );
}

export default Header;