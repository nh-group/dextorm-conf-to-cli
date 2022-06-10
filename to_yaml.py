#!/usr/bin/env python3
import yaml
from yaml import Loader
import argparse
import sys
def to_dict(keys, value, res):
    if (len(keys) == 0):
        return
    if (len(keys) == 1):
        res[keys[0]] = value
    else:
        if keys[0] not in res:
            res.update({keys[0]: {}})
        to_dict(keys[1:], value, res[keys[0]])

param_list = [arg[2:] for arg in sys.argv]

res = {}
for param in param_list:
    param = param.strip()
    splitted_params = param.split("=")
    if (len(splitted_params) <= 1):
        continue
    splitted_keys = splitted_params[0].split(".")
    to_dict(splitted_keys, splitted_params[1], res)

print(yaml.safe_dump(res))
