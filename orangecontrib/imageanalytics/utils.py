import hashlib
import pickle
import re

_HOSTNAME_REGEX = re.compile(r'^(https?://)?(?P<hostname>[\wd.]+)')
_PORT_REGEX = re.compile(r':(?P<port>\d{2,4})/?')


def save_pickle(obj, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(obj, f)


def load_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def md5_hash(bytes_):
    md5 = hashlib.md5()
    md5.update(bytes_)
    return md5.hexdigest()
