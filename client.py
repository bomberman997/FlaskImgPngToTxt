import requests,os,shutil

# This is assuming that you are running docker locally

url = 'http://localhost:8080/addfile'

file_name = 'final_file.png'

# Bread and Butter this opens a byte stream of the PNG and opens a session using requests. Sends to server and prints status code.
# 200 Status is good.

with open(file_name,'rb') as img:
    name_img = os.path.basename(file_name)
    files = {'file':(file_name,img,'multipart/form-data',{'Expires':'0'})}
    with requests.Session() as s:
        r = s.post(url,files=files)
        print(r.status_code)

# Url to get file back as a text file.

url = 'http://localhost:8080/return-files/final_file.txt'

# Similiar to the previous step except in reverse. Using requests opens a stream from the Host and dumps raw byte stream into file and saves.

response = requests.get(url, stream=True)
with open('save.txt', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response