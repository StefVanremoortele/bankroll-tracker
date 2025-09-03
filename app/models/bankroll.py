from ..extensions import db
from datetime import datetime

class Bankroll(db.Model):
    __tablename__ = 'bankrolls'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    currency = db.Column(db.String(8), nullable=False, default='EUR')
    starting_balance = db.Column(db.Numeric(12, 2), nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to user
    user = db.relationship('User', backref='bankrolls')

    # Optional: relationship to transactions
    # transactions = db.relationship('BankrollTxn', backref='bankroll', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'currency': self.currency,
            'starting_balance': float(self.starting_balance),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
