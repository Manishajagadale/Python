def Prime(num):

    for num in range(0, 23):
        # if num > 1:
        for i in range(2, num):
            if(num % i == 0):

                break
        else:
            print(num)
          #  num = 5
# Prime(n)
