## Explanation

- `main.py` is the main application runner; it allows to select which task to run, based on their order

- `tasks.py` contains the functions required to produce each task's output as per received document

- `utils.py` is a bare utilities file whose purpose is to offer reusable functions for this task's purpose; they are fairly trivial functionalities

- `test_tasks.py` and `test_utils.py` are the Pytest tests for each module

- **Time used:** just under 2 hours (including refactoring time)

- A *test driven* approach has been followed, using the **RED-GREEN-REFACTOR** pattern (write a test, run the test, write the function, test again, refactor the code)

- No extra libraries and dependencies as per test requirement; due to carefulness, utilities such as itertools have been avoided

- Functions have been chosen to keep the codebase simple and avoid over engineering the code for the purpose of this task; however, some improvements could be made if the scope of the exercise increases (eg: a RowRecord class would simplify access to its values)