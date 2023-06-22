# import requests

# url = "https://api.covid19api.com/summary"

# response = requests.get(url)

# if response.status_code == 200:
#     covid_data = response.json()
#     global_data = covid_data["Global"]
#     total_confirmed = global_data["TotalConfirmed"]
#     total_deaths = global_data["TotalDeaths"]
#     total_recovered = global_data["TotalRecovered"]
#     new_confirmed = global_data["NewConfirmed"]
#     new_deaths = global_data["NewDeaths"]
#     new_recovered = global_data["NewRecovered"]
    
#     print("Dunyoda jami tasdiqlangan holatlar soni: ", total_confirmed)
#     print("Dunyoda jami vafot etganlar soni: ", total_deaths)
#     print("Dunyoda jami sog'ayganlar soni: ", total_recovered)
#     print("Yangi tasdiqlangan holatlar soni: ", new_confirmed)
#     print("Yangi vafot etganlar soni: ", new_deaths)
#     print("Yangi sog'ayganlar soni: ", new_recovered)
# else:
#     print("Xatolik yuz berdi: ", response.status_code)












