#!/bin/bash

POD_NAME=$1

POD_ID=$(kubectl get po | awk '{print $1}' | grep -v NAME | grep -v Terminating | grep ${POD_NAME})

kubectl exec -it ${POD_ID} -- python3 -u main.py