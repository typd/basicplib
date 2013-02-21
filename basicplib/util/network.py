import urllib
import urllib2
import socket

def download(url, path, timeout=10):
    response = urllib2.urlopen(url, timeout=timeout)
    data = response.read()
    response.close()
    with open(path, 'wb') as file:
        file.write(data)

def get_str(url):
    f = urllib.urlopen(url)
    data = f.read()
    f.close()
    return data

