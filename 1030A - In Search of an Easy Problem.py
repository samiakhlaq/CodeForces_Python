person = int(input())
opinion = set(map(int,input().split(" ")))
if 1 in opinion:
    print("HARD")
else:
    print("EASY")
