import Project 5: Favorite Movies Tracker # type: ignore

favorite_movies = []

while True:
    print("\nMenu")
    print("1. Add a movie")
    print("2. Display list of movies")
    print("3. Remove a movie from the list")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        movie = input("Enter the name of the movie: ").title()
        if movie not in favorite_movies:
            favorite_movies.append(movie)
            print(f"{movie} has been added to your list")
        else:
            print(f"{movie} already exists")

    elif choice == "2":
        if favorite_movies:
            print("Your favorite movies are:")
            for movie in favorite_movies:
                print(movie)
    
        else:
            print("You haven't added any movies yet.")

    elif choice == "3":
        movie = input("Enter the name of the movie: ").title()
        favorite_movies.remove(movie)
        print(f"{movie} has been deleted from your list.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print(f"Invalid input. Please try again")
        