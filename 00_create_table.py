import os

import dbf
import datetime as dt
from pathlib import Path

path_to_file = Path.cwd() / "test_files/test.dbf"

try:
    path_to_file.unlink()
    print(f"\n{path_to_file}")
    print("File deleted successfully.")

except FileNotFoundError:
    print(f"\n{path_to_file}")
    print("File not found.")

finally:
    print(f"\nCreating new dbf table on:")
    print(f"{path_to_file}")

    table = dbf.Table(
            filename=str(path_to_file),
            field_specs='name C(15); birthdate D; patentes N(7, 0)',
            on_disk=True,  # False = creates in-memory table, True = persist on disk
            )
    # table.open(dbf.READ_WRITE) #  This line allows to append, insert, delete lines to the in-memory table.
    print("File created successfully.")

    people_data = [
        ("Alice", dt.date(1955, 5, 15), 125333),
        ("Josh", dt.date(1954, 7, 1), 650000),
        ("Melany", dt.date(1985, 11, 5), 750000),
        ("Bob", dt.date(1995, 7, 30), 256321)
    ]

    # add some records to it
    with table:
        for person in people_data:
            table.append(person)

    print("Table populated successfully.")