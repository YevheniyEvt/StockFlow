from flaskr.directory import directory_bp

from flaskr.directory.views import (
    ContractDetailAPI,
    ContractListAPI,
    ContractUpdateAPI,
    ContractCreateAPI,
    ContractDeleteAPI,
)

directory_bp.add_url_rule(
    "/contracts",
    view_func=ContractListAPI.as_view("contract_list"), methods=['GET']
)

directory_bp.add_url_rule(
    "/contracts/create",
    view_func=ContractCreateAPI.as_view("contract_create"), methods=['POST']
)

directory_bp.add_url_rule(
    "/contracts/<int:id>",
    view_func=ContractDetailAPI.as_view("contract_detail"), methods=['GET']
)

directory_bp.add_url_rule(
    "/contracts/<int:id>/update",
    view_func=ContractUpdateAPI.as_view("contract_update"), methods=['PATCH']
)

directory_bp.add_url_rule(
    "/contracts/<int:id>/delete",
    view_func=ContractDeleteAPI.as_view("contract_delete"), methods=['DELETE']
)



