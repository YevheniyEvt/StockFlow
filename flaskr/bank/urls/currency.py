from flaskr.bank import bank_bp

from flaskr.bank.views import (
    CurrencyDetailAPI,
    CurrencyListAPI,
    CurrencyUpdateAPI,
    CurrencyCreateAPI,

)

bank_bp.add_url_rule(
    "/currency",
    view_func=CurrencyListAPI.as_view("currency_list"), methods=['GET']
)

bank_bp.add_url_rule(
    "/currency/<int:id>",
    view_func=CurrencyDetailAPI.as_view("currency_detail"), methods=['GET']
)

bank_bp.add_url_rule(
    "/currency/create",
    view_func=CurrencyCreateAPI.as_view("currency_create"), methods=['POST']
)

bank_bp.add_url_rule(
    "/currency/<int:id>/update",
    view_func=CurrencyUpdateAPI.as_view("currency_update"), methods=['PATCH']
)


