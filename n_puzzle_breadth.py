import math


def bfs(initialState , finalState):
    frontier = []         #frontier = μετωπο αναζητησης
    frontier.append(initialState)
    closed = []           #closed = κλειστο συνολο
    current = frontier[0] #current = μικροσκοπιο
    moves = 0
    while current != finalState:
        moves+=1
        if current in closed:
            frontier.pop(frontier.index(current))
        else:
            frontier.extend(find_children(current))
            frontier.pop(frontier.index(current))
            closed.append(current)

        current = frontier[0]


        #check if current is in closed
            #if not:
                #find the current's children
                #pop the current from the frontier
                #add current to closed
            #if yes:
                #pop current from frontier
    return print("Found solution: ", current , " in ", moves, "moves")

def find_children(state):

    n = len(state)
    dimmensions = int(math.sqrt(n))

    index_empty = state.index(0)

    top_row = [i for i in range(n) if i < dimmensions]

    bottom_row = [i for i in range(n) if n - dimmensions <= i < n]

    left_column = [i for i in range(n) if i % dimmensions == 0]

    right_column = [i for i in range(n) if (i + 1) % dimmensions == 0]

    in_top = False
    in_bot = False
    in_left = False
    in_right = False
    if index_empty in top_row :
        in_top = True
    elif index_empty in bottom_row :
        in_bot = True

    if index_empty in left_column :
        in_left = True
    elif index_empty in right_column :
        in_right = True

    children = []

    if in_top :
        if in_left:
            children.append(right(state))
            children.append(down(state))


        elif in_right:
            children.append(left(state))
            children.append(down(state))


        else:
            children.append(left(state))
            children.append(right(state))
            children.append(down(state))


    elif in_bot:
        if in_left:
            children.append(up(state))
            children.append(right(state))


        elif in_right:
            children.append(left(state))
            children.append(up(state))

        else:
            children.append(left(state))
            children.append(up(state))
            children.append(right(state))

    else:
        if in_left:
            children.append(up(state))
            children.append(right(state))
            children.append(down(state))

        elif in_right:
            children.append(left(state))
            children.append(up(state))
            children.append(down(state))

        else:
            children.append(left(state))
            children.append(up(state))
            children.append(right(state))
            children.append(down(state))

    return children

def right(state):
    items = list(state)

    i = items.index(0)

    n = int(math.sqrt(len(items)))

    if (i+1) % n != 0:
        del items[i]

        items.insert(i+1, 0)

        return items
    else:
        pass


def left(state):
    items = list(state)

    i = items.index(0)

    n = int(math.sqrt(len(items)))

    if i % n != 0:

        del items[i]

        items.insert(i-1, 0)

        return items
    else:
        pass


def up(state):
    items = list(state)

    i = items.index(0)

    n = int(math.sqrt(len(items)))

    if int(i/n)>0:

        del items[i]
        up_i = items.index(items[i-n])
        up_val = items[up_i]
        del items[up_i]

        items.insert(i-n, 0)
        items.insert(i,up_val)

        return items
    else:
        pass



def down(state):
    items = list(state)

    i = items.index(0)

    n = int(math.sqrt(len(items)))

    if int(i/n)<n-1:

        del items[i]
        down_i = items.index(items[i+n-1])
        down_val = items[down_i]
        del items[down_i]

        items.insert(i+n-1, 0)
        items.insert(i,down_val)

        return items
    else:
        pass


bfs([3,2,4,1,0,5,6,7,8],[1,2,3,4,5,6,7,8,0])
