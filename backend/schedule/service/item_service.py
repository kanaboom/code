from typing import Union
from common.interface.schemas.entity.schedule_entity import ScheduleEntity
from common.interface.schemas.model.schedule_model import ScheduleModel
from common.postgres.query import get_query
from sqlmodel import Session, select, text

def create_item(db: Session):
    try:
        text_query = get_query("./sql/schedule/schedule.sql")
        text_query = str(text_query)
        text_query = text(text_query)
        text_query = text_query.colums(
            ScheduleModel.schedule_id,
            ScheduleModel.title,
            ScheduleModel.start_day,
            ScheduleModel.end_day
        )
        query = select(
            [ScheduleModel]
        ).from_statement(text_query)
        return db.exec(query).all()
    except Exception as e:
        raise e
def update_item():
    try:
        pass
    except Exception as e:
        raise e
    else:
        pass
def read_item():
    try:
        pass
    except Exception as e:
        raise e
    else:
        pass
def delete_item():
    try:
        pass
    except Exception as e:
        raise e
    else:
        pass