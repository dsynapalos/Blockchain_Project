import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain():
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof=1, previous_hash='0'):
        return True
