def FizzBuzz(int):
    if int%3==0 and int%5==0:
        return "FizzBuzz"

    if int%5==0:
        return "Buzz"

    if int%3==0:
        return "Fuzz"
    
    return int