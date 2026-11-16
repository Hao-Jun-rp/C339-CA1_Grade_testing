import pytest
from src.grade_average import calculate_average
from src.grade_pass import has_passed

@pytest.mark.parametrize(
    "mark_one, mark_two, expected",
    [
        (0, 0, 0.0),          # Lower boundary
        (100, 100, 100.0),    # Upper boundary
        (50, 70, 60.0),       # Typical whole-number average
        (50, 51, 50.5),       # Fractional average (exposes // 2 floor division bug)
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
        (True, 50),      # bool is not a valid int
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

# -------------- test for score pass/fail function --------------
@pytest.mark.parametrize(
    "score",
    [
        50, #exact pass boundary (exposes bug in has_passed function)
        51, #just above pass boundary
        100, #upper boundary 
    ]
)
def test_has_passed(score):
    result = has_passed(score)
    assert result is True
    
@pytest.mark.parametrize(
    "score",
    [
        0, #lower boundary
        49, #just below pass boundary
    ]
)
def test_has_not_passed(score):
    result = has_passed(score)
    assert result is False

@pytest.mark.parametrize("score", [-1,101])

def test_has_passed_out_of_range(score):
    with pytest.raises(ValueError):
        has_passed(score)
        
@pytest.mark.parametrize("score", [True,False, 50.5, "50", None])
def test_has_passed_invalid_types(score):
    with pytest.raises(TypeError):
        has_passed(score)