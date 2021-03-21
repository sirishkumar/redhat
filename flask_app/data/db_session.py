import logging
import os

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database
from data.modelbase import SqlAlchemyBase

__factory = None


def global_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file")

    conn_str = 'sqlite:///' + db_file.strip()
    engine = sa.create_engine(conn_str, echo=True)
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    from data.githubapitoken import GithubAPIToken
    SqlAlchemyBase.metadata.create_all(engie)


def global_init_mysql():
    global __factory

    if __factory:
        return

    db_conn = os.environ.get("DB_SERVICE")
    #conn_str = "mysql+pymysql://{0}:{1}@{2}/userdb".format("root", "root", db_conn)
    conn_str = 'postgresql://{0}:{1}@{2}/userdb'.format('postgres', 'postgres', db_conn)
    logging.info(f"connection string {conn_str}")
    engine = sa.create_engine(conn_str, echo=True)

    if not database_exists(engine.url):
        create_database(engine.url)

    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    from data.githubapitoken import GithubAPIToken
    SqlAlchemyBase.metadata.create_all(engine)

def create_session() -> Session:
    global __factory
    return __factory()

