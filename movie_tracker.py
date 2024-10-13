def favorite_movie_tracker():
    user_name = input("Enter your full name: ").title()
    split = user_name.split(" ")
    print(f"Hello {split[0]}")


    no_of_movies = int(input("How many movies do you want to track?\n "))
    print("OK")

    favorite_movies = []

    #Total number of movies in the list must always be less than or equal to the number stipulated by users to be tracked.
    #if total number in list is less than number of movies, inquire if they want to add more list

    while len(favorite_movies) <= no_of_movies:
        movie_list = input("List the movies: ").split(",")

        for movie in movie_list: #to store each movie in the list
            if movie.strip().title() not in favorite_movies:
                favorite_movies.append(movie.strip().title()) #capitalize the output
            else: 
                print("Movie already exists.")
            
        print("You have the following movies tracked: ")
        for movie in favorite_movies:
            print(movie)

    #Once the user exhausts the number, throw a message and asks if they would like to increase limits. if yes, they add, and no the program stops 
    #cinema showings for each movie

        if len(favorite_movies) == no_of_movies:
            increase_limit = input("You've exhausted your track limit. Do you want to increase it? Type yes/no?\n").lower()
            if increase_limit == "yes":
                new_limit = int(input("Enter new limit:\n "))
                no_of_movies += new_limit
                print("You have now increased your limit by " + str((new_limit + no_of_movies)-no_of_movies))
            elif increase_limit == "no":
                break
            else:
                print("Invalid input")
                

    #let's make each input unique



