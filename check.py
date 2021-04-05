#!/usr/bin/env python

import yaml
from tabulate import tabulate
print("Inside python script")

charts = "kafka"

headers = ["cpu","memory"]

for i in ["bld","int","prd"]:
    file_path="/home/jenkins/agent/workspace/dashboard/out-dir-"+i+"/kafka/templates/deployment.yaml"

    yaml_file = open(file_path).read()
    yaml_dict=yaml.load(yaml_file, yaml.SafeLoader)

    spec = yaml_dict['spec']

    #print(spec)

    container_spec=spec['template']['spec']['containers']

    for x in container_spec:
        resources = x['resources']
        print("************************************")
        print(i.upper(), "CPU", resources['requests']['cpu'])
        print(i.upper(), "Memory", resources['requests']['memory'])

        print(tabulate(resources['requests'], headers, tablefmt="grid"))
