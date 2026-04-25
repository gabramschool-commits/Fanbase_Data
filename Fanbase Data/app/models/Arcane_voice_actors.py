from sqlmodel import Field, SQLModel


class Arcane_voice_actors(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    nationality: str
    age: int
    known_for: str