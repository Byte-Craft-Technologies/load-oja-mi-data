import os
import uuid

import pandas as pd
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader

from data.file_util import save_image
from model.category import Category
from repositories.category_repository import find_by_name, save_category


def read_excel_sheet():
    
    workbook = load_workbook("output_with_images.xlsx")
    workbook_sheet = workbook["Category"]
    
    image_loader = SheetImageLoader(workbook_sheet)
    
    dataframe = pd.read_excel("output_with_images.xlsx",sheet_name="Category")
    
    for index, row in dataframe.iterrows():
        
        category_name = row["categoryName"]
        cell_address = f"B{index + 2}"
        
        if image_loader.image_in(cell_address):
            image_url = save_image(image_loader.get(cell_address),category_name.lower(),"category")
        
        category_by_name = find_by_name(category_name)
        if category_by_name is None:
            description = row["description"] if row["description"] is not None else ""
            category = Category(
                id= str(uuid.uuid4()),
                name= category_name,
                image_url= image_url,
                created_at= pd.Timestamp.now(),
                description= description)
            
            save_category(category)
            

