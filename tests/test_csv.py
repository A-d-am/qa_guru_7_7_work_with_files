import csv
import os
from conftest import RESOURCES_DIR


def test_csv():
    if not os.path.exists(RESOURCES_DIR):
        os.mkdir('resources')

    csv_file_path = os.path.join(RESOURCES_DIR, 'new_csv.csv')
    with open(csv_file_path, 'w', newline="") as csv_file:
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
