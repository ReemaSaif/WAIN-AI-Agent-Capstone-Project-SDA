
from llm_extractor import extract_preferences
from retrieval import retrieve_places
from ranking import rank_places
from generate_final_response import generate_final_response


def run_wain(user_message):
    """
    Run the complete WAIN recommendation pipeline.

    1. Extract user preferences from the user's message.
    2. Retrieve matching places from PostgreSQL.
    3. Rank the retrieved places.
    4. Generate the final natural-language response.
    5. Return the preferences, ranked results, and final response.
    """

    # 1. Extract preferences
    preferences = extract_preferences(user_message)
    preferences_dict = preferences.model_dump()

    # 2. Retrieve matching places from PostgreSQL
    results = retrieve_places(preferences)

    # 3. Rank the retrieved places
    ranked_results = rank_places(
        places=results,
        preferences=preferences_dict,
        limit=10
    )

    # 4. Generate the final natural-language response
    final_response = generate_final_response(
        user_question=user_message,
        preferences=preferences_dict,
        ranked_places=ranked_results
    )

    # 5. Return all results
    return {
        "user_message": user_message,
        "preferences": preferences_dict,
        "results": ranked_results,
        "final_response": final_response
    }


