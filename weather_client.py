import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')


def main():
    print_header()
    zip = input('Enter Zip Code: ')
    html = get_url(zip)
    report = get_weather_from_html(html)
    print(report.cond, report.temp, report.scale, report.loc, )


def print_header():
    print("-----------------------")
    print("Weather App analytics")
    print("-----------------------")


def get_url(zip_code):
    url = 'http://wunderground.com/weather-forecast/{}'.format(zip_code)
    response = requests.get(url)
    print(response.status_code)
    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # class_ css identifier
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()
    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    # print(condition, temp, scale, loc)
    # return condition, temp, scale, loc
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)

    return report


# loc :str <- type hint
def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text
    text = text.strip()
    return text


if __name__ == '__main__':
    main()
