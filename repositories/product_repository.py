from data.connect import get_connection, release_connection


def find_by_name(name):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM product p WHERE p.product_name = %s;",
                    (name,),
                )
                return cursor.fetchone()
    finally:
        release_connection(conn)


def save(product):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO product
                        (product_id, product_name, product_image_url, created_at, category_id, is_deleted)
                    VALUES (%s, %s, %s, %s, %s, false);
                    """,
                    (
                        product.product_id,
                        product.name,
                        product.image_url,
                        product.created_at,
                        product.category_id,
                    ),
                )
    finally:
        release_connection(conn)
