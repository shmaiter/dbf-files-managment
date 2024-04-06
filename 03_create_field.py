import dbf

# FIRST: make the connection with the table
db = dbf.Table("database/people.dbf")

saldos = [125333, 562000, 451256]

# SECOND: add the field or column
with db:
    db.add_fields(field_specs="saldos_pat N(6, 0)")
    for index, record in enumerate(db):
        dbf.write(saldos_pat=saldos[index])
