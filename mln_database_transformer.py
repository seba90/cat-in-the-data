import pandas as pd
from predicates import *


df = pd.read_csv('data/train.csv')
df = df.drop('id', 1)


databases_as_str = '\n---\n'.join(['\n'.join([
    BIN_0.format(x.values[0]).replace(" ", ""),\
BIN_1.format(x.values[1]).replace(" ", ""),\
BIN_2.format(x.values[2]).replace(" ", ""),\
BIN_3.format(x.values[3]).replace(" ", ""),\
BIN_4.format(x.values[4]).replace(" ", ""),\
NOM_0.format(x.values[5]).replace(" ", ""),\
NOM_1.format(x.values[6]).replace(" ", ""),\
NOM_2.format(x.values[7]).replace(" ", ""),\
NOM_3.format(x.values[8]).replace(" ", ""),\
NOM_4.format(x.values[9]).replace(" ", ""),\
NOM_5.format(x.values[10]).replace(" ", ""),\
NOM_6.format(x.values[11]).replace(" ", ""),\
NOM_7.format(x.values[12]).replace(" ", ""),\
NOM_8.format(x.values[13]).replace(" ", ""),\
NOM_9.format(x.values[14]).replace(" ", ""),\
ORD_0.format(x.values[15]).replace(" ", ""),\
ORD_1.format(x.values[16]).replace(" ", ""),\
ORD_2.format(x.values[17]).replace(" ", ""),\
ORD_3.format(x.values[18]).replace(" ", ""),\
ORD_4.format(x.values[19]).replace(" ", ""),\
ORD_5.format(x.values[20]).replace(" ", ""),\
DAY.format(x.values[21]).replace(" ", ""),\
MONTH.format(x.values[22]).replace(" ", ""),\
TARGET.format(x.values[23])]).replace(" ", "") for _,x in df.iterrows()])

f = open("cat-in-the-data.db", "w")
f.write(databases_as_str)
f.close()
