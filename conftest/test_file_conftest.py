def test_write_ten_time(write_file):
    print('\nWrite the file test.')
    num_lines_before = sum(1 for line in open(write_file.name))
    print(num_lines_before)

    for i in range(10):
        write_file.write('\nX Y Z %d' % (i + 1))

    write_file.flush()

    num_lines_after = sum(1 for line in open(write_file.name))
    print(num_lines_after)
    assert (num_lines_after - num_lines_before) == 10

def test_field_count(read_file):
    print('\nRead one line.')

    read_file.readline()
    field_count = len(read_file.readline().split())
    print(field_count)

    assert field_count == 4