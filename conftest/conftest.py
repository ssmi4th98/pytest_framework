import pytest
import os

@pytest.fixture()
def write_file():
    print('\n Create File')
    f = open('newFile.txt','w+')

    for i in range(10):
        f.write('\n X Y Z %d' % (i + 1))

    f.flush()

    yield f

    print('\nClose File')
    f.close()


@pytest.fixture()
def read_file():
    print('\n Create Read File')
    f = open('readOnly_File.txt','w+')

    for i in range(10):
        f.write('\n X Y Z %d' % (i + 1))

    f.close()

    f = open('readOnly_File.txt','r')

    yield f

    print('\nClose File')
    f.close()

