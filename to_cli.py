#!/usr/bin/env python3
import yaml
from yaml import Loader
import argparse




def to_dict(keys, value, res):
    if (len(keys) == 0):
        return
    if (len(keys) == 1):
        res[keys[0]] = value
    else:
        if keys[0] not in res:
            res.update({keys[0]: {}})
        to_dict(keys[1:], value, res[keys[0]])


def to_cli(input_dict, prefix):
    res = []
    for k, v in input_dict.items():

        new_prefix = ".".join([prefix, k]) if prefix != "--" else "--" + k
        if type(v) == dict:
            res = res + to_cli(v, new_prefix)
        elif type(v) == list:
            for i in v:
                res.append(f"{new_prefix}={i}")
        else:
            res.append(f"{new_prefix}={v}")
    return res



parser = argparse.ArgumentParser(description='Handle Dextorm Configuration')
parser.add_argument('dextorm_conf_file', help="dextorm configuration file")
args = parser.parse_args()


with open(args.dextorm_conf_file) as f:
    data = yaml.load(f, Loader=Loader)
print(" ".join(to_cli(data, "--")))
