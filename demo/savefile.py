def save_file(name, shoesize, age):
    f = open("data.txt", "a")
    f.write(name + " " + shoesize + " " + age)
    f.close()

    #open and read the file after the appending:
    f = open("data.txt", "r")
    print(f.read())