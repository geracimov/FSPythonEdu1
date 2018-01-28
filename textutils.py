from nltk import pos_tag


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(_word):
    if not _word:
        return False
    pos_info = pos_tag([_word])
    return pos_info[0][1] == 'VB'


def get_verbs_from_function_name(function_name):
    return [_word for _word in function_name.split('_') if is_verb(_word)]
