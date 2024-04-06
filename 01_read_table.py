import dbf

dbf_filename = "./test_files/test.dbf"
encoding = "utf8"
table = dbf.Table(dbf_filename, codepage=encoding, on_disk=True)
field_names = table.field_names
table.open()
for record in table:
    # READ 1 => shows fieldnames and data in vertical way
    # print(record)

    # READ 2 => shows data only in lists
    # print(record[0:])

    # READ 3 => shows fieldnames and data in dictionaries
    row = {field_name: record[field_name] for field_name in field_names}
    print(row)  # You can use row.field_name to get each field's data also
