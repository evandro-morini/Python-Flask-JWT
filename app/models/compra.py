import datetime
from app import db, ma


class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=datetime.datetime.now())
    revendedor_id = db.Column(db.Integer, db.ForeignKey('revendedor.id'), nullable=False)
    cashback = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer)

    def __init__(self, valor, revendedor_id, cashback, status):
        self.valor = valor
        self.revendedor_id = revendedor_id
        self.cashback = cashback
        self.status = status


class CompraSchema(ma.Schema):
    class Meta:
        fields = ('id', 'valor', 'data', 'revendedor_id', 'cashback', 'status')


compra_schema = CompraSchema()
compras_schema = CompraSchema(many=True)