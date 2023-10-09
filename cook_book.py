# cook_book_task_1

with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file.read().split('\n\n'):
            # print(line)
            name, *ingredients = line.split('\n')
            cook_lst = []
            for ingredient in ingredients[1:]:
                ing_name, quantity, un_measure = ingredient.split('|')
                cook_lst.append(
                    {
                        'ingredient_name': ing_name,
                        'quantity': int(quantity),
                        'un_measure': un_measure,
                    }
                )
            cook_book[name] = cook_lst
        del cook_book['Фахитос']

import json
print(f'cook_book= {json.dumps(cook_book, indent= 2, ensure_ascii=False)}')

# cook_book_task_2
from pprint import pprint


def get_shop_list_by_dishes(dishes, person_count):
    ing_dict = {}
    for dish_n, ingred in cook_book.items():
        if dish_n in dishes:
            for ingredient in ingred:
                name, quantity, un_measure = ingredient.values()
                ing_dict.setdefault(name, {"un_measure": un_measure, "quantity": 0})
                ing_dict[name]["quantity"] += quantity * person_count
    pprint(ing_dict)


print(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))








