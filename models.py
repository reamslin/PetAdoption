from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    """connect to database"""

    db.app = app
    db.init_app(app)

NO_PHOTO_URL = "https://emorywheel.com/wp-content/uploads/2018/11/no-picture-available.png"

class Pet(db.Model):
    """Pet model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    name = db.Column(db.Text,
    nullable=False)

    species = db.Column(db.Text,
    nullable=False)

    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
    nullable=False,
    default=True)

    def image_url(self):
        """Returns the image of the pet"""

        return self.photo_url or NO_PHOTO_URL

