def to_int(x):
    return int(x)

def similarity_score(list1, list2):
    answer = 0
    for id in list1:
        answer += (id) * (list2.count(id))
    return answer

with open('puzzle_input.txt', 'r') as file:
    list1 = []
    list2 = []
    
    for line in file:
        id1, id2 = line.strip().split()
        list1.append(id1)
        list2.append(id2)

    list1, list2 = list(map(to_int, list1)), list(map(to_int, list2))
    list1.sort()
    list2.sort()


print(f"similarity score: {similarity_score(list1, list2)}")