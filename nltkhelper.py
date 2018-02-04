from nltk import pos_tag


def is_verb(word):
    if not word:
        return False
    nltk_verbs = ['VB', 'VBD']
    pos_info = pos_tag([word])
    return nltk_verbs.__contains__(pos_info[0][1])


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_verbs_from_function_name_list(function_name_list):
    verbs = []
    for function_name in function_name_list:
        verbs.append(get_verbs_from_function_name(function_name))
    return verbs
