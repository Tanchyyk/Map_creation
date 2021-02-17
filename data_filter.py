import random


def write_file(path: str):
    new_file = open("reduced_data.list", "w+")

    with open(path, "r", errors='ignore') as file:
        for line in file.readlines()[14:]:
            probability = random.uniform(0, 1)
            if probability > 0.99:
                new_file.write(line)


def make_film_lst(path: str) -> list:
    films = []
    with open(path, "r+") as file:
        for line in file.readlines():
            info = [line[:line.index("(")].strip(), line[line.index("(") + 1:line.index(")")].strip()]
            if "{" in line:
                info.append(line[line.index("}") + 1:].strip())
            else:
                info.append(line[line.index(")") + 1:].strip())
            films.append(info)

    clear_films_info = []

    for film in films:
        if film[1].isnumeric():
            film[1] = int(film[1])
            clear_films_info.append(film)

    for film in clear_films_info:
        while "(" in film[-1]:
            film[-1] = film[-1].replace(film[-1][film[-1].index("("): film[-1].index(")") + 1], "")

        if "\t" in film[-1]:
            film[-1] = film[-1].replace("\t", "")
        film[-1] = ", ".join(film[-1].split(", ")[-3:])

    while len(clear_films_info) > 50:
        clear_films_info.remove(clear_films_info[random.randint(0, len(clear_films_info) - 1)])
    return clear_films_info
