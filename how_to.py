from serializable import Serializable

class Photo(Serializable):
	params = [
		('service_id', str), 
		('id', int), 
		('tags', list), 
		('title', str)
	]

photo = Photo(
	service_id='flickr', 
	id=12131, 
	tags=['#happy', '#smile'], 
	title="Happiness"
)

print(photo.json_me())
print(photo.service_id)

params = {
	'service_id': 'flickr', 
	'id': 12131, 
	'tags': ['#happy', '#smile'], 
	'title': 'Happiness'
}

photo = Photo(**params)

print(photo.json_me())
print(photo.service_id)



