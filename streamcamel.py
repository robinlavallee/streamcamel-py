#!/usr/bin/python3
import requests
import sys
import urllib.parse

class StreamCamel:
    def __fetch(self, url):
        max_retry = 3
        attempt = 1
        while True:
            try:
                print("Fetch URL: {}".format(url))
                r = requests.get(url = url, timeout=10)
                break
            except requests.exceptions.RequestException as err:
                print('timed out')
                attempt = attempt + 1
                if attempt > max_retry:
                    print("HTTP Exception: {}".format(err))
                    fakeData = ""
                    return fakeData
                else:
                    print("(Going to retry) HTTP Exception: {}".format(err))

        return r.json()

    def __page_anything(self, count, max_count, route):
        remaining = count
        cursor = ""

        final_json = []

        while (remaining > 0):
            batch_size = min(remaining, max_count)
            json = self.__fetch('https://api.streamcamel.com/{}?limit={}&cursor={}'.format(route, batch_size, cursor))

            if 'data' in json:
                final_json += json['data']

            cursor = ""
            if 'pagination' in json and 'cursor' in json['pagination']:
                cursor = json['pagination']['cursor']

            if cursor == "":
                break

            remaining -= batch_size

        return final_json

    def top_companies(self, count=sys.maxsize):
        return self.__page_anything(count, 100, 'companies')

    def top_games(self, count=sys.maxsize):
        return self.__page_anything(count, 100, 'games')

    def top_streamers(self, count=sys.maxsize):
        return self.__page_anything(count, 500, 'users')

    def company_games(self, company, count=sys.maxsize):
        return self.__page_anything(count, 100, 'companies/{}/games'.format(company))

    def missing_games(self):
        return self.__fetch('https://api.streamcamel.com/games_without_igdb?limit=5000')

    def users_stats(self):
        return self.__fetch('https://api.streamcamel.com/users_stats?limit=5000')

    def games_stats(self, company=None):
        if company is None:
            return self.__fetch('https://api.streamcamel.com/games_stats?limit=5000')
        else:
            company_encoded = urllib.parse.quote(company)
            return self.__fetch('https://api.streamcamel.com/games_stats?limit=5000&company=' + company_encoded)

        
