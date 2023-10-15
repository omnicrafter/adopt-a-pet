from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/animals-cat-head-people-profile-silhouette--public-domain--29.png"


def connect_db(app):
    # with app.app_context():
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE_URL)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        """Show info about pet"""

        p = self
        return f"<Pet {p.id} {p.name} {p.species} {p.age} {p.available}>"

    def get_photo_url(self):
        """Return photo url or default image"""

        return self.photo_url if self.photo_url else DEFAULT_IMAGE_URL
