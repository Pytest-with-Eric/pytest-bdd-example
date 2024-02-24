@banking
Feature: Bank Transactions
    Tests related to banking Transactions

    @deposit
    Scenario Outline: Deposit into Account
        Given the account balance is $<balance>
        When I deposit $<deposit>
        Then the account balance should be $<new_balance>
        Examples:
            | balance | deposit | new_balance |
            | 100     | 20      | 120         |
            | 0       | 5       | 5           |
            | 100     | 0       | 100         |