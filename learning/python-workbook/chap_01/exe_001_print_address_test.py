from exe_001_print_address import print_address


def test_exe_001():
    """ To start the tests, type from CLI: pytest """
    name: str = 'ATTENE ALESSANDRO'
    address: str = 'Via della Speranza, 13'
    cap: int= 20019
    city: str = 'Milano (MI)'
    complete_address: str = f"{name}\n{address}\n{cap} - {city}"
    result_address: str = print_address(complete_address)
    assert result_address == complete_address
