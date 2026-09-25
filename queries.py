from database.connection import get_connection

def search_places(
    budget=None,
    category=None,
    subcategory=None,
    location=None,
    min_rating=None,
    max_duration=None,
    activity_preference=None,
    opening_hours=None,
    limit=10
):

    """
       Search places from the PostgreSQL places table
       based on the preferences provided by the user.

       All filters are optional.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            id,
            place_name,
            category,
            subcategory,
            location,
            rating,
            estimated_cost_sar,
            price_level,
            duration_hours_needed,
            activity_type,
            opening_hours
        FROM places
        WHERE 1=1
    """

    parameters = []

    # Budget filter
    if budget is not None:
        query += """
            AND estimated_cost_sar <= %s
        """
        parameters.append(budget)


    # Category filter
    if category is not None:
        query += """
            AND LOWER(category) = LOWER(%s)
        """
        parameters.append(category)

    # Subcategory filter
    if subcategory is not None:
        query += """
            AND LOWER(subcategory) LIKE LOWER(%s)
        """
        parameters.append(f"%{subcategory}%")

    # Location filter
    if location is not None:
        query += """
            AND LOWER(location) LIKE LOWER(%s)
        """
        parameters.append(f"%{location}%")


    # Rating filter
    if min_rating is not None:
        query += """
            AND rating >= %s
        """
        parameters.append(min_rating)


    # Duration filter
    if max_duration is not None:
        query += """
            AND duration_hours_needed <= %s
        """
        parameters.append(max_duration)


    if activity_preference is not None:
        preferences = [
            p.strip()
            for p in activity_preference.split("/")
            if p.strip()
        ]

        for preference in preferences:
            query += """
                AND LOWER(activity_type) LIKE LOWER(%s)
            """
            parameters.append(f"%{preference}%")


    # Opening hours filter
    if opening_hours is not None:
        query += """
            AND LOWER(opening_hours) LIKE LOWER(%s)
        """
        parameters.append(f"%{opening_hours}%")


    # Sort retrieved results
    query += """
        ORDER BY rating DESC, estimated_cost_sar ASC
        LIMIT %s
    """
    parameters.append(limit)


    try:
        cursor.execute(query, parameters)
        rows = cursor.fetchall()

        return rows

    finally:
        cursor.close()
        connection.close()


