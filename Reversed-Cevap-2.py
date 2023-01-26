givenlist = [[1, 2], [3, 4], [5, 6, 7]]

def reversed(l):
    for i in range(len(l)):
        if type (l[i]) == list:
            l[i] = l[i][::-1]
            reversed(l[i])
    return (l[::-1])

reversedlist = reversed(givenlist)
print (reversedlist)
