class Animal(object):
    def __init__(self, args):
        args = args.strip("\n")
        self.__args = args.split(" ")

    def set_attr(self, args):
        args = args.strip("\n")
        self.__args = args.split(" ")

    def get_attr(self, item):
        return self.__args[item]


def readList(file):
    animals: list[Animal] = []
    quest: list[str] = []
    with open(file) as f:
        lines = f.readlines()
        for lineCt, line in enumerate(lines):
            if 1 < lineCt < 24:
                quest.append(line)
            elif lineCt >= 24:
                animals.append(Animal(line))
    return quest, animals


if __name__ == '__main__':
    guesses = []
    questions, zoo = readList("zoo.txt")
    for animal in zoo:
        print(animal.get_attr(0))
    for question in questions:
        guesses.append(input(question))

    for animal in zoo:
        match = True
        for idx, guess in enumerate(guesses):
            if guess != animal.get_attr(idx + 1):
                # print("It's not a ",animal.args[0])
                match = False
                break
        if match:
            print(f"It could be a {animal.get_attr(0)}")
