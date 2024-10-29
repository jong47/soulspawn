import pytest
import uuid
from alpaca.trading.client import TradingClient

@pytest.mark.integration_test
def test_get_account_info(trading_client) -> None:
    """
    params:
    - trading_client: TradingClient from alpaca.trading.client
    """
    account = trading_client.get_account()

    assert account is not None
    assert isinstance(account.id, uuid.UUID)
    assert isinstance(account.status, str)
    assert account.currency == "USD"







# broker_client = BrokerClient('api-key', 'secret-key')

# # search for accounts created after January 30th 2022.
# #Response should contain Contact and Identity fields for each account.
# filter = ListAccountsRequest(
#     created_after=datetime.datetime.strptime("2022-01-30", "%Y-%m-%d"),
#     entities=[AccountEntities.CONTACT, AccountEntities.IDENTITY]
# )

# accounts = broker_client.list_accounts(search_parameters=filter)