@banking
Feature: Bank Transactions
    Tests related to banking Transactions

    @deposit
    Scenario: Deposit into Account
        Given the account balance is $"100"
        When I deposit $"20"
        Then the account balance should be $"120"

    @withdrawal
    Scenario: Withdraw from Account
        Given the account balance is $"100"
        When I withdraw $"20"
        Then the account balance should be $"80"