from savefile import save_file

name = input("Please enter your name")
shoesize = input("Please enter shoesize")
age = input("Please enter age") 

if shoesize == age:
    print("You are part of a lucky few!")


numbers = [1,2,3]
i = 0
while i < len(numbers):
  print(numbers[i])
  i += 1
  

for x in numbers:
  print(x)

def test(name):
   print("Hello", name)

test("Lewis")
test("Cohen")
test("Chris")

save_file(name, shoesize, age)