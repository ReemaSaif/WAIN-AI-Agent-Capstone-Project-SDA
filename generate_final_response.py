import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the .env file.")

client = OpenAI(api_key=api_key)


def generate_final_response(user_question, preferences, ranked_places):
    """
    Generate a natural-language recommendation response from
    ranked PostgreSQL results.

    The LLM must use only the information provided in ranked_places
    and must not invent facts.
    """

    # No matching results
    if not ranked_places:

        budget = preferences.get("budget")
        location = preferences.get("preferred_location")
        activity = preferences.get("activity_preference")
        category = preferences.get("preferred_category")
        subcategory = preferences.get("preferred_subcategory")

        # Build a description of the user's preferences
        conditions = []

        if budget is not None:
            conditions.append(f"your {budget} SAR budget")

        if activity:
            conditions.append(f"activities for {activity.lower()}")

        if category:
            conditions.append(category.lower())

        if subcategory:
            conditions.append(subcategory.lower())

        if location:
            conditions.append(f"in {location}")

        # Construct the message
        if conditions:
            description = " and ".join(conditions)

            return (
                f"I couldn't find any places matching {description}. "
                "Try expanding your search to nearby areas or adjusting "
                "your budget or preferences."
            )

        return (
            "I couldn't find any places matching your request. "
            "Try adjusting your preferences and searching again."
        )

    # Convert database results into text for the LLM
    places_text = []

    for i, place in enumerate(ranked_places, start=1):
        places_text.append(
            f"""
Recommendation {i}:
Place name: {place[1]}
Category: {place[2]}
Subcategory: {place[3]}
Location: {place[4]}
Rating: {place[5]}
Estimated cost: {place[6]} SAR
Price level: {place[7]}
Duration: {place[8]} hours
Activity type: {place[9]}
Opening hours: {place[10]}
"""
        )

    places_text = "\n".join(places_text)

    # Prompt for response generation

    prompt = f"""
You are WAIN, an AI-powered place recommendation agent for Riyadh.

The user asked:
"{user_question}"

The system extracted these preferences:
{preferences}

The following places were retrieved from PostgreSQL and ranked
by WAIN's ranking algorithm:

{places_text}

Your task:
Generate a concise, natural-language recommendation response
for the user.

IMPORTANT RULES:

1. Use ONLY information explicitly provided in the place data above.
2. NEVER invent, assume, or infer information that is not provided.
3. Do not add places that are not listed above.
4. Do not invent prices, ratings, locations, opening hours, features,
   services, facilities, or other facts.
5. Do not claim that a place is open unless the provided opening-hours
   information supports that statement.
6. Respect the user's stated preferences, budget, location, category,
   rating, duration, and activity requirements.
7. Present recommendations in the SAME ORDER as provided.
8. Do not mention ranking scores.
9. Do not mention the database, retrieval process, ranking algorithm,
   or "order returned" in the final response.
10. Mention useful information when available:
    - place name
    - location
    - rating
    - estimated cost
    - duration
    - activity type
    - opening hours
11. Explain briefly why the recommendations match the user's request,
    but only using information explicitly provided.
12. If information is missing, simply omit it.
13. If multiple places are provided, number the recommendations.
14. Keep the response natural, helpful, and concise.
15. Do not make claims about quality or suitability that cannot be
    supported by the provided data.
16. End the response after presenting the recommendations.
Do not offer services or capabilities that are not implemented by WAIN.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text.strip()

