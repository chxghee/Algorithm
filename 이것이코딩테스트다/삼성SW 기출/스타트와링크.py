# https://www.acmicpc.net/problem/14889
from itertools import combinations
import sys
input = sys.stdin.readline


def calc_team_ability(team):

    team_abil = 0
    for val in team:
        team_abil += calc_my_ability(val, team)
    return team_abil

def calc_my_ability(p, team):
    abil = 0
    for val in team:
        if p != val:
            abil += s[p][val]
    return abil

def get_other_team_members(team):
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
    other_team = get_other_team_members(team)
    our_team_ability =  calc_team_ability(team)
    other_team_ability = calc_team_ability(other_team)
    result = min(result, abs(our_team_ability - other_team_ability))

print(result)
    


# dfs 백트래킹을 이용한 방법 
def dfs(start, team):
    global result

    if len(team) == n // 2:
        other_team = [p for p in range(n) if p not in team]
        our_team_ability = calc_team_ability(team)
        other_team_ability = calc_team_ability(other_team)
        result = min(result, abs(our_team_ability - other_team_ability))
        return

    for i in range(start, n):
        team.append(i)
        dfs(i + 1, team)
        team.pop()


# dfs(0, [])

