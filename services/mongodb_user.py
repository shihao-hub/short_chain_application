from typing import List

from bson import ObjectId

from models.mongodb_model import User, ShortUrl


class UserService:
    @staticmethod
    def get_user(user_id: str) -> User:
        return User.objects.get(id=ObjectId(user_id))

    @staticmethod
    def get_user_by_name(name: str) -> User:
        return User.objects.filter(username=name).first()

    @staticmethod
    def get_users() -> List[User]:
        return User.objects.all()

    @staticmethod
    def create_user(**kwargs) -> User:
        user = User(**kwargs)
        user.save()
        return user

    @staticmethod
    def update_user(user_id: str, **kwargs):
        User.objects.filter(id=ObjectId(user_id)).update_one(**kwargs)

    @staticmethod
    def delete_user(user_id: str):
        User.objects.filter(id=ObjectId(user_id)).delete()
