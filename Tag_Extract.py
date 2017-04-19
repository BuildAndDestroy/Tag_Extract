#!/usr/bin/python

def main():
    import re, urllib

    try:
        import urllib.request
    except:
        pass

    def variables():
        host = str(raw_input("(ex. example.com) Host: "))
        site = host.split()
        return site

    regex_title = re.compile(r'<title>+.*</title>+', re.I|re.M)
    regex_link = re.compile(r'<link+.*>', re.I|re.M)
    regex_script = re.compile(r'<script+.*>+', re.I|re.M)
    regex_script_2 = re.compile(r'<script>+[\s\S]+?</script>', re.I|re.M)
    regex_meta = re.compile(r'<meta+.*>', re.I|re.M)
    regex_iframes = re.compile(r'<iframe+.*>+', re.I|re.M)

    for s in variables():
        print('+--------+')
        print("|  Host  |")
        print('+--------+')
        print('%s') % (s)
        try:
            u = urllib.urlopen('http://' + s)
        except:
            u = urllib.request.urlopen('http://' + s)
        text = u.read()
        title = re.findall(regex_title, str(text))
        link = re.findall(regex_link, str(text))
        meta = re.findall(regex_meta, str(text))
        iframes = re.findall(regex_iframes, str(text))
        script = re.findall(regex_script, str(text))
        script_2 = re.findall(regex_script_2, str(text))

    print('')
    print('+---------+')
    print('|  Title  |')
    print('+---------+')
    for tag in title:
        print(tag)
    print('')
    print('+-------------+')
    print('|  Link Tags  |')
    print('+-------------+')
    for tag in link:
        print(tag)
    print('')
    print('+-------------+')
    print('|  Meta Tags  |')
    print('+-------------+')
    for tag in meta:
        print(tag)
    print('')
    print('+-----------+')
    print('|  iframes  |')
    print('+-----------+')
    for tag in iframes:
        print(tag)
    print('')
    print('+---------------+')
    print('|  JavaScripts  |')
    print('+---------------+')
    for tag in script:
        if tag == '<script>':
            pass
        else:
            print(tag)
    for tag in script_2:
        print(tag)


if __name__ == '__main__':
    main()