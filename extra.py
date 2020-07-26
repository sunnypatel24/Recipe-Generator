# Extra code for filtering recipes feature. May be implemented at a future date.


# categoryChoice = getCategoryChoice()
    # areaChoice = getAreaChoice() 
    # if (categoryChoice == "" and areaChoice == ""):
    #     anyChoice()
    # else:
    #     specificChoice(categoryChoice, areaChoice)


# def getCategoryChoice():
#     categoryChoice = input("Please select a category of meal that you would like to see a recipe for. Press enter for any category: ")
#     return categoryChoice


# def getAreaChoice():
#     areaChoice = input("Please select an area of a meal that you would like to see a recipe for. Press enter for any area: ")
#     return areaChoice


# def anyChoice():
#     recipe = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
#     rawMeal = recipe.text
#     meal = rawMeal.split(",")
#     print(meal)


# def specificChoice(categoryChoice, areaChoice):
#     recipe = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
#     rawMeal = recipe.text
#     meal = rawMeal.split(",")
#     while (categoryChoice not in meal or areaChoice not in meal):
#         recipe = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
#         rawMeal = recipe.text
#         meal = rawMeal.split(",")
#     print(meal)