from ..extensions import db

class MessageModel(db.Model):
    text = db.Column(db.String(250), nullable=False)
    uid = db.Column(db.String(250), nullable=False, primary_key=True)
    createdAt = db.Column(db.String(250), primary_key=True)
    photoURL = db.Column(db.String(250), nullable=False)
    
    def __repr__(self):
        return f"Message: timestamp = {self.createdAt}, uid = {self.uid}, text = {self.text}, photoURL = {self.photoURL}"