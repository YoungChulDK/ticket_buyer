import time

def print_initial_message(price_limit, rate_limit):
    """
    Print the initial message to the terminal when the script starts.
    """
    print("")
    print("-------------------")
    print("-  CPH Half 2024 --")
    print("-------------------")
    print("")
    print(f"Looking for tickets priced below {price_limit} DKK, updating every {rate_limit} seconds.")
    print("A browser window will open once a ticket is available.\n")

def print_status_message(search_attempts, total_tickets, lowest_price):
    """
    Print the status message showing the current search attempts, total tickets, 
    and the lowest available ticket price.
    """
    status_message = f"Still searching... Attempt {search_attempts}. Available tickets: {total_tickets}"
    if lowest_price is not None:
        status_message += f" | Lowest priced available ticket: {lowest_price} DKK"
    print(status_message)

def wait_for_rate_limit(rate_limit):
    """
    Pause execution for the rate limit duration.
    """
    time.sleep(rate_limit)
