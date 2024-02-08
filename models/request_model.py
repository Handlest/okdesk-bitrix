from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy import Column, String, Integer, Date

from config import Base


class RatingRequest(Base):
    __tablename__ = "rating_request"
    id = Column(Integer, primary_key=True, nullable=False, index=True, unique=True, autoincrement=True)
    issue_id = Column(Integer, nullable=False)
    author_id = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    closed_at = Column(Date, comment='Дата перехода состояния заявки в "закрыта"')


RatingRequest_Pydantic = sqlalchemy_to_pydantic(RatingRequest)