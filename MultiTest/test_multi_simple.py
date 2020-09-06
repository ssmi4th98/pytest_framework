# to stop the test suite from going all the way through, you can break the test suite upon failure.

def test_type():
    assert type(1 + 2) is int

def test_add_int():
    assert 5 + 2 == 9

def test_string():
    assert 'u' in 'sun'

def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'
