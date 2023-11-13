from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column as BaseColumn

class Base(DeclarativeBase):
    pass

class Column(BaseColumn):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('nullable', False)
        super().__init__(*args, **kwargs)