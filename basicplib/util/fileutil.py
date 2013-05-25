import os
import zipfile


def convert_to_valid_path(path, substitution=''):
    name = ''
    valid_chars = ['.', ' ', '_', '-', os.path.sep]
    for char in path:
        if char.isalpha() or char.isdigit() or char in valid_chars:
            name += char
        else:
            name += substitution
    return name.strip()

def is_dir_path(path):
    if not path:
        return False
    return path.endswith(os.path.sep)

def save(data, path):
    ensure_dir(path)
    flag = 'w'
    if bytes == type(data):
        flag = 'wb'
    with open(path, flag) as savedfile:
        savedfile.write(data)

def unzip(path, to_dir=None):
    if not to_dir:
        to_dir = os.path.dirname(path)
    to_dir = os.path.join(to_dir, os.path.splitext(os.path.basename(path))[0])
    zfile = zipfile.ZipFile(path, 'r')
    for filename in zfile.namelist():
        if is_dir_path(filename):
            continue
        data = zfile.read(filename)
        save(data, os.path.join(to_dir, filename))

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

def ensure_dir(path):
    if os.path.exists(path):
        return
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def ensure_path(path):
    if os.path.exists(path):
        return
    ensure_dir(path)
    if not is_dir_path(path):
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
