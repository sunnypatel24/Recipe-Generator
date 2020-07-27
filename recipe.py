import requests

VALID_CATEGORIES = ["Pork", "Starter", "Chicken", "Side", "Seafood", "Miscellaneous", "Beef", "Breakfast", "Pasta", "Lamb", "Dessert", "Vegetarian", "Vegan"]
    
VALID_AREAS = ["Irish", "British", "Italian", "French", "American", "Moroccan", "Tunisian", "Jamaican", "Indian", "Chinese", "Japanese", "Vietnamese", "Thai", "Polish", "Canadian", "Mexican", "Greek", "Unknown", "Spanish", "Malaysian", "Turkish", "Dutch"]


def main():   
    intro()
    getMeal()
    

def intro():
    print("Welcome! This is a program to generate a random recipe for a meal.\n")
    print("The categories recipes are pulled from are: ")
    category_length = len(VALID_CATEGORIES)
    for category in range(category_length - 1):
        print(VALID_CATEGORIES[category], end = ", ")
    print(VALID_CATEGORIES[category_length - 1])
    print("\n")
    print("The areas recipes are pulled from are: ")
    area_length = len(VALID_AREAS)
    for area in range(area_length - 1):
        print(VALID_AREAS[area], end = ", ")
    print(VALID_AREAS[area_length - 1])
    print("\n")


def getMeal():
    recipe = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    raw_meal = recipe.text
    meal_list = raw_meal.split(",")
    meal = "Meal: "
    mealName = meal_list[1].replace("\"strMeal\":", "").strip('"')
    print(meal + mealName)

    category = "Category: "
    category_name = meal_list[3].replace("\"strCategory\":", "").strip('"')
    print(category + category_name)

    area = "Area: "
    area_name = meal_list[4].replace("\"strArea\":", "").strip('"')
    print(area + area_name)

    index = 5
    while ("\"strMealThumb\"" not in meal_list[index]):
        index += 1
    meal_pic = "Picture of Meal: "
    meal_link = meal_list[index].replace("\"strMealThumb\":", "").strip('"')     
    print(meal_pic + meal_link)

    while ("\"strYoutube\"" not in meal_list[index]):
        index += 1
    meal_video = "Video for how to make the meal: "
    vid_link = meal_list[index].replace("\"strYoutube\":", "").strip('"')
    print(meal_video + vid_link)

    ingredients = {}
    for var in range(1, 21):
        name = ""
        string = meal_list[index + var]
        string_length = len(string)
        for i in range(18, string_length):
            name += string[i]
            name = name.strip('"')
        ingredients.update({name : var})
    ingredients.popitem()
    
    index += var + 1
    print(meal_list[index])
        
        
    
    
    # print()
    # index += 2;
    
    

main()    