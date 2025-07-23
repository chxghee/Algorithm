# https://www.acmicpc.net/problem/14889
from itertools import combinations
import sys
input = sys.stdin.readline


def calc_team_ability(team):

    team_abil = 0
    for val in team:
        team_abil += calc_ability(val, team)
    return team_abil

def calc_ability(p, team):
    abil = 0
    for val in team:
        if p != val:
            abil += s[p][val]
    return abil

def get_other_team_member(team):
    other_team = []
    for p in people:
        if p not in team:
            other_team.append(p)
    return other_team

    
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
people = [i for i in range(n)]

combis = list(combinations(people, n // 2))

result = int(1e9)
for team in combis:
    other_team = get_other_team_member(team)
    our_team_ability =  calc_team_ability(team)
    other_team_ability = calc_team_ability(other_team)
    result = min(result, abs(our_team_ability - other_team_ability))

print(result)
    