
from hypothesis import given, strategies as st
import pytest

from salon_booking import parse_booking, duration_average, payable_bill


@given(
    service=st.text(
        alphabet=st.characters(blacklist_characters=":"),
        min_size=1,
        max_size=40
    ),
    minutes=st.integers(min_value=0, max_value=600)
)
def test_parse_booking_no_crash(service, minutes):
    text = f"{service}:{minutes}"
    result = parse_booking(text)

    assert result == (service.strip().title(), float(minutes))


@given(
    durations=st.lists(
        st.integers(min_value=0, max_value=600),
        min_size=1,
        max_size=30
    )
)
def test_duration_average_no_crash(durations):
    text = ",".join(map(str, durations))
    result = duration_average(text)

    assert result == sum(durations) // len(durations)


@given(
    bill=st.integers(min_value=0, max_value=100000),
    discount=st.integers(min_value=0, max_value=100000)
)
def test_payable_bill_no_crash(bill, discount):
    text = f"{bill}|{discount}"
    result = payable_bill(text)

    expected = max(bill * 1.18 - discount, 0)

    assert result == pytest.approx(expected)
