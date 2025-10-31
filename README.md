# Airflow-Workflow DEMO App - Authentication System

This repository contains a small **authentication system** written in Python, designed as an **academic example** for demonstrating **workflow automation** using **Apache Airflow** & **Docker**.

The goal of this project is to provide a minimal, testable application that can be automatically cloned and tested through a workflow — illustrating the principles of **Workflow as Code**, **Continuous Integration**, and **Software Engineering**.


## Purpose

This app serves as a simple, self-contained **Software Engineering use case** to demonstrate how Airflow can :
1. Clone a GitHub repository.
2. Install its dependencies.
3. Run automated unit tests (`pytest`).
4. Display the results inside the Airflow UI.


## Features

- User creation and deletion  
- Password hashing and verification  
- Email validation  
- Login / Logout logic  
- In-memory user database  
- Full integration workflow tests  

All functionality is covered by automated **unit and integration tests**, making it perfect for demonstration in a CI/CD or workflow orchestration environment.


## Project Structure
```bash
Airflow-Workflow-DemoApp/
├── src/
│ ├── utils.py            # Password hashing & email validation.
│ ├── user.py             # User class and in-memory database.
│ └── auth.py             # Authentication system (login, logout, session tracking).
│
├── tests/
│ ├── test_utils.py       # Unit tests for hashing, email validation, and password checks.
│ ├── test_user.py        # Unit tests for user creation, deletion, and duplicates.
│ ├── test_auth.py        # Unit tests for authentication and sessions.
│ └── test_integration.py # Full workflow test combining all modules.
│
├── requirements.txt      # Python dependencies.
└── README.md
```

## Running the Tests

To execute all unit tests locally :
```bash
# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Run all tests with verbose output
pytest -v
```

Result :
```bash
====================================================================== test session starts =======================================================================
platform win32 -- Python 3.13.6, pytest-8.4.2, pluggy-1.6.0 -- D:\<path>\Airflow-Workflow-DemoApp\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\<path>\Airflow-Workflow-DemoApp
collected 27 items

tests/test_auth.py::test_login_success PASSED                                                                                                               [  3%]
tests/test_auth.py::test_login_wrong_password PASSED                                                                                                        [  7%]
tests/test_auth.py::test_login_nonexistent_user PASSED                                                                                                      [ 11%]
tests/test_auth.py::test_logout_success PASSED                                                                                                              [ 14%]
tests/test_auth.py::test_logout_user_not_logged_in PASSED                                                                                                   [ 18%]
tests/test_auth.py::test_multiple_logins_independent_sessions PASSED                                                                                        [ 22%]
tests/test_integration.py::test_full_authentication_workflow PASSED                                                                                         [ 25%]
tests/test_user.py::test_create_user_valid PASSED                                                                                                           [ 29%]
tests/test_user.py::test_create_user_invalid_email PASSED                                                                                                   [ 33%]
tests/test_user.py::test_create_user_empty_password PASSED                                                                                                  [ 37%]
tests/test_user.py::test_add_user_and_get_user PASSED                                                                                                       [ 40%]
tests/test_user.py::test_add_existing_user_raises_error PASSED                                                                                              [ 44%]
tests/test_user.py::test_remove_user_success PASSED                                                                                                         [ 48%]
tests/test_user.py::test_remove_user_not_found_returns_false PASSED                                                                                         [ 51%]
tests/test_user.py::test_user_count PASSED                                                                                                                  [ 55%]
tests/test_utils.py::test_hash_password_generates_different_hashes_for_different_inputs PASSED                                                              [ 59%]
tests/test_utils.py::test_hash_password_raises_error_on_empty_password PASSED                                                                               [ 62%] 
tests/test_utils.py::test_check_password_returns_true_for_correct_password PASSED                                                                           [ 66%] 
tests/test_utils.py::test_check_password_returns_false_for_wrong_password PASSED                                                                            [ 70%] 
tests/test_utils.py::test_check_password_returns_false_if_inputs_missing PASSED                                                                             [ 74%] 
tests/test_utils.py::test_is_valid_email_valid_formats[test@example.com] PASSED                                                                             [ 77%] 
tests/test_utils.py::test_is_valid_email_valid_formats[john.doe@university.edu] PASSED                                                                      [ 81%] 
tests/test_utils.py::test_is_valid_email_valid_formats[a_b-c@domain.co] PASSED                                                                              [ 85%] 
tests/test_utils.py::test_is_valid_email_invalid_formats[invalidemail] PASSED                                                                               [ 88%] 
tests/test_utils.py::test_is_valid_email_invalid_formats[noatsign.com] PASSED                                                                               [ 92%] 
tests/test_utils.py::test_is_valid_email_invalid_formats[wrong@.com] PASSED                                                                                 [ 96%]
tests/test_utils.py::test_is_valid_email_invalid_formats[@missinguser.com] PASSED                                                                           [100%] 

======================================================================= 27 passed in 0.06s =======================================================================
```

## How It Fits into an Airflow Workflow

This repository can be used in a DAG (*Directed Acyclic Graph*) to demonstrate workflow automation.

Example Airflow tasks:
- Clone this GitHub repo.
- Install dependencies.
- Run ```pytest -v``` inside a Docker container.
- Return results to the Airflow log.

This provides a realistic demonstration of “Workflow as Code”, where pipelines manage and validate real software projects automatically.

## Authors

Created for the Software Engineering course project (Fall 2025) by SEMENIKHINE MICHEL, BURRONI BLU & ESSIFI RAYAN.
