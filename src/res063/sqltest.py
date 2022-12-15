from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////books.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()

    # Create record
    db.session.add(Book(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3))
    db.session.commit()

# db = sqlite3.connect(".\\src\\res063\\books-collection.db")
# cursor = db.cursor()
# cursor.execute(
#     "CREATE TABLE books("
#     "id INTEGER PRIMARY KEY, "
#     "title varchar(250) NOT NULL UNIQUE, "
#     "author varchar(250) NOT NULL, "
#     "rating FLOAT NOT NULL"
#     ")"
# )
