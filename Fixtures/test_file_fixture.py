import pytest
import os  ## helps with os level functions such as opening a file or reading it.

@pytest.fixture  # this sets up the decorator This sets up the fixture and run for each test.
def test_file():
    print("\nCreate File")
    f = open('test_file.txt','a+')  # opens file in append mode
    return f

def test_write_ten_times(test_file):  # this is the fixture function as part of the test.
    print('\nWriting line ten times.')
    num_lines_before = sum(1 for line in open(test_file.name))

    for i in range(10):
        test_file.write('x y z %d\n' % (i +1))

    test_file.flush()
    num_lines_after = sum(1 for line in open(test_file.name))

    assert (num_lines_after - num_lines_before) == 10
    test_file.close()

def test_file_size_on_write(test_file):
    print('\nWrite one line.')
    size_before = os.stat(test_file.name).st_size

    test_file.write('a b c 1\n')
    test_file.flush()

    size_after = os.stat(test_file.name).st_size
    assert (size_after - size_before) > 0
    test_file.close()





