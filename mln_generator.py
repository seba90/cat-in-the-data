from shutil import copyfile
from itertools import combinations
from predicates import *

import itertools
TEMPLATE_NAME = 'cat-in-the-data-template.mln'

copyfile('cat-in-the-data-stump.mln', TEMPLATE_NAME)

PREDICATE_LIST = [BIN_0,
                  BIN_1,
                  BIN_2,
                  BIN_3,
                  BIN_4,
                  NOM_9,
                  NOM_8,
                  NOM_7,
                  NOM_6,
                  NOM_5,
                  NOM_4,
                  NOM_3,
                  NOM_2,
                  NOM_1,
                  NOM_0,
                  ORD_5,
                  ORD_4,
                  ORD_3,
                  ORD_2,
                  ORD_1,
                  ORD_0,
                  DAY,
                  MONTH]


combis = list(combinations(PREDICATE_LIST, 2))
formulas = ['0 {} ^ target(+?x3)\n'.format(' ^ '.join(combi).format('+?x1', '+?x2')) for combi in combis]

with open(TEMPLATE_NAME, "a") as template_file:
    for formula in formulas:
        template_file.write(formula)





