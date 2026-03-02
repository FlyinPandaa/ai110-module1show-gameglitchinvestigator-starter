import random
from logic_utils import (
    get_range_for_difficulty,
    check_guess,
    ensure_secret_in_range,
)


def test_get_range_for_difficulty_hard():
    low, high = get_range_for_difficulty("Hard")
    assert (low, high) == (1, 200)


def test_hard_range_larger_than_normal():
    _, high_hard = get_range_for_difficulty("Hard")
    _, high_normal = get_range_for_difficulty("Normal")
    assert high_hard > high_normal


def test_ensure_secret_in_range_regenerates_when_out_of_range():
    low, high = 1, 20
    original = 90  # outside 1..20
    new_secret = ensure_secret_in_range(original, low, high)
    assert low <= new_secret <= high
    # If original already in range, it should be returned unchanged
    original2 = 10
    same = ensure_secret_in_range(original2, low, high)
    assert same == original2


def test_check_guess_hints_direction():
    # When guess > secret the outcome should be Too High and hint instructs LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()

    # When guess < secret the outcome should be Too Low and hint instructs HIGHER
    outcome2, message2 = check_guess(40, 50)
    assert outcome2 == "Too Low"
    assert "HIGHER" in message2.upper()
