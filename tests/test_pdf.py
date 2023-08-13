import pypdf
import os
from conftest import RESOURCES_DIR


def test_pdf():
    pdf_file_path = os.path.join(RESOURCES_DIR, 'docs-pytest-org-en-latest.pdf')
    reader = pypdf.PdfReader(pdf_file_path)
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    first_page_text = first_page.extract_text()
    expected_first_page_text = ('pytest Documentation\nRelease 0.1\nholger krekel, '
                                'trainer and consultant, https://merlinux.eu/\nJul 14, 2022')

    count = 0

    pdf_file_images_folder = os.path.abspath('pdf_file_images')

    if not os.path.exists(pdf_file_images_folder):
        os.mkdir('pdf_file_images')

    for image_file in first_page.images:
        image_file_name = str(count) + image_file.name
        path_to_image_file = os.path.join(pdf_file_images_folder, image_file_name)
        with open(path_to_image_file, 'wb') as fp:
            fp.write(image_file.data)
            count += 1

    assert number_of_pages == 412, f'Wrong number of pdf document pages: expected {412}, got {number_of_pages}'
    assert first_page_text == expected_first_page_text, \
        f'Wrong first page text: expected {expected_first_page_text} first page text, got {first_page_text}'
    assert count == len(os.listdir(pdf_file_images_folder)), (f'Expected {count + 1} files in {pdf_file_images_folder},'
                                                              f'got {len(os.listdir(pdf_file_images_folder))}')
