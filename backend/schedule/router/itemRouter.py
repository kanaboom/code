import backend.schedule.service.item_service as service
from fastapi import APIRouter
from common.postgres import postgres
from sqlmodel import Session

router = APIRouter()

# routerはURLの定義とサービスの呼び出しを行う。必要があればバリデーションチェックも行う
@router.get("/item")
async def list_tasks():
    db: Session = Depends(postgres.get_db)

    return service.read_item()


@router.post("/item")
async def create_task():
    pass


@router.put("/item/{item_id}")
async def update_task():
    pass


@router.delete("/item{item_id}")
async def delete_task():
    pass