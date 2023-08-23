import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplication(self):
        url = config.get('common info ', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username


    @staticmethod
    def getUserpassword():
        password = config.get('common info', 'userpassword')
        return password