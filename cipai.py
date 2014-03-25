# -*- coding: utf-8 -*-
from __future__ import division

from consts import REF_PATH
import os
import codecs

breakings = list(u',.，。、')
brk_1 = list(u'.。')
brk_2 = list(u',，、')

def divide_by_breakings(rec):
    content = rec.content
    rst = []
    cnt = 0
    for c in content:
        if c == u' ' or c == u'\r' or c == u'\n':
            continue
        elif not c in breakings:
            cnt += 1
        else:
            if cnt > 0:
                if c in brk_1:
                    rst.append((cnt, 1))
                else:
                    rst.append((cnt, 2))
            cnt = 0
    if cnt > 0:
        rst.append((cnt, 1))
    return rst

def is_similar(rec_a, rec_b):
    '''
        Return true when structures of 2 poetry is similar.
        How we define similarity:
            1. Only a few breakings are different.
            2. Level 1 breakings are firstly considered.
                2.1 Lack of L2 breakings is okay.
                2.2 Length difference of 2 sentence contributes to total difference according to the level.
            3(Todo). Check Dan-diao and Shuang-diao usage.
    '''

    if abs(len(rec_a.content) - len(rec_b.content)) > 5:
        return False

    brk_a = divide_by_breakings(rec_a)
    brk_b = divide_by_breakings(rec_b)

    br_cost = [0, 2, 0]
    len_cost = 1

    # algo: dynamic programming
    f = [[100000 for i in range(len(brk_b) + 1)] for j in range(len(brk_a) + 1)]
    f[0][0] = 0
    # TODO: accelerate
    for i1 in range(len(brk_a) + 1):
        for j1 in range(len(brk_b) + 1):
            for i2 in range(i1):
                for j2 in range(j1):
                    cost = f[i2][j2]
                    len_a = 0
                    len_b = 0
                    for k in range(i2 + 1, i1):
                        cost += br_cost[brk_a[k - 1][1]]
                    for k in range(i2 + 1, i1 + 1):
                        len_a += brk_a[k - 1][0]
                    for k in range(j2 + 1, j1):
                        cost += br_cost[brk_b[k - 1][1]]
                    for k in range(i2 + 1, j1 + 1):
                        len_b += brk_b[k - 1][0]

                    tot = cost + abs(len_a - len_b) * len_cost
                    f[i1][j1] = min(f[i1][j1], tot)
    diff = f[len(brk_a)][len(brk_b)]
    if (diff < 3 or (diff ** 2 / (len(brk_a) * len(brk_b)) < 0.05)):
        return True
    else:
        return False

def is_equal(rec_a, rec_b):
    if abs(len(rec_a.content) - len(rec_b.content)) > 5:
        return False

    brk_a = divide_by_breakings(rec_a)
    brk_b = divide_by_breakings(rec_b)

    br_cost = [1, 1, 1]
    len_cost = 1

    # algo: dynamic programming
    f = [[100000 for i in range(len(brk_b) + 1)] for j in range(len(brk_a) + 1)]
    f[0][0] = 0
    # TODO: accelerate
    for i1 in range(len(brk_a) + 1):
        for j1 in range(len(brk_b) + 1):
            for i2 in range(i1):
                for j2 in range(j1):
                    cost = f[i2][j2]
                    len_a = 0
                    len_b = 0
                    for k in range(i2 + 1, i1):
                        cost += br_cost[brk_a[k - 1][1]]
                    for k in range(i2 + 1, i1 + 1):
                        len_a += brk_a[k - 1][0]
                    for k in range(j2 + 1, j1):
                        cost += br_cost[brk_b[k - 1][1]]
                    for k in range(i2 + 1, j1 + 1):
                        len_b += brk_b[k - 1][0]
                    
                    tot = cost + abs(len_a - len_b) * len_cost
                    f[i1][j1] = min(f[i1][j1], tot)
    if f[len(brk_a)][len(brk_b)] == 0:
        return True
    else:
        return False

class CipaiAlias(object):

    def __init__(self, pai):
        self._alias = set([pai])
        self._lier = set()
        f = codecs.open(os.path.join(REF_PATH, "cipai_alias.txt"), "r", "utf-8")
        lines = f.readlines()
        f.close()
        for line in lines:
            lst = [x.strip() for x in line.split(u"、")]
            if pai in lst:
                self._alias |= set(lst)
        for line in lines:
            lst = [x.strip() for x in line.split(u"、")]
            for name in lst:
                for alias in self._alias:
                    if name != alias and name.find(alias) == 0: # is prefix
                        self._lier |= set([name])
        print("===")
        for each in self._lier:
            print each
        print("===")

    def match(self, subject):
        
        for alias in self._alias:
            if subject.find(alias) == 0:
                for lier in self._lier:
                    if subject.find(lier) and lier.find(alias):
                        break
                else:
                    return alias
        else:
            return False
