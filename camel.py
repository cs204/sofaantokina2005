
camelCase=input("Верблюжий стиль: ")



for l in camelCase:


    if l.isupper():

        print("_" +l.lower(), end="")


    else:
        print(l, end="")

print()

