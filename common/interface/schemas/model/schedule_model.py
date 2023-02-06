from datetime import datetime

from sqlmodel import Field, SQLModel

class ScheduleModel(SQLModel, table=True):

    __tablename__: str = "schedule"
    __table_args__ = {'extend_exisiting' : True}

    schedule_id: str = Field(description="スケジュールID", primary_key=True)
    title: str = Field(description="スケジュールタイトル")
    start_day: str = Field(description="開始日")
    end_day: str = Field(description="終了日")