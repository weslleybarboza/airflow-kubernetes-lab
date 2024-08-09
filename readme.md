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

# DBT
https://medium.com/@dennis-sin/dbt-in-production-airflow-with-kubernetes-36db10d2a8f1
https://medium.com/@dennis-sin/amazing-tool-when-developing-dbt-in-container-82405376b89d
