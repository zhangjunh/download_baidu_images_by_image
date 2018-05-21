import os
import hashlib
import logging
import sys

def delrepetitions(allpath):

    for each_ in os.listdir(allpath):

        if each_.find('result_') > -1:

            path = os.path.join(allpath, each_).replace('\\','/')
            print(path)

            def logger():

                logger = logging.getLogger()
                if not logger.handlers:

                    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

                    file_handler = logging.FileHandler("test.log")
                    file_handler.setFormatter(formatter)

                    console_handler = logging.StreamHandler(sys.stdout)
                    console_handler.formatter = formatter

                    logger.addHandler(file_handler)
                    logger.addHandler(console_handler)

                    logger.setLevel(logging.INFO)
                return logger

            def get_md5(filename):
                m = hashlib.md5()
                mfile = open(filename, "rb")
                m.update(mfile.read())
                mfile.close()
                md5_value = m.hexdigest()
                return md5_value

            def get_urllist():

                base = (path+'/')
                list = os.listdir(base)
                urlList=[]
                for i in list:
                    url = base + i
                    urlList.append(url)
                return  urlList


            log = logger()
            md5List =[]
            urlList =get_urllist()
            for a in urlList:
                md5 =get_md5(a)
                if (md5 in md5List):
                    os.remove(a)
                    print("repeated：%s"%a)
                    log.info("repeated：%s"%a)
                else:
                    md5List.append(md5)
                    print("operated", len(md5List), "pictures" if len(md5List) > 1 else "picture", "altogether.")


if __name__ == '__main__':
    delrepetitions(os.getcwd())