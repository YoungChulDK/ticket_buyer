import argparse
import time
from check_ticket import check_ticket_status
from utils import print_initial_message, print_status_message, wait_for_rate_limit
import webbrowser

def main(price_limit, rate_limit):
    # Print the initial message
    print_initial_message(price_limit, rate_limit)

    search_start_time = time.time()
    search_attempts = 0

    while True:
        # Check for available tickets
        tickets_found, total_tickets, lowest_price = check_ticket_status(price_limit)

        # If tickets are found that meet the price limit, open browser and exit
        if tickets_found:
            print("Tickets found! Opening the browser now...")
            webbrowser.open_new_tab("https://secure.onreg.com/onreg2/bibexchange/?eventid=6277&language=us")
            break

        search_attempts += 1

        # Print status message every 10 seconds
        if time.time() - search_start_time > 10:
            print_status_message(search_attempts, total_tickets, lowest_price)
            search_start_time = time.time()  # Reset the timer

        # Wait before next check
        wait_for_rate_limit(rate_limit)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor ticket availability for CPH Half 2024")
    parser.add_argument("--price_limit", type=float, default=600, help="Maximum ticket price (in DKK) to notify for (default is 600 DKK)")
    parser.add_argument("--rate_limit", type=int, default=2, help="Number of seconds between checks (default is 2 seconds)")

    args = parser.parse_args()

    # Run the main program
    main(args.price_limit, args.rate_limit)
