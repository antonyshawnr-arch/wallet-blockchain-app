from flask import Flask, jsonify, request, render_template
from blockchain import Blockchain
from wallet import Wallet

app = Flask(__name__)

blockchain = Blockchain()
wallets = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_wallet', methods=['POST'])
def create_wallet():
    name = request.json.get("name")
    wallet = Wallet(name)
    wallets[wallet.address] = wallet
    return jsonify(wallet.to_dict())

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    sender = wallets.get(data['from'])
    receiver = wallets.get(data['to'])
    amount = int(data['amount'])

    result = sender.send(receiver, amount, blockchain)
    return jsonify({"message": result})

@app.route('/mine', methods=['GET'])
def mine():
    proof = blockchain.proof_of_work(blockchain.last_block['proof'])
    block = blockchain.new_block(proof)
    return jsonify(block)

@app.route('/chain', methods=['GET'])
def chain():
    return jsonify(blockchain.chain)

if __name__ == '__main__':
    app.run(debug=True)
