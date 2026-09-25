
from llm_extractor import extract_preferences

tests = [
    # "I want Indian restaurants with rating above 4.5",
    # "I have 300 SAR and I want something with my family around Qiddiya City.",
    # "I want a restaurant in Al Olaya and my budget is 200 SAR.",
    # "Find a cafe in Al Wurud",
    # "Something fun with my kids",
    # "I want to go to Cinemas",
    # "Give me Saudi food restaurants",
    # "Find an Entertainment place in Riyadh Park",
    # "I want somewhere luxury",
    # "Where can I get fried chicken",
    # "I want fine dining restaurants",
    # "Find luxury dining places",
    # "I want specialty coffee places",
    # "I want matcha",
    # "Find malls with cinemas",
    # "I want VR games",
    # "Give me Escape room places",
    # "I want outdoor places",
    # "I want an open‑air mall",
    # "I want burgers",
    # "I want fried chicken",
    # "I want pizza",
    # "I want shawarma",
    # "I want sandwiches",
    # "I want fast food",
    # "I want sightseeing places"
    # "I want a coffee place that opens 24 hours"
    # "Can you give me karting spots"
    # "Suggest me places that are in Diriyah",
    # "Give me public parks that has rating more than 4.2",
    # "Find places in Hittin",
    # "Give me a place that is free"
    # "I have 250 SAR and want something fun with friends",
    # "I want place that sell abayas",
    # "What is in Ghirnatah",
    # "I want Japanese food",
    # "Find nature attractions",
    # "I want a coffee bakery",
    # "Find me a library café in Riyadh",
    # "Find restaurants near VIA Riyadh",
    # "Affordable cafes under 25 SAR",
    # "I want to eat Lebanese food",
    "I want to see the snow, where should I go",

]


for t in tests:
    print("USER:", t)
    preferences = extract_preferences(t)
    print("Extracted Preferences:", preferences)
    print("-" * 50)

