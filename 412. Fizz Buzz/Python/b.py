def fizzBuzz(n):
    f, b, fb = "Fizz", "Buzz", "FizzBuzz"
    arr = [str(i + 1) for i in range(n)]

    for i in range(2, n, 3):
        arr[i] = f

    for i in range(4, n, 5):
        arr[i] = b

    for i in range(14, n, 15):
        arr[i] = fb

    return arr