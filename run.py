import json

def load_movies():
    try:
        with open('movies.json', 'r') as f:
            movies = json.load(f)
    except FileNotFoundError:
        movies = []
    return movies

def save_movies(movies):
    with open('movies.json', 'w') as f:
        json.dump(movies, f)

def add_movie():
    title = input("Enter the title of the movie: ")
    director = input("Enter the director of the movie: ")
    year = input("Enter the year of the movie: ")
    movies = load_movies()
    movie = {'title': title, 'director': director, 'year': year}
    movies.append(movie)
    save_movies(movies)
    print(f"Added movie: {title}")

def view_movies():
    movies = load_movies()
    if len(movies) == 0:
        print("No movies found.")
    else:
        for movie in movies:
            print(f"{movie['title']} ({movie['year']}) - directed by {movie['director']}")

def search_movie():
    title = input("Enter the title of the movie to search: ")
    movies = load_movies()
    found_movies = [movie for movie in movies if title.lower() in movie['title'].lower()]
    if len(found_movies) == 0:
        print(f"No movie with title '{title}' found.")
    else:
        for movie in found_movies:
            print(f"{movie['title']} ({movie['year']}) - directed by {movie['director']}")

def delete_movie():
    title = input("Enter the title of the movie to delete: ")
    movies = load_movies()
    updated_movies = [movie for movie in movies if title.lower() not in movie['title'].lower()]
    if len(updated_movies) == len(movies):
        print(f"No movie with title '{title}' found.")
    else:
        save_movies(updated_movies)
        print(f"Deleted movie: {title}")

def main():
    while True:
        print("\nSelect a command:")
        print("1. Add a movie")
        print("2. View all movies")
        print("3. Search for a movie")
        print("4. Delete a movie")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            view_movies()
        elif choice == '3':
            search_movie()
        elif choice == '4':
            delete_movie()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()
