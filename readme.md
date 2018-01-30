TopVerbs
=====================

## Назначение
Сбор статистики использования глаголов в названиях питоновских функций

## Как работает
Программа по указаному каталогу ищет файлы *.py и выводит список глаголов, встречающийхся в названиях функций,
а также количество использования этих глаголов.

На вход принимается каталог, в котором происходит поиск фавйлов

## Как запускать
Основная функция для запуска get_top_verbs_in_path2
Параметры для запуска: Путь, расширение файлов, макс количество самых используемых глаголов, список подкаталогов

## Примеры
* запуск по 1 каталогу: `get_verbs_in_path(path, extension)`
`topverbs.get_verbs_in_path('c:\\temp','.py')`

* запуск по списку каталогов: `get_verbs_in_paths(paths, extension)`
`topverbs.get_verbs_in_path(['c:\\temp','c:\\temp2'],'.py')`

* печать статистики по группе каталогов: `verbs_in_paths_print_stats(PATHS, EXTENSION, MAX_COUNT)`
`verbs_in_paths_print_stats(['c:\\temp','c:\\temp2'], '.py', 2)`

вывод:
`total 33 words, 3 unique
do 25
get 6`

* запуск из консоли
`c:\temp .py 2 django flask pyramid reddit requests sqlalchemy`
