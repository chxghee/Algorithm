# https://www.acmicpc.net/contest/problem/1585/1
import sys
input = sys.stdin.readline

d = {
    "animal" : "Panthera tigris",
    "tree": "Pinus densiflora",
    "flower": "Forsythia koreana"
}

while True:
    s = input().rstrip()

    if s == "end":
        exit(0)
    else:
        print(d[s])
