# to stop the test suite from going all the way through, you can break the test suite upon failure.
# use of decorators to mark tests then you only need to reference the "number" marker (flag is -m)
# you can use debug mode using the --pdb flag in console


import pytest


#@pytest.mark.number
def test_type():
    assert type(1 + 2) is int

#@pytest.mark.number
def test_add_int():
    assert 5 + 2 == 9

@pytest.mark.skip(reason = "This is just a test.")
def test_string():
    assert 'u' in 'sun'

#@pytest.mark.string
def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'
