from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    product_id: str
    name: str
    image_url: Optional[str]
    created_at: object
    category_id: str
    description: Optional[str]
    is_deleted: bool = False
