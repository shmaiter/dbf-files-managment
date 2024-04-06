import dbf

dbf_filename = "some-file.dbf"
encoding = "utf8"
table = dbf.Table(dbf_filename, codepage=encoding, on_disk=True)
field_names = table.field_names
table.open()
for record in table:
    row = {field_name: record[field_name] for field_name in field_names}
    print(row)  # You can use row.field_name to get each field's data also