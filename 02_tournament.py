0# -*- coding: utf-8 -*-

# Если нужно из текущего файла сделать консольный скрипт для формирования файла с результатами турнира:
# (Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>)


import argparse
from Score_Tournament import score_tournament, score_tournament_europe

parser = argparse.ArgumentParser(description='Get Bowling Score File')
parser.add_argument('input', type=str, help='Input file to get scores')
parser.add_argument('output', type=str, help='Output file to get scores')
args = parser.parse_args()
score_tournament(in_file=args.input, out_file=args.output)
