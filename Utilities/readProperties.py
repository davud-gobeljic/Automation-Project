import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\davud\PycharmProjects\atlantbh_test\Configurations\config.ini")

class ReadConfig():
    @staticmethod
    def getURL():
        url = config.get('common info', 'baseURL')
        return url
