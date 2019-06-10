import requests

from interfaceTest import readConfig as readConfig
from interfaceTest.common.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()


class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.param = {}
        self.data = {}
        self.url = None
        self.files = {}

    # set url
    def set_url(self, url):
        self.url = host + url

    # set header
    def set_headers(self, headers):
        self.headers = headers

    def set_param(self, param):
        self.param = param

    def set_data(self, data):
        self.data = data

    def set_files(self, files):
        self.files = files

    # defined http get method

    def get(self):
        try:
            response = requests.get(self.url, params=self.param, headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            return response

        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def post(self):
        try:
            response = requests.post(self.url, header=self.headers, data=self.data, files=self.files,
                                     timeout=float(timeout))
            response.text
            return response

        except TimeoutError:
            self.logger.error("Time out!")
            return None


if __name__ == '__main__':
    url = 'http://wiki.baidu.com/dosearchsite.action'
    header = {'content_type': 'application/x-www-form-urlencoded'}
    param = {'queryString': '订单中心环境'}
    data = {'queryString': '订单中心环境'}
    timeout = 0.5
    requests.get(url, headers=header, params=param, timeout=timeout)
    requests.post(url, headers=header, data=data, timeout=timeout)
