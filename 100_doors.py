# A program that opens and closes doors
# https://www.freecodecamp.org/learn/coding-interview-prep/rosetta-code/100-doors


doors = []
i = 1
for i in range(1, 101):
    for num in range(1, 101):
        if num not in doors and num % i == 0:
            doors.append(num)
            doors.sort()
        elif num in doors and num % i == 0:
            doors.remove(num)
            doors.sort()
        else:
            continue
    print(f'{i}:{doors}\n')

