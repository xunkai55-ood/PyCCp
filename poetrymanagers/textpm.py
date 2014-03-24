# Text Poetry Manager

import os
from ..record import load_from_file

class TextPM(object):
    'Text Based Poetry Manager.'

    def __init__(self, prefix):
        if not os.path.isdir(prefix):
            raise Exception, "Your prefix is not valid."
        self._prefix = prefix

    def get_all(self, all_version = False):
        file_names = os.listdir(self._prefix)
        rst = []
        for each in file_names:
            #rst.append(load_from_file(each.decode("utf-8")))
            try:
                rst.append(load_from_file(os.path.join(self._prefix, each)))
            except:
                raise Exception, "Cannot load text file" + each
        return rst


