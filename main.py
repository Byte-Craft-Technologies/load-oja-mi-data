import persist_category
import persist_product
import persist_variation
from download import download_excel


def main():
    download_excel()
    persist_category.save()
    persist_product.save()
    persist_variation.save()
    
if __name__ == "__main__":
    main()