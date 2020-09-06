import pytest

def divide(x,y):
    return x / y

def test_divide_pass():
    assert divide(9,3) == 3

# def test_divide_fail():
#    assert divide(9,a) == 3

# as lines 9 and 10 are what we want to test for

def test_divide_fail():
    with pytest.raises(TypeError):
        divide(9,'a')

# def test_divide_zero():
#    assert divide(9,0) == 3

# as lines 18 and 19 are what we want to test for, use a "with" block to raise the proper error.

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(9,0)

# type error (line 15) does not address the use of an issue with putting in a fake letter (no litteral)

def test_divide_non_lit():   # also these def do not take "-" in names only "_"
    with pytest.raises(NameError):
        divide(9,a)

