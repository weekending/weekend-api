from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
)

from app.domain import Post, PostCategory
from .base import Base


class PostCategoryEntity(Base):
    __tablename__ = "t_post_category"
    __domain__ = PostCategory

    id = Column(Integer, primary_key=True)
    name = Column(String(20), comment="카테고리명", nullable=False)
    code = Column(String(10), comment="코드", nullable=False)
    allow_anonymous = Column(
        Boolean, default=False, nullable=False, comment="비회원 작성 가능 여부"
    )
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")


class PostEntity(Base):
    __tablename__ = "t_post"
    __domain__ = Post

    id = Column(Integer, primary_key=True)
    category_id = Column(
        Integer,
        ForeignKey("t_post_category.id", ondelete="CASCADE"),
        nullable=False,
    )
    user_id = Column(
        Integer, ForeignKey("t_user.id", ondelete="CASCADE"), nullable=True
    )
    title = Column(String(50), comment="제목", nullable=False)
    content = Column(Text, comment="내용")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
