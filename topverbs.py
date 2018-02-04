import collections
import fileshelper as fh
import nltkhelper as nh
import listhelper as lh


def get_verbs_in_path(path_loc, extension):
    verbs = []
    for filename in fh.get_filenames_by_path(path_loc, extension):
        for v in nh.get_verbs_from_function_name_list(fh.get_funcnames_from_file(filename)):
            verbs.append(v)
    return lh.flat(verbs)


def get_verbs_in_paths(paths_loc, extension):
    verbs = []
    for path_loc in paths_loc:
        verbs.append(get_verbs_in_path(path_loc, extension))
    return lh.flat(verbs)


def verbs_in_paths_print_stats(paths_loc, extension, max_verb_count):
    wds = get_verbs_in_paths(paths_loc, extension)

    print('total %s words, %s unique' % (len(wds), len(set(wds))))
    for word, occurence in collections.Counter(wds).most_common(max_verb_count):
        print(word, occurence)


if __name__ == '__main__':
    import sys

    path = sys.argv[1]
    ext = sys.argv[2]
    max_count = int(sys.argv[3])
    projects = sys.argv[4:]

    paths = [fh.join_path_filename(path, project) for project in projects]

    verbs_in_paths_print_stats(paths, ext, max_count)
