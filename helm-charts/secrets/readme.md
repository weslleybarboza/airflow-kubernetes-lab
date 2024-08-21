# Convert to base64

``` sh
echo -n 'username' | base64
```


# Apply secret manifest

``` sh
kubectl apply -f secret.yaml
```

# Checking secret
``` sh
kubectl get secrets
kubectl describe secret <my-secret>
```
