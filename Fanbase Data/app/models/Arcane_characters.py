from sqlmodel import Field, SQLModel


class Arcane_characters(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    alias: str
    role: str
    city: str
    status: str
    age: int
    voice_actor_id: int = Field(
        foreign_key="arcane_voice_actors.id"
    )


