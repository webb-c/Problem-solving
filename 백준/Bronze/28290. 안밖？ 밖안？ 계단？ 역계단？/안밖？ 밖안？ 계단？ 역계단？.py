import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    tagun = input()
    if tagun == "fdsajkl;" or tagun == "jkl;fdsa":
        print("in-out")
    elif tagun == "asdf;lkj" or tagun == ";lkjasdf":
        print("out-in")
    elif tagun == "asdfjkl;":
        print("stairs")
    elif tagun == ";lkjfdsa":
        print("reverse")
    else:
        print("molu")

if __name__ == "__main__":
    main()
