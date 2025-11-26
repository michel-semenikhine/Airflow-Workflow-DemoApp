# Airflow Workflow — DIRECTED ACYCLIC GRAPH

## Overview
This project demonstrates how to build and run **batch-oriented workflows** using **Apache Airflow**, executed inside a **Dockerized environment**.  
It includes:

- A **custom Airflow Docker image** with Git + pytest installed  
- A complete pipeline (**DAG**) named `github_test_pipeline`  
- A workflow that:
  1. Clones a GitHub repository  
  2. Installs its Python dependencies  
  3. Runs pytest unit tests  
  4. Displays the results inside Airflow  
  5. Cleans temporary files  

This project is used for academic purposes in the context of the *Software Engineering* course.

---

# Project Structure
```
AIRFLOW-WORKFLOW-DEMOAPP/
│
├── config/
├── dags/
│ └── github_test_pipeline.py # Main workflow DAG
│
├── logs/
├── plugins/
├── docker-compose.yaml # Airflow services configuration
├── Dockerfile # Custom Airflow image
└── README.md
```

---

# Requirements

Before running this project, you need:

- **Docker Desktop** installed and running
- **Docker Compose** enabled  
- Local ports **8080**, **5432**, **6379** available  

---

# Custom Docker Image

This project uses a **custom Airflow image** based on **apache/airflow:2.9.3-python3.12**

The Dockerfile installs:

- **Git** → required for cloning repositories  
- **pytest** → required for running test suites  

```dockerfile
FROM apache/airflow:2.9.3-python3.12

# Install Git
USER root
RUN apt-get update && apt-get install -y git

# Back to airflow user
USER airflow
RUN pip install --no-cache-dir pytest
```

---

# Getting Started
## Build the environment

From inside the project folder, run these 2 commands to setup Airflow:
```bash
docker compose build --no-cache
docker compose up -d
```
This step initializes:
- The Airflow database
- All required Airflow services
- The custom image with Git + pytest installed

All Airflow services will start:
- airflow-webserver
- airflow-scheduler
- airflow-worker
- airflow-triggerer
- postgres
- redis

You can inspect running containers by using the following command:
```bash
docker ps
```

## Access the Airflow UI

Open your browser at: http://localhost:8080

Default credentials:
- username: airflow
- password: airflow

When you are done using Docker and want to remove all data: :
```bash
docker compose down --volumes --remove-orphans
```
This will stop all containers and remove:
- Database files
- Any cached container data

# Running the DAG
## DAG: github_test_pipeline

The DAG performs:
1. Clone the GitHub repository
2. Install dependencies (if requirements.txt exists)
3. Run pytest
4. Clean up temporary files

In airflow web UI:
1. Search the dag in search field: `github_test_pipeline`
2. Once found, launch the dag by clicking the arrow button on top right (named "Trigger DAG")
3. You can follow progress in Graph View


After the DAG finished its process, you will find the logs inside logs folder as `dag_id=github_test_pipeline`:

`task_id=clone_repo`\
`task_id=install_dependencies`\
`task_id=run_pytest`\
`task_id=cleanup_temp`\

The main log is `task_id=run_pytest`, it contains logs of DEMOapp unit tests.

```log
[2025-11-26T13:21:06.634+0000] {subprocess.py:93} INFO - collecting ... collected 27 items
[2025-11-26T13:21:06.635+0000] {subprocess.py:93} INFO - 
[2025-11-26T13:21:06.636+0000] {subprocess.py:93} INFO - tests/test_auth.py::test_login_success PASSED                            [  3%]
[2025-11-26T13:21:06.637+0000] {subprocess.py:93} INFO - tests/test_auth.py::test_login_wrong_password PASSED                     [  7%]
[2025-11-26T13:21:06.638+0000] {subprocess.py:93} INFO - tests/test_auth.py::test_login_nonexistent_user PASSED                   [ 11%]
[2025-11-26T13:21:06.639+0000] {subprocess.py:93} INFO - tests/test_auth.py::test_logout_success PASSED                           [ 14%]
[2025-11-26T13:21:06.639+0000] {subprocess.py:93} INFO - tests/test_auth.py::test_logout_user_not_logged_in PASSED                [ 18%]
[2025-11-26T13:21:06.640+0000] {subprocess.py:93} INFO - tests/test_auth.py::test_multiple_logins_independent_sessions PASSED     [ 22%]
[2025-11-26T13:21:06.641+0000] {subprocess.py:93} INFO - tests/test_integration.py::test_full_authentication_workflow PASSED      [ 25%]
[2025-11-26T13:21:06.641+0000] {subprocess.py:93} INFO - tests/test_user.py::test_create_user_valid PASSED                        [ 29%]
[2025-11-26T13:21:06.642+0000] {subprocess.py:93} INFO - tests/test_user.py::test_create_user_invalid_email PASSED                [ 33%]
[2025-11-26T13:21:06.642+0000] {subprocess.py:93} INFO - tests/test_user.py::test_create_user_empty_password PASSED               [ 37%]
[2025-11-26T13:21:06.643+0000] {subprocess.py:93} INFO - tests/test_user.py::test_add_user_and_get_user PASSED                    [ 40%]
[2025-11-26T13:21:06.643+0000] {subprocess.py:93} INFO - tests/test_user.py::test_add_existing_user_raises_error PASSED           [ 44%]
[2025-11-26T13:21:06.644+0000] {subprocess.py:93} INFO - tests/test_user.py::test_remove_user_success PASSED                      [ 48%]
[2025-11-26T13:21:06.644+0000] {subprocess.py:93} INFO - tests/test_user.py::test_remove_user_not_found_returns_false PASSED      [ 51%]
[2025-11-26T13:21:06.645+0000] {subprocess.py:93} INFO - tests/test_user.py::test_user_count PASSED                               [ 55%]
[2025-11-26T13:21:06.645+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_hash_password_generates_different_hashes_for_different_inputs PASSED [ 59%]
[2025-11-26T13:21:06.646+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_hash_password_raises_error_on_empty_password PASSED [ 62%]
[2025-11-26T13:21:06.646+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_check_password_returns_true_for_correct_password PASSED [ 66%]
[2025-11-26T13:21:06.647+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_check_password_returns_false_for_wrong_password PASSED [ 70%]
[2025-11-26T13:21:06.647+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_check_password_returns_false_if_inputs_missing PASSED [ 74%]
[2025-11-26T13:21:06.648+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_is_valid_email_valid_formats[test@example.com] PASSED [ 77%]
[2025-11-26T13:21:06.648+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_is_valid_email_valid_formats[john.doe@university.edu] PASSED [ 81%]
[2025-11-26T13:21:06.649+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_is_valid_email_valid_formats[a_b-c@domain.co] PASSED [ 85%]
[2025-11-26T13:21:06.649+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_is_valid_email_invalid_formats[invalidemail] PASSED [ 88%]
[2025-11-26T13:21:06.649+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_is_valid_email_invalid_formats[noatsign.com] PASSED [ 92%]
[2025-11-26T13:21:06.650+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_is_valid_email_invalid_formats[wrong@.com] PASSED [ 96%]
[2025-11-26T13:21:06.650+0000] {subprocess.py:93} INFO - tests/test_utils.py::test_is_valid_email_invalid_formats[@missinguser.com] PASSED [100%]
[2025-11-26T13:21:06.651+0000] {subprocess.py:93} INFO - 
[2025-11-26T13:21:06.651+0000] {subprocess.py:93} INFO - ============================== 27 passed in 0.13s ==============================
```



# Authors
Created for the Software Engineering course project (Fall 2025) by:

- Semenikhine Michel
- Burroni Blu
- Essifi Rayan