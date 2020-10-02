
movies = []

while True:
    movie_input = input("Enter movie: ")
    if movie_input == "exit":
        break
    else:
        movies.append(movie_input)

movies_file = open("../movies.txt", "a")

for movie in movies:
    movies_file.write(movie + "\n")