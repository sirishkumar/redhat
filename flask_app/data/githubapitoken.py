from datetime import datetime

import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase


class GithubAPIToken(SqlAlchemyBase):
    __tablename__ = 'githubapitokens'

    id = sa.Column(sa.String(30), primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.now)
    server = sa.Column(sa.String(40), default="http://github.com")
    hashed_token = sa.Column(sa.String(60), nullable=False)
    email = sa.Column(sa.String(60), unique=True, nullable=True)

    def __repr__(self):
        return '<GithubAPIToken {}>'.format(self.id)
