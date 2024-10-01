import datetime

from fastapi_users_db_sqlalchemy.generics import now_utc, TIMESTAMPAware
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class DateAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMPAware(timezone=True), index=True, nullable=False, default=now_utc
    )
    update_at: Mapped[datetime] = mapped_column(
        TIMESTAMPAware(timezone=True), index=True, nullable=False, default=now_utc
    )