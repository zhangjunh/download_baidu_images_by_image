import os
import shutil

def finalmerges(allpath, inpath):

    topath = allpath

    for root, dirs, _ in os.walk(topath):

        for each in dirs:

            if each.find('result_') > -1:

                try:
                    os.chdir(os.path.join(inpath, each.split("_")[-1]).replace('\\', '/'))

                    for file in os.listdir(os.getcwd()):
                        srcFile = os.path.join(os.getcwd(), file).replace('\\', '/')
                        targetFile = os.path.join(root, each, file).replace('\\', '/')
                        shutil.copyfile(srcFile, targetFile)

                    print("copy finished:", each)

                except FileNotFoundError:
                    shutil.rmtree(os.path.join(root, each).replace('\\', '/'))
                    print("removed:", each)


if __name__ == '__main__':
    finalmerges(os.getcwd(), "D:/trains")