from flaskr.bank import bank_bp

from flaskr.bank.views import (
    BankAccountCompanyDetailAPI,
    BankAccountCompanyListAPI,
    BankAccountCompanyUpdateAPI,
    BankAccountCompanyCreateAPI,

)

bank_bp.add_url_rule(
    "/bank_account_company",
    view_func=BankAccountCompanyListAPI.as_view("bank_account_company_list"), methods=['GET']
)

bank_bp.add_url_rule(
    "/bank_account_company/<int:id>",
    view_func=BankAccountCompanyDetailAPI.as_view("bank_account_company_detail"), methods=['GET']
)

bank_bp.add_url_rule(
    "/bank_account_company/create",
    view_func=BankAccountCompanyCreateAPI.as_view("bank_account_company_create"), methods=['POST']
)

bank_bp.add_url_rule(
    "/bank_account_company/<int:id>/update",
    view_func=BankAccountCompanyUpdateAPI.as_view("bank_account_company_update"), methods=['PATCH']
)


