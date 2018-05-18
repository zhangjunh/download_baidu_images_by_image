import requests
import json
import re
import os
import urllib
import urllib.request
import time
import subprocess
import socket


def save_img(img_url,file_name,file_path):

    try:
        if not os.path.exists(file_path):
            print ('create dirs:',file_path)

            os.makedirs(file_path)

        file_suffix = os.path.splitext(img_url)[-1]

        filename = '{}{}{}{}{}'.format(file_path,os.sep,file_name, int(round(time.time()*1000)), file_suffix)

        socket.setdefaulttimeout(10)

        try:
            urllib.request.urlretrieve(img_url,filename=filename)
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.request.urlretrieve(img_url,filename=filename)
                    break
                except socket.timeout:
                    err_info = 'reloading for %d time' % count if count == 1 else 'reloading for %d times' % count
                    print(err_info)
                    count += 1
            if count > 5:
                print("downloading picture failed")

    except IOError as e:
        print ('file operation failed:',e)
    except Exception as e:
        print ('failed：',e)

def spiders(allpath):

    path = os.path.join(allpath, "additive").replace('\\','/')

    for root, _, files in os.walk(path):

        for each in files:

            imagepath = os.path.join(root, each).replace('\\','/')
            print(imagepath)

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            }

            url = "http://image.baidu.com/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true"
            fileopen = open(imagepath, "rb")
            files = {
                'file': fileopen
            }

            fnull = open(os.devnull, 'w')
            result0 = subprocess.call('ping www.baidu.com', shell=True, stdout=fnull, stderr=fnull)
            fnull.close()
            while result0:
                print('Waiting for Baidu.')
                time.sleep(60)
                fnull = open(os.devnull, 'w')
                result0 = subprocess.call('ping www.baidu.com', shell=True, stdout=fnull, stderr=fnull)
                fnull.close()

            temp_data = json.loads(requests.post(url=url, headers=headers, files=files).text)

            ans_url = "http://image.baidu.com/pcdutu?queryImageUrl=" + str(temp_data['url']) + "&querySign" + temp_data[
                "querySign"] + "&fm=home&uptype=upload_pc&result=result_camera"
            page_source = requests.get(url=ans_url, headers=headers).text
            multi_data = re.findall('"ObjURL":"(.*?)"', page_source)

            index = 0
            for u in multi_data:
                index += 1
                save_img(u, 'add_' + str(index) + '_', os.path.join(allpath, "result_" + root.split('\\')[-1]))
                print(index, "pictures" if index > 1 else "picture", "saved.")
            fileopen.close()
            os.remove(imagepath)
            print("delete imgae:", imagepath)
            if not os.listdir(root):
                os.rmdir(root)
                print("delete empty dir:", root.replace('\\','/'))


if __name__ == '__main__':
    spiders(os.getcwd())