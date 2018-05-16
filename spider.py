import requests
import json
import re
import os
import urllib
import urllib.request
import time
import subprocess


def save_img(img_url,file_name,file_path):

    try:
        if not os.path.exists(file_path):
            print ('创建文件夹',file_path)

            os.makedirs(file_path)

        file_suffix = os.path.splitext(img_url)[-1]

        filename = '{}{}{}{}{}'.format(file_path,os.sep,file_name, int(round(time.time()*1000)), file_suffix)

        urllib.request.urlretrieve(img_url,filename=filename)
    except IOError as e:
        print ('文件操作失败',e)
    except Exception as e:
        print ('错误 ：',e)

def spiders(allpath):

    path = os.path.join(allpath, "additive").replace('\\','/')

    for root, _, files in os.walk(path):

        for each in files:

            imagepath = os.path.join(root, each).replace('\\','/')
            print(imagepath)

            # 定义统一的headers
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
            }

            # 图片上传
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

            # 获得图像识别结果
            ans_url = "http://image.baidu.com/pcdutu?queryImageUrl=" + str(temp_data['url']) + "&querySign" + temp_data[
                "querySign"] + "&fm=home&uptype=upload_pc&result=result_camera"
            page_source = requests.get(url=ans_url, headers=headers).text
            multi_data = re.findall('"ObjURL":"(.*?)"', page_source)

            index = 0
            for u in multi_data:
                index += 1
                save_img(u, 'add_' + str(index) + '_', os.path.join(allpath, "result_" + root.split('\\')[-1]))
                print(index, "pictures" if index > 1 else "picture", "Saved.")
            fileopen.close()
            os.remove(imagepath)
            print("Delete imgae:", imagepath)
            if not os.listdir(root):
                os.rmdir(root)
                print("Delete empty dir:", root.replace('\\','/'))


if __name__ == '__main__':
    spiders(os.getcwd())