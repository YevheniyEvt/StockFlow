import enum

class ProductMovementStatus(enum.Enum):
    SELLING = "selling"
    PURCHASE = "purchase"


class FinancialOperationsStatus(enum.Enum):
    DEBITING = "debiting"
    CREDITING = "crediting"