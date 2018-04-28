import requests
import urllib.parse

class getsmscode:
    def req(self, args, endpoint):
        if not endpoint in [1, 2]:
            raise Exception('Endpoint must be 1 or 2.')
        if endpoint == 1:
            return requests.get(self.endpoint1 + urllib.parse.urlencode(args)).text
        elif endpoint == 2:
            return requests.get(self.endpoint2 + urllib.parse.urlencode(args)).text
    
    def __init__(self, username, token):
        self.endpoint1 = 'http://www.getsmscode.com/do.php?'
        self.endpoint2 = 'http://www.getsmscode.com/vndo.php?'
        res = self.req({'action': 'login', 'username': username, 'token': token}, 1)
        if res == 'username is wrong':
            raise Exception(res)
        elif res == 'token is wrong':
            raise Exception(res)
        else:
            self.username = username
            self.token = token
            return None
    
    def get_balance(self):
        res = self.req({'action': 'login', 'username': self.username, 'token': self.token}, 1)
        aargs = res.split('|')
        if not aargs[1]:
            raise Exception(res)
        return aargs[1]
    
    def get_number(self, pid, cocode):
        if cocode == 'cn':
            res = self.req({'action': 'getmobile', 'username': self.username, 'token': self.token, 'pid': pid}, 1)
        else:
            res = self.req({'action': 'getmobile', 'username': self.username, 'token': self.token, 'pid': pid, 'cocode': cocode}, 2)
        if res.isdigit():
            return res
        raise Exception(res)
    
    def get_sms(self, number, pid, cocode):
        if cocode == 'cn':
            res = self.req({'action': 'getsms', 'username': self.username, 'token': self.token, 'pid': pid, 'mobile': number, 'author': self.username}, 1)
        else:
            res = self.req({'action': 'getsms', 'username': self.username, 'token': self.token, 'pid': pid, 'mobile': number, 'cocode': cocode}, 2)
        if res.startswith('1|'):
            return res.replace('1|', '')
        return False
    
    def add_blacklist(self, number, pid, cocode):
        if cocode == 'cn':
            res = self.req({'action': 'addblack', 'username': self.username, 'token': self.token, 'pid': pid, 'mobile': number}, 1)
        else:
            res = self.req({'action': 'addblack', 'username': self.username, 'token': self.token, 'pid': pid, 'mobile': number, 'cocode': cocode}, 2)
        if res == 'Message|Had add black list':
            return True
        return False
