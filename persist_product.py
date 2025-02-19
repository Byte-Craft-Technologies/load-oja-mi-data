import uuid

import pandas as pd
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader

from config import EXCEL_FILE
from data.file_util import save_image
from model.product import Product
from repositories import category_repository, product_repository


def save():
    workbook = load_workbook(EXCEL_FILE)
    workbook_sheet = workbook["Product"]
    image_loader = SheetImageLoader(workbook_sheet)

    dataframe = pd.read_excel(EXCEL_FILE, sheet_name="Product")

    for index, row in dataframe.iterrows():
        product_name = row["productName"]
        category_name = row["categoryName"]

        category_by_name = category_repository.find_by_name(category_name)
        if category_by_name is None:
            continue

        cell_address = f"D{index + 2}"
        image_url = None  # initialised before the conditional to avoid UnboundLocalError
        if image_loader.image_in(cell_address):
            image_url = save_image(
                image_loader.get(cell_address),
                product_name.lower().replace(" ", "_"),
                "product",
            )

        product_by_name = product_repository.find_by_name(product_name)
        if product_by_name is not None:
            continue

        product = Product(
            product_id=str(uuid.uuid4()),
            name=product_name,
            image_url=image_url,
            created_at=pd.Timestamp.now(),
            description=row["description"],
            category_id=category_by_name[0],
        )
        product_repository.save(product)
