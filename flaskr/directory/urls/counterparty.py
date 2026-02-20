from . import directory_bp

from flaskr.directory.views import (
    CounterpartyDetailAPI,
    CounterpartyListAPI,
    CounterpartyUpdateAPI,
    CounterpartyCreateAPI,
    CounterpartyDeleteAPI,
)

directory_bp.add_url_rule(
    "/counterparts",
    view_func=CounterpartyListAPI.as_view("counterparty_list"), methods=['GET']
)

directory_bp.add_url_rule(
    "/counterparts/create",
    view_func=CounterpartyCreateAPI.as_view("counterparty_create"), methods=['POST']
)

directory_bp.add_url_rule(
    "/counterparts/<int:id>",
    view_func=CounterpartyDetailAPI.as_view("counterparty_detail"), methods=['GET']
)

directory_bp.add_url_rule(
    "/counterparts/<int:id>/update",
    view_func=CounterpartyUpdateAPI.as_view("counterparty_update"), methods=['PATCH']
)

directory_bp.add_url_rule(
    "/counterparts/<int:id>/delete",
    view_func=CounterpartyDeleteAPI.as_view("counterparty_delete"), methods=['DELETE']
)



