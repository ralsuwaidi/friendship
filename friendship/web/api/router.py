from fastapi.routing import APIRouter

from friendship.web.api import dummy, echo, monitoring, friend

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
api_router.include_router(friend.router, prefix="/friends", tags=["friends"])
