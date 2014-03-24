# -*- coding: utf-8 -*-

import codecs
import json

class Record(object):

    def __init__(self, subject, a_info, content, version = ""):
        
        # basic info
        self.subject = subject
        self.a_info = a_info
        self.content = content
        self.version = version

    def __unicode__(self):
        return self.content + u"——《" + self.subject + u"》[" + self.a_info["dynasty"] + u"]" + self.a_info["author"]

    def __str__(self):
        return unicode(self).encode('utf-8')

def load_from_dict(d):
    if not d.has_key("version"):
        d["version"] = ""
    return Record(d["subject"], d["a_info"], d["content"], d["version"])

def load_from_file(f_name):

    f = codecs.open(f_name, "r", "utf-8")
    s = f.read()
    f.close()
    return load_from_dict(json.loads(s))
