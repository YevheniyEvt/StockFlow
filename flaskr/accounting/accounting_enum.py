import enum

class ProductMovementType(enum.Enum):
    SELLING = "selling"
    PURCHASE = "purchase"


class FinancialOperationsStatus(enum.Enum):
    DEBITING = "debiting"
    CREDITING = "crediting"