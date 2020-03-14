def test_class_blockchain_method_create_block_is_defined(blockchain):
    assert blockchain.create_block(1, '0')


def test_class_blockchain_method_create_block_returns_dict(blockchain):
    assert type(blockchain.create_block(1, '0')) == type({})


def test_class_blockchain_method_create_block_appends_block_to_chain(blockchain):
    assert blockchain.chain != []


def test_class_blockchain_method_get_previous_block_returns_chain(blockchain):
    assert blockchain.get_previous_block() == blockchain.chain[-1]


def test_class_blockchain_method_proof_of_work(blockchain):
    new_proof = blockchain.proof_of_work(blockchain.chain[-1]['proof'])
    assert new_proof


def test_class_blockchain_method_hash(blockchain):
    assert blockchain.hash(blockchain.get_previous_block())


def test_class_blockchain_method_is_chain_valid(blockchain):
    assert blockchain.is_chain_valid(blockchain.chain)
