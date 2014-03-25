# -*- coding: utf-8 -*-

from consts import REF_PATH
import json
import os.path
import codecs

class YunDict(object):

    def __init__(self):
        f = codecs.open(os.path.join(REF_PATH, "ci_lin_zheng_yun"), "r", "utf-8")
        self.dic = json.load(f)

    def __getitem__(self, x):
        if self.dic.has_key(x) == 0:
            return None
        return self.dic[x]

    def gets(self, x):
        lst = self.dic[x]
        s = u""
        if lst:
            for d in lst:
                if len(s):
                    s += u"\n"
                s += u"第" + str(d["bu"]).decode("utf-8") + u"部: " + d["sheng"] + u"声"
            return s
        else:
            return u"None"
