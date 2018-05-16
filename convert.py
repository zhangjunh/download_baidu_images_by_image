import os
from PIL import Image
import logging
import sys

def converts(allpath):

    def logger():
        """ 获取logger"""
        logger = logging.getLogger()
        if not logger.handlers:
            # 指定logger输出格式
            formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
            # 文件日志
            file_handler = logging.FileHandler("test.log")
            file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
            # 控制台日志
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.formatter = formatter  # 也可以直接给formatter赋值
            # 为logger添加的日志处理器
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
            # 指定日志的最低输出级别，默认为WARN级别
            logger.setLevel(logging.INFO)
        return logger
    log = logger()

    for root, dirs, _ in os.walk(allpath):

        for each in dirs:

            if each.find('result_') > -1:

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

                print(each)


if __name__ == '__main__':
    converts(os.getcwd())