



#spam = [['cat', 'bat', 'cow'], ['0', '1', '2']]

#print(spam[1][1:])
#print(len(spam))

#spam[0][1] = 'dog'

#print(spam[0][1])

#print(spam)

#spam = [1, 2, 3] + ['a', 'b', 'c']
#print(spam)

#del spam[3]
#print(spam)

catNames =[]

while True:
        print('enter cat name:' + str(len(catNames)) + 'or press enter to stop')
        name = input()

        catNames = catNames + [name]
        if name == '':
            break

for name in catNames:
    print(''+ name)
