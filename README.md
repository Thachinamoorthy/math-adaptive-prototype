# math-adaptive-prototype
# Math Adventures - AI-Powered Adaptive Learning Prototype

This repository contains a minimal prototype for an adaptive math learning application, as per the "Adaptive Learning Assignment".

## Objective

The goal of this prototype is to demonstrate an AI-powered system that dynamically personalizes learning difficulty[cite: 2]. [cite_start]It helps children (ages 5-10) practice basic math by adjusting puzzle difficulty based on their performance, aiming to keep them in their optimal challenge zone[cite: 2, 3].

## Features

**Puzzle Generation**: Creates simple math puzzles (addition, subtraction, multiplication)[cite: 3, 4].
**Difficulty Levels**: Supports three levels: Easy, Medium, and Hard[cite: 13].
**Performance Tracking**: Tracks user correctness and response time for each puzzle.
**Adaptive Engine**: Uses a simple, rule-based logic to automatically adjust puzzle difficulty up or down based on user performance[cite: 4, 9, 14].
**Session Summary**: Displays a basic performance summary at the end of the session.

## Project Structure
README.md  
requirements.txt 
src/ init.py  main.py puzzle_generator.py  tracker.py  adaptive_engine.py

How to Run
This is a pure Python console application. No external libraries are required.

1.  Clone the repository.
2.  Navigate to the `math-adaptive-prototype` directory.
3.  Run the main application from the root directory:

    ```bash
    python -m src.main
    ```

4.  Follow the on-screen prompts to enter your name, choose a starting difficulty, and answer the math puzzles.
