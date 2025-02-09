from app.models import User


class UserService:
    async def get_user_info(self, user_id: int) -> dict:
        user = await User.find_one(User.id == user_id)
        return user.to_dict()
