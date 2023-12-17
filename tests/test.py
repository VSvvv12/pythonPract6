from app import calculator
import pytest


@pytest.fixture
def calculator_instance_pos():
    return calculator.Calculator(5, 3)


@pytest.fixture
def calculator_instance_neg():
    return calculator.Calculator(-5, -3)


def test_plus_first(calculator_instance_pos):
    result = calculator_instance_pos.plus()
    assert result == 8


def test_plus_second(calculator_instance_neg):
    result = calculator_instance_neg.plus()
    assert result == -8


def test_minus_first(calculator_instance_pos):
    result = calculator_instance_pos.minus()
    assert result == 2


def test_minus_second(calculator_instance_neg):
    result = calculator_instance_neg.minus()
    assert result == -2


def test_division_first(calculator_instance_pos):
    result = calculator_instance_pos.division()
    assert result == 1.6666666666666667


def test_division_second(calculator_instance_neg):
    result = calculator_instance_neg.division()
    assert result == 1.6666666666666667


def test_multiplication_first(calculator_instance_pos):
    result = calculator_instance_pos.multiplication()
    assert result == 15


def test_multiplication_second(calculator_instance_neg):
    result = calculator_instance_neg.multiplication()
    assert result == 15


def test_degree_first(calculator_instance_pos):
    result = calculator_instance_pos.degree()
    assert result == 125


def test_degree_second(calculator_instance_neg):
    result = calculator_instance_neg.degree()
    assert result == -0.008


def test_arithmetic_first(calculator_instance_pos):
    result = calculator_instance_pos.arithmetic()
    assert 2 <= result <= 400


def test_arithmetic_second(calculator_instance_neg):
    result = calculator_instance_neg.arithmetic()
    assert -400 <= result <= -2
