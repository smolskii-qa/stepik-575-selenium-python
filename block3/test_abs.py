class TestAbs:
    def test_abs1(self):
        assert abs(-42) == 42, "Should be absolute value of a number"

    def test_abs2(self):
        assert abs(-42) == -42, "Should be absolute value of a number"


if __name__ == "__main__":
    TestAbs.test_abs1()
    TestAbs.test_abs2()
