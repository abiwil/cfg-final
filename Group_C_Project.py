

import requests

app_id = '42d32143'
app_key = '361f623d4c5d6e9b9a3d8b6643ecf00c'  # secondary key: '5e736dcffae24d62194a6e00f8236add'


def query(*ingredients):  # scrapes data from edamame API using ingredient(s) and meal type. Returns list of results
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&"mealType={}"'.format(ingredients, app_id,
                                                                                         app_key, meal)
    response = requests.get(url)
    results = response.json()
    return results['hits']


def recipe_info():  # displays recipe info and creates list for formatted output in .txt file
    print('\n', '-------------------------------------------------------------------------', '\n')
    recipe_list = []  # empty list to save dictionary of formatted results
    recipe_num = 1  # counter for recipe name
    for hit in q:
        neat_recipe = {}  # empty dictionary for formatted results
        get_recipe = hit['recipe']
        # Console output
        print('Recipe Name: {}'.format(get_recipe['label']))
        print('Cook time: {} mins'.format(int(get_recipe['totalTime'])))
        print('Labels: {}'.format(get_recipe['healthLabels']))
        print('Calories: {}'.format(int(get_recipe['calories'])))
        print('Visit site: {}'.format(get_recipe['url']))
        print('\n')
        # .txt file output
        neat_recipe['recipe name'] = 'Recipe {} : {}'.format(str(recipe_num), get_recipe['label'])
        neat_recipe['total cook time'] = 'Cook time: {} mins'.format(int(get_recipe['totalTime']))
        neat_recipe['health info'] = 'Labels: {}'.format(get_recipe['healthLabels'])
        neat_recipe['calories'] = 'Calories: {}'.format(int(get_recipe['calories']))
        neat_recipe['url'] = 'Visit site: {}{}'.format(get_recipe['url'], '\n')
        recipe_list.append(neat_recipe)
        recipe_num = recipe_num + 1
    return recipe_list


print("Welcome to Group C's project: " + "\033[1m" "Recip-easy!" + "\033[0m" + "\n" +
      "Got ingredients but no inspiration? " + "Use our programme to find your next meal!" + "\n")
meal = (input('What kind of meal do you want to make? (Breakfast, Lunch, Dinner, Snack or leave blank) ').lower())
ingredient1 = input('What are you cooking with? ')
prompt = (input('Do you have another ingredient? (y/n) ').lower())
if prompt == 'y':
    ingredient2 = input('What else are you cooking with? ')
    q = query(ingredient1, ingredient2)
else:
    q = query(ingredient1)

with open('recipe_results.txt', 'w+') as file_object:
    for item in recipe_info():
        lines = list(item.values())  # to get values in a reader friendly list
        for l in lines:
            file_object.writelines('%s\n' % l)

print('-------------------------------------------------------------------------', '\n')
print('Search complete! Check recipe_results.txt to see a record of your search.')


