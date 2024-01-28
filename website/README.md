# Info

This will be a dummy async REST API with a couple of static dummy webpages:
- index
- about

index page will show total number of API requests. The information will be stored in a postrgres DB.
about page will be just a static page.

There will be a couple of REST API endpoints:
- /rand
- /requests

/rand will return a 15-character long random base64 string.
/requests will return a total number of API requests.

# Tech stack
- python 3.12
- Fast API 0.109.0
- uvicorn 0.27.0
