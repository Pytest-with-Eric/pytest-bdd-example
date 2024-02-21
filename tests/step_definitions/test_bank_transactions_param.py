import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers

# Load all scenarios from the feature file
scenarios("../features/bank_transactions_param.feature")


# # Load a single scenario from the feature file
# @scenario("../features/bank_transactions.feature", "Deposit into Account")
# def test_scenario():
#     pass


# Fixtures
@pytest.fixture
def account_balance():
    return {"balance": 0}  # Using a dictionary to allow modifications


# Given Steps
@given(
    parsers.cfparse(
        'the account balance is $"{balance:Number}"', extra_types={"Number": int}
    )
)
def account_initial_balance(account_balance, balance):
    account_balance["balance"] = balance


# When Steps
@when(parsers.cfparse('I deposit $"{deposit:Number}"', extra_types={"Number": int}))
def deposit(account_balance, deposit):
    account_balance["balance"] += deposit


# Then Steps
@then(
    parsers.cfparse(
        'the account balance should be $"{new_balance:d}"', extra_types={"Number": int}
    )
)
def account_balance_should_be(account_balance, new_balance):
    assert account_balance["balance"] == new_balance
