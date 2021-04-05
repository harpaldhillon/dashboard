#!/usr/bin/env python

import yaml
from tabulate import tabulate
print("Inside python script")

charts = "kafka"

headers = ["Environment","Component","Kind","Replicas","CPU (Request)", "Memory (Request)", "CPU (Limit)", "Memory (Limit)"]

for i in ["bld","int","prd"]:
    file_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i+"/kafka/templates/deployment.yaml"

    yaml_file = open(file_path).read()
    yaml_dict=yaml.load(yaml_file, yaml.SafeLoader)

    spec = yaml_dict['spec']

    print(spec)

    container_spec=spec['template']['spec']['containers']

    for x in container_spec:
        resources = x['resources']
        print("************************************")
        print(i.upper(), "CPU", resources['requests']['cpu'])
        print(i.upper(), "Memory", resources['requests']['memory'])

table = []

table.append(["BLD","Kafka","Deployment","2","128m","100Mi","228m","500Mi"])
table.append(["INT","Kafka","Deployment","3","228m","200Mi","528m","500Mi"])
table.append(["PRD","Kafka","Deployment","6","1228m","1200Mi","1528m","1500Mi"])

print("************************************")
print("************************************")
print("************************************")
print(tabulate(table, headers, tablefmt="fancy_grid"))
print("************************************")
print("************************************")
print("************************************")