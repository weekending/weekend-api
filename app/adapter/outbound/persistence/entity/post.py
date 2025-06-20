from datetime import timezone

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    Text,
    inspect,
)
from sqlalchemy.orm import relationship
from zoneinfo import ZoneInfo

from app.core.settings import get_settings
from app.domain import Post, PostCategory, PostComment
from .base import Base
from .user import UserEntity


settings = get_settings()
kst = ZoneInfo(settings.TIMEZONE)


class PostCategoryEntity(Base):
    __tablename__ = "t_post_category"
    __domain__ = PostCategory

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, comment="카테고리명")
    code = Column(String(10), unique=True, nullable=False, comment="코드")
    allow_anonymous = Column(
        Boolean, default=False, nullable=False, comment="비회원 작성 가능 여부"
    )
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    sequence = Column(Integer, nullable=False, comment="순번")


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
    title = Column(String(50), nullable=False, comment="제목")
    content = Column(Text, comment="내용")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    category = relationship(PostCategoryEntity, lazy="joined")
    user = relationship(UserEntity, lazy="joined")

    @classmethod
    def from_domain(cls, post: Post) -> "PostEntity":
        return cls(
            id=post.id,
            category_id=post.category_id,
            user_id=post.user_id,
            title=post.title,
            content=post.content,
            is_active=post.is_active,
            created_dtm=post.created_dtm,
        )

    def to_domain(self, **kwargs) -> Post:
        insp = inspect(self)
        category_loaded = "category" not in insp.unloaded
        user_loaded = "user" not in insp.unloaded
        return Post(
            id=self.id,
            category_id=self.category_id,
            user_id=self.user_id,
            title=self.title,
            content=self.content,
            is_active=self.is_active,
            comment_count=kwargs.get("comment_count", 0),
            updated_dtm=self.updated_dtm,
            created_dtm=self.created_dtm.replace(tzinfo=timezone.utc).astimezone(kst),
            category=self.category.to_domain() if category_loaded else None,
            user=self.user.to_domain() if user_loaded and self.user else None,
        )


class PostCommentEntity(Base):
    __tablename__ = "t_post_comment"
    __domain__ = PostComment

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer, ForeignKey("t_user.id", ondelete="SET NULL"), nullable=True
    )
    post_id = Column(
        Integer, ForeignKey("t_post.id", ondelete="CASCADE"), nullable=False
    )
    parent_id = Column(
        Integer, ForeignKey("t_post_comment.id", ondelete="SET NULL"), nullable=True
    )
    level = Column(SmallInteger, comment="댓글 본문")
    content = Column(String(255), comment="댓글 본문")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    user = relationship(UserEntity, lazy="joined")
