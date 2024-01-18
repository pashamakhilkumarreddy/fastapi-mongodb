from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass


@dataclass
class User(BaseModel):
    name: str = Field(min_length=1, max_length=21)
    profession: str = Field(min_length=1, max_length=30)
    phone: str
    image: str = ''
    image_url: str
    created_at: str = datetime.now()
    update_at: str = datetime.now()
    is_active: Optional[bool] = False

    def toJson(self):
        user = {
            'name': self.name,
            'profession': self.profession,
            'phone': self.phone,
            'image_url': self.image_url,
            'is_active': self.is_active,
        }
        return user
