
from llm_extractor import StructuredPreferences
from database.queries import search_places


def retrieve_places(preferences: StructuredPreferences):
    """
    Retrieve places from PostgreSQL based on the user's
    extracted preferences.
    """

    places = search_places(
        budget=preferences.budget,
        category=preferences.preferred_category,
        subcategory=preferences.preferred_subcategory,
        location=preferences.preferred_location,
        min_rating=preferences.min_rating,
        max_duration=preferences.max_duration,
        activity_preference=preferences.activity_preference,
        opening_hours=preferences.opening_hours
    )

    return places


