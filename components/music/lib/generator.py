import json, datetime
def main(header):
    al = '''
# {}

|Title|Date|
|---|---|
'''.format(header)
    with open('output.json') as f:
        output = json.loads(f.read())
    outputStr = []
    for i in output:
        outputStr.insert(0, "|['{}']({})|{}|".format(i['title'].replace('|', ''), i['url'], datetime.date.fromtimestamp(i['date']).strftime("%Y-%m-%d")))
    al += "\n".join(outputStr)
    with open('output.md', 'w') as f:
        f.write(al)
if __name__ == "__main__":
    main()