def test_class_blockchain_variable_chain_is_list(blockchain):
    assert type(blockchain.chain) == type([])


def test_class_blockchain_method_block_variable_index_is_number(blockchain):
    assert type(blockchain.create_block(1, '0')["index"]) == type(0)


def test_class_blockchain_method_block_variable_timestamp_is_timestamp(blockchain):
    assert type(blockchain.create_block(1, '0')["timestamp"]) == type("")


def test_class_blockchain_method_block_variable_proof_is_number(blockchain):
    assert type(blockchain.create_block(1, '0')["proof"]) == type(0)


def test_class_blockchain_method_block_variable_previous_hash_is_dict(blockchain):
    assert type(blockchain.create_block(1, '0')["previous_hash"]) == type("")
