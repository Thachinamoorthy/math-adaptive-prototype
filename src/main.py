import time
from . import puzzle_generator
from .tracker import PerformanceTracker
from .adaptive_engine import AdaptiveEngine

def get_initial_difficulty() -> str:
    """
    Prompts user to select an initial difficulty level.
    
    """
    while True:
        print("Choose your starting difficulty:")
        print("  1. Easy")
        print("  2. Medium")
        print("  3. Hard")
        choice = input("Enter choice (1, 2, or 3): ")
        
        if choice == '1':
            return puzzle_generator.LEVEL_EASY
        elif choice == '2':
            return puzzle_generator.LEVEL_MEDIUM
        elif choice == '3':
            return puzzle_generator.LEVEL_HARD
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    """
    Main function to run the adaptive learning session.
    """
    print("Welcome to Math Adventures!")
    
    # 1. Start: Get user name and initial difficulty 
    user_name = input("What's your name? ")
    print(f"\nHi, {user_name}! Let's practice some math.")
    
    initial_difficulty = get_initial_difficulty()
    
    # Initialize Core Components [cite: 11]
    tracker = PerformanceTracker()
    engine = AdaptiveEngine(initial_difficulty)
    
    num_questions = 10 # Total number of puzzles in one session
    current_difficulty = engine.get_difficulty_str()
    
    print(f"\nSession starting with {num_questions} puzzles. Good luck!")

    for i in range(num_questions):
        print(f"\n--- Puzzle {i + 1} of {num_questions} (Level: {current_difficulty}) ---")
        
        # 2. Puzzle: Generate and show the puzzle 
        question, correct_answer = puzzle_generator.generate_puzzle(current_difficulty)
        
        # 3. Performance Tracking: Start timer and get answer 
        start_time = time.time()
        
        try:
            user_answer_str = input(f"What is {question}? ")
            user_answer = int(user_answer_str)
        except ValueError:
            print("Oops! That's not a valid number. We'll count that as incorrect.")
            user_answer = None

        end_time = time.time()
        time_taken = end_time - start_time
        
        # Check correctness
        is_correct = (user_answer == correct_answer)
        
        if is_correct:
            print(f"Correct! You took {time_taken:.2f} seconds.")
        else:
            print(f"Not quite. The correct answer was {correct_answer}.")

        # 3. Performance Tracking: Log the result 
        tracker.log(is_correct, time_taken, current_difficulty)
        
        # 4. Adaptive Logic: Update difficulty for the *next* loop 
        current_difficulty = engine.update_difficulty(tracker)
        
    # 5. Summary: Show session statistics 
    final_level = engine.get_difficulty_str()
    tracker.print_summary(next_level=final_level)

if __name__ == "__main__":
    main()
