import random

# Use constants for difficulty levels for clarity
LEVEL_EASY = "Easy"
LEVEL_MEDIUM = "Medium"
LEVEL_HARD = "Hard"


def generate_puzzle(difficulty: str) -> (str, int):
    """
    Creates a math problem dynamically based on the difficulty level.
    [cite: 12]
    """
    if difficulty == LEVEL_EASY:
        # Easy: Single-digit addition
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        question = f"{a} + {b}"
        answer = a + b
    elif difficulty == LEVEL_MEDIUM:
        # Medium: Two-digit addition/subtraction (no negative results)
        a = random.randint(10, 30)
        b = random.randint(10, 20)
        if a > b:
            question = f"{a} - {b}"
            answer = a - b
        else:
            question = f"{a} + {b}"
            answer = a + b
    elif difficulty == LEVEL_HARD:
        # Hard: Single-digit multiplication
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        question = f"{a} * {b}"
        answer = a * b
    else:
        # Default to Easy if difficulty is unknown
        return generate_puzzle(LEVEL_EASY)

    return question, answer
