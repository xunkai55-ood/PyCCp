from .record import Record

class Ci(Record):

    def __init__(self, sub, a_info, content, version = '', cipai = ''):
        super(Ci, self).__init__(sub, a_info, content, version)
        self.cipai = cipai
        if self.cipai == '':
            # To Be Done
            pass

    def save(self, ci_manager):
        return ci_manager.save(self)

