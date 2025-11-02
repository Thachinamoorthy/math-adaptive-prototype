import time

class PerformanceTracker:
    """
    Logs performance metrics (correctness, time) for each puzzle.
    [cite: 4, 12]
    """
    def __init__(self):
        # Stores logs of (is_correct, time_taken, difficulty)
        self.results = []
        self.session_start_time = time.time()

    def log(self, is_correct: bool, time_taken: float, difficulty: str):
        """Logs a single puzzle's result."""
        self.results.append((is_correct, time_taken, difficulty))
        print(f"Result logged: Correct={is_correct}, Time={time_taken:.2f}s, Level={difficulty}")

    def get_last_n_results(self, n: int) -> list:
        """Helper to get the last N results for the adaptive engine."""
        return self.results[-n:]

    def get_summary(self) -> dict:
        """
        Calculates session statistics for the final summary.
        [cite: 10, 12]
        """
        if not self.results:
            return {
                "total": 0,
                "correct": 0,
                "accuracy": 0,
                "avg_time": 0,
                "total_session_time": 0,
            }

        total = len(self.results)
        correct = sum(1 for res in self.results if res[0])
        accuracy = (correct / total) * 100
        avg_time = sum(res[1] for res in self.results) / total
        total_session_time = time.time() - self.session_start_time

        return {
            "total": total,
            "correct": correct,
            "accuracy": accuracy,
            "avg_time": avg_time,
            "total_session_time": total_session_time,
        }

    def print_summary(self, next_level: str):
        """
        Displays the final end-of-session performance summary.
        
        """
        summary = self.get_summary()
        
        print("\n--- Session Summary ---")
        print(f"Total Puzzles: {summary['total']}")
        print(f"Correct Answers: {summary['correct']}")
        print(f"Accuracy: {summary['accuracy']:.1f}%")
        print(f"Average Time: {summary['avg_time']:.2f} seconds/puzzle")
        print(f"Total Session Time: {summary['total_session_time']:.2f} seconds")
        print("---")
        print(f"Recommended starting level next time: {next_level}")
        print("\nGreat job! Keep practicing!\n")
