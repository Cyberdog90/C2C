import random


def strgen():
    with open("strgen.txt", "w") as f:
        for i in range(300):
            for j in range(99):
                f.write(chr(random.randrange(33, 126)))
            f.write("\n")


"""
def cou():
    with open("strgen.txt", "r") as f:
        data = f.readlines()
        data = list("".join(data))
        print(len(data))

"""
strgen()
# cou()
