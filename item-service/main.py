from typing import List
import fastapi
import uvicorn
from fastapi import HTTPException
from pydantic import BaseModel

api = fastapi.FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    views: int
    is_sold: bool

items =[
    {
        'name': 'item 1',
        'description': 'item 1 desc',
        'price': 1,
        'views': 1,
        'is_sold': False,
    },
    {
        'name': 'item 2',
        'description': 'item 2 desc',
        'price': 2,
        'views': 2,
        'is_sold': False,
    },
    {
        'name': 'item 3',
        'description': 'item 3 desc',
        'price': 3,
        'views': 3,
        'is_sold': False,
    },
]

@api.get('/items', response_model = List[Item])
async def get_items():
    return items


@api.post('/items/', status_code=201)
async def add_item(new_item: Item):
    item = new_item.dict()
    items.append(item)
    return {'id': len(items) -1}


@api.put('/items/{id}')
async def update_item(id: int, updated_item: Item):
    item = updated_item.dict();
    items_len = len(items)
    if 0 <= id <= items_len:
        items[id] = item
        return None
    raise HTTPException(status_code=404, detail='Item with give id does not exists')

uvicorn.run(api, host="127.0.0.1", port=8000)
