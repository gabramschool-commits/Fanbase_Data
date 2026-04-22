from sqlmodel import Field, SQLModel


class Arcane_characters(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str  
    faction: str  
    role: str  
    age: int  
    status: str  
