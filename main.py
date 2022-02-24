import os
import cv2
import re
import yaml
import argparse
import utils.os_module as om
from pprint import pprint


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Templete Project")
    parser.add_argument('--config', '-c', type=str, default="./config.yaml", help="yaml file path")
    args = parser.parse_args()
    print(f"config path : {args.config}")
    
    with open(args.config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    
    for key_, val_ in config.items():
        print("{} : {} | type : {}".format(key_, val_, re.sub("\'>","", re.sub("<class \'", "", str(type(val_))))))
