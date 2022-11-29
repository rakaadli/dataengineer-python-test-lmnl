

givenInteger = 100

def HelloWorld(givenInteger):
    if givenInteger % 2 != 0:
        print("Hello")
    else:
        if givenInteger >= 2 and givenInteger <= 5:
            print("World")
        elif givenInteger >= 6 and givenInteger <= 20:
            print("Hello")
        elif givenInteger > 20:
            print("World")

HelloWorld(givenInteger)