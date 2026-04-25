from fastapi import APIRouter, HTTPException , status
from app.models.Arcane_characters import Arcane_characters
from sqlmodel import Session, select

router = APIRouter(prefix="/Arcane_characters", tags=["Arcane_characters"])
from ..database import engine

@router.get("/", summary="Get all Arcane_characters")
async def get_all():
    with Session(engine) as session:
        statement = select(Arcane_characters)
        results = session.exec(statement).all()
        return results



@router.post("/", summary="Create a new Arcane_characters", status_code=status.HTTP_201_CREATED)
async def create_item(_Arcane_characters : Arcane_characters):
    with Session(engine) as session:
        session.add(_Arcane_characters)
        session.commit()
        session.refresh(_Arcane_characters)
        return _Arcane_characters


@router.get("/{item_id}", summary="Get Arcane_characters by ID")
async def get_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Arcane_characters, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Arcane_characters not found")
        return item



@router.put("/{item_id}", summary="Update Arcane_characters")
async def update_item(_Arcane_characters : Arcane_characters , item_id: int):
    with Session(engine) as session:

        item = session.get(Arcane_characters, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Arcane_characters not found")

        for key, value in _Arcane_characters.model_dump(exclude_unset=True).items():
            setattr(item, key, value)

        session.add(item)
        session.commit()
        session.refresh(item)
        return item


@router.delete("/{item_id}", summary="Delete Arcane_characters" ,status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):

    with Session(engine) as session:
        item = session.get(Arcane_characters, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Arcane_characters not found")

        session.delete(item)
        session.commit()
        return None
