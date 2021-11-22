import requests, json, datetime, os

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

def getBiliEntriesFromApi(fid, be):
    info = requests.get('https://api.bilibili.com/x/v3/fav/resource/list?media_id={}&pn=1&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp'.format(fid)).json()
    info = info['data']['medias']
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
    return newEntries, newEntriesUrl

def getYtbEntries(be):
    with open('./latest.json') as f:
        info = json.loads(f.read())
    newEntries = []
    newEntriesUrl = []
    for i in info:
        url = "https://www.youtube.com/watch?v={}".format(i['id'])
        if url not in be:
            ge = {
                        'url': url,
                        'title': i['title'],
                        'date': datetime.datetime.today().timestamp()
                    }
            newEntries.insert(0, ge)
            newEntriesUrl.insert(0, url)
    print(newEntriesUrl)
    return newEntries, newEntriesUrl

def main(biliFid, ytbId):
    with open('./output.json') as f:
        al = json.loads(f.read())
    with open('./history.list') as f:
        be = f.read()
    be = be.split('\n')

    if biliFid != '':
        newEntries, newEntriesUrl = getBiliEntriesFromApi(biliFid, be)
        al += newEntries
        be += newEntriesUrl
        with open('./output.json', 'w') as f:
            f.write(json.dumps(al))
        with open('./history.list', 'w') as f:
            f.write('\n'.join(be))

    if ytbId != '':
        newEntries, newEntriesUrl = getYtbEntries(be)
        al += newEntries
        be += newEntriesUrl
        with open('./output.json', 'w') as f:
            f.write(json.dumps(al))
        with open('./history.list', 'w') as f:
            f.write('\n'.join(be))
    
if __name__ == "__main__":
    main('53706285', 'PLXQAecVlk3h8GyTHVeNAuWB_b2TEoLlPV')