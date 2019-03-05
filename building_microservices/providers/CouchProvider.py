import requests
product = {
  "myapplication": [
    {
      "version": "1.0",
      "description": "pre-interview technical test",
      "lastcommitsha": "abc57858585"
    }
  ]
        }

class CouchProvider(object):
    
    def read_product(self) -> str:
        return product,200
        
        