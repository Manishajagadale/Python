

for fizzbuzz in range(20):

    if fizzbuzz % 5 == 0 and fizzbuzz % 3 == 0:
        print("FizzBuzz")
        continue

    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue

    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue

    # print numbers
    print(fizzbuzz)