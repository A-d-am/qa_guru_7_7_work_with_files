import csv
import os
from conftest import TESTS_ROOT_PATH


def test_csv():
    tests_dir = TESTS_ROOT_PATH
    resources_dir = os.path.join(tests_dir, 'resources')

    if not os.path.exists(resources_dir):
        os.mkdir('resources')

    csv_file_path = os.path.join(resources_dir,'new_csv.csv')
    with open(csv_file_path, 'w') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_file_path) as csv_file:
        csv_file_rows = list()
        csvreader = csv.reader(csv_file, delimiter=';')
        for row in csvreader:
            csv_file_rows.append(row)

    assert csv_file_rows[0] == ['Bonny', 'Born', 'Peter'], (f"Wrong data in row {0}: "
                                                            f"expected {['Bonny', 'Born', 'Peter']}, "
                                                            f"got {csv_file_rows[0]}")
    assert csv_file_rows[1] == ['Alex', 'Serj', 'Yana'], (f"Wrong data in row {1}: "
                                                            f"expected {['Alex', 'Serj', 'Yana']}, "
                                                            f"got {csv_file_rows[1]}")

