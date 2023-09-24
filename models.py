import atexit

from sqlalchemy import Column, DateTime, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DSN = 'postgresql://postgres:postgres@localhost:5432/app'
engine = create_engine(DSN)
atexit.register(engine.dispose)

Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


class Advertising(Base):
    __tablename__ = "app_advertising"

    id = Column(Integer, primary_key=True)
    header = Column(String, nullable=False)
    description = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    owner = Column(String, nullable=False)

Base.metadata.create_all()
