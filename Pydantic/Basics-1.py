from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime|None
    tastes: dict[str,PositiveInt]

# external_data = {
#     'id': 123,
#     'signup_ts': '2019-06-01 12:22',
#     'tastes': {
#         'wine': 9,
#         b'chinese': 7,
#         'cabbage': '1',
#     }
# }

external_data = {'id': 'not an int', 'tastes': {}} 
try:
    user = User(**external_data)
    print(user.id)
    print(user.model_dump)
except ValidationError as e:
    print(e.errors())

