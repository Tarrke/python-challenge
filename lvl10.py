# Clue :
# a = [ 1, 11, 21, 1211, 111221 ]

def calculateNextItem(item):
    next = ''
    c = 0
    l = len(item)
    o = item[c]
    cpt = 0
    while c < l:
        if item[c] == o:
            cpt += 1
        else:
            next += str(cpt) + o
            cpt = 1
            o = item[c]
        c += 1
    next += str(cpt) + item[c-1]
    return next

index = 30
current = 1

a = ['1']

while current <= index:
    print('Current Index:', current)
    a.append(calculateNextItem(a[current-1]))
    current += 1

print(len(a[30]))