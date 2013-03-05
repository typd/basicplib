import urllib
import urllib2

def download(url, path, timeout=10):
    response = urllib2.urlopen(url, timeout=timeout)
    data = response.read()
    response.close()
    with open(path, 'wb') as downloadfile:
        downloadfile.write(data)

def get_str(url):
    request = urllib.urlopen(url)
    data = request.read()
    request.close()
    return data

