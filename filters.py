from .record import Record
from .cipai import is_similar
from .cipai import is_equal

class PoetryFilter(object):

    def __init__(self):
        pass

    def filter(self):
        pass

class SubjectPF(PoetryFilter):

    def __init__(self, key):
        self._key = key

    def __unicode__(self):
        return u"It's a subject poetry filter\n    Keyword: " + self._key

    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def filter(self, ups):
        downs = []
        for rec in ups:
            if rec.subject.find(self._key) >= 0:
                downs.append(rec)
        return downs

class PaiSimilarityPF(PoetryFilter):

    def __init__(self, std):
        self._std = []
        for a in std:
            for b in self._std:
                if is_equal(a, b):
                    break
            else:
                self._std.append(a)

    def __unicode__(self):
        u = u"It's a Pai similarity poetry filter\n Standards:"
        for each in self._std:
            u += each.__unicode__() + u"\n"
        return u

    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def filter(self, ups):
        downs = []
        for rec in ups:
            print rec.subject
            for std in self._std:
                if is_similar(rec, std):
                    downs.append(rec)
                    break
        return downs

