from pydantic import BaseModel

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.documents.models.document_enum import GoodsDeliveryNoteStatus
from flaskr.documents.models import (
    GoodsDeliveryNote,
)

from flaskr.documents.services.mixin import DocumentsAllMixin, CreateDocumentItemMixin
from flaskr.accounting.services.movements import MovementService

__all__ = (
    'GoodsDeliveryNoteService',
)



class GoodsDeliveryNoteService(DocumentsAllMixin, CreateDocumentItemMixin, BaseService[GoodsDeliveryNote]):
    model = GoodsDeliveryNote

    @classmethod
    def create(cls, *args, **kwargs):
        goods_delivery_note = super().create(*args, **kwargs, commit=False)
        invoice = goods_delivery_note.invoice
        
        goods_delivery_note.counterparty_id = invoice.counterparty_id
        goods_delivery_note.warehouse_id = invoice.warehouse_id
        goods_delivery_note.operation_type_id = invoice.operation_type_id
        goods_delivery_note.contract_id = invoice.contract_id
        goods_delivery_note.comment = invoice.comment
        goods_delivery_note.amount = invoice.amount

        for item in invoice.items:
            cls._create_document_item(item, goods_delivery_note.id)
        db.session.commit()
        db.session.refresh(goods_delivery_note)
        return goods_delivery_note


    @classmethod
    def change_status(cls, note_id: int, status: str):
        note = cls.get_or_404(note_id)
        pre_update_status = note.status
        new_status = GoodsDeliveryNoteStatus(status)

        status_change_to_held = (new_status == GoodsDeliveryNoteStatus.HELD and
                                 pre_update_status != GoodsDeliveryNoteStatus.HELD)

        if status_change_to_held:
            try:
                for item in note.items:
                    MovementService.create_selling(item, commit=False)
                note.status = GoodsDeliveryNoteStatus.HELD
                db.session.commit()
            except Exception:
                db.session.rollback()
                raise
        else:
            note.status = new_status
            db.session.commit()
        return note