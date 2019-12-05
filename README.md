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
`/products/` {{POST}} add new product \
`/products/` {{GET}} product list with pagination \
`/products/{id}/` {{GET}} {{DELETE}} {{PATCH}} {{UPDATE}} get product details \
`/product/{p_id}/attributes/` {{GET}} get single product attributes/variants \
`/product/{p_id}/attributes/{a_id}/` {{GET}} get single product single attribute/variant, {{DELETE}} {{PATCH}} {{UPDATE}} \

`filters enabled` you can filters and search. For attributes you can filter with `price_lt` and `price_gt`

Add Product JSON Format `{{POST}} => Create`
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