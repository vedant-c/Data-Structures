def min_len(points):
    x1=points[0][0]
    x2=points[1][0]
    y1=points[0][1]
    y2=points[1][1]

    return max( abs(x2-x1),abs(y2-y1))


def get_min_length(array):
    length=0
    for i in range(len(array)-1):
        length+=min_len([array[i],array[i+1]])

    return length

x=get_min_length([[1,1],[3,4],[-1,0]])
print(x)
