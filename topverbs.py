import os
import collections

import sys

import textutils
import treeshelper


def get_top_verbs_in_path1(_path, _top_size=10):
    global Path
    Path = _path
    trees = [t for t in get_trees(None) if t]
    fncs = [f for f in get_functions_in_trees(trees)
            if not (f.startswith('__') and f.endswith('__'))]
    print('functions extracted')
    verbs = flat([get_verbs_from_function_name(function_name) for function_name in fncs])
    return collections.Counter(verbs).most_common(_top_size)


def get_top_verbs_in_path(path, max_count=10):
    return path + ' - ' + str(max_count)


def get_top_verbs_in_path2(path, count, projects):
    print("path^ " + path)
    print("count^ " + str(count))
    for proj in projects:
        print(str(proj) + "!")


if __name__ == '__main__':
    get_top_verbs_in_path2(sys.argv[1], sys.argv[2], sys.argv[3:])
    # PATH = sys.argv[1]
    # MAX_COUNT = sys.argv[2]
    # print(get_top_verbs_in_path(PATH, MAX_COUNT))
    # for param in sys.argv:
    #     print(param)

    # wds = []
    # projects = [
    #     'django',
    #     'flask',
    #     'pyramid',
    #     'reddit',
    #     'requests',
    #     'sqlalchemy',
    # ]
    # top_size = 200
    #
    # for project in projects:
    #     path = os.path.join('.', project)
    #     wds += get_top_verbs_in_path(path, top_size)
    #
    # print('total %s words, %s unique' % (len(wds), len(set(wds))))
    # for word, occurence in collections.Counter(wds).most_common(top_size):
    #     print(word, occurence)
