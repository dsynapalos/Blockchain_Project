def test_class_blockchain_variable_chain_is_list(blockchain):
    assert isinstance(blockchain.chain, list)


def test_class_blockchain_variable_chain_not_empty(blockchain):
    assert blockchain.chain != []


def test_class_blockchain_method_block_variable_index_is_number(blockchain):
    assert isinstance(blockchain.create_block(1, '0')["index"], int)


def test_class_blockchain_method_block_variable_timestamp_is_timestamp(blockchain):
    assert isinstance(blockchain.create_block(1, '0')["timestamp"], str)


def test_class_blockchain_method_block_variable_proof_is_number(blockchain):
    assert isinstance(blockchain.create_block(1, '0')["proof"], int)


def test_class_blockchain_method_block_variable_previous_hash_is_string(blockchain):
    assert isinstance(blockchain.create_block(1, '0')["previous_hash"], str)
