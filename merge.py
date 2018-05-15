import os
import shutil

def merge(allpath):

    for each_ in os.listdir(allpath):

        if each_.find('result_') > -1:

            path = os.path.join(allpath, each_).replace('\\','/')

            for root, dirs, files in os.walk(path):

                for each in dirs:

                    os.chdir(os.path.join(root, each).replace('\\','/'))

                    for file in os.listdir(os.getcwd()):

                        srcFile = os.path.join(os.getcwd(), file)
                        targetFile = os.path.join(path, file)
                        shutil.copyfile(srcFile, targetFile)

            os.chdir(allpath)

            for root, dirs, files in os.walk(path):

                for each in dirs:

                    shutil.rmtree(os.path.join(root, each).replace('\\','/'))
                    print("Delete dir:", os.path.join(root, each).replace('\\','/'))


if __name__ == '__main__':
    merge(os.getcwd())