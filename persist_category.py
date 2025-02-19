import uuid

import pandas as pd
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader

from config import EXCEL_FILE
from data.file_util import save_image
from model.category import Category
from repositories.category_repository import find_by_name, save_category


def save():
    workbook = load_workbook(EXCEL_FILE)
    workbook_sheet = workbook["Category"]
    image_loader = SheetImageLoader(workbook_sheet)

    dataframe = pd.read_excel(EXCEL_FILE, sheet_name="Category")

    for index, row in dataframe.iterrows():
        category_name = row["categoryName"]
        cell_address = f"B{index + 2}"

        image_url = None
        if image_loader.image_in(cell_address):
            image_url = save_image(
                image_loader.get(cell_address),
                category_name.lower().replace(" ", "_"),
                "category",
            )

        category_by_name = find_by_name(category_name)
        if category_by_name is not None:
            continue

        description = row["description"] if not pd.isna(row["description"]) else ""
        category = Category(
            category_id=str(uuid.uuid4()),
            category_name=category_name,
            image_url=image_url,
            created_at=pd.Timestamp.now(),
            description=description,
        )
        save_category(category)
