# 람다식을 이용한 여러 기준으로 정렬

# 첫 숫자 내림 차순 
# 두번째 숫자 오름 차순
# 세번때 내림차순
# 이름 알파벳순 (사전 빠른순)

data = [['Junkyu', 50, 60, 100], 
        ['Sangkeun', 80, 60, 50], 
        ['Sunyoung', 80, 70, 100], 
        ['Soong', 50, 60, 90], 
        ['Haebin', 50, 60, 100], 
        ['Kangsoo', 60, 80, 100], 
        ['Donghyuk', 80, 60, 100], 
        ['Sei', 70, 70, 70], 
        ['Wonseob', 70, 70, 90], 
        ['Sanghyun', 70, 70, 80], 
        ['nsj', 80, 80, 80], 
        ['Taewhan', 50, 60, 90]]

result = sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0]))

print(result)