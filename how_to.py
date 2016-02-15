from serializable import Serializable

"""To create a class you only need to specify its params"""
class Photo(Serializable):
	params = [
		('service_id', str), 
		('id', int), 
		('tags', list), 
		('title', str)
	]

"""Main"""

"""Instantiate an object"""
photo = Photo(
	service_id='flickr', 
	id=12131, 
	tags=['#happy', '#smile'], 
	title="Happiness"
)

print(photo.json_me())
print(photo.service_id)


"""Instantiate an object"""
params = {
	'service_id': 'flickr', 
	'id': 12131, 
	'tags': ['#happy', '#smile'], 
	'title': 'Happiness'
}

photo = Photo(**params)

print(photo.json_me())
print(photo.service_id)



