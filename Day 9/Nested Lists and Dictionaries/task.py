# nested dictionary version 1

travel_log = {
    "France":
        ["Lille", "Paris", "Dijon"]
}

print(travel_log.get("France"))
print(travel_log["France"])
print(travel_log["France"][0])  # --- prints Lille
print(f"I travel to {travel_log['France'][0]} and I love this place.")

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][0])

# nested dictionary version 2

travel_log2 = {
    "Germany":
        {"Cities": ["Stuttgart", "Berlin", "Hamburg"],
         "Towns": ["Heidelberg", "Bonn", "Mainz"]
        }
}

print(travel_log2) # prints cities and towns
print(travel_log2["Germany"]["Cities"]) # prints all cities
print(travel_log2["Germany"]["Cities"][1]) # prints Berlin

print(f"Let's go to {travel_log2['Germany']['Towns'][2]} again. It's a cool place.")