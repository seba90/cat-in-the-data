import pandas as pd

BIN_0 = 'bin_0({})'
BIN_1 = 'bin_1({})'
BIN_2 = 'bin_2({})'
BIN_3 = 'bin_3({})'
BIN_4 = 'bin_4({})'
NOM_0 = 'nom_0({})'
NOM_1 = 'nom_1({})'
NOM_2 = 'nom_2({})'
NOM_3 = 'nom_3({})'
NOM_4 = 'nom_4({})'
NOM_5 = 'nom_5({})'
NOM_6 = 'nom_6({})'
NOM_7 = 'nom_7({})'
NOM_8 = 'nom_8({})'
NOM_9 = 'nom_9({})'
ORD_0 = 'ord_0({})'
ORD_1 = 'ord_1({})'
ORD_2 = 'ord_2({})'
ORD_3 = 'ord_3({})'
ORD_4 = 'ord_4({})'
ORD_5 = 'ord_5({})'
DAY = 'day({})'
MONTH = 'month({})'
TARGET = 'target({})'

df = pd.read_csv('data/train.csv')
df = df.drop('id', 1)


databases_as_str = '\n---\n'.join(['\n'.join([
    BIN_0.format(x.values[0]),\
BIN_1.format(x.values[1]),\
BIN_2.format(x.values[2]),\
BIN_3.format(x.values[3]),\
BIN_4.format(x.values[4]),\
NOM_0.format(x.values[5]),\
NOM_1.format(x.values[6]),\
NOM_2.format(x.values[7]),\
NOM_3.format(x.values[8]),\
NOM_4.format(x.values[9]),\
NOM_5.format(x.values[10]),\
NOM_6.format(x.values[11]),\
NOM_7.format(x.values[12]),\
NOM_8.format(x.values[13]),\
NOM_9.format(x.values[14]),\
ORD_0.format(x.values[15]),\
ORD_1.format(x.values[16]),\
ORD_2.format(x.values[17]),\
ORD_3.format(x.values[18]),\
ORD_4.format(x.values[19]),\
ORD_5.format(x.values[20]),\
DAY.format(x.values[21]),\
MONTH.format(x.values[22]),\
TARGET.format(x.values[23])]) for _,x in df.iterrows()])

f = open("cat-in-the-dat.db", "w")
f.write(databases_as_str)
f.close()
