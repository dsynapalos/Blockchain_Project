def test_get_chain_function_returns_tuple(get_chain):
    assert isinstance(get_chain, tuple)


def test_get_chain_function_returns_response_dict(get_chain):
    assert isinstance(get_chain[0], dict)


def test_get_chain_function_returns_response_succesful(get_chain):
    assert get_chain[1] == 200


def test_get_chain_function_response_dict_contains_message(get_chain):
    assert isinstance(get_chain[0]['message'], str)


def test_get_chain_function_response_dict_contains_chain(get_chain):
    assert isinstance(get_chain[0]['chain'], list)


def test_get_chain_function_response_chain_not_empty(get_chain):
    assert get_chain[0]['chain'] != []


def test_get_chain_function_response_dict_contains_chain_length(get_chain):
    assert isinstance(get_chain[0]['length'], int)


def test_get_chain_function_response__chain_length_not_zero(get_chain):
    assert get_chain[0]['length'] != 0
