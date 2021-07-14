from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def get_flights(destination, time, flight_type, driver):
    """
    Scrapes flights from SYD airport
    destination: city in Australia
    time: time of day %Y-%m-%d
    flight_type: 'departure' or 'arrival'
    """
    destination = destination.lower()

    url = f"https://www.sydneyairport.com.au/flights/" + \
    f"?query={destination}" + \
    f"&flightType={flight_type}&terminalType=domestic" + \
    f"&date={time}" + "&sortColumn=scheduled_time&ascending=true&showAll=false"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")
    flights = soup.find('div', {'id': 'flight-cards'}).find_all('div',
                {"class": "flight-card"})
    
    # Tuples of (airline, flight_number, scheduled_time, arrival_time, url)
    flight_info = []
    
    # Iterate through flight cards
    for flight in flights:
        airline = flight.find("span", {"class": "with-image"}).text
        number = flight.find("div", {"class": "flight-numbers"}).text
        schedule = flight.find("div", {"class": "large-scheduled-time"}
            ).find("div", {"class": "heading-large"}).text
        arrival = flight.find("div", {"class": "estimated-time"}
            ).find("div", {"class": "heading-large"}).text

        url = flight.find("a", {"class": "detail-wrapper"})["href"]

        flight_info.append((airline, number, schedule, arrival, url))

    return flight_info


def main():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)    

    root_url = "https://www.sydneyairport.com.au/"

    try:
        flights = get_flights("melbourne", "2021-07-14", "departure", driver)

        for f in flights[0:5]:
            

    finally:
        print("Quitting driver")
        driver.quit()



if __name__ == "__main__":
    main()