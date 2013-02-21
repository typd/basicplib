import os

def purge_filename(name):
    assert name != None
    return name.replace('/', ' ').replace(':', ' ')

def get_size(file):
    return os.path.getsize(file)

def get_size_str(file):
    size = get_size(file)
    if size > 1000000000:
        return "%.2fG" % (float(size) / 1000000000)
    elif size > 1000000:
        return "%.2fM" % (float(size) / 1000000)
    elif size > 1000:
        return "%.2fK" % (float(size) / 1000)
    else:
        return "%dB" % size
