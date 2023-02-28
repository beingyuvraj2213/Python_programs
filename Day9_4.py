travel_log=[
    {
        "country":"France",
        "cities_visited":{"Paris","Lille","Dijon"},
        "visits":12 
    },
    { 
        "country":"India",
        "cities_visited":{"New Delhi","Patna","Hazaribagh"},
        "visits":5
    },
]

def add_new_country(country_visited,times_visit,cities):
    new_country={}
    new_country["country"]=country_visited
    new_country["cities_visited"]=cities
    new_country["visits"]=times_visit

    travel_log.append(new_country)  

  
country_visited=input("Enter the country visited : ")
times_visit=input("Enter the times visited : ")

cities=[]
for i in range(3):
    cities.append(input("Enter the cities visited : "))   

add_new_country(country_visited,times_visit,cities) 

print(travel_log)