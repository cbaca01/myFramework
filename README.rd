Do the following:
- Add to PYTHONPATH this:
  ** NOTE: NEED TO MAKE THIS DYNAMIC **
  export PYTHONPATH=*********






# MOVE TO YOUR MODELS!

# SELECT
db = Database()
books = db.table.books
query = db.session.query(books).all()
result = db.fetchAll(query)

print result

db.closeConnection()

#INSERT
# db = Database()
# books = db.table.books
# stmt = books(title='War and Peace', primary_author='Leo Tolstoy')
# db.session.add(stmt)
# db.session.commit()
# db.closeConnection()

# DELETE
# db = Database()
# books = db.table.books
# db.session.query(books).filter_by(id=10).delete()
# db.session.commit()
# db.closeConnection()

# UPDATE
# db = Database()
# books = db.table.books
# db.session.query(books).filter_by(id=9).update({'primary_author': 'Leo Tolstoy'})
# db.session.commit()
# db.closeConnection()


/***********************************************/
from includes.table_mapper import TableMapper

db = Database()
db.connect()


property_types = TableMapper(db.table.property_types, db.session)
#data1 = {'title': 'The Great Gatsby', 'primary_author': 'F. Scott Fitzgerald'}

# data2 = [
# 	{'title': 'Great Expectations', 'primary_author': 'Charles Dickens'},
# 	{'title': 'The Old Man And The Sea', 'primary_author': 'Ernest Hemingway'}
# ]

#params = {'id': 3}
#params = {}
#data = {'title': 'War and Peace'}
# params = {'id': 5}

#books.insert(data2)
#books.insert(data2)
#books.delete(params)
#print db.fetchRow(books.update(data, params))

#print books.select()

# Get all rows
# print db.fetchAll(property_types.select())

# Get specific row
# print db.fetchRow(books.select(params))

# # Get specific column
# print db.fetchRow(books.select(params))['title']

# print db.fetchAll(db.genStoredProcedureCall('test_schema.getallpropertytypestableset()'))
# print db.fetchRow(db.genStoredProcedureCall('test_schema.getpropertytypetablesetbyid(2)'))
db.genStoredProcedureCall('test_schema.getpropertytypetablesetbyid')

# db.session.commit()
db.closeConnection()

#session = db.session
#books = db.table.books
#property_types = db.table.property_types

#print params

#allBooks = session.query(books).all()
#allPropertyTypes = session.query(property_types).filter_by(id = 1)
#print db.fetchAll(allBooks)
#print db.fetchAll(allPropertyTypes)


property_types = TableMapper(db.table.property_types, db.session)

print db.fetchRow(db.genStoredProcedureCall(proc='test_schema.getallpropertytypestableset', params={'id': 2}))
# db.genStoredProcedureCall('test_schema.getpropertytypetablesetbyid')
# Proper way to call a stored function
# SELECT * FROM test_schema.getpropertytypetablesetbyid(i_id:=2);

# Latest build:
from includes.table_mapper import TableMapper

db = Database()
db.connect()


property_types = TableMapper(db.table.property_types, db.session)

print db.fetchRow(db.genStoredProcedureCall(proc='test_schema.getallpropertytypestableset', params={'id': 2}))
# db.genStoredProcedureCall('test_schema.getpropertytypetablesetbyid')
# Proper way to call a stored function
# SELECT * FROM test_schema.getpropertytypetablesetbyid(i_id:=2);

# db.session.commit()
db.closeConnection()


# Updating
data = {'title': 'The Great Gatsby', 'primary_author': 'F. Scott Fitzgerald'}
params = {'id': 17}

print db.fetchAll(Books.update(data, params))


Books = TestModel(db)

data = {'title': 'The Great Gatsby!!!', 'primary_author': 'F. Scott Fitzgerald'}
params = {'id': 17}

Books.store(data)

# Commit data
db.session.commit()

data = {'title': 'The Great Gatsby', 'primary_author': 'F. Scott Fitzgerald'}
params = {'id': 17}

print Books.update(data, params)

print Books.delete(params)



put this back:
export PYTHONPATH=******