for num in range(0, 20):
    for i in range(2, num):
        if (num % i == 0):
            break
        else:
            print(num)
            break
