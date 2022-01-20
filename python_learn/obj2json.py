import json
from typing import ValuesView
import jsonschema

class People():
    def __init__(self, name, age, pet):
        self.name = name
        self.age = age
        self.pet = pet
class Pet():
    def __init__(self, pet_type, pet_name):
        self.pet_type = pet_type
        self.pet_name = pet_name
        self.test = None

def pet2json():
    pet = Pet('Cat', 'Lili')
    js = json.dumps(pet.__dict__)
    print(js)

json_data = {
  "productId": '1',
  "productName": "A green door",
  "price": 12.50,
  "tags": [ "home", "green" ]
}

json_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/product.schema.json",
  "title": "Product",
  "description": "A product from Acme's catalog",
  "type": "object",
  "properties": {
    "productId": {
      "description": "The unique identifier for a product",
      "type": "integer"
    },
    "productName": {
      "description": "Name of the product",
      "type": "string"
    },
    "price": {
      "description": "The price of the product",
      "type": "number",
      "exclusiveMinimum": 0
    },
    "tags": {
      "description": "Tags for the product",
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "uniqueItems": True
    },
    "dimensions": {
      "type": "object",
      "properties": {
        "length": {
          "type": "number"
        },
        "width": {
          "type": "number"
        },
        "height": {
          "type": "number"
        }
      },
      "required": [ "length", "width", "height" ]
    },
    "warehouseLocation": {
      "description": "Coordinates of the warehouse where the product is located.",
      "$ref": "https://example.com/geographical-location.schema.json"
    }
  },
  "required": [ "productId", "productName", "price" ]
}

# try: 
#     jsonschema.validate(json_data, json_schema)
#     print("test")
# except jsonschema.ValidationError as ex:
#     msg = ex
#     print(ex)



file_check_submit_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/product.schema.json",
  "title": "file_check_submit",
  "description": "file check submit",
  "required": [ "task_id", "data_id", "data_type", "data_url", "data_source_type"],
  "type": "object",
  "properties": {
    "task_id": {
      "description": "任务ID",
      "type": "string"
    },
    "data_id": {
      "description": "资源标识符",
      "type": "integer"
    },
    "data_type": {
      "description": "资源类型,枚举类型,",
      "type": "integer",
      "enum": [0, 1, 2, 3, 4, 5, 6, 7, 8]
    },
    "data_url": {
      "description": "资源路径,文件路径,不包括文件夹",
      "type": "string",
    },
    "srt_url": {
      "description": "外挂字幕路径,当data_type为2  字幕和视频混合格式 srt+video时,这个字段为必须",
      "type": "string",
    },
    "data_source_type": {
      "description": "数据来源,枚举类型,",
      "type": "integer",
      "enum": [0, 1, 2, 3, 4, 5]
    },
  },

}

file_check_submit_json = {
    "task_id": "1",
    "data_id": 1,
    "data_type": 7,
    "data_url": "/root/",
    "data_source_type": 1
}

try: 
    jsonschema.validate(file_check_submit_json, file_check_submit_schema)
    print("test")
except jsonschema.ValidationError as ex:
    msg = ex
    print(ex)