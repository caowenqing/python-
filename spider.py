import ssl
from html.parser import HTMLParser
from urllib import request

ssl._create_default_https_context = ssl._create_unverified_context

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self._title = [False]
        self._time =[False]
        self._place = [False]
        self.time = ''   # 用于拼接时间

    def _attr(self, attrlist, attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        #print('<%s>' % tag)
        if tag == 'h3' and self._attr(attrs, 'class') == 'event-title':
            self._title[0] = True
        if tag == 'time':
            self._time[0] = True
        if tag == 'span' and self._attr(attrs, 'class') == 'event-location':
            self._place[0] = True

    def handle_endtag(self, tag):
        # </time> 结束拼接
        if tag == 'time':
            self._time.append(self.time)  # 将time完整内容放入self._time
            self.time = ''                # 初始化 self.time
            self._time[0] = False

    def handle_startendtag(self, tag, attrs):
        #print('<%s/>' % tag)
        pass

    def handle_data(self, data):
        #print('data: %s' % data)
        if self._title[0] == True:
            self._title.append(data)
            self._title[0] = False
        if self._time[0] == True:
            self.time += data             # 拼接time
        if self._place[0] == True:
            self._place.append(data)
            self._place[0] = False

    def handle_comment(self, comment):
        #print('<!-- %s -->' % comment)
        pass

    def handle_entityref(self, name):
        if self._time[0] == True:
            self.time += '-'               # &ndash -> '-'

    def handle_charref(self, name):
        #print('&#%s:' % name)
        pass

    def show_content(self):
        for n in range(1, len(self._title)):
            print('会议主题: %s' % self._title[n])
            print('时间:  %s' % self._time[n])
            print('地点: %s' % self._place[n])
            print('--------------------------------------')

html = ''
try:
    page = request.urlopen('https://www.python.org/events/python-events/')  # 打开网页
    html = page.read()  # 读取网页内容
finally:
    page.close()

parser = MyHTMLParser()
parser.feed(html.decode('utf-8'))
parser.show_content()
