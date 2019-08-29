import re

class SiaData:

    def get_jsessionid(login_ans):
        match = re.search('[0-9|A-Z]*.web', str(login_ans))
        if match is None:
            return ''
        else:
            return login_ans[match.start() : match.end()-4]