import ormar

from friendship.db.base import BaseMeta


class Category(ormar.Model):
    """Model for demo purpose."""

    class Meta(BaseMeta):
        tablename = "category"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=200)  # noqa: WPS432
    reminder_frequency: int = ormar.Integer(minimum=1, maximum=365)  # noqa: WPS432
