def speed(speed):
    if speed <= 70:
        return "OK"
    else:
        speed1 = (speed - 70)//5
        if speed1 <= 12:
            return print(f"point: {speed1}")
        else:
            return print("license suspended")


enter = speed(int(input("Enter speed:")))
print(enter)
