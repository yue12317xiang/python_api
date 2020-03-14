import logging
class Mylog:
    def mylog(self,msg,Level):
        mylog = logging.getLogger("这是一个日志收集器")
        mylog.setLevel("DEBUG")
        formatter =logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        cf = logging.StreamHandler()
        cf.setLevel("DEBUG")
        cf.setFormatter(formatter)
        fe = logging.FileHandler("test_log.txt",encoding='utf-8')
        fe.setLevel("ERROR")
        fe.setFormatter(formatter)
        mylog.addHandler(cf)
        mylog.addFilter(fe)
        if Level == 'DEBUG':
            mylog.debug(msg)
        elif Level == "INFO":
            mylog.info(msg)
        elif Level == 'WARNING':
            mylog.warning(msg)
        elif Level == 'ERROR':
            mylog.error(msg)
        else:
            mylog.critical(msg)
        mylog.removeHandler(cf)
        mylog.removeFilter(fe)
    def info(self,msg):
        self.mylog(msg,'INFO')
    def debug(self,msg):
        self.mylog(msg,'DEBUG')
    def warning(self,msg):
        self.mylog(msg,'WARNING')
    def error(self,msg):
        self.mylog(msg,'ERROR')
    def critical(self,msg):
        self.mylog(msg,'CRITICAL')
if __name__ == '__main__':
    res = Mylog().mylog("这是第四层：",'ERROR')
    res1 = Mylog().info("这是info层")
    
    
