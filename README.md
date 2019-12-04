# Sample Product CRUD API with Django Rest Framework

API URLs \
`/products/add/` add new product \
`/products/list/` product list with pagination \
`/products/{id}/` get product details \
`/products/{id}/attributes/` get product attributes/variants \

Add Product JSON Format \
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