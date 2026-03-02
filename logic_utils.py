def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # Changed: rebalance Hard to be a larger range than Normal
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Return a tuple (outcome, message)
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            # Changed: when guess is greater than secret, the hint should
            # instruct the player to go LOWER (not higher).
            return "Too High", "📈 Go LOWER!"
        else:
            # Guess is lower than secret; instruct player to go HIGHER.
            return "Too Low", "📉 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📈 Go LOWER!"
        return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def ensure_secret_in_range(secret, low: int, high: int):
    """Return the existing secret if it's within [low, high], otherwise
    return a new random secret inside the range.
    """
    import random

    try:
        if low <= secret <= high:
            return secret
    except Exception:
        # In case secret and bounds are not directly comparable, regenerate
        pass

    return random.randint(low, high)
