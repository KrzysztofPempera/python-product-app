from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column as BaseColumn

Base = declarative_base()

class Column(BaseColumn):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('nullable', False)
        super().__init__(*args, **kwargs)