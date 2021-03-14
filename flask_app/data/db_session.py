import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
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
    SqlAlchemyBase.metadata.create_all(engine)


def global_init_mysql():
    global __factory

    if __factory:
        return

    conn_str = "mysql+pymysql://{0}:{1}@db:3306/userdb".format("root", "root")
    engine = sa.create_engine(conn_str, echo=True)
    engine.execute("CREATE DATABASE IF NOT EXISTS userdb")
    engine.execute("USE userdb")


    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    from data.githubapitoken import GithubAPIToken
    SqlAlchemyBase.metadata.create_all(engine)

def create_session() -> Session:
    global __factory
    return __factory()

