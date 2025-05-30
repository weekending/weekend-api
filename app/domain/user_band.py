from enum import Enum

from pydantic import BaseModel

from .user import User


class MemberType(Enum):
    LEADER = "LEADER"
    NORMAL = "NORMAL"

    def is_leader(self) -> bool:
        return self == self.LEADER


class UserBand(BaseModel):
    id: int = None
    user_id: int
    band_id: int
    member_type: MemberType
    user: User | None
