# Sample Product CRUD API with Django Rest Framework
Instructions
Clone the git repository \
`cd project_folder` \
Commands \
`python -m venv env` create virtual env \
`.\env\Scripts\activate` activate \
`pip install requirements.txt` install requirements from requirements.txt file \
`python manage.py makemigrations` run migration \
`python manage.py migrate` apply migrations \
`python manage.py createsuperuser` create super user

API URLs \
`/products/add/` add new product \
`/products/list/` product list with pagination \
`/products/{id}/` get product details \
`/products/{id}/update/` product update {patch} \
`/products/{id}/attributes/` get product attributes/variants \
`/products/attributes/{id}/update/` attribute update patch

Add Product JSON Format 
```
{
  "title": "T-Shirt",
  "price": "150.00",
  "currency": "BDT", // default 'BDT'
  "attributes": [
    {
      "type": "Color",
      "name": "Black",
      "price": "100.00"
    },
    {
      "type": "Color",
      "name": "White",
      "price": "150.00"
    }
  ]
}
```