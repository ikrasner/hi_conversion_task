from application import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column('password', db.String(20))

    def __repr__(self):
        return '<User %r>' % self.name


class Invite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    used = db.Column(db.Integer)
