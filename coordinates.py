#Project: Create a program that uses a tuple to store coordinates (x, y)  

coordinates = []

while True:
    x = float(input("Input 'x' coordinate: "))
    y = float(input("input 'y' coordinate: "))
    coordinates_pair = (x,y)
    coordinates.append(coordinates_pair)
    t = tuple(coordinates)
    print(t)

    continue_input = input("Do you want to add more coordinates, yes/no: ").lower()

    if continue_input != "yes":
        break

print("Your total coordinates: ")  
for coordinates_pair in coordinates:
    print(coordinates_pair)

# set to store unique items.

items_set = set()

while True:
    user_input = input("Enter anything: ")
    
    items_set.add(user_input)

    continue_input = input("Do you want to add more? yes/no: ").lower()

    if continue_input != "yes":
        break

print(f"Here are the list of items you added: ")
for user_input in items_set:
    print(user_input)


 



    


