# Install packages using chocolatey
```sh
choco install kubernetes-helm
choco install kubectl
choco install kubens
```

# Docker kubernetes - check nodes
```sh
kubectl config get-contexts
kubectl get nodes
```

# Pulling the helm chart
```sh
helm repo add apache-airflow https://airflow.apache.org/
helm install my-airflow apache-airflow/airflow --version 1.15.0
helm repo list
```

# Creating and using a namespace
```sh
kubectl create namespace airflow

# list namespaces
kubens 
# activate namespaces
kubens airflow
```

# Install helm

## Using the standard helm chart
https://artifacthub.io/packages/helm/apache-airflow/airflow

```sh
helm install airflow293 -n airflow apache-airflow/airflow --version 1.15.0

# if the namespace is not created
helm install airflow293 -n airflow apache-airflow/airflow --version 1.15.0 --create-namespace

# check pods
kubectl get pods

```
## using custom helm chart

```sh
helm install airflow293 -n airflow helm-charts\airflow
```



## outcome example
```sh
NAME: airflow293
LAST DEPLOYED: Fri Aug  9 12:44:08 2024
NAMESPACE: airflow
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Thank you for installing Apache Airflow 2.9.3!

Your release is named airflow293.
You can now access your dashboard(s) by executing the following command(s) and visiting the corresponding port at localhost in your browser:

Airflow Webserver:     kubectl port-forward svc/airflow293-webserver 8080:8080 --namespace airflow
Default Webserver (Airflow UI) Login credentials:
    username: admin
    password: admin
Default Postgres connection credentials:
    username: postgres
    password: postgres
    port: 5432

You can get Fernet Key value by running the following:

    echo Fernet Key: $(kubectl get secret --namespace airflow airflow293-fernet-key -o jsonpath="{.data.fernet-key}" | base64 --decode)

###########################################################
#  WARNING: You should set a static webserver secret key  #
###########################################################

You are using a dynamically generated webserver secret key, which can lead to
unnecessary restarts of your Airflow components.

Information on how to set a static webserver secret key can be found here:
https://airflow.apache.org/docs/helm-chart/stable/production-guide.html#webserver-secret-key
```

# Fowarding port
```sh
kubectl port-forward svc/airflow293-webserver 8081:8080
```
Open the browser: http://localhost:8081/home
user/password: admin/admin


# Removing all pods
```sh
helm uninstall airflow293 -n airflow apache-airflow/airflow
```

# Quality check

## Code - using SQL FLUFF
https://www.getdbt.com/coalesce-2020/presenting-sqlfluff

[![tasks](assets\images\sqlfluff.jpg )](https://odsc.com/blog/building-a-robust-data-pipeline-with-the-dag-stack-dbt-airflow-and-great-expectations/)

Allow us:
- define the standard of the codes in terms of space, identation, good practices
- we can define the rules and track the changes
- can automaticaly format the code following the rules defined
- for new employees, it helps to keep the standard

CI/CD:
- it can validate if the code follow the rules while building the image as a quality check.

## Data

https://zoltanctoth.medium.com/boost-your-dbt-tests-using-great-expectations-in-dbt-1c2d33d53fb3

https://www.getdbt.com/coalesce-2020/building-a-robust-data-pipeline-with-dbt-airflow-and-great-expectations

We have some libraries like:
- dbt test
- dbt expectation
- great expectation

Data needs to be tested.

[![tasks](assets\images\test_flow.png )]

### Dbt test
- used for simple tests
- we can build custom tests

### Dbt expectation

- into the box
- we can set while we develop the project

[![tasks](assets\images\dbt_expectation.png )]

### Dbt Great expectation

[![tasks](assets\images\great_expectations.png )]
- it is library whith many tests
- kl diverged test
- distribuition test
- statistics tests
- can provide documentation/report of the data quality


# Deployment

## Airflow
https://medium.com/@dennis-sin/dbt-in-production-airflow-with-kubernetes-36db10d2a8f1
https://medium.com/bluecore-engineering/were-all-using-airflow-wrong-and-how-to-fix-it-a56f14cb0753

## Dbt
https://medium.com/@dennis-sin/amazing-tool-when-developing-dbt-in-container-82405376b89d


## Options

### 1. Use the workers pod to process the data
We can use the library Cosmos to create the dag and tasks.

[![astronomer-cosmos](assets\images\cosmos_jaffle_shop_dag.png )](https://www.astronomer.io/docs/learn/airflow-dbt)

Pros:
- Easy to deploy
- It will manage the sequence of each task and its dependence

Cons:
- The Airflow Python libraries versions can conflict with DBT libraries as we go along
- Both projects (Dags and DBT) will be almost 100% attached as they share the same libraries
- We can have issues if we decided to upgrade the versiont of one application, or it can block us to do upgrade.

Questions:
- Is possible the Cosmos library to launch a new pod as a task? If yes, we can enjoy it's orquestration and change the way that a task will be executed.

### 2. For each task or group of task, we can launch one pod

[![tasks](assets\images\airflow_dbt_tasks.png )](https://odsc.com/blog/building-a-robust-data-pipeline-with-the-dag-stack-dbt-airflow-and-great-expectations/)

Pros:
- We can use the pods to launch the jobs - avoiding packages conflicts
- Is possible to manage the whole pipeline by layer - Example: run ingestion + test.
- Combine DBT expectation with our pipeline testint each phase
- We have the domain of what will be executed

Cons:
- We need to build/code all dags and the orchestration managing the dependencies of the pipeline

Questions:
- .