#!/usr/bin/env python

import yaml
import subprocess
from tabulate import tabulate
print("Inside python script")

charts = "kafka"
table = []
table_volume = []

headers = ["Environment","Component","Kind","Replicas", "Container Name", "CPU (Request)", "Memory (Request)", "CPU (Limit)", "Memory (Limit)"]

headers_volumes = ["Environment","Component","Kind","Replicas", "Volume Name", "Access Mode", "Storage"]


for i in ["bld"]:
    dir_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i

    #cmd = "find "+dir_path+" -type f -name '*yaml' -exec grep -H 'Deployment\|StatefulSet' {} \;|awk -F: '{print $1}'"

    cmd = "find "+dir_path+" -type f -name '*yaml' -exec grep -H 'StatefulSet' {} \;|awk -F: '{print $1}'"


    print(cmd)

    out = subprocess.check_output(cmd, shell=True, universal_newlines=True)

    file_list = out.split()

    print(file_list)

    for f in file_list:
      print("Processing file:")
      print(f)
      yaml_file = open(f).read()
      yaml_dict=yaml.load(yaml_file, yaml.SafeLoader) 
      spec = yaml_dict['spec']
      container_spec=spec['template']['spec']['containers']

      volume_templates=spec['volumeClaimTemplates']

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

      for v in volume_templates:
        obj = []
        #name = v['name']
        spec_volume = v['spec']

        obj.append(i.upper())
        obj.append(yaml_dict['metadata']['name'])
        obj.append(yaml_dict['kind'])    
        obj.append(spec['replicas'])
        obj.append(v['metadata']['name'])

        obj.append(spec_volume['accessModes'])
        obj.append(spec_volume['resources']['requests']['storage'])
        #obj.append(spec_volume['resources']['requests']['memory'])

        table_volume.append(obj)
    

for i in ["int"]:
    dir_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i

    cmd = "find "+dir_path+" -type f -name '*yaml' -exec grep -H 'Deployment\|StatefulSet' {} \;|awk -F: '{print $1}'"

    print(cmd)

    out = subprocess.check_output(cmd, shell=True, universal_newlines=True)

    file_list = out.split()

    print(file_list)

    for f in file_list:
      print("Processing file:")
      print(f)
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
      print("Processing file:")
      print(f)
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

print("************************************")
print("************************************")
print("************************************")
#print(tabulate(table, headers, tablefmt="fancy_grid"))
print("************************************")
print("************************************")
print("************************************")



print(tabulate(table_volume, headers_volumes, tablefmt="fancy_grid"))