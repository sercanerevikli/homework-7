names = ("Ross", "Rachel", "Chandler", "Monica", "Joey", "Phoebe")
listOfFriends = set()

for invitedName in names:
    getName = input("Enter the name have you invited: ")
    ListOfNames = getName.split()
    for invitedName in ListOfNames:
        listOfFriends.add(invitedName)

for invitedName in enumerate(listOfFriends):
    print(invitedName)