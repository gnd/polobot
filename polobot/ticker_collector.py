import urllib.request
import json

class ticker_collector():
    def __init__(self, api_url):
        self.api_url = api_url

    def get_url(self, url):
        conn = urllib.request.urlopen(url)
        if (conn.getcode() == 200):
            data = conn.read()
            jsonData = json.loads(data)
        else:
            print("Error receiving data", conn.getcode())
        return jsonData
        
    def collect_basic_ticker(self):
        data = self.get_url(self.api_url)
        return data
