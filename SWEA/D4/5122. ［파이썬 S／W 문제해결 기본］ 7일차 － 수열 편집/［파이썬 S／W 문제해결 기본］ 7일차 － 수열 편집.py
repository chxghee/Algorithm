
tc = int(input())

for i in range(1, tc+1):

    n, m, l = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(m):
        line = input().strip().split()
        cmd = line[0]

        if cmd == 'I':
            idx = int(line[1])
            new_number = int(line[2])
            numbers.insert(idx, new_number)


        elif cmd == 'C':
            idx = int(line[1])
            change_number = int(line[2])
            numbers[idx] = change_number

        else:
            idx = int(line[1])
            numbers.pop(idx)
    
    if len(numbers) <= l:
        print(f"#{i} -1")
    else:
        print(f"#{i} {numbers[l]}")
