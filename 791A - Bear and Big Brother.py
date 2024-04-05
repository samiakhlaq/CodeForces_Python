Limak,Bob = map(int,input().split(" "))
year = 0
while True:
    if Limak > Bob :
        break
    else:
        Limak = Limak * 3
        Bob = Bob * 2 
        year = year + 1
print(year) 