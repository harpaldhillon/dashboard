#!/usr/bin/env python

import yaml
import subprocess
from tabulate import tabulate
print("Inside python script")

charts = "kafka"
table = []

headers = ["Environment","Component","Kind","Replicas", "Container Name", "CPU (Request)", "Memory (Request)", "CPU (Limit)", "Memory (Limit)"]


for i in ["bld"]:
    dir_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i

    cmd = "find "+dir_path+" -type f -name '*yaml' -exec grep -H 'Deployment\|StatefulSet' {} \;|awk -F: '{print $1}'"

    print(cmd)

    out = subprocess.check_output(cmd, shell=True, universal_newlines=True)

    file_list = out.split()

    print(file_list)

    for f in file_list:
      yaml_file = open(f).read()
      yaml_dict=yaml.load(yaml_file, yaml.SafeLoader) 
      spec = yaml_dict['spec']
      container_spec=spec['template']['spec']['containers']

      for x in container_spec:
        obj = []
        name = x['name']
        resources = x['resources']

        obj.append(i.upper())
        obj.append("Kafka")
        obj.append(yaml_dict['kind'])    
        obj.append(spec['replicas'])
        obj.append(name)

        obj.append(resources['requests']['cpu'])
        obj.append(resources['requests']['memory'])
        obj.append(resources['limits']['cpu'])
        obj.append(resources['limits']['memory'])

        table.append(obj)

for i in ["int"]:
    dir_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i

    cmd = "find "+dir_path+" -type f -name '*yaml' -exec grep -H 'Deployment\|StatefulSet' {} \;|awk -F: '{print $1}'"

    print(cmd)

    out = subprocess.check_output(cmd, shell=True, universal_newlines=True)

    file_list = out.split()

    print(file_list)

    for f in file_list:
      yaml_file = open(f).read()
      yaml_dict=yaml.load(yaml_file, yaml.SafeLoader) 
      spec = yaml_dict['spec']
      container_spec=spec['template']['spec']['containers']

      for x in container_spec:
        obj = []
        name = x['name']
        resources = x['resources']

        obj.append(i.upper())
        obj.append("Kafka")
        obj.append(yaml_dict['kind'])    
        obj.append(spec['replicas'])
        obj.append(name)

        obj.append(resources['requests']['cpu'])
        obj.append(resources['requests']['memory'])
        obj.append(resources['limits']['cpu'])
        obj.append(resources['limits']['memory'])

        table.append(obj)

for i in ["prd"]:
    dir_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i

    cmd = "find "+dir_path+" -type f -name '*yaml' -exec grep -H 'Deployment\|StatefulSet' {} \;|awk -F: '{print $1}'"

    print(cmd)

    out = subprocess.check_output(cmd, shell=True, universal_newlines=True)

    file_list = out.split()

    print(file_list)

    for f in file_list:
      yaml_file = open(f).read()
      yaml_dict=yaml.load(yaml_file, yaml.SafeLoader) 
      spec = yaml_dict['spec']
      container_spec=spec['template']['spec']['containers']

      for x in container_spec:
        obj = []
        name = x['name']
        resources = x['resources']

        obj.append(i.upper())
        obj.append("Kafka")
        obj.append(yaml_dict['kind'])    
        obj.append(spec['replicas'])
        obj.append(name)

        obj.append(resources['requests']['cpu'])
        obj.append(resources['requests']['memory'])
        obj.append(resources['limits']['cpu'])
        obj.append(resources['limits']['memory'])

        table.append(obj)

# for i in ["prd"]:
#     file_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i+"/kafka/templates/deployment.yaml"

#     yaml_file = open(file_path).read()
#     yaml_dict=yaml.load(yaml_file, yaml.SafeLoader)

#     spec = yaml_dict['spec']
#     container_spec=spec['template']['spec']['containers']

#     for x in container_spec:
#         obj_prd = []
#         name = x['name']
#         resources = x['resources']

#         obj_prd.append(i.upper())
#         obj_prd.append("Kafka")
#         obj_prd.append(yaml_dict['kind'])    
#         obj_prd.append(spec['replicas'])
#         obj_prd.append(name)

#         obj_prd.append(resources['requests']['cpu'])
#         obj_prd.append(resources['requests']['memory'])
#         obj_prd.append(resources['limits']['cpu'])
#         obj_prd.append(resources['limits']['memory'])

#         table.append(obj_prd)


print("************************************")
print("************************************")
print("************************************")
print(tabulate(table, headers, tablefmt="fancy_grid"))
print("************************************")
print("************************************")
print("************************************")
