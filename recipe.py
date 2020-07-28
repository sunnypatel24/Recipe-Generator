import requests

VALID_CATEGORIES = ["Pork", "Starter", "Chicken", "Side", "Seafood", "Miscellaneous", "Beef", "Breakfast", "Pasta", "Lamb", "Dessert", "Vegetarian", "Vegan"]
    
VALID_AREAS = ["Irish", "British", "Italian", "French", "American", "Moroccan", "Tunisian", "Jamaican", "Indian", "Chinese", "Japanese", "Vietnamese", "Thai", "Polish", "Canadian", "Mexican", "Greek", "Unknown", "Spanish", "Malaysian", "Turkish", "Dutch"]

def main():
    intro()
    meal = get_meal_details()
    getIngredients(meal)
    get_website(meal)


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


def get_meal_details():
    recipe = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    meal = recipe.json()
    for dictionary in meal["meals"]:
        print("Meal: ", dictionary["strMeal"], "\n")
        print("Category: ", dictionary["strCategory"], "\n")
        print("Area: ", dictionary["strArea"], "\n")
        print("Instructions: ", dictionary["strInstructions"], "\n")
        print("Picture of Meal: ", dictionary["strMealThumb"], "\n")
        print("Video: ", dictionary["strYoutube"], "\n")
        print("Ingredients and their measurements:", "\n")
    return meal


def getIngredients(meal):
    ingredients = {}
    for dictionary in meal["meals"]:
        ingredients[dictionary["strIngredient1"]] = dictionary["strMeasure1"]
        ingredients[dictionary["strIngredient2"]] = dictionary["strMeasure2"]
        ingredients[dictionary["strIngredient3"]] = dictionary["strMeasure3"]
        ingredients[dictionary["strIngredient4"]] = dictionary["strMeasure4"]
        ingredients[dictionary["strIngredient5"]] = dictionary["strMeasure5"]
        ingredients[dictionary["strIngredient6"]] = dictionary["strMeasure6"]
        ingredients[dictionary["strIngredient7"]] = dictionary["strMeasure7"]
        ingredients[dictionary["strIngredient8"]] = dictionary["strMeasure8"]
        ingredients[dictionary["strIngredient9"]] = dictionary["strMeasure9"]
        ingredients[dictionary["strIngredient10"]] = dictionary["strMeasure10"]
        ingredients[dictionary["strIngredient11"]] = dictionary["strMeasure11"]
        ingredients[dictionary["strIngredient12"]] = dictionary["strMeasure12"]
        ingredients[dictionary["strIngredient13"]] = dictionary["strMeasure13"]
        ingredients[dictionary["strIngredient14"]] = dictionary["strMeasure14"]
        ingredients[dictionary["strIngredient15"]] = dictionary["strMeasure15"]
        ingredients[dictionary["strIngredient16"]] = dictionary["strMeasure16"]
        ingredients[dictionary["strIngredient17"]] = dictionary["strMeasure17"]
        ingredients[dictionary["strIngredient18"]] = dictionary["strMeasure18"]
        ingredients[dictionary["strIngredient19"]] = dictionary["strMeasure19"]
        ingredients[dictionary["strIngredient20"]] = dictionary["strMeasure20"]
    if (ingredients.get('') == ''):
        ingredients.pop('')
    elif (ingredients.get(None) == None):
        ingredients.popitem()
    keys_list = list(ingredients)
    values = ingredients.values()
    values_list = list(values)
    for i in range(len(keys_list)):
        print(keys_list[i],":", values_list[i])


def get_website(meal):
    print()
    for dictionary in meal["meals"]:
        print("Website of Recipe: ", dictionary["strSource"])


main()