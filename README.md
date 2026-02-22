# Python TDD Project – Rövarspråket & Pattern Cipher

This project demonstrates Test-Driven Development (TDD) and test coverage analysis in Python.

## Task 1 – Rövarspråket
- Implemented encoding and decoding logic.
- Wrote unit tests using unittest.
- Identified and fixed defects in consonant handling.
- Achieved 100% statement and branch coverage.

## Task 2 – Pattern Cipher
- Implemented rule-based single-word transformation.
- Applied equivalence partitioning to design unit tests.
- Used pytest for testing.
- Achieved 100% statement and branch coverage.

##  Technologies Used
- Python
- unittest
- pytest
- pytest-cov
- Anaconda Terminal

##  How to Run the Project

### Run Task 1 Tests

cd DDM_Task1
python test_Task1_Rover.py


### Run Task 2 Tests

cd DDM_Task2
pytest -q


### Generate Coverage Report

pytest --cov --cov-branch --cov-report=html


Coverage reports are generated inside the `htmlcov` directory.

This was a collaborative academic project focused on understanding unit testing, coverage analysis, and debugging practices.
