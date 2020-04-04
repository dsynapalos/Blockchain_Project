import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse


class Blockchain():

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof=1, previous_hash='0'):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'transactions': self.transactions
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof == False:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[0:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[0:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    def add_transaction(self, sender, reciever, ammount):
        self.transactions.append({'sender': sender, 'receiver': reciever, 'amount': ammount})
        previous_block = self.get_previous_block()
        next_block = previous_block['index'] + 1
        return next_block


app = Flask(__name__)
blockchain = Blockchain()


@app.route('/', methods=['GET'])
def root():
    return {
               'message': 'Root stub. Try appending methods such as /help'
           }, 200


@app.route('/help', methods=['GET'])
def help():
    return {
               'message': 'This is a list of available methods.',
               '/mine_block': 'Will create a new block and add it into the blockchain.',
               '/get_chain': 'Will display the current blockchain structure.',
               '/is_valid': 'Will test current chain for validity.'
           }, 200


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    new_proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(new_proof, previous_hash)
    return {
               'message': 'Block successfully mined',
               'index': block['index'],
               'timestamp': block['timestamp'],
               'proof': block['proof'],
               'previous_hash': block['previous_hash'],

           }, 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    return {
               'message': 'Chain successfully fetched',
               'chain': blockchain.chain,
               'length': len(blockchain.chain)

           }, 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    if blockchain.is_chain_valid(blockchain.chain):
        return {
                   'message': 'Chain is valid.'

               }, 200
    else:
        return {
                   'message': 'Chain is invalid.'
               }, 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
