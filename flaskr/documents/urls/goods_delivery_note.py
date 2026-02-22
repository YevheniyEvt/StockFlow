from flaskr.documents import documents_bp

from flaskr.documents.views import (
    GoodsDeliveryNoteDetailAPI,
    GoodsDeliveryNoteListAPI,
    GoodsDeliveryNoteUpdateAPI,
    GoodsDeliveryNoteChangeStatusAPI,
    GoodsDeliveryNoteCreateAPI,

)

documents_bp.add_url_rule(
    "/goods_delivery_notes",
    view_func=GoodsDeliveryNoteListAPI.as_view("goods_delivery_note_list"), methods=['GET']
)

documents_bp.add_url_rule(
    "/goods_delivery_notes/<int:id>",
    view_func=GoodsDeliveryNoteDetailAPI.as_view("goods_delivery_note_detail"), methods=['GET']
)

documents_bp.add_url_rule(
    "/goods_delivery_notes/create",
    view_func=GoodsDeliveryNoteCreateAPI.as_view("goods_delivery_note_create"), methods=['POST']
)

documents_bp.add_url_rule(
    "/goods_delivery_notes/<int:id>/update",
    view_func=GoodsDeliveryNoteUpdateAPI.as_view("goods_delivery_note_update"), methods=['PATCH']
)

documents_bp.add_url_rule(
    "/goods_delivery_notes/<int:id>/update-status",
    view_func=GoodsDeliveryNoteChangeStatusAPI.as_view("goods_delivery_note_update_status"), methods=['PATCH']
)



