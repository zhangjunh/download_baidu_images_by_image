import os
from PIL import Image
import logging
import sys

def converts(allpath):

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
    log = logger()

    for root, dirs, _ in os.walk(allpath):

        for each in dirs:

            if each.find('result_') > -1:

                print(each)
                os.chdir(os.path.join(root, each).replace('\\', '/'))


                for infile in os.listdir(os.getcwd()):

                    f, e = os.path.splitext(infile)
                    outfile = f + ".jpeg"
                    if infile != outfile:
                        try:
                            Image.open(infile).save(outfile)
                            print("converted", infile)
                            os.remove(infile)
                        except IOError:
                            log.info("Convert failed：%s %s" % (each, infile))
                            print("cannot convert:", each, infile)



if __name__ == '__main__':
    converts(os.getcwd())