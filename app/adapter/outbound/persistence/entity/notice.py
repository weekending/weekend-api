from sqlalchemy import Boolean, Column, Integer, String, Text

from app.domain import Notice
from .base import Base


class NoticeEntity(Base):
    __tablename__ = "t_notice"
    __domain__ = Notice

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, comment="제목")
    content = Column(Text, comment="내용")
    is_active = Column(Boolean, default=True, nullable=False, comment="활성화 여부")
