
import os

def main():
    f = open("test.txt", "r")
    test = f.readline()
    x = test.replace(" | ", ",")
    x = x.replace("\n", ",")
    print(x)

    test2 = f.readline().strip()
    print(test2 == "(")

main()