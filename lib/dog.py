from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models import Base, Dog

def create_table(Base,engine):
    # engine = create_engine('sqlite:///dogs.db', echo=True)
    Base.metadata.create_all(engine)
    # return engine  

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

# Example usage
# engine = create_engine('sqlite:///dogs.db', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

# create_table(Base)

# Now you can use other functions like save(), get_all(), etc.

