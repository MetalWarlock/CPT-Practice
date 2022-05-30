with open('input.txt') as f:
    a = sorted([int(x) for x in f.read().split('\n')], reverse=True)

b = []


def sum_to(containers, goal, values_in_goal=0):

    if len(containers) == 0:
        return 0

    head = containers[0]
    tail = containers[1:]

    if head > goal:
        with_head = 0
    elif head == goal:
        b.append(values_in_goal + 1)
        with_head = 1
    else:
        with_head = sum_to(tail, goal - head, values_in_goal + 1)

    return with_head + sum_to(tail, goal, values_in_goal)


with open('output1.txt', 'w') as f:
    print(sum_to(a, 150), file=f)