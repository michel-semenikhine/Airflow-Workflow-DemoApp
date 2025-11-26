from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# ----------------------------
# DAG: GitHub Test Pipeline
# ----------------------------

# Default DAG config
default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="github_test_pipeline",
    default_args=default_args,
    description="Clone GitHub repo, install dependencies, and run pytest.",
    schedule_interval=None,  # exécution manuelle
    start_date=datetime(2025, 10, 17),
    catchup=False,
    tags=["github", "pytest", "demo"],
) as dag:

    # Step 1 : Clone the GitHub repository
    clone_repo = BashOperator(
        task_id="clone_repo",
        bash_command=(
            "rm -rf /tmp/Airflow-Workflow-DemoApp && "
            "git clone https://github.com/michel-semenikhine/Airflow-Workflow-DemoApp.git /tmp/Airflow-Workflow-DemoApp"
        ),
    )

    # Step 2 : Install dependencies from requirements.txt
    install_deps = BashOperator(
        task_id="install_dependencies",
        bash_command=(
            "pip install -r /tmp/Airflow-Workflow-DemoApp/requirements.txt || echo 'No requirements.txt found'"
        ),
    )

    # Step 3 : Run pytest and log results
    run_tests = BashOperator(
        task_id="run_pytest",
        bash_command=(
            "cd /tmp/Airflow-Workflow-DemoApp && pytest -v > /tmp/test_results.log || true && "
            "cat /tmp/test_results.log"
        ),
    )

    # Step 4 : Cleanup temporary files
    cleanup = BashOperator(
        task_id="cleanup_temp",
        bash_command="rm -rf /tmp/Airflow-Workflow-DemoApp",
    )

    # Task dependencies
    clone_repo >> install_deps >> run_tests >> cleanup
