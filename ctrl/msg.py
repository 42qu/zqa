# coding:utf-8

from _handler import Handler
from _urlmap import urlmap
from model.foo import getmsg
from model.foo import getreply
from model.foo import getreplys
from model.foo import post_reply
from model.foo import chooseanswer

@urlmap('/m/(\d+)')
class Msg(Handler):
    def get(self,id):
        r = getmsg(id)
        if not r:
            self.redirect('/')
        else:
            info = dict()
            info['id'] = r['id']
            info['who'] = r['who'].encode('utf-8')
            info['text'] = r['t'].encode('utf-8')
            if r['answer_id']:
                re = getreply(r['answer_id'])
                info['answer'] = {
                    'text': re['t'].encode('utf-8').replace(r'\n','<br />'),
                    'who' : re['who'].encode('utf-8')
                }
            else:
                info['answer'] = {'text':'尚未产生','who':None}
        self.render(info=info,re=getreplys(id))
    def post(self,id):
        answer = int(self.get_argument('answer',0))
        if answer:
            chooseanswer(id,answer)
            self.redirect('/m/%s'%id)
            return
        who = self.get_argument('who','匿名')
        t = self.get_argument('text','').replace('\n',r'\n')
        if t:
            post_reply(id,who,t)
        self.redirect('/m/%s'%id)

