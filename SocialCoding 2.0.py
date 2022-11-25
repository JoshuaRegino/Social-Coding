import requests

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "IP": ip_address,
        "CITY": response.get("city"),
        "REGION": response.get("region"),
        "COUNTRY": response.get("country_name"),
        "CAPITAL": response.get("country_capital"),
        "TIME ZONE": response.get("timezone"),
        "CURRENCY": response.get("currency_name"
    }
    return location_data


print(get_location())
