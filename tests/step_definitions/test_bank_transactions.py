import pytest
from pytest_bdd import scenarios, scenario, given, when, then

# Load all scenarios from the feature file
scenarios("../features/bank_transactions.feature")


# # Load a single scenario from the feature file
# @scenario("../features/bank_transactions.feature", "Deposit into Account")
# def test_scenario():
#     pass


# Fixtures
@pytest.fixture
def account_balance():
    return {"balance": 100}  # Using a dictionary to allow modifications


# Given Steps
@given("the account balance is $100")
def account_initial_balance(account_balance):
    account_balance["balance"] = 100


# When Steps
@when("I deposit $20")
def deposit(account_balance):
    account_balance["balance"] += 20


# Then Steps
@then("the account balance should be $120")
def account_balance_should_be(account_balance):
    assert account_balance["balance"] == 120
