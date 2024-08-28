from pendulum import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)

with DAG(
    dag_id="spining_dbt_pod",
    schedule="@once",
    start_date=datetime(2023, 3, 30),
) as dag:
    example_kpo = KubernetesPodOperator(
        kubernetes_conn_id="k8s_conn",
        image="weslleybarboza/dbt:v1.0",
        arguments=["build"]
        name="spining_dbt_pod",
        task_id="task-one",
        is_delete_operator_pod=True,
        get_logs=True,
    )

    example_kpo