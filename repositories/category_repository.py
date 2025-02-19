from data.connect import get_connection, release_connection


def find_by_name(name):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM product_category c WHERE c.category_name = %s;",
                    (name,),
                )
                return cursor.fetchone()
    finally:
        release_connection(conn)


def save_category(category):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO product_category
                        (category_id, category_image_url, category_name, created_at, description, is_deleted)
                    VALUES (%s, %s, %s, %s, %s, false);
                    """,
                    (
                        category.category_id,
                        category.image_url,
                        category.category_name,
                        category.created_at,
                        category.description,
                    ),
                )
    finally:
        release_connection(conn)
