animals = []
animals.append("cat")
animals.append("dog")

birds = ["cock", "parrot"]
animals.extend(birds)
animals.insert(2, "fish")
count = len(animals)


print (animals)
print (count)
