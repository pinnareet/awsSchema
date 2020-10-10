# AUTOGENERATED! DO NOT EDIT! File to edit: apigateway.ipynb (unless otherwise specified).

__all__ = ['Response', 'Event', 'Product', 'Products']

# Cell
from dataclasses import field
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, Undefined
from pprint import pformat
from typing import Optional, List, Callable, Any
import ujson as json

@dataclass_json
@dataclass
class Response:
  '''
    parse response from apigateway
  '''
  body: str
  statusCode: int = 200
  header: dict = field(default_factory = dict)
  @classmethod
  def fromDict(cls, dictInput:dict):
    '''
      output object from Dict,
      dictInput should follow apigateway proxy integration
    '''
    body = dictInput.pop('body')
    return cls(
      body = json.loads(body),
      **dictInput
    )
  @classmethod
  def getReturn(cls, body:dict, header:dict = {}, statusCode:int = 200)->dict:
    '''
      output dictionary which is suitable for apigateway proxy integration return
    '''
    returnObj = cls(
      body = json.dumps(body),
      header = header,
      statusCode = statusCode
                   ).to_dict()
    return returnObj
@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Event:
  '''
    parse event from apigateway
  '''
  def __repr__(self):
    return pformat({
      'header': self.header,
      'body': self.getBody()
           })
  body: str
  header: dict = field(default_factory = dict)
  def getBody(self):
    return json.loads(self.body)
  def getProducts(self):
    return Products.from_json(self.body)
  def getKey(self, key='product'):
    return body.get(key)
  key = lambda self: json.loads(self.body)['key']
  firstKey = lambda self: next(iter(json.loads(self.body).items()))
@dataclass_json
@dataclass
class Product:
  cprcode: str
  iprcode: str
  oprcode: str
  ordertype: str
  pr_abb: str
@dataclass_json
@dataclass
class Products:
  products: List[Product]