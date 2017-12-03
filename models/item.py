from db import db



class ItemModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    price = db.Column(db.Float(precision = 2))
    store_id = db.Column(db.Integer, db.ForeignKey('store_model.id'),
                         nullable=False)

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def __repr__(self):
        return self.name


    def json(self):
        return {"name": self.name, "price" : self.price}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
