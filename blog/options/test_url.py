from django.urls import include, path

VERSION = 'v2'


def get_include(url, name, v=VERSION):
    *root, t = name.split('.')
    pattern = []
    try:
        pattern.append(path(url, (include('.'.join((*root, v, t))))))
    except ModuleNotFoundError:
        pass
    finally:
        pattern.append(path(url, include(name)))
    return pattern
