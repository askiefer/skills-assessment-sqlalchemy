"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter( db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950) ).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').first()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # ex 1960
    year = int(request.args.get("year"))
    cars = db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter(Model.year == year).all()
    for model, brand_name, headquarters in cars:
    	print "Model: {}, Brand: {}, HQ'd: {}".format(model, brand_name, headquarters)
def get_brands_summary():
	"""Printsout each brand name, and each model name for that brand
     using only ONE database query."""
	rows = db.session.query(Brand.name, Model.name).all()
	for brand, model in rows:
		print "\n" + "Brand: {}, Model: {}".format(brand, model)

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
	
	# The datatype is a new Query object with the returned value beign instances of Brands that fit the 
	# given criteria in the query (in this case, we are filtering by the name attribute of Ford. 
	# Because .all(), .first(), or .one() aren't including in the query, the full list of rows 
	# isn't returned to us.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

	# An association table manages many to many relationships by creating two one to many relationships.
	# It is sometimes referred to as a hidden table whose only purpose is to connect two tables.
	# In this schema, all 3 tables have primary keys. The primary keys of the other two tables 
	# become foreign keys in the association table.

# -------------------------------------------------------------------
# Part 3

# ex mystr = "Tes" -> list of Tesla objects
# mystr = "Tes Bu BM Cad" -> Does this have to return a list of all Tesla, Buick, BMW, and Cadillac objects?
# If that was the intended case, this could get super granular, for example mystr = "T B C" would return 
# Tesla, Cadillac, Buick, among others, as these brands contain the input string, which in this case 
# is just letters 

def search_brands_by_name(mystr):
	"""Returns a list of objects whose name contains or is equal to the input string."""
	word_list = mystr.split(" ")
	for word in word_list:
		Brand.query.filter(Brand.name.like('%'+word+'%')).all()

# (1960, 1980)
def get_models_between(start_year, end_year):
	int(start_year)
	int(end_year)
	Model.query.filter(Model.year >= start_year, Model.year <= end_year).all()

