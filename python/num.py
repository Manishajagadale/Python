def fizz_buzz(n):
    n = []
   # for nums in 30:
    for nums in range(50):
        if nums % 3 == 0 and nums % 5 == 0:
            print("fizz_buzz")
        elif nums % 3:
            print("fizz")
        elif nums % 5:
            print("buzz")
        elif nums % 3 != 0 and nums % 5 != 0:
            print(nums)
        else:
            print("invalid argument")
