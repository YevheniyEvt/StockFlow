import enum


class DocumentType(enum.Enum):
    GOODS_RECEIVED_NOTE = "goods_received_note"
    ORDER = "order"
    INVOICE = "invoice"
    GOODS_DELIVERY_NOTE = "goods_delivery_note"
    TAX_INVOICE = "tax_invoice"


class GoodsReceivedNoteStatus(enum.Enum):
    DRAFT = "draft"
    HELD = "held"
    CANCELED = "canceled"


class OrderStatus(enum.Enum):
    DRAFT = "draft"
    CONFIRMED_BY_CLIENT = "confirmed_by_client"


class InvoiceStatus(enum.Enum):
    DRAFT = "draft"
    INVOICED = "invoiced"
    PARTIALLY_PAID = "partially_paid"
    PAID = "paid"
    OVERDUE = "overdue"
    CANCELED = "canceled"


class GoodsDeliveryNoteStatus(enum.Enum):
    DRAFT = "draft"
    SENT = "sent"
    SIGNED = "signed"
    HELD = "held"
    REJECTED = "rejected"
    REFUND = "refund"


class TaxInvoiceStatus(enum.Enum):
    DRAFT = "draft"
    REGISTERED = "registered"
    REJECTED = "rejected"
