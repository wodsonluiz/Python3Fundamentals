current_movies = {"The Grich": "11:00am", 
                  "Rudolph": "1:00pm",
                  "Frosty the snowman": "3:00pm",
                  "Chistmas vacation": "5:00pm"}

print("We're showing the following movies")

for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for? \n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, "is playint at", showtime)

