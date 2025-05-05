# Creates a new release object :
* helm install **A release name**   **the name of the chart**


# if you edit any thing :
* helm upgrade **A release name**   **the name of the chart**


# Get the application URL by running this commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services a1-qq-chrt)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT


  
# You can access to the service using ip and port that generate from command above 



