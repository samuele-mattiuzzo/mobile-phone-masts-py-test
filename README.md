# Mobile Phone Masts - data.gov.uk open dataset test


## Requirements
- Python 3
- Pytest

## Setup

  ```
  $ python3 -m venv env  # Create a virtual environment
  $ . env/bin/activate  # Activate our virtual environment
  $ pip install --upgrade pip  # Upgrade pip
  $ pip install -r requirements.txt  # Install pytest
  ```

## Running the app

- executing tasks 1 through 4 automatically

  ```
  $ python3 main.py
  ```


- executing a single task

  ```
  $ python3 main.py --t[1,2,3,4]
  ```

- running the tests

  ```
  $ py.test
  ```
