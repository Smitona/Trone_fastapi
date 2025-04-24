from datetime import datetime as dt
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class ThroneRequest(Base):
    __tablename__ = 'throne_requests'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    address: Mapped[str] = mapped_column(unique=True)
    data_time: Mapped[dt] = mapped_column(default=dt.now, onupdate=dt.now)


class Wallet(Base):
    __tablename__ = 'wallets'

    balance: Mapped[float] = mapped_column(default=0.00)
    energy: Mapped[str]