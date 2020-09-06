def rectangle_per(length,width):
	return 2 * (length + width)

def test_perimeter():  # this must start with the prefix "test" to get picked up by the pytest framework.
	assert rectangle_per(3, 4) == 14
