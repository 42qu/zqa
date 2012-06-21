# coding:utf-8

def css(f):
    return '<link href="/static/css/%s"' % f + \
        ' rel="stylesheet" type="text/css">'

def js(f):
    return '<script src="/static/js/%s.js"></script>' %f

def jquery():
    return '<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>'

