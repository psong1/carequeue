from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    symptoms: Mapped[str] = mapped_column(String(500))
    priority: Mapped[int] = mapped_column(String(20))
    check_in_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())