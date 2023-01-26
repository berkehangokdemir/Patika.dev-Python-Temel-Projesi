typedlist = [[3,4], [[["a"]]], "b", 8, ["patika.dev"], 3.4, [["berkehan"]], 11, 12, True]
flattenedlist = []

def flatten(x):
    for i in x:
        if type(i) == list:
            flatten(i)
        elif type(i) != list:
            flattenedlist.append(i)

flatten(typedlist)
print(flattenedlist)
