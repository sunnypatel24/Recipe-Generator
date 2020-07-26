import requests

VALID_CATEGORIES = ["Pork", "Starter", "Chicken", "Side", "Seafood", "Miscellaneous", "Beef", "Breakfast", "Pasta", "Lamb", "Dessert", "Vegetarian", "Vegan"]
    
VALID_AREAS = ["Irish", "British", "Italian", "French", "American", "Moroccan", "Tunisian", "Jamaican", "Indian", "Chinese", "Japanese", "Vietnamese", "Thai", "Polish", "Canadian", "Mexican", "Greek", "Unknown", "Spanish", "Malaysian", "Turkish", "Dutch"]


def main():   
    intro()
    getMeal()
    

def intro():
    print("Welcome! This is a program to generate a random recipe for a meal.\n")
    print("The categories recipes are pulled from are: ")
    categoryLength = len(VALID_CATEGORIES)
    for category in range(categoryLength - 1):
        print(VALID_CATEGORIES[category], end = ", ")
    print(VALID_CATEGORIES[categoryLength - 1])
    print("\n")
    print("The areas recipes are pulled from are: ")
    areaLength = len(VALID_AREAS)
    for area in range(areaLength - 1):
        print(VALID_AREAS[area], end = ", ")
    print(VALID_AREAS[areaLength - 1])
    print("\n")


def getMeal():
    recipe = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    rawMeal = recipe.text
    mealList = rawMeal.split(",")
    meal = "Meal: "
    mealName = mealList[1].replace("\"strMeal\":", "").strip('"')
    print(meal + mealName)
    category = "Category: "
    categoryName = mealList[3].replace("\"strCategory\":", "").strip('"')
    print(category + categoryName)
    area = "Area: "
    areaName = mealList[4].replace("\"strArea\":", "").strip('"')
    print(area + areaName)
    index = 5
    while ("\"strMealThumb\"" not in mealList[index]):
        index += 1
    mealPic = "Picture of Meal: "
    mealLink = mealList[index].replace("\"strMealThumb\":", "").strip('"')     
    print(mealPic + mealLink)
    while ("\"strYoutube\"" not in mealList[index]):
        index += 1
    mealVideo = "Video for how to make the meal: "
    vidLink = mealList[index].replace("\"strYoutube\":", "").strip('"')
    print(mealVideo + vidLink)

main()    