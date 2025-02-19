from data.connect import get_connection, release_connection


def find_by_name_type_and_product(name, variation_type, product_id):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM variation v WHERE v.variation_name = %s AND v.variation_type = %s AND v.product_id = %s;",
                    (name, variation_type, product_id),
                )
                return cursor.fetchone()
    finally:
        release_connection(conn)


def save(variation):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO variation
                        (variation_id, product_id, variation_type, variation_name, created_at,
                         price, description, bag_size, size, weight, unit)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                    """,
                    (
                        variation.variation_id,
                        variation.product_id,
                        variation.variation_type,
                        variation.variation_name,
                        variation.created_at,
                        variation.price,
                        variation.variation_description,
                        variation.bag_size,
                        variation.size,
                        variation.weight,
                        variation.unit,
                    ),
                )
    finally:
        release_connection(conn)
