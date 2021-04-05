#!/usr/bin/env python

import yaml
from tabulate import tabulate
print("Inside python script")

charts = "kafka"

obj_int = []
obj_bld = []
obj_prd = []

headers = ["Environment","Component","Kind","Replicas","CPU (Request)", "Memory (Request)", "CPU (Limit)", "Memory (Limit)"]


for i in ["bld"]:
    file_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i+"/kafka/templates/deployment.yaml"

    yaml_file = open(file_path).read()
    yaml_dict=yaml.load(yaml_file, yaml.SafeLoader)

    print("****kind******")
    print(yaml_dict['kind'])
    
    
    
    obj_bld.append(i.upper())
    obj_bld.append("Kafka")
    obj_bld.append(yaml_dict['kind'])

    
    spec = yaml_dict['spec']

    #print(spec)

    print("****replicas******")
    print(spec['replicas'])

    obj_bld.append(spec['replicas'])

    container_spec=spec['template']['spec']['containers']

    for x in container_spec:
        resources = x['resources']
        print("************************************")
        print(i.upper(), "CPU", resources['requests']['cpu'])
        print(i.upper(), "Memory", resources['requests']['memory'])

        obj_bld.append(resources['requests']['cpu'])
        obj_bld.append(resources['requests']['memory'])
        obj_bld.append(resources['limits']['cpu'])
        obj_bld.append(resources['limits']['memory'])



for i in ["int"]:
    file_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i+"/kafka/templates/deployment.yaml"

    yaml_file = open(file_path).read()
    yaml_dict=yaml.load(yaml_file, yaml.SafeLoader)

    print("****kind******")
    print(yaml_dict['kind'])

    obj_int.append(i.upper())
    obj_int.append("Kafka")
    obj_int.append(yaml_dict['kind'])


    spec = yaml_dict['spec']

    #print(spec)

    print("****replicas******")
    print(spec['replicas'])

    obj_int.append(spec['replicas'])

    container_spec=spec['template']['spec']['containers']

    for x in container_spec:
        resources = x['resources']
        print("************************************")
        print(i.upper(), "CPU", resources['requests']['cpu'])
        print(i.upper(), "Memory", resources['requests']['memory'])

        obj_int.append(resources['requests']['cpu'])
        obj_int.append(resources['requests']['memory'])
        obj_int.append(resources['limits']['cpu'])
        obj_int.append(resources['limits']['memory'])

for i in ["prd"]:
    file_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i+"/kafka/templates/deployment.yaml"

    yaml_file = open(file_path).read()
    yaml_dict=yaml.load(yaml_file, yaml.SafeLoader)

    print("****kind******")
    print(yaml_dict['kind'])

    obj_prd.append(i.upper())
    obj_prd.append("Kafka")
    obj_prd.append(yaml_dict['kind'])


    spec = yaml_dict['spec']

    #print(spec)

    print("****replicas******")
    print(spec['replicas'])

    obj_prd.append(spec['replicas'])

    container_spec=spec['template']['spec']['containers']

    for x in container_spec:
        resources = x['resources']
        print("************************************")
        print(i.upper(), "CPU", resources['requests']['cpu'])
        print(i.upper(), "Memory", resources['requests']['memory'])

        obj_prd.append(resources['requests']['cpu'])
        obj_prd.append(resources['requests']['memory'])
        obj_prd.append(resources['limits']['cpu'])
        obj_prd.append(resources['limits']['memory'])

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


print("************************************")
print(obj_bld)
print("************************************")
print(obj_int)
print("************************************")
print(obj_prd)
print("************************************")

