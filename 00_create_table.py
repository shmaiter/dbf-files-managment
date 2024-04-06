import dbf
import datetime as dt

# create an in-memory table
table = dbf.Table(
        filename='test_files/test.dbf',
        field_specs='name C(15); birthdate D; saldos_p N(7, 0)',
        on_disk=True,
        )
# table.open(dbf.READ_WRITE) #  This line allows to append, insert, delete lines to the in-memory table.

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
