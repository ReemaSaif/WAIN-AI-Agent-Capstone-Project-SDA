from wain_agent import run_wain

questions = [
    # "I want Indian restaurants with rating above 4.5",
    # "I have 300 SAR and I want something with my family around Qiddiya City.",
    # "I want a restaurant in Al Olaya and my budget is 200 SAR.",
    # "I want to go to Cinemas",
    # "Give me Saudi food restaurants",
    # "I want specialty coffee places",
    # "I want burgers",
    # "I want VR games",
    # "I want a coffee bakery",
    # "Give me public parks that has rating more than 4.2",
    # "I want place that sell abayas",
    # "I want to see the snow, where should I go",
    # "Find me a library café in Riyadh",
    # "Affordable cafes under 25 SAR",
    # "Find an Entertainment place in Riyadh Park",
    # "Something fun with my kids",
    # "I want a coffee place that opens 24 hours",
    # "Suggest me places that are in Diriyah",
    # "Give me a place that is free",
    # "Find restaurants in VIA Riyadh",
    # "I want to eat Lebanese food",
    # "Find luxury dining places",
    # "I want somewhere luxury",
    # "Can you give me karting spots",
    # # "Find me a fun activity with friends in Ar Rimal under 100 SAR",
    # "I have 250 SAR and want something fun with friends",
    # "I have 150 SAR, want something fun with friends in Hittin",  # Negative case/no match
    "I want hummes",
    "I want kimichi",
    "I want kabsa",
    "Give me a place that sell tacos",

]


for i, question in enumerate(questions, start=1):

    print("\n" + "=" * 80)
    print(f"TEST {i}")
    print("=" * 80)

    print("\nUSER QUESTION:")
    print(question)

    try:
        response = run_wain(question)

        print("\nEXTRACTED PREFERENCES:")
        print(response["preferences"])

        print("\nMATCHING PLACES:")

        results = response["results"]

        if not results:
            print("No places found.")
        else:
            print(f"Found {len(results)} place(s):\n")

            for place in results:
                print(
                    f"- {place[1]} | "
                    f"Category: {place[2]} | "
                    f"Subcategory: {place[3]} | "
                    f"Location: {place[4]} | "
                    f"Rating: {place[5]} | "
                    f"Cost: {place[6]} SAR | "
                    f"Duration: {place[8]} hours | "
                    f"Activity: {place[9]}"
                )

        # Print the LLM-generated final response
        print("\n" + "=" * 80)
        print("WAIN FINAL RESPONSE")
        print("=" * 80)
        print(response["final_response"])


    except Exception as e:
        print("\nERROR:")
        print(e)

