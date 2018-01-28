import os
import ast


def get_trees(_path, with_filenames=False, with_file_content=False):
    filenames = []
    trees = []
    for dirname, dirs, files in os.walk(_path, topdown=True):
        files_gen = (file for file in files if file.endswith('.py'))
        for file in list(files_gen)[0:101]:
            filenames.append(os.path.join(dirname, file))
    print('total %s files' % len(filenames))

    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None

        if with_filenames:
            if with_file_content:
                trees.append((filename, main_file_content, tree))
            else:
                trees.append((filename, tree))
        else:
            trees.append(tree)
    print('trees generated')
    return trees


def get_functions_in_trees(_trees):
    def get_functions_in_tree(_tree):
        return [node.name.lower() for node in ast.walk(_tree) if isinstance(node, ast.FunctionDef)]

    return flat([get_functions_in_tree(tree) for tree in _trees])