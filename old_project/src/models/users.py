from sqlalchemy import Column, Integer, String, TIMESTAMP
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50),unique=True)
    fullname = Column(String(50),nullable=False)
    email = Column(String(120), unique=True,nullable=False)
    password = Column(String(50),nullable=False)
    created_on = Column(TIMESTAMP)

    def __init__(self, name, fullname, email,password,created_on=None):
        self.name = name
        self.fullname = fullname
        self.password = password
        self.email = email
	self.created_on = created_on or datetime.now()

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.name, self.fullname, self.email, self.password)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
