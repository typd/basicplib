import os

def purge_filename(name):
    assert name != None
    return name.replace('/', ' ').replace(':', ' ')

def get_size(path):
    if os.path.isdir(path):
        total = 0
        for f in os.listdir(path):
            total += get_size(os.path.join(path, f))
        return total
    else:
        return os.path.getsize(path)

def ensure_path(path):
    if os.path.exists(path):
        return
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    if not os.path.isdir(path):
        open(path, 'w').close()

def get_size_str(path):
    size = get_size(path)
    if size > 1000000000:
        return "%.2fG" % (float(size) / 1000000000)
    elif size > 1000000:
        return "%.2fM" % (float(size) / 1000000)
    elif size > 1000:
        return "%.2fK" % (float(size) / 1000)
    else:
        return "%dB" % size
