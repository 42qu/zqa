#coding:utf-8

from _handler import Handler
from _urlmap import urlmap
from model.foo import getmsgs
from model.foo import getreply
from model.foo import post_msg

@urlmap('/')
class Index(Handler):
    def get(self):
        msg_lst = []
        ret = getmsgs()
        if ret:
            for i in ret:
                m = dict()
                m['id'] = i['id']
                m['who'] = i['who']
                m['text'] = i['t'].encode('utf-8')
                if i['answer_id']:
                    re = getreply(i['answer_id'])
                    m['answer'] = {
                        'text': re['t'].encode('utf-8').replace(r'\n','<br />'),
                        'who' : re['who'].encode('utf-8')
                    }
                else:
                    m['answer'] = {'text':'尚未产生','who':None}

                msg_lst.append(m)
        self.render(msg_lst=msg_lst)
    def post(self):
        who = self.get_argument('who','匿名')
        t = self.get_argument('text','')
        if t:
            post_msg(who,t)
        self.redirect('/')

