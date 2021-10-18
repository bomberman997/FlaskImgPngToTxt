
def old_():

    # import json
    # import requests

    # # Ton to be sent
    # datas = {'var1' : 'var1','var2'  : 'var2',}

    # #my file to be sent
    # local_file_to_send = 'payload/qc.PNG'
    # with open(local_file_to_send, 'w') as f:
    #     f.write('I am a file\n')

    # url = "http://127.0.0.1:8080/addfile"

    # files = [
    #     ('document', (local_file_to_send, open(local_file_to_send, 'rb'), 'application/octet')),
    #     ('datas', ('datas', json.dumps(datas), 'application/json')),
    # ]

    # r = requests.post(url, files=files)
    # print(str(r.content, 'utf-8'))
    pass

import os
import requests
from glob import glob

from werkzeug.utils import send_file

def files_get():
    PATH = 'C:\\Users\\billy\\code\\tessPackage\\pngs\\'
    return [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.png'))]

def pick_server(servNum):
    if servNum > 2: servNum = 0 

    servNum = 0

    port = ['81']#['81','82','83']
    new_url = 'http://localhost:{}/addfile'.format(port[servNum])

    servNum = servNum + 1

    return new_url,servNum

def sender(file_name,server_url):
    # url = 'http://localhost:8080/addfile'

    # file_name = 'qc copy.png'

    with open(file_name,'rb') as img:

        name_img = os.path.basename(file_name)
        files = {'file':(file_name,img,'multipart/form-data',{'Expires':'0'})}

        with requests.Session() as s:
            r = s.post(server_url,files=files)
            print(r.status_code)

result = files_get()
counter = 0

for x in result:
    print(x)
    url,counter = pick_server(counter)
    print(url)
    sender(x,url)


    ## Convert oG client script into function that can handle file and get CSV back or store somewhere else.

