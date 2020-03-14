def test_get_new_proof(blockchain):
    assert blockchain.proof_of_work(blockchain.get_previous_block()['proof'])


def test_get_previous_hash(blockchain):
    assert blockchain.hash(blockchain.get_previous_block())


def test_create_block(blockchain):
    assert blockchain.create_block(blockchain.proof_of_work(blockchain.get_previous_block()['proof']),
                                   blockchain.hash(blockchain.get_previous_block()))


def test_mine_block_function_returns_tuple(mine_block):
    assert isinstance(mine_block, tuple)


def test_mine_block_function_returns_response_dict(mine_block):
    assert isinstance(mine_block[0], dict)


def test_mine_block_function_returns_response_succesful(mine_block):
    assert mine_block[1] == 200


def test_mine_block_function_response_dict_contains_message(mine_block):
    assert isinstance(mine_block[0]['message'], str)


def test_mine_block_function_response_dict_contains_index(mine_block):
    assert isinstance(mine_block[0]['index'], int)


def test_mine_block_function_response_dict_contains_timestamp(mine_block):
    assert isinstance(mine_block[0]['timestamp'], str)


def test_mine_block_function_response_dict_contains_proof(mine_block):
    assert isinstance(mine_block[0]['proof'], int)


def test_mine_block_function_response_dict_contains_previous_hash(mine_block):
    assert isinstance(mine_block[0]['previous_hash'], str)
