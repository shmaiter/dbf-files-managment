import dbf

# FIRST: make the connection with the table
table = dbf.Table("test_files/test.dbf")
field_names = table.field_names
saldos = [125333, 562000, 451256, 450225]

# SECOND: add the field or column
with table:
    if "licores" not in field_names:
        table.add_fields(field_specs="licores N(7, 0)")

    for index, record in enumerate(table):
        dbf.write(record, licores=saldos[index])
        print(record[0:])
