import os

HELLO_ABSPATH = os.path.abspath('hello')
print(HELLO_ABSPATH)

print(os.path.dirname(HELLO_ABSPATH))

CURRENT_FILE_PATH = os.path.abspath(__file__)
print(CURRENT_FILE_PATH)

PROJECT_ROOT_PATH = os.path.dirname(CURRENT_FILE_PATH)
print(PROJECT_ROOT_PATH)

ANYFILE_PATH = os.path.abspath('resources/anyfile')
print(ANYFILE_PATH)
with open('resources/anyfile') as file:
    print(file.read())

JOINED_PATH = os.path.join(PROJECT_ROOT_PATH, '', 'hello')
print(JOINED_PATH)

NEW_RESOURCE_PATH = os.path.join(PROJECT_ROOT_PATH, 'new_resource')
print(NEW_RESOURCE_PATH)

IS_RESOURCE_EXISTS = os.path.exists(NEW_RESOURCE_PATH)
print(IS_RESOURCE_EXISTS)

if not IS_RESOURCE_EXISTS:
    os.mkdir('new_resource')
IS_RESOURCE_EXISTS = os.path.exists(NEW_RESOURCE_PATH)
print(IS_RESOURCE_EXISTS)
