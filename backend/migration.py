from sqlalchemy import create_engine
from models.users import Base as users_base
from models.events import Base as event_base
# from models.tickets import Base as tickets_base


DATABASE_URL = "sqlite:///db.db"
engine = create_engine(DATABASE_URL)
users_base.metadata.create_all(bind=engine)
event_base.metadata.create_all(bind=engine)
