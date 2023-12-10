# Файл содержит функции для оформления задач в кодом варианте, а также для markdown размертки.

def theme_decorator(type: str, theme: str) -> str:
  '''
  Функция для создания оформления темы ДЗ / КР.
  '''
  out_str = f'# --- {type} / {theme} --- #'
  decor_line = f'# {"-" * (len(out_str) - 4)} #'

  return decor_line + '\n' + out_str + '\n' + decor_line


def replit_task_creator(name: str, num: int, text: str, test_in: list,
                        test_out: list) -> str:
  '''
  Функция для оформления задачи в текстовом формате.
  '''
  t_name = f'# Задание №{num}. {name}.'
  t_text = f'\n# {text}'

  t_tests = ''

  for i in range(len(test_in)):
    if len(test_in) > 1:
      t_tests += f'\n\n# Пример ввода - {i + 1}:'
    else:
      t_tests += '\n\n# Пример ввода:'

    for in_item in test_in[i]:
      t_tests += f'\n# {in_item}'

    if len(test_in) > 1:
      t_tests += f'\n\n# Пример вывода - {i + 1}:'
    else:
      t_tests += '\n\n# Пример вывода:'

    for out_item in test_out[i]:
      t_tests += f'\n# {out_item}'

  return t_name + t_text + t_tests


def colab_task_creator(name: str, num: int, text: str, test_in: list,
                       test_out: list) -> str:
  '''
  Функция для оформления задачи в текстовом формате.
  '''
  t_name = f'# Задание №{num}. {name}.**'
  t_text = f'\n {text}'

  t_tests = ''

  for i in range(len(test_in)):
    if len(test_in) > 1:
      t_tests += f'\n\n\n**Пример ввода - {i + 1}:**'
    else:
      t_tests += '\n\n\n**Пример ввода:**'

    for in_item in test_in[i]:
      t_tests += f'\n\n{in_item}'

    if len(test_in) > 1:
      t_tests += f'\n\n\n**Пример вывода - {i + 1}:**'
    else:
      t_tests += '\n\n\n**Пример вывода:**'

    for out_item in test_out[i]:
      t_tests += f'\n\n{out_item}'

  return t_name + t_text + t_tests


name = ''
num = 0
text = ''
tests_in = [[]]
tests_out = [[]]

# print(theme_decorator('Домашнее задание', 'Словари - I'))
# print(replit_task_creator(name, num, text, tests_in, tests_out))
# print(colab_task_creator(name, num, text, tests_in, tests_out))
