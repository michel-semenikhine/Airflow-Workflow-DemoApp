from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

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
    schedule_interval=None,
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

    # Step 2.5 : Analyze the project structure and metrics
    project_analysis = BashOperator(
        task_id="project_analysis",
        bash_command="""
        echo "===== Project Analysis ====="
        echo "Project size:"
        du -sh /tmp/Airflow-Workflow-DemoApp

        echo "Number of Python files:"
        find /tmp/Airflow-Workflow-DemoApp -name "*.py" | wc -l

        echo "Number of test files:"
        find /tmp/Airflow-Workflow-DemoApp -path "*tests*" -name "*.py" | wc -l
        """,
    )

    # Step 3 : Run pytest and log results
    run_tests = BashOperator(
        task_id="run_pytest",
        bash_command=(
            "cd /tmp/Airflow-Workflow-DemoApp && pytest -v > /tmp/test_results.log || true && "
            "cat /tmp/test_results.log"
        ),
    )

    # Step 3.5 : Summarize pipeline results
    def pipeline_summary():
        import os
        project_path = "/tmp/Airflow-Workflow-DemoApp"
        test_log = "/tmp/test_results.log"

        print("===== PIPELINE SUMMARY =====")
        if os.path.exists(project_path):
            print(f"Project directory exists: {project_path}")
        else:
            print("Project directory not found")

        if os.path.exists(test_log):
            print("Test results file found")
            with open(test_log, "r") as f:
                lines = f.readlines()

            print("Last test execution lines:")
            for line in lines[-5:]:
                print(line.strip())
            passed_tests = sum(1 for line in lines if "PASSED" in line)
            print(f"Total passed tests: {passed_tests}")
        else:
            print("No test results file found")
        print("Pipeline summary completed.")

    pipeline_summary = PythonOperator(
        task_id="pipeline_summary",
        python_callable=pipeline_summary
    )

    # Step 4 : Cleanup temporary files
    cleanup_temp = BashOperator(
        task_id="cleanup_temp",
        bash_command="rm -rf /tmp/Airflow-Workflow-DemoApp",
    )

    # Task dependencies
    clone_repo >> install_deps >> project_analysis >> run_tests >> pipeline_summary >> cleanup_temp
