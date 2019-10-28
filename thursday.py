import json
from random import choice


def load_names():
    with open("people.json", "r") as file:
        return json.load(file)


def load_chores():
    with open("chores.json") as chore_file:
        return json.load(chore_file)


def save(day_chores):
    with open("days/thursday.json", "w") as daily_chore_file:
        json.dump(day_chores, daily_chore_file)


def main():
    iterations = 0
    empty_list = []
    names = load_names()
    chores = ["B", "C", "H", "I", "J", "K", "L", "T", "P"]
    while iterations != 9:
        name = choice(names)
        chore = choice(chores)
        index_of_chore = chores.index(chore)
        if index_of_chore == 0 or index_of_chore == -1:
            pass
        else:
            index_of_chore + 1

        index_of_name = names.index(name)
        if index_of_name == -1 or index_of_name == 0:
            pass
        else:
            index_of_name + 1
        chores.pop(index_of_chore)
        names.pop(index_of_name)
        daily_chore = name + " : " + chore
        if name in daily_chore:
            iterations += 1
            empty_list.append(daily_chore)
    save(empty_list)


if __name__ == "__main__":
    main()
