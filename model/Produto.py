from marshmallow import Schema, fields

class Produto():
  def __init__(self, produtoID, nome, marca, valor):
    self.produtoID = produtoID
    self.nome = nome
    self.marca = marca
    self.valor = valor

  def __repr__(self):
    return '<Produto(name={self.nome!r})>'.format(self=self)


class ProdutoSchema(Schema):
  produtoID = fields.Number()
  nome = fields.Str()
  marca = fields.Str()
  valor = fields.Number()