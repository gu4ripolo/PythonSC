"""
Enter 'a' to add a movie.
Enter 'l' to see a movie.
Enter 'f' to find a movie
Enter 'q' to quit.
"""

movies = []


def userMenu():
    print("Enter 'a' to add a movie. Enter 'l' to see a movie. Enter 'f' to find a movie. Enter 'q' to quit.")
    userinput = input("Select an option: ")

    while userinput != 'q':

        if userinput == 'a':
            addMovie()
        elif userinput == 'l':
            listMovies()
        elif userinput == 'f':
            findMovie()
        else:
            print("Invalid option")

        userinput = input("\nSelect an option: ")


def addMovie():

    name = input("Enter the movie name: ")
    director = input("Enter the director name: ")
    year = int(input("Enter the movie release year: "))
    movie =  \
        {
            "name": name,
            "director": director,
            "year": year
        }
    movies.append(movie)


def listMovies():
    for movie in movies:
        print(f"Movie Name: {movie['name']}")
        print(f"Movie Director: {movie['director']}")
        print(f"Movie Release year: {movie['year']}")

def listMovie(movie):
    print(f"Movie Name: {movie['name']}")
    print(f"Movie Director: {movie['director']}")
    print(f"Movie Release year: {movie['year']}")


def findMovie():
    moviename =input("Enter the movie name: ")
    for movie in movies:
        if moviename == movie['name']:
            listMovie(movie)
        else:
            print("The movie has not been found")
            break

userMenu()


