import configparser
class Read_Config:
    def read_config(self,file_path,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]
if __name__ == '__main__':
    Read_Config().read_config("case.config",'MODE','mode')
    Read_Config().read_config("case.config",'SHOP','shop')
    

