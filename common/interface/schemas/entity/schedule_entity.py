from typing import Optional

from pydantic import BaseModel, Field

class ScheduleEntity(BaseModel):
    schedule_id: Optional[str] = Field(description="スケジュールID", example="123456789")
    title: Optional[str] = Field(description="スケジュールタイトル", example="商談")
    start_day: Optional[str] = Field(description="開始日", example="yyyymmdd")
    end_day: Optional[str] = Field(description="終了日", example="yyyymmdd")

    class Config:
        orm_mode = True