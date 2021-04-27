from src.infra.config import DBConnectionHandler
from src.infra.entities import Users

# pylint: disable=E1101


class FakerRepo:
    """A simple Repository """

    def insert_user(cls):
        """ something """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Dev Back", password="lhamar")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
