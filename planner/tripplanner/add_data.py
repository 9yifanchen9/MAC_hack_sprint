from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
from selenium.webdriver.firefox.options import Options
from pprint import pprint
import csv


def get_flights(destination, date, flight_type, driver):
    """
    Scrapes flights from SYD airport
    destination: city in Australia
    time: time of day %Y-%m-%d
    flight_type: 'departure' or 'arrival'
    """
    root_url = "https://www.sydneyairport.com.au"
    destination = destination.lower()

    url = f"https://www.sydneyairport.com.au/flights/" + \
    f"?query={destination}" + \
    f"&flightType={flight_type}&terminalType=domestic" + \
    f"&date={date}" + "&sortColumn=scheduled_time&ascending=true&showAll=false"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")
    flights = soup.find('div', {'id': 'flight-cards'}).find_all('div',
                {"class": "flight-card"})
    
    # Tuples of (airline, flight_number, scheduled_time, arrival_time, url)
    flight_info = []
    
    # Iterate through flight cards
    for flight in flights:
        date = date
        airline = flight.find("span", {"class": "with-image"}).text
        number = flight.find("div", {"class": "flight-numbers"}).text
        schedule = flight.find("div", {"class": "large-scheduled-time"}
            ).find("div", {"class": "heading-large"}).text
        arrival = flight.find("div", {"class": "estimated-time"}
            ).find("div", {"class": "heading-large"}).text

        url = root_url + flight.find("a", {"class": "detail-wrapper"})["href"]

        flight_info.append((date, airline, number, schedule, arrival, url))

    return flight_info


def write_to_csv(flights, filename="flights.csv"):
    f = open(filename, "w+", newline='')
    writer = csv.writer(f)
    for flight in flights:
        writer.writerow(flight)

    f.close()


def create_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    return driver

def get_datetime_obj(date, time):
    if time == "-":
        return None

    date_obj = datetime.datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M")
    return date_obj


def main():
    driver = create_driver()

    try:
        flights = get_flights("melbourne", "2021-07-14", "departure", driver)
        write_to_csv(flights)

    finally:
        print("Quitting driver")
        driver.quit()


if __name__ == "__main__":
    main()