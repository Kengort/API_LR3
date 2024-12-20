import requests

api_key = 'PAZN5XE-M9V44Y5-G5W7DGT-RZ08AFF'
base_url = 'https://www.kinopoisk.ru'  # Убедитесь, что это правильный базовый URL

def get_request(endpoint):
    url = f"{base_url}{endpoint}"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)

    # Проверка статус-кода
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print("Response text:", response.text)
        return None

    return response.json()

# Запрос к /movie/{1012}
group_id = 1012
movie_response = get_request(f"/movie/{group_id}")
print("Movie Response:", movie_response)

# Запрос к /v1/movie/possible-values-by-field
possible_values_response = get_request("/v1/movie/possible-values-by-field")
print("Possible Values Response:", possible_values_response)

# Запрос к /movie/random
random_movie_response = get_request("/movie/random")
print("Random Movie Response:", random_movie_response)

# Запрос к /movie/search
search_term = 'Inception'
search_response = get_request(f"/movie/search?query={search_term}")
print("Search Response:", search_response)
