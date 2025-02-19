from dataclasses import dataclass
from math import isnan
from typing import Optional

import pandas as pd


@dataclass
class Variation:
    variation_id: str
    product_id: str
    variation_name: str
    variation_type: str
    price: float
    variation_description: Optional[str]
    bag_size: Optional[float]
    size: Optional[object]
    weight: Optional[float]
    unit: Optional[float]
    created_at: object

    def __post_init__(self):
        if self.bag_size is not None and isinstance(self.bag_size, float) and isnan(self.bag_size):
            self.bag_size = None
        if self.size is not None and isinstance(self.size, float) and pd.isna(self.size):
            self.size = None
        if self.weight is not None and isinstance(self.weight, float) and isnan(self.weight):
            self.weight = None
        if self.unit is not None and isinstance(self.unit, float) and isnan(self.unit):
            self.unit = None
