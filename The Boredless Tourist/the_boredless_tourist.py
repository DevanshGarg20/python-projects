destinations = ["Paris,France", "Shanghai,China", "LosAngeles,USA", "So Paulo, Brazil", "Cairo,Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai,China', ['historical site', 'art']]

#TRAVELLING TO FARAWAY LANDS

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index
print(get_destination_index("LosAngeles,USA"))
print(get_destination_index("Paris,France"))
#print(get_destination_index("Hyderabad,India"))
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

#VISITING INTERESTING PLACES

attractions = [[] for dest in destinations]
print(attractions)
def add_attraction(destination,attraction):
  try:
    destination_index = get_destination_index(destination)
  except:
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return 
add_attraction("LosAngeles,USA",['VeniceBeach',['beach']])
add_attraction("Paris,France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris,France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai,China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai,China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai,China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles,USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo,Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo,Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo,Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo,Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)

#FINDING THE BEST PLACES TO GO

def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for i in attractions_in_city:
    possible_attraction = i
    attraction_tags = possible_attraction[1]
    for j in interests:
      if j in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest
la_arts = find_attractions("Shanghai,China",['art'])
print(la_arts)

#SEE THE PARTS OF A CITY YOU WANT TO SEE

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination,traveler_interests)
  interests_string = "Hi "
  interests_string = interests_string + traveler[0]
  interests_string = interests_string + ",we think you'll like these places around " + traveler[1] + ": "
  for k in traveler_attractions:
    interests_string = interests_string + k
  return interests_string
smills_france = get_attractions_for_traveler(['dereck Smill','Paris,France',['monument']])
print(smills_france)