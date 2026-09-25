
def calculate_rating_score(place):
    """
    Calculate a normalized rating score between 0 and 1.

    Place tuple:
    0: id
    1: place_name
    2: category
    3: subcategory
    4: location
    5: rating
    6: estimated_cost_sar
    7: price_level
    8: duration_hours_needed
    9: activity_type
    10: opening_hours
    """

    rating = place[5]

    if rating is None:
        return 0

    return max(0, min(rating / 5, 1))


def calculate_activity_score(place, activity_preference):
    """
    Calculate how well the place matches the user's activity preferences.
    """

    if not activity_preference:
        return 0

    place_activity = (place[9] or "").lower()

    preferences = [
        p.strip().lower()
        for p in activity_preference.split("/")
        if p.strip()
    ]

    if not preferences:
        return 0

    matched = sum(
        1 for preference in preferences
        if preference in place_activity
    )

    return matched / len(preferences)


def calculate_budget_score(place, budget):
    """
    Score affordability.

    Lower-cost places receive a higher score when a budget is provided.
    """

    if budget is None:
        return 0

    cost = place[6]

    if cost is None:
        return 0

    if budget <= 0:
        return 1 if cost == 0 else 0

    if cost > budget:
        return 0

    return 1 - (cost / budget)


def calculate_duration_score(place, max_duration):
    """
    Score duration fit.

    Shorter activities receive a higher score when a maximum duration
    is specified.
    """

    if max_duration is None:
        return 0

    duration = place[8]

    if duration is None:
        return 0

    if max_duration <= 0:
        return 1 if duration == 0 else 0

    if duration > max_duration:
        return 0

    return 1 - (duration / max_duration)


def calculate_final_score(place, preferences):
    """
    Calculate the final ranking score.

    Returns a score between 0 and 100.
    """

    rating_score = calculate_rating_score(place)

    activity_score = calculate_activity_score(
        place,
        preferences.get("activity_preference")
    )

    budget_score = calculate_budget_score(
        place,
        preferences.get("budget")
    )

    duration_score = calculate_duration_score(
        place,
        preferences.get("max_duration")
    )

    # Base weights
    weights = {
        "rating": 0.40,
        "activity": 0.40,
        "budget": 0.20,
    }

    # Adjust weights when the user provides no activity preference
    if not preferences.get("activity_preference"):
        weights = {
            "rating": 0.70,
            "budget": 0.30,
        }

    # Adjust weights when the user provides a duration preference
    if preferences.get("max_duration") is not None:
        weights["duration"] = 0.15

        # Reduce other weights proportionally
        remaining = 0.85
        original_total = sum(weights.values()) - 0.15

        if original_total > 0:
            for key in list(weights.keys()):
                if key != "duration":
                    weights[key] = (weights[key] / original_total) * remaining

    score = (
        rating_score * weights.get("rating", 0)
        + activity_score * weights.get("activity", 0)
        + budget_score * weights.get("budget", 0)
        + duration_score * weights.get("duration", 0)
    )

    return round(score * 100, 2)


def rank_places(places, preferences, limit=10):
    """
    Rank places based on the user's preferences.

    Returns the original place tuples, sorted by ranking score.
    """

    scored_places = []

    for place in places:
        score = calculate_final_score(place, preferences)
        scored_places.append((score, place))


    # Sort by score, then rating as a tie-breaker

    scored_places.sort(
        key=lambda item: (
            item[0],
            item[1][5] or 0
        ),
        reverse=True
    )


    # Print ranking scores during development
    for score, place in scored_places:
        print(f"{place[1]} → Ranking Score: {score}")


    return [
        place
        for score, place in scored_places[:limit]
    ]

