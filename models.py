from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CoffeeBean(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100), nullable=False)
    grinder_setting = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<CoffeeBean {self.image}>'
