print ("Vimeo Test")

import pycurl
import vimeo

v = vimeo.VimeoClient(
    token='0d36c7b02cc04383dac4aa1d4b47f4a5',
    key='c2287350d907bd6a00b62b68d3929039ed74e900',
    secret='tXhQtZsx+aWCV9AalD5xBe4/PUf6Y5EW5GhoDIBwBMJ0tl+6oVxm1sVuuywQnxV8UaGUT6dkSE+R7QMF6ptPZGXzHis5oqm9AjJ1+sirCFeuyu78otPK6NkWfSGiFrr4'
)

# Make the request to the server for the "/me" endpoint.
data = v.get('https://api.vimeo.com/users/3004813')

# Make sure we got back a successful response.
print (data.status_code)
assert data.status_code == 200

# Load the body's JSON data.
print (data.json())


