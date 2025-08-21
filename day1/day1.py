
def to_int(x):
    return int(x)

def calculate(list1, list2):
    diff = []
    for a,b in zip(list1, list2):
        diff.append(abs(b - a))
    return int(sum(diff))


with open('puzzle_input.txt', 'r') as file:
    list1, list2 = [], []
    
    for line in file:
        id1, id2 = line.strip().split()
        list1.append(id1)
        list2.append(id2)
    list1, list2 = list(map(to_int, list1)), list(map(to_int, list2))
    list1.sort()
    list2.sort()

print(calculate(list1, list2))
