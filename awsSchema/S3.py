# AUTOGENERATED! DO NOT EDIT! File to edit: S3.ipynb (unless otherwise specified).

__all__ = ['S3Event']

# Cell
from dataclasses import field
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, Undefined

# Cell
@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class S3Event:
  '''
    parse event from apigateway
  '''
  body: str
  headers: dict = field(default_factory = dict)
  statusCode: int = 200
  def getBody(self):
    return json.loads(self.body)
  def getProducts(self):
    return Products.from_json(self.body)
  def getKey(self, key='product'):
    return body.get(key)
  key = lambda self: json.loads(self.body)['key']
  firstKey = lambda self: next(iter(json.loads(self.body).items()))
  @classmethod
  def getKeyObject(cls, event):
    s3Event = event['Records'][0]
    bucket = s3Event['s3']['bucket']['name']
    key = s3Event['s3']['object']['key']
    return bucket, key