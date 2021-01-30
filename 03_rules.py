# -*- coding: utf-8 -*-

# Правила подсчета очков изменяются так:
#
# Если во фрейме страйк, сумма очков за этот фрейм будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за два следующих броска (в одном или двух фреймах,
# в зависимости от того, был ли страйк в следующем броске).
# Если во фрейме сбит спэр, то сумма очков будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за первый бросок в следующем фрейме.
# Если фрейм остался открытым, то сумма очков будет равна количеству сбитых кеглей в этом фрейме.
# Страйк и спэр в последнем фрейме - по 10 очков.
#
# То есть для игры «Х4/34» сумма очков равна 10+10 + 10+3 + 3+4 = 40,
# а для игры «ХXX347/21» - 10+20 + 10+13 + 10+7 + 3+4 + 10+2 + 3 = 92

import argparse
from Score_Tournament import score_tournament_europe

parser = argparse.ArgumentParser(description='Get Bowling Score File')
parser.add_argument('input', type=str, help='Input file to get scores')
parser.add_argument('output', type=str, help='Output file to get scores')
args = parser.parse_args()
score_tournament_europe(in_file=args.input, out_file=args.output)


# python -m 03_rules tournament.txt t_res.txt
