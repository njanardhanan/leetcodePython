
def test_assert(actual, expected):
    if actual == expected:
        print("PASSED")
    else:
        print('Excepted ' + str(expected) + ' but was ' + str(actual))