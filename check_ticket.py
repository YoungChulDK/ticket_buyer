import requests
from bs4 import BeautifulSoup
import urllib3  # To suppress warnings

# Suppress only the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_ticket_status(price_limit):
    """
    This function fetches the ticket status from the website and returns whether 
    a ticket is available under the given price limit. It also returns the total 
    number of tickets and the lowest price for 'Buy' tickets.
    """
    url = "https://secure.onreg.com/onreg2/bibexchange/?eventid=6277&language=us"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        rows = soup.find_all('tr')
        total_tickets = 0
        lowest_price = float('inf')

        for row in rows:
            columns = row.find_all('td')
            if len(columns) == 4:
                event_name = columns[0].text.strip()
                bib_number = columns[1].text.strip()
                price = columns[2].text.strip()

                price_value = float(price.replace('DKK', '').strip())
                button = columns[3].find('a', class_='btn button_cphhalf')

                if button:
                    button_text = button.text.strip()

                    if button_text.lower() == 'buy':
                        total_tickets += 1
                        if price_value < lowest_price:
                            lowest_price = price_value

                        if price_value <= price_limit:
                            return True, total_tickets, lowest_price

        return False, total_tickets, lowest_price if lowest_price != float('inf') else None
    else:
        print("Failed to fetch the webpage.")
        return False, 0, None
