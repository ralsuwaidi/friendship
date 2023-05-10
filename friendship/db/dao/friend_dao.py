from typing import List, Optional
from friendship.db.models.friend import FriendModel
import datetime


class FriendDAO:
    """Class for accessing friend table."""

    async def create_friend(
        self,
        name: str,
        last_contacted: Optional[datetime.date],
        category: Optional[int],
        friendship_score: int = 0,
    ) -> None:
        """
        Add single friend to session.

        :param name: name of a friend.
        :param last_contacted: date and time of last communication with friend.
        :param category: id of the friend's category.
        :param friendship_score: current friendship score for the friend.
        """
        await FriendModel.objects.create(
            name=name,
            last_contacted=last_contacted,
            category=category,
            friendship_score=friendship_score,
        )

    async def get_all_friends(
        self,
        limit: int,
        offset: int,
    ) -> List[FriendModel]:
        """
        Get all friend models with limit/offset pagination.

        :param limit: limit of friends.
        :param offset: offset of friends.
        :return: stream of friends.
        """
        return await FriendModel.objects.limit(limit).offset(offset).all()

    async def filter_friends(
        self,
        name: Optional[str] = None,
        category: Optional[int] = None,
        last_contacted: Optional[datetime.date] = None,
    ) -> List[FriendModel]:
        """
        Get specific friends based on given filters.

        :param name: name of the friend.
        :param category: id of the friend's category.
        :param last_contacted: date and time of last communication with friend.
        :return: list of filtered friends.
        """
        query = FriendModel.objects

        if name:
            query = query.filter(FriendModel.name == name)

        if category:
            query = query.filter(FriendModel.category == category)

        if last_contacted:
            query = query.filter(FriendModel.last_contacted == last_contacted)

        return await query.all()