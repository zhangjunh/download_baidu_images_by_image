import os

def renames(allpath):

    for root, dirs, _ in os.walk(allpath):

        for each in dirs:

            if each.find('result_') > -1:
                os.chdir(allpath)
                name = each.split('_')[-1]
                os.rename(each, name)
                print ("renamed:", each)


if __name__ == '__main__':
    renames(os.getcwd())