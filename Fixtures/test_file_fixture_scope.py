import pytest
import os

#@pytest.fixture(scope='module')   # here we set the scope of the fixture to apply it conditionally run only once during suite.
@pytest.fixture()   # here we strip out the scope The fixture is then executed for each test.
def test_file():
    print('\nTest for Scope')  #setUp function
    f = open('test_file.txt','a+')
    yield f  # here we use the yield to hold the sequence in order : a generator

    print('\nClose file') # tearDown.
    f.close()

def test_write_ten_times(test_file):  # this is the fixture function as part of the test.
    print('\nWriting line ten times.')
    num_lines_before = sum(1 for line in open(test_file.name))

    for i in range(10):
        test_file.write('x y z %d\n' % (i +1))

    test_file.flush()
    num_lines_after = sum(1 for line in open(test_file.name))

    assert (num_lines_after - num_lines_before) == 10


def test_file_size_on_write(test_file):
    print('\nWrite one line.')
    size_before = os.stat(test_file.name).st_size

    test_file.write('a b c 1\n')
    test_file.flush()

    size_after = os.stat(test_file.name).st_size
    assert (size_after - size_before) > 0