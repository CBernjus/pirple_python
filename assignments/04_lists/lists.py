# Homework Assignment  # 4 - Lists

myUniqueList = []
myLeftovers = []


def add(thing):
    if thing in myUniqueList:
        myLeftovers.append(thing)
        return False
    else:
        myUniqueList.append(thing)
        return True


add("Hello")
add("Hi")
add("Hey")

print(add("Hi"))
print(add("World"))

print(myUniqueList)
print(myLeftovers)
