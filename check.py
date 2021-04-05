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

    #print(dir_path)

    print(f"{dir_path}")

    out = subprocess.check_output(f"find {dir_path} -type f -name '*yaml' -exec grep -H 'Deployment\|StatefulSet' {} \;|awk -F: '{print $1}'", shell=True, universal_newlines=True)

    file_list = out.split()

    print(file_list)

    for f in file_list:
      yaml_file = open(f).read()
      yaml_dict=yaml.load(yaml_file, yaml.SafeLoader) 
      spec = yaml_dict['spec']
      container_spec=spec['template']['spec']['containers']

      for x in container_spec:
        obj_bld = []
        name = x['name']
        resources = x['resources']

        obj_bld.append(i.upper())
        obj_bld.append("Kafka")
        obj_bld.append(yaml_dict['kind'])    
        obj_bld.append(spec['replicas'])
        obj_bld.append(name)

        obj_bld.append(resources['requests']['cpu'])
        obj_bld.append(resources['requests']['memory'])
        obj_bld.append(resources['limits']['cpu'])
        obj_bld.append(resources['limits']['memory'])

        table.append(obj_bld)

# for i in ["int"]:
#     file_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i+"/kafka/templates/deployment.yaml"

#     yaml_file = open(file_path).read()
#     yaml_dict=yaml.load(yaml_file, yaml.SafeLoader)
#     spec = yaml_dict['spec']
#     container_spec=spec['template']['spec']['containers']

#     for x in container_spec:
#         obj_int = []
#         name = x['name']
#         resources = x['resources']
       
#         obj_int.append(i.upper())
#         obj_int.append("Kafka")
#         obj_int.append(yaml_dict['kind'])    
#         obj_int.append(spec['replicas'])
#         obj_int.append(name)

#         obj_int.append(resources['requests']['cpu'])
#         obj_int.append(resources['requests']['memory'])
#         obj_int.append(resources['limits']['cpu'])
#         obj_int.append(resources['limits']['memory'])

#         table.append(obj_int)

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
