if __name__ == '__main__':
    with open('basic_readme.md') as f:
        basic = f.read()
    # music
    with open('./components/music/output.md') as f:
        al = f.read().split('\n')
    al = al[3:10]
    al.insert(0, '## Favorite Music\n')
    al.append('\n[more...](https://github.com/BeautyYuYanli/beautyyuyanli/blob/master/components/music/output.md)\n')
    basic = basic.replace('$$$favMusic$$$', '\n'.join(al))

    # dance
    with open('./components/dance/output.md') as f:
        al = f.read().split('\n')
    al = al[3:10]
    al.insert(0, '## Favorite Dance\n')
    al.append('\n[more...](https://github.com/BeautyYuYanli/beautyyuyanli/blob/master/components/dance/output.md)\n')
    basic = basic.replace('$$$favDance$$$', '\n'.join(al))

    with open('readme.md', 'w') as f:
        f.write(basic)
    