names = {'Basil': 'qwerty', 'Alice': 'alice'}

while True:
    n = input("Please enter your name. (empty enter - exit)")
    if n == '':
        break
    if n in names.keys():
        while True:
            p = input("Please enter your password. (empty enter - exit)")
            if p == '':
                break
            elif names.get(n) == p:
                print("Password for user:", n, "is correct")
                break
            else:
                print("Password for user:", n, "is incorrect")
                print("Please try again…")
    else:
        print("Err: Name is incorrect or unused")
        print("Please try again…")

