from data.connect import connect_to_db


def find_by_name(name):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM product_category c where c.category_name = %s;",(name,))
    row = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return row
def save_category(category):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO product_category (category_id, category_image_url, category_name, created_at, description,is_deleted)
        VALUES (%s, %s, %s, %s, %s,false);
        """,
        (category.id, category.image_url, category.name, category.created_at, category.description)
    )
    connection.commit()
    cursor.close()
    connection.close()