# Constants map string levels to numeric for easier logic
LEVEL_MAP = {"Easy": 0, "Medium": 1, "Hard": 2}
LEVEL_MAP_REV = {0: "Easy", 1: "Medium", 2: "Hard"}

MIN_LEVEL = 0
MAX_LEVEL = 2

class AdaptiveEngine:
    """
    Uses rule-based logic to decide the next difficulty level.
    [cite: 1, 12]
    """
    def __init__(self, initial_difficulty: str):
        # Set the starting difficulty level 
        self.current_level_num = LEVEL_MAP.get(initial_difficulty, MIN_LEVEL)
        print(f"Adaptive Engine initialized. Starting level: {self.get_difficulty_str()}")

    def get_difficulty_str(self) -> str:
        """Returns the string name of the current level."""
        return LEVEL_MAP_REV[self.current_level_num]

    def update_difficulty(self, tracker) -> str:
        """
        The core adaptive logic.
        Checks the last 2 results and decides whether to change difficulty.
        [cite: 9, 14]
        """
        
        # Get the last two performance results from the tracker [cite: 18]
        last_two_results = tracker.get_last_n_results(2)

        # Don't change difficulty if we don't have enough data yet
        if len(last_two_results) < 2:
            return self.get_difficulty_str()

        # Check for 2 correct in a row to level up
        all_correct = all(res[0] for res in last_two_results)
        
        # Check for 2 incorrect in a row to level down
        all_incorrect = all(not res[0] for res in last_two_results)

        # --- Rule-Based Logic ---
        # If doing well -> increase difficulty 
        if all_correct and self.current_level_num < MAX_LEVEL:
            self.current_level_num += 1
            print(f"\n[Adaptive Engine]: Great job! Increasing difficulty to {self.get_difficulty_str()}...\n")
        
        # If struggling -> decrease difficulty 
        elif all_incorrect and self.current_level_num > MIN_LEVEL:
            self.current_level_num -= 1
            print(f"\n[Adaptive Engine]: No problem. Let's try something easier. Decreasing difficulty to {self.get_difficulty_str()}...\n")
        
        # Otherwise, stay at the current level
        
        return self.get_difficulty_str()
