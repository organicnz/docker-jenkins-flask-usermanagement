from project import db, bcrypt
from datetime import datetime
from flask import current_app


class User(db.Model):
    """
    Class that represents a user of the application

    The following attributes of a user are stored in this table:
        * email - email address of the user
        * hashed password - hashed password (using Flask-Bcrypt)
        * registered_on - date & time that the user registered

    REMEMBER: Never store the plaintext password in a database!
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.String(60), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=True)
    role = db.Column(db.String, default='user')

    def __init__(self, email, plaintext_password, role='user'):
        """Create a new User object using the email address and hashing the
        plaintext password using Bcrypt.
        """
        self.email = email
        self.hashed_password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')
        self.registered_on = datetime.now()
        self.role = role

    def is_correct_password(self, plaintext_password: str):
        return bcrypt.check_password_hash(self.hashed_password, plaintext_password)

    def set_password(self, plaintext_password):
        self.hashed_password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')

    def __repr__(self):
        return f'<User: {self.email}>'

    @property
    def is_authenticated(self):
        """Return True if the user has been successfully registered."""
        return True

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the user ID as a unicode string (`str`)."""
        return str(self.id)
