import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Load all scenarios from the feature file
scenarios("../features/bank_transactions_param.feature")

MY_TYPES = {"Number": int}


# Fixtures
@pytest.fixture
def account_balance():
    return {"balance": 0}  # Using a dictionary to allow modifications


# Given Steps
@given(
    parsers.cfparse('the account balance is $"{balance:Number}"', extra_types=MY_TYPES)
)
def account_initial_balance(account_balance, balance):
    account_balance["balance"] = balance


# When Steps
@when(parsers.cfparse('I deposit $"{deposit:Number}"', extra_types=MY_TYPES))
def deposit(account_balance, deposit):
    account_balance["balance"] += deposit


# When Steps
@when(parsers.cfparse('I withdraw $"{withdrawal:Number}"', extra_types=MY_TYPES))
def withdraw(account_balance, withdrawal):
    account_balance["balance"] -= withdrawal


# Then Steps
@then(
    parsers.cfparse(
        'the account balance should be $"{new_balance:d}"', extra_types=MY_TYPES
    )
)
def account_balance_should_be(account_balance, new_balance):
    assert account_balance["balance"] == new_balance
