# Python object serializer
Python serializer class (can be extended by other classes)

Thanks to the Serializable class, each object can be serializable. I created it because I like saving my objects in key -> value storage systems.
In this way, you can create a class that extends this one in order to obtain a serializable object.

##Define a serializable object

To define a new serializable object you only need to specify its params and extend the Serializable object. Params can be a list of strings or a list of tuples **(param_name, type)**.

```
from serializable import Serializable

class Photo(Serializable):
	params = [
		('service_id', str), 
		('id', int), 
		('tags', list), 
		('title', str)
	]
```

##Instantiate and serialize an object
Create a new object is simple. After you created its instance, you can save it into the database as text using the ***json_me()*** method. You can recreate the same object from text using its constructor. 

This is an example:

```
from serializable import Serializable
from ... import Photo

photo = Photo(
	service_id='flickr', 
	id=12131, 
	tags=['#happy', '#smile'], 
	title="Happiness"
)

exported_json = photo.json_me()
#exported_json = '{"tags": ["#happy", "#smile"], "id": 12131, "service_id": "flickr", "title": "Happiness"}'
```

##Deserialize - instantiate an object from the exported text

```
import json
from ... import Photo

exported_json = '{"tags": ["#happy", "#smile"], "id": 12131, "service_id": "flickr", "title": "Happiness"}'
params = json.loads(exported_json)

photo = Photo(**params)
```

##Attributes
You can easily access the object attributes

```
from ... import Photo

photo = Photo(
	service_id='flickr', 
	id=12131, 
	tags=['#happy', '#smile'], 
	title="Happiness"
)

print(photo.service_id)
```
