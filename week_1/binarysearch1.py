"""
movies_and_shows = [
    "Game of Thrones",
    "Harry Potter and the Sorcerer's Stone",
    "Avengers: Endgame",
    "Batman v Superman: Dawn of Justice",
    "Iron Man",
    "Spider-Man: No Way Home",
    "The Dark Knight",
    "Thor: Ragnarok",
    "Wonder Woman",
    "Black Panther",
    "Doctor Strange",
    "The Witcher",
    "Friends",
    "Stranger Things",
    "The Mandalorian",
    "Guardians of the Galaxy",
    "The Flash",
    "The Boys",
    "Breaking Bad",
    "Narcos",
    "Shazam!",
    "Pokiri",
    "Baahubali: The Beginning",
    "Arjun Reddy",
    "RRR",
    "Sye",
    "Ala Vaikunthapurramuloo",
    "Khaidi No. 150",
    "Jersey",
    "Pushpa: The Rise"
]


movie_tvshow = input("Enter the Movie or TV Show: ")

length = len(movies_and_shows)

low = 0

high = length -1

while low<=high:

    mid =(low+high) // 2

    if movies_and_shows[mid] == movie_tvshow:
        print("Found")
        break
    
    elif movies_and_shows[mid] > movie_tvshow:
        high = mid -1
    
    else:
        low = mid +1

else:
    print("Not Found")

"""



movies_and_shows = [
    "Game of Thrones",
    "Harry Potter and the Sorcerer's Stone",
    "Avengers: Endgame",
    "Batman v Superman: Dawn of Justice",
    "Iron Man",
    "Spider-Man: No Way Home",
    "The Dark Knight",
    "Thor: Ragnarok",
    "Wonder Woman",
    "Black Panther",
    "Doctor Strange",
    "The Witcher",
    "Friends",
    "Stranger Things",
    "The Mandalorian",
    "Guardians of the Galaxy",
    "The Flash",
    "The Boys",
    "Breaking Bad",
    "Narcos",
    "Shazam!",
    "Pokiri",
    "Baahubali: The Beginning",
    "Arjun Reddy",
    "RRR",
    "Sye",
    "Ala Vaikunthapurramuloo",
    "Khaidi No. 150",
    "Jersey",
    "Pushpa: The Rise"
]

# Convert the list to lowercase
movies_and_shows = [movie.lower() for movie in movies_and_shows]

# Take input from the user and convert it to lowercase
movie_tvshow = input("Enter the Movie or TV Show: ").lower()

length = len(movies_and_shows)
low = 0
high = length - 1

# Perform binary search
while low <= high:
    mid = (low + high) // 2

    if movies_and_shows[mid] == movie_tvshow:
        print("Found")
        break
    elif movies_and_shows[mid] > movie_tvshow:
        high = mid - 1
    else:
        low = mid + 1

else:
    print("Not Found")
