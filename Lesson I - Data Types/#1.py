src_name = str (input("enter your name"))
name = src_name
if len(name) <= 1000:
    name = name.split()
    for x in range(len(name)):
        name[x] = name[x].capitalize()
    a= ' '.join(name)
    print (a)
else:
    print("too many letters")