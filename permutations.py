from itertools import permutations

def main():
    string = input("What string would you like to use?: ")
    perms = [''.join(p) for p in permutations(string)]
    for item in perms:
        print(item)

if __name__ == '__main__':
    main()
