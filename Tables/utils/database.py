import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError


class Database:
    def __init__(self, db_conn_url):
        """Create instance of class to be used when defining tables"""
        # tell SQLAlchemy how you'll define tables and models
        self.Base = declarative_base()
        # connect database
        self.engine = sqlalchemy.create_engine(db_conn_url)
        # create session factory
        self.sessionmaker = sqlalchemy.orm.sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        # set up scoped_session registry
        # #add ability to access scoped session registry (implicitly)
        self.session = self.init_scoped_session()

    def create_table(self):
        """Create mapped tables in the database"""

        # make sure db is initialize and up to date
        self.Base.metadata.create_all(bind=self.engine)

    def init_scoped_session(self):
        """Create empty scoped session registry upon app startup"""
        return sqlalchemy.orm.scoped_session(
            self.sessionmaker
        )

    def insert(self, obj):
        """Adds table object to the database"""
        try:
            self.session.add(obj)
            self.session.commit()
            self.session.remove()

        except IntegrityError as err:
            self.session.rollback()
            print(err)
