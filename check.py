#!/usr/bin/env python

import yaml
from tabulate import tabulate
print("Inside python script")

charts = "kafka"

headers = ["cpu","memory"]

for i in ["bld","int","prd"]:
    file_path="$WORKSPACE/out-dir-${i}/kafka/templates/deployment.yaml"


    yaml_file = open(file_path).read()
    yaml_dict=yaml.load(yaml_file, yaml.SafeLoader)

    spec = yaml_dict['spec']

    print(spec)