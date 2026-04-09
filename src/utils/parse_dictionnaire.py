def parse_dictionnaire():
    with open("src/data/dictionnaire.txt", "r") as file:
        return [line.split(";")[0].strip() for line in file if line.strip()]
