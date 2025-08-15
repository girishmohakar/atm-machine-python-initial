
# World Bank Python Simulation

This is a simple Python program that simulates a basic banking system. It allows a user to log in with a password and deposit or withdraw money from their account while checking the available balance.

## Features

- User login with password verification.
- Deposit money into the account.
- Withdrawal check against available balance.
- Friendly user messages and error handling.

## Requirements

- Python 3.x installed on your system.

## How to Run

1. Clone or download the script.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the script.
4. Run the program using:
   ```bash
   python world_bank.py
````

5. Enter the password when prompted (`1234` is the default password).
6. Follow the instructions to deposit or check balance.

## Program Flow

1. The program displays a welcome message.
2. The user is prompted to enter a password.
3. If the password is correct:

   * User can enter an amount to deposit.
   * Program checks if the deposit/withdrawal amount does not exceed available balance.
   * Updates and displays the available balance.
4. If the password is incorrect, the program displays an "invalid password" message.

## Example

```
Welcome to world bank

enter password 1234
welcome user
enter the amount you want to deposit 500
amount has been deposited available balance 500
thank you and have nice day
```

## Notes

* The initial account balance is set to `1000`.
* Password is hardcoded as `1234`.
* The program currently handles only a single transaction per run.
