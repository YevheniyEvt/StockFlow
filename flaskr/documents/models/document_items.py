from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from flaskr import db
from flaskr.core.mixins import ItemsMixin, CreatedUpdatedDateTimeMixin

__all__ = (
    'DocumentItem',
)


class DocumentItem(ItemsMixin, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = "document_item"

    document_id: Mapped[int] = mapped_column(ForeignKey("document.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=True)
    service_id: Mapped[int] = mapped_column(ForeignKey("service.id"), nullable=True)

    document: Mapped["Document"] = relationship(back_populates="items")
    product: Mapped["Product"] = relationship(back_populates="document_products")
    service: Mapped["Service"] = relationship("Service", back_populates="document_services")