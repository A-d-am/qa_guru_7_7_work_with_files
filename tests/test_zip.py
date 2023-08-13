import zipfile
import os
from conftest import RESOURCES_DIR


def test_zip():
    zip_file_path = os.path.join(RESOURCES_DIR, 'hello.zip')
    with zipfile.ZipFile(zip_file_path) as hellozip:
        all_files_in_zip = hellozip.namelist()
        hellozip.extract('hello/Hello.txt', path=RESOURCES_DIR)
        text = hellozip.read('hello/Hello.txt')
        assert 'hello/Hello.txt' in all_files_in_zip, f"No file {'Hello.txt'} in zip with name {'hello.zip'}"
        assert text == b'Hello, World!'

    os.remove(os.path.join(RESOURCES_DIR, 'hello'))
