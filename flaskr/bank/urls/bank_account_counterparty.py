from flaskr.bank import bank_bp

from flaskr.bank.views import (
    BankAccountCounterpartyDetailAPI,
    BankAccountCounterpartyListAPI,
    BankAccountCounterpartyUpdateAPI,
    BankAccountCounterpartyCreateAPI,

)

bank_bp.add_url_rule(
    "/bank_account_counterparty",
    view_func=BankAccountCounterpartyListAPI.as_view("bank_account_counterparty_list"), methods=['GET']
)

bank_bp.add_url_rule(
    "/bank_account_counterparty/<int:id>",
    view_func=BankAccountCounterpartyDetailAPI.as_view("bank_account_counterparty_detail"), methods=['GET']
)

bank_bp.add_url_rule(
    "/bank_account_counterparty/create",
    view_func=BankAccountCounterpartyCreateAPI.as_view("bank_account_counterparty_create"), methods=['POST']
)

bank_bp.add_url_rule(
    "/bank_account_counterparty/<int:id>/update",
    view_func=BankAccountCounterpartyUpdateAPI.as_view("bank_account_counterparty_update"), methods=['PATCH']
)


