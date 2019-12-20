from app import db, ma


class Revendedor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def __init__(self, nome, email, cpf, senha):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha


class RevendedorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'email', 'cpf', 'senha')


revendedor_schema = RevendedorSchema()
revendedores_schema = RevendedorSchema(many=True)