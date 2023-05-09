from databases import Database

from friendship.settings import settings

database = Database(str(settings.db_url))
