#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd

json_open = open("sum_6to12.json", 'r')
base = pd.read_json(json_open)

base = base[base['count']>20]

base.to_json("sum.json",force_ascii=False,orient="records")