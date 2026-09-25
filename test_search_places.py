from database.queries import search_places

results = search_places(
    budget=100,
    category="Entertainment",
    # subcategory=None,
    # location=None,
    min_rating=4.0,
    # max_duration=None,
    # activity_preference=None,
    # opening_hours=None,
    limit=10
)


print("\nWAIN SEARCH RESULTS")
print("=" * 50)

for place in results:
    print(place)


