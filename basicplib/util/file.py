import os

def purge_filename(name):
    assert name != None
    return name.replace('/', ' ').replace(':', ' ')


def get_size(path):
    if os.path.isdir(path):
        total = 0
        for _file in os.listdir(path):
            total += get_size(os.path.join(path, _file))
        return total
    else:
        return os.path.getsize(path)


def ensure_path(path):
    if os.path.exists(path):
        return
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.isdir(path):
        open(path, 'a').close()


def get_size_str(path):
    size = get_size(path)
    return get_size_str_from_size(size)


def get_size_str_from_size(size):
    if size > 1000000000:
        return "%.2fG" % (float(size) / 1000000000)
    elif size > 1000000:
        return "%.2fM" % (float(size) / 1000000)
    elif size > 1000:
        return "%.2fK" % (float(size) / 1000)
    else:
        return "%dB" % size
