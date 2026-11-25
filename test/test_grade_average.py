import pytest
from src.grade_average import calculate_average
from src.grade_pass import has_passed

@pytest.mark.parametrize(
    "mark_one, mark_two, expected",
    [
        (0, 0, 0.0),          # Lower boundary
        (100, 100, 100.0),    # Upper boundary
        (50, 70, 60.0),       # Typical whole-number average
        (50, 51, 50.5),       # Fractional average (exposes float err)
    ],
)
def test_calculate_average_valid_inputs(mark_one, mark_two, expected):
    assert calculate_average(mark_one, mark_two) == expected
    
    
@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (-1, 50),    # mark_one just below lower bound
        (50, -1),    # mark_two just below lower bound
        (101, 50),   # mark_one just above upper bound
        (50, 101),   # mark_two just above upper bound
    ],
)
def test_calculate_average_out_of_range(mark_one, mark_two):
    # Act & Assert
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)
        
        
@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (True, 50),      # bool is not a valid int rkw
        (50, False),     # bool is not a valid int
        (50.5, 50),      # float invalid
        ("50", 50),      # string invalid
        (None, 50),      # None invalid
    ],
)
def test_calculate_average_invalid_types(mark_one, mark_two):
    # Act & Assert
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)

