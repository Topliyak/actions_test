import pytest
from app.models import Calculator

# Непадающие тесты
def test_calculator_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0

def test_calculator_multiply():
    assert Calculator.multiply(3, 4) == 12
    assert Calculator.multiply(0, 5) == 0

# Падающие тесты (закомментированы)
def test_calculator_divide():
    """Этот тест упадет при делении на ноль"""
    assert Calculator.divide(10, 2) == 5
    # Следующая строка вызовет исключение - тест упадет
    Calculator.divide(5, 0)

def test_failing_assertion():
    """Тест с неправильным утверждением"""
    result = Calculator.add(1, 1)
    assert result == 3  # Неправильное утверждение - тест упадет
