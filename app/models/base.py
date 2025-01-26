from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_base

from app.core.database.mixin import ModelMixin

_Base = declarative_base()


class BaseModel(_Base, ModelMixin):
    __abstract__ = True

    updated_dtm = Column(DateTime, comment="수정 일시")
    created_dtm = Column(
        DateTime, comment="생성 일시", nullable=False, default=datetime.now
    )
