# Project 07: Neuro-Market Pulse
# A simplified stock market simulator for logic testing

import random

def simulate_market(current_price):
    # Logic: Market fluctuates between -5% and +7%
    change_percent = random.uniform(-0.05, 0.07)
    new_price = current_price * (1 + change_percent)
    return round(new_price, 2)

def main():
    print("--- Neuro-Market Pulse v1.0 ---")
    balance = 1000.0  # Starting capital
    stock_price = 150.0
    shares_owned = 0
    
    print(f"Starting Balance: ${balance} | Stock Price: ${stock_price}")

    for day in range(1, 6): # Simulating 5 days of trading
        print(f"\nDay {day}:")
        stock_price = simulate_market(stock_price)
        print(f"Current Stock Price: ${stock_price}")
        
        action = input("Action: [Buy / Sell / Hold]: ").lower()
        
        if action == "buy":
            qty = int(input("Quantity to buy: "))
            cost = qty * stock_price
            if cost <= balance:
                balance -= cost
                shares_owned += qty
                print(f"Success! Balance: ${balance:.2f}")
            else:
                print("Error: Insufficient funds.")
                
        elif action == "sell":
            qty = int(input("Quantity to sell: "))
            if qty <= shares_owned:
                balance += qty * stock_price
                shares_owned -= qty
                print(f"Success! Balance: ${balance:.2f}")
            else:
                print("Error: Not enough shares.")
        
        print(f"Status: {shares_owned} shares owned | Net Worth: ${(balance + shares_owned * stock_price):.2f}")

    print("\n--- Final Trading Report ---")
    print(f"Final Net Worth: ${(balance + shares_owned * stock_price):.2f}")

if __name__ == "__main__":
    main()