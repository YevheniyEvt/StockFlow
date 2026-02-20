from flaskr.directory import directory_bp

from flaskr.directory.views import (
    OrganizationDetailAPI,
    OrganizationListAPI,
    OrganizationUpdateAPI,
    OrganizationCreateAPI,
    OrganizationDeleteAPI,
)


directory_bp.add_url_rule(
    "/organizations",
    view_func=OrganizationListAPI.as_view("organization_list"), methods=['GET']
)

directory_bp.add_url_rule(
    "/organizations/create",
    view_func=OrganizationCreateAPI.as_view("organization_create"), methods=['POST']
)

directory_bp.add_url_rule(
    "/organizations/<int:id>",
    view_func=OrganizationDetailAPI.as_view("organization_detail"), methods=['GET']
)

directory_bp.add_url_rule(
    "/organizations/<int:id>/update",
    view_func=OrganizationUpdateAPI.as_view("organization_update"), methods=['PATCH']
)

directory_bp.add_url_rule(
    "/organizations/<int:id>/delete",
    view_func=OrganizationDeleteAPI.as_view("organization_delete"), methods=['DELETE']
)



