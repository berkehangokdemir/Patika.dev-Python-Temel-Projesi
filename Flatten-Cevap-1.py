givenlist = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flattenedlist = []

def flatten(x):
    for i in x:
        if type(i) == list:
            flatten(i)
        elif type(i) != list:
            flattenedlist.append(i)

flatten(givenlist)
print(flattenedlist)
