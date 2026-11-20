import pytest
from src.grade_pass import has_passed

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