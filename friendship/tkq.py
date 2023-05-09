import taskiq_fastapi
from taskiq import InMemoryBroker, ZeroMQBroker

from friendship.settings import settings

broker = ZeroMQBroker()

if settings.environment.lower() == "pytest":
    broker = InMemoryBroker()

taskiq_fastapi.init(
    broker,
    "friendship.web.application:get_app",
)
