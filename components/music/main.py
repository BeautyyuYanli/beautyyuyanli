import requests, json, datetime

def getBiliEntriesFromGithub():
    def getNewEntries():
        al = requests.get('https://raw.githubusercontent.com/BeautyYuYanli/music-down-bili/production/production/history.list').text
        al = al.split('\n')
        with open('./history.list') as f:
            be = f.read()
        be = be.split('\n')
        newEntries = []
        for i in al:
            if i not in be:
                newEntries.append(i)
        print(newEntries)
        return newEntries

    def getTitle(url):
        aid = url.split('av')[1]
        info = requests.get('https://api.bilibili.com/x/web-interface/view?aid={}'.format(aid)).json()
        print(info['data']['title'])
        return info['data']['title']

    with open('./output.json') as f:
        output = json.loads(f.read())

    newEntries = getNewEntries()
    for i in newEntries:
        al = {
            'url': i,
            'title': getTitle(i),
            'date': datetime.datetime.today().timestamp()
        }
        output.append(al)
    with open('./output.json', 'w') as f:
        f.write(json.dumps(output))
    with open('./history.list', 'w') as f:
        f.write(requests.get('https://raw.githubusercontent.com/BeautyYuYanli/music-down-bili/production/production/history.list').text)

def getBiliEntriesFromApi():
    info = requests.get('https://api.bilibili.com/x/v3/fav/resource/list?media_id=53706285&pn=1&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp').json()
    info = info['data']['medias']
    with open('./output.json') as f:
        al = json.loads(f.read())
    with open('./history.list') as f:
        be = f.read()
    be = be.split('\n')
    newEntries = []
    newEntriesUrl = []
    for i in info:
        url ="https://www.bilibili.com/video/av{}".format(str(i['id'])) 
        if url not in be:
            ge = {
                        'url': url,
                        'title': i['title'],
                        'date': datetime.datetime.today().timestamp()
                    }
            newEntries.insert(0, ge)
            newEntriesUrl.insert(0, url)
    print(newEntriesUrl)
    al += newEntries
    be += newEntriesUrl
    with open('./output.json', 'w') as f:
        f.write(json.dumps(al))
    with open('./history.list', 'w') as f:
        f.write('\n'.join(be))

if __name__ == "__main__":
    # getBiliEntriesFromGithub()
    getBiliEntriesFromApi()