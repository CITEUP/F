import math

t = 1
t = t+1
while t := t-1 :
    a = str(input())
    b = str(input())
    c = str(input())
    d = str(input())
    if((a == "####" and b == "...." and c == "####" and d == "....") or (b == "####" and a == "...." and d == "####" and c == "....") or (a == "#.#." and b == ".#.#" and c == "#.#." and d == ".#.#") or (b == "#.#." and a == ".#.#" and d == "#.#." and c == ".#.#") or (a == "#.#." and b == "#.#." and c == "#.#." and d == "#.#.") or (a == ".#.#" and b == ".#.#" and c == ".#.#" and d == ".#.#")): 
        print("NO")
    else: print("YES")

