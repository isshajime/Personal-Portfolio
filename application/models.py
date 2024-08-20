from flask_sqlalchemy import SQLAlchemy
# from flask import current_app as app
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from datetime import datetime
from . import db

class Base(DeclarativeBase):
  pass

# db = SQLAlchemy()


class Quote(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    quote: Mapped[str] = mapped_column(String(500), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)

    def __init__(self, date, quote, author):
       self.date = date
       self.quote = quote
       self.author = author

    def save_to_db(self):
       db.session.add(self)
       db.session.commit()

    def read_db(self):
        today_quote = db.session.execute(db.select(self).where(self.date == today_date)).scalar()
        return today_quote



