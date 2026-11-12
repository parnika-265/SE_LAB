from hypothesis import given, strategies as st
from processor import (
    verify_isbn10_format,
    calculate_depreciation_factor,
    lookup_condition_multiplier,
)


@given(st.text() | st.none())
def test_verify_isbn10_format_no_crash(s):
    try:
        verify_isbn10_format(s)
    except Exception as e:
        assert False, f"verify_isbn10_format crashed with {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_calculate_depreciation_factor_safe(s):
    try:
        result = calculate_depreciation_factor(s)
    except Exception as e:
        assert False, f"calculate_depreciation_factor crashed with {type(e).__name__}: {e}"
    assert result is None or 0.1 <= result <= 1.0


@given(st.text() | st.none())
def test_lookup_condition_multiplier_safe(s):
    try:
        result = lookup_condition_multiplier(s)
    except Exception as e:
        assert False, f"lookup_condition_multiplier crashed with {type(e).__name__}: {e}"
    assert result is None or result in (1.25, 1.00, 0.80, 0.60, 0.30)
