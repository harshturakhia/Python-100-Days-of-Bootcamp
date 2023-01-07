# Nesting dictionary & list in dictionary

# Nesting dictionary  in dictionary

tarvel_vlog = {
    "France": {
        "City_visisted": ["Harsh", "Vipesh", "Turakhia"],
        "Total_cities": 12,
    }
    # "Germany": {
    #     "City_visisted": ["Harsh", "Vipesh", "Turakhia"],
    #     "Total_cities": 12,
    # }
}

# Nesting dictionary in list
travel_vlog = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "Country": "Germany",
        "total_cities": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10,
    },
]


# def add_new_country(country, cities_visited, total_visits):
