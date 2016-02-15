from serializable import Serializable
import json

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

exported_json = photo.json_me()
print(exported_json)
print(photo.service_id)


"""
Instantiate an object from exported text
exported_json = '{"tags": ["#happy", "#smile"], "id": 12131, "service_id": "flickr", "title": "Happiness"}'
"""
params = json.loads(exported_json)
photo = Photo(**params)

print(photo.json_me())
print(photo.service_id)