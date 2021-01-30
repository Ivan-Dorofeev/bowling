# -*- coding: utf-8 -*-

import argparse
from bowling import get_score

parser = argparse.ArgumentParser(description='Get Bowling Score')
parser.add_argument('result', type=str, help='Input frames to get scores')
args = parser.parse_args()
get_score(get_string=args.result)
