from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from friendship.db.dao.friend_dao import FriendDAO
from friendship.web.api.friend.schema import FriendModelDTO, FriendModelInputDTO

router = APIRouter()


@router.get("/", response_model=List[FriendModelDTO])
async def get_friends(
    limit: int = 10,
    offset: int = 0,
    friend_dao: FriendDAO = Depends(),
) -> List[FriendModelDTO]:
    """
    Retrieve all friend objects from the database.

    :param limit: limit of friend objects, defaults to 10.
    :param offset: offset of friend objects, defaults to 0.
    :param friend_dao: DAO for friend models.
    :return: list of friend objects from database.
    """
    friends = await friend_dao.get_all_friends(limit=limit, offset=offset)
    return [FriendModelDTO.from_orm(friend) for friend in friends]


@router.post("/")
async def create_friend(
    new_friend_object: FriendModelInputDTO,
    friend_dao: FriendDAO = Depends(),
) -> None:
    """
    Creates friend model in the database.

    :param new_friend_object: new friend model item.
    :param friend_dao: DAO for friend models.
    """
    await friend_dao.create_friend(**new_friend_object.dict())
