from ormar import ModelMeta

from friendship.db.config import database
from friendship.db.meta import meta


class BaseMeta(ModelMeta):
    """Base metadata for models."""

    database = database
    metadata = meta
