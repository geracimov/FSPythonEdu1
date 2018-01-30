import collections
import fileshelper as fh
import nltkhelper as nh


def get_verbs_in_path(path, extension):
    verbs = []
    for filename in fh.get_filenames_by_path(path, extension):
        for v in nh.get_verbs_from_function_name_list(fh.get_funcnames_from_file(filename)):
            verbs.append(v)
    return nh.flat(verbs)


def get_verbs_in_paths(paths, extension):
    verbs = []
    for path in paths:
        verbs.append(get_verbs_in_path(path, extension))
    return nh.flat(verbs)


def verbs_in_paths_print_stats(paths, extension, max_count):
    wds = get_verbs_in_paths(paths, extension)

    print('total %s words, %s unique' % (len(wds), len(set(wds))))
    for word, occurence in collections.Counter(wds).most_common(max_count):
        print(word, occurence)


if __name__ == '__main__':
    import sys

    PATH = sys.argv[1]
    EXTENSION = sys.argv[2]
    MAX_COUNT = int(sys.argv[3])
    PROJECTS = sys.argv[4:]

    PATHS = [fh.join_path_filename(PATH, project) for project in PROJECTS]

    verbs_in_paths_print_stats(PATHS, EXTENSION, MAX_COUNT)
