def user_name():
    # Get user's full name and return the first name
    user_name = input("Enter your full name: ").title()
    first_name = user_name.split(" ")[0]
    return first_name

def get_movies_limit():
    # Gets and return the number of movies the user wants to track
    return int(input("How many movies do you want to track?\n "))
    
def add_movies(favorite_movies, no_of_movies):
    # Adds movies to favorite movie list
    while len(favorite_movies) < no_of_movies:
        movie_list = input("List the movies (comma-seperated):\n ").split(",")

        for movie in movie_list: #to store each movie in the list
            if movie.strip().title() not in favorite_movies:
                    favorite_movies.append(movie.strip().title()) #capitalize the output
            else: 
                print("Movie already exists.")
                
            print("You have the following movies tracked: ")
        for movie in favorite_movies:
            print(movie)

    return favorite_movies

def increase_limits(favorite_movies, no_of_movies):
     # Prompts users to increase limit
     if len(favorite_movies) == no_of_movies:
        increase = input("You've exhausted your track limit. Do you want to increase it? Type yes/no?\n").lower()
        if increase == "yes":
            new_limit = int(input("Enter new limit:\n "))
            no_of_movies += new_limit
            print ("You have now increased your limit by " + str((new_limit + no_of_movies)-no_of_movies))
        elif increase == "no":
            return no_of_movies, False # Stop tracking
        else:
            print("Invalid input")
        return no_of_movies, True # Continue tracking
     
def favorite_movie_tracker():
    first_name = user_name()
    print(f"Hello {first_name}")
    no_of_movies = get_movies_limit()
    favorite_movies = []

    while True:
        favorite_movies = add_movies(favorite_movies, no_of_movies)

          # If limit reached, ask user to increase or exit

        if len(favorite_movies) >= no_of_movies:
            no_of_movies, continue_tracking = increase_limits(favorite_movies, no_of_movies)
            if not continue_tracking:
                break 
               
    print("Final list of tracked movies:")
    for movie in favorite_movies:
        print(movie)

    return favorite_movies

def display_list(favorite_movies):
    print("Your favorite movies are:")
    for movie in favorite_movies:
        print(movie)
               
                