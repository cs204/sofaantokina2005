
menu = {
    "кофе": 20.00,
    "чай": 10.00,
    "булочка": 5.00,
    "салат": 30.40,
    "пирожное": 45.50,
}


amount =0

while True:
    try:
        x = input ("Блюдо: ")
        if x in menu:
            amount += menu[x]


    except EOFError:
        break


print(f"\nСумма: {amount:.2f}")