from flask import Flask, jsonify, request
from model.Produto import Produto, ProdutoSchema


app = Flask(__name__)

produtos = [
  Produto (1, 'Sapato Preto', 'Augustini', 150.49),
  Produto (2, 'Bolsa Verde', 'ThePack', 1620),
  Produto (3, 'Sapato Branco', 'Augustini', 210.50 ),
  Produto (4, 'Jeans Azul', 'Jeansouth', 69.50 ),
  Produto (5, 'Corrente Dourada', 'Plata New', 5800 ),
  Produto (6, 'Óculos Beje', 'Plata New', 650 ),
  Produto (7, 'Camisa Amarela', 'Jeansouth', 59 ),
  Produto (8, 'Tênis Verde', 'Augustini', 299.99 ),
  Produto (9, 'Bota Cinza', 'Augustini', 370 ),
]

@app.route('/produtos')
def get_produtos():
    schema = ProdutoSchema(many=True)
    result = schema.dump(produtos)
    return jsonify(result)

@app.route('/produtos/<int:produtoID>', methods = ['GET'])
def get_produto(produtoID):
    schema = ProdutoSchema(many=True)
    result = schema.dump(produtos)
    for product in result:
      if(product['produtoID'] == produtoID):
        return product
    return("Not Found")