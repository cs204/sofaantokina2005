while True:
    fuel=input("Дробь: ")
    try:
        x, y = fuel.split("/")
        z=int(x)
        s=int(y)
        f=z/s

        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
p=int(f*100)

if p <= 1:
    print("E")
elif p>=99:
    print("F")
else:
    print(f"{p}%")