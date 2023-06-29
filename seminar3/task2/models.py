from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

association_table = db.Table('association',
                             db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
                             db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True))


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    books = db.relationship('Book', secondary=association_table, backref='authors')

    def __repr__(self):
        return f"Author({self.firstname} {self.lastname})"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Author({self.title}"

# class Association(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)


#
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
#     courses = db.relationship('Course', secondary=association_table, backref='students')
#
# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
