from sqlalchemy import select
from app.models.reader import Reader
from app.db import Session

def check_if_id_duplicated(card_id:str):
    hashed_card_id = Reader.set_card_id(card_id)

    with Session() as session:
        stmt = select(Reader).where(Reader.card_id_hash == hashed_card_id)
        reader = session.execute(stmt).scalar_one_or_none()

        if reader is None:
            return False
        else:
            return True