list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for i in range(0, len(list)/2):
    list[i], list[-1-i] = list[i-1], list[i]

print list



