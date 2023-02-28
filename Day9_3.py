capitals={
    "France":"Paris",
    "India":"New Delhi",
}

# Nesting a list in a dictionary

# travel_log={
#     "France":["Paris","Lille","Dijon"],
#     "India":["New Delhi","Patna","Hazaribagh"],
# }

# Nesting Dictionary in a Dictionary

# travel_log={
#     "France":{"cities_visited":["Paris","Lille","Dijon"],"total_visits":12 },
#     "India":{"cities_visited":["New Delhi","Patna","Hazaribagh"],"total_visits":5},
# }


# Nesting Dictionary in a list

travel_log=[
    {
        "country":"France",
        "cities_visited":{"Paris","Lille","Dijon"},
        "total_visits":12 
    },
    { 
        "country":"India",
        "cities_visited":{"New Delhi","Patna","Hazaribagh"},
        "total_visits":5
    },
]

print(travel_log)