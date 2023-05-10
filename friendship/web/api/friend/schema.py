from pydantic import BaseModel
from typing import Optional
import datetime

class FriendModelDTO(BaseModel):
    """
    DTO for Friend models.

    It is returned when accessing Friend models from the API.
    """

    id: int
    name: str
    last_contacted: Optional[datetime.date]
    category: Optional[int]
    friendship_score: int

    class Config:
        orm_mode = True


class FriendModelInputDTO(BaseModel):
    """DTO for creating new Friend model."""

    name: str
    last_contacted: Optional[datetime.date]
    category: Optional[int]
    friendship_score: int = 0