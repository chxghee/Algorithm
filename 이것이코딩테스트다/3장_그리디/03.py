import sys

st = list(sys.stdin.readline().rstrip())
nums = [int(x) for x in st]

# 방법 1 연속된 문자 세트 수 // 2

convert = 1

for i in range(1, len(nums)):

    if nums[i-1] != nums[i]:
        convert += 1


print(convert // 2)

# 방법 2 전부 0으로 전부 1로 만드는 경우 중 작은것

cnt1=0
cnt2=0

for i in range(1, len(nums)):
    if nums[i-1] != nums[i]:
        if nums[i] == 1:
            cnt1 += 1
        if nums[i] == 0:
            cnt2 += 1

print(min(cnt1,cnt2))