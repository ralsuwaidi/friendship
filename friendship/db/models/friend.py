import ormar
from typing import Optional
import datetime

from friendship.db.base import BaseMeta
from friendship.db.models.category import Category

class FriendModel(ormar.Model):
    """Model for demo purpose."""

    class Meta(BaseMeta):
        tablename = "friend"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=200)  # noqa: WPS432
    last_contacted: Optional[datetime.date] = ormar.Date()
    category: Optional[Category] = ormar.ForeignKey(Category)
    friendship_score = ormar.Integer(minimum=0, maximum=100)