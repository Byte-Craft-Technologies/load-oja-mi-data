import uuid

import pandas as pd

from config import EXCEL_FILE
from model.variation import Variation
from repositories import product_repository, variation_repository


def save():
    dataframe = pd.read_excel(EXCEL_FILE, sheet_name="Variation")

    for index, row in dataframe.iterrows():
        variation_name = row["variationName"]
        variation_type = row["variationType"]
        product_name = row["productName"]

        product_by_name = product_repository.find_by_name(product_name)
        if product_by_name is None:
            continue

        variation_by_name_and_type = variation_repository.find_by_name_type_and_product(
            variation_name, variation_type, product_by_name[0]
        )
        if variation_by_name_and_type is not None:
            continue

        variation = Variation(
            variation_id=str(uuid.uuid4()),
            product_id=product_by_name[0],
            variation_type=variation_type,
            variation_name=variation_name,
            created_at=pd.Timestamp.now(),
            price=row["price"],
            variation_description=row["variationDescription"],
            bag_size=row["bagSize"],
            size=row["size"],
            weight=row["weight"],
            unit=row["unit"],
        )
        variation_repository.save(variation)
