from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
    inspect,
)
from sqlalchemy.orm import Mapped, relationship

from app.domain import Notice, NoticeImage, NoticeImageType
from .base import Base


class NoticeImageEntity(Base):
    __tablename__ = "t_notice_image"
    __domain__ = NoticeImage

    id = Column(Integer, primary_key=True)
    notice_id = Column(
        Integer, ForeignKey("t_notice.id", ondelete="CASCADE"), nullable=False
    )
    type = Column(
        Enum(NoticeImageType, native_enum=False),
        default=NoticeImageType.IMAGE,
        nullable=False,
        comment="이미지 타입",
    )
    image_url = Column(Text, nullable=False, comment="이미지 URL")
    link = Column(Text, comment="클릭 시 이동할 URL")
    sequence = Column(Integer, default=0, nullable=False, comment="정렬 순서")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    notice = relationship("NoticeEntity", back_populates="images")


class NoticeEntity(Base):
    __tablename__ = "t_notice"
    __domain__ = Notice

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, comment="제목")
    content = Column(Text, comment="내용")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
    images: Mapped[list[NoticeImageEntity]] = relationship(
        back_populates="notice", order_by=NoticeImageEntity.sequence.asc()
    )

    def to_domain(self) -> Notice:
        insp = inspect(self)
        return Notice(
            id=self.id,
            title=self.title,
            content=self.content,
            is_active=self.is_active,
            images=(
                [img.to_domain() for img in self.images]
                if "images" not in insp.unloaded
                else []
            ),
            updated_dtm=self.updated_dtm,
            created_dtm=self.created_dtm,
        )
