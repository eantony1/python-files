classmate_fave_foods = {"pizza", "sushi", "tacos", "ramen", "sandwich"}

my_fave_foods = {input("Enter your first favorite food: "), 
                 input("Enter your second favorite food: "), 
                 input("Enter your third favorite food: ")}

common_foods = my_fave_foods & classmate_fave_foods

if common_foods:
    print("Our common favorite foods: ")
    for food in common_foods:
        print(food)
