from dataclasses import dataclass, field
from typing import Optional

import pandas as pd


@dataclass
class Category:
    category_id: str
    category_name: str
    image_url: Optional[str]
    created_at: object
    description: Optional[str]
    is_deleted: bool = False

    def __post_init__(self):
        if self.description is not None and isinstance(self.description, float) and pd.isna(self.description):
            self.description = None
