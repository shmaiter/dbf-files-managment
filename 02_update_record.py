import dbf

table = dbf.Table("test_files/test.dbf")

with table:
    for record in table:

        if record["NAME"].strip() == "Bob":
            # record["birthdate"] = dt.date(1995, 8, 21)
            dbf.write(record, name="Mary")
        print(record[0:])


# untested

# import dbf
# from antipathy import Path
#
# for path, dirs, files in Path.walk('.'):
#     files = [f for f in files if f.ext == '.dbf']
#     for db in files:
#         if I_want_to_change_this_table(db):
#             with dbf.Table(db) as db:
#                 db.add_fields('Field2 C(4)')
#                 for record in db:
#                     dbf.write(Field2=record.Field1[-4:])
#                 db.delete_fields('Field1')
#                 db.pack()