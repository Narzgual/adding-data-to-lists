

catNames =[]

while True:
        print('enter cat name:' + str(len(catNames)) + 'or press enter to stop')
        name = input()

        catNames = catNames + [name]
        if name == '':
            break

for name in catNames:
    print(''+ name)
