from fastapi import APIRouter, HTTPException , status
from app.models.Arcane_voice_actors import Arcane_voice_actors
from sqlmodel import Session, select

router = APIRouter(prefix="/Arcane_voice_actors", tags=["Arcane_voice_actors"])
from ..database import engine

@router.get("/", summary="Get all Arcane_voice_actors")
async def get_all():
    with Session(engine) as session:
        statement = select(Arcane_voice_actors)
        results = session.exec(statement).all()
        return results



@router.post("/", summary="Create a new Arcane_voice_actors", status_code=status.HTTP_201_CREATED)
async def create_item(_Arcane_voice_actors : Arcane_voice_actors):
    with Session(engine) as session:
        session.add(_Arcane_voice_actors)
        session.commit()
        session.refresh(_Arcane_voice_actors)
        return _Arcane_voice_actors


@router.get("/{item_id}", summary="Get Arcane_voice_actors by ID")
async def get_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Arcane_voice_actors, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Arcane_voice_actors not found")
        return item



@router.put("/{item_id}", summary="Update Arcane_voice_actors")
async def update_item(_Arcane_voice_actors : Arcane_voice_actors , item_id: int):
    with Session(engine) as session:

        item = session.get(Arcane_voice_actors, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Arcane_voice_actors not found")

        for key, value in _Arcane_voice_actors.model_dump(exclude_unset=True).items():
            setattr(item, key, value)

        session.add(item)
        session.commit()
        session.refresh(item)
        return item


@router.delete("/{item_id}", summary="Delete Arcane_voice_actors" ,status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):

    with Session(engine) as session:
        item = session.get(Arcane_voice_actors, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Arcane_voice_actors not found")

        session.delete(item)
        session.commit()
        return None
