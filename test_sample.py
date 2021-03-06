from sample import FizzBuzz

def test_is_divisible_by_5_and_3():
    assert FizzBuzz(15) == "FizzBuzz"

def test_is_divisible_by_5():
    assert FizzBuzz(5) == "Buzz"

def test_is_divisible_by_3():
    assert FizzBuzz(3) == "Fuzz"

def test_if_neither_divisible_by_5_nor_3():
    assert FizzBuzz(11) == 11