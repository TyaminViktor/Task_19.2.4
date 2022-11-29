from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_success(self):
        assert self.calc.multiply(-2, 3) == -6

    def test_division_success(self):
        assert self.calc.division(10, 2) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(0, -2) == 2

    def test_adding_success(self):
        assert self.calc.adding(0, -2) == -2

    def teardown(self):
        print("Выполнение метода Teardown")
