from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)

    # age = db.Column(db.Integer, nullable=False)
    # gender = db.Column(db.String(10), nullable=False)
    # group = db.Column(db.Integer, nullable=False)
    # email = db.Column(db.String(80), nullable=False)
    # faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    # grades = db.relationship('Performance', backref='student', lazy=True)

    def __repr__(self):
        return f"User({self.firstname}, {self.lastname})"
