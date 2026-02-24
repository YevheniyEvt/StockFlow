from flaskr.documents import documents_bp

from flaskr.documents.views import (
    GoodsReceivedNoteDetailAPI,
    GoodsReceivedNoteListAPI,
    GoodsReceivedNoteUpdateAPI,
    GoodsReceivedNoteChangeStatusAPI,
    GoodsReceivedNoteCreateAPI,
    HeldGodsReceivedNote,
)

documents_bp.add_url_rule(
    "/goods_received_notes",
    view_func=GoodsReceivedNoteListAPI.as_view("goods_received_note_list"), methods=['GET']
)

documents_bp.add_url_rule(
    "/goods_received_notes/<int:id>",
    view_func=GoodsReceivedNoteDetailAPI.as_view("goods_received_note_detail"), methods=['GET']
)

documents_bp.add_url_rule(
    "/goods_received_notes/create",
    view_func=GoodsReceivedNoteCreateAPI.as_view("goods_received_note_create"), methods=['POST']
)

documents_bp.add_url_rule(
    "/goods_received_notes/<int:id>/update",
    view_func=GoodsReceivedNoteUpdateAPI.as_view("goods_received_note_update"), methods=['PATCH']
)

documents_bp.add_url_rule(
    "/goods_received_notes/<int:id>/update-status",
    view_func=GoodsReceivedNoteChangeStatusAPI.as_view("goods_received_note_update_status"), methods=['PATCH']
)

documents_bp.add_url_rule(
    "/goods_received_notes/<int:id>/held",
    view_func=HeldGodsReceivedNote.as_view("goods_received_note_held"), methods=['POST']
)



