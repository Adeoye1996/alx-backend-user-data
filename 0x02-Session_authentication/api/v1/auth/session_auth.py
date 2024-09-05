<<<<<<< HEAD

#!/usr/bin/env python3
"""API session authentication module"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Session Authentication """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for user_id """

        if user_id is None or isinstance(user_id, str) is False:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns User ID based on Session ID """

        if session_id is None or isinstance(session_id, str) is False:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns a User instance based on cookie value """

        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Deletes user session to logout """

        if request is None:
            return False
        cookie = self.session_cookie(request)
        if cookie is None or self.user_id_for_session_id(cookie) is None:
            return False
        del self.user_id_by_session_id[cookie]
=======
#!/usr/bin/env python3
""" Python Module """
from .auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ Implement Session Authorization protocol methods
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user with id user_id

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a user ID based on a session ID

        Args:
            session_id (str, optional): _description_. Defaults to None.

        Returns:
                str: _description_
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Return a user instance based on a cookie value

        Args:
            request (_type_, optional): _description_. Defaults to None.
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ Deletes a user session

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
>>>>>>> 646451b1fdb2f0a8abe26ac0778318e09c29c9d6
        return True
