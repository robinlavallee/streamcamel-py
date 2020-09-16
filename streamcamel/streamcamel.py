#!/usr/bin/python3
import requests
import sys

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

    def __top_anything(self, count, max_count, type):
        remaining = count
        cursor = ""

        final_json = []

        while (remaining > 0):
            batch_size = min(remaining, max_count)
            json = self.__fetch('https://api.streamcamel.com/{}?limit={}&cursor={}'.format(type, batch_size, cursor))

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
        return self.__top_anything(count, 100, 'companies')

    def top_games(self, count=sys.maxsize):
        return self.__top_anything(count, 100, 'games')

    def top_streamers(self, count):
        return self.__top_anything(count, 500, 'users')

    def missing_games(self):
        return self.__fetch('https://api.streamcamel.com/games_without_igdb?limit=5000')

    def users_stats(self):
        return self.__fetch('https://api.streamcamel.com/users_stats?limit=5000')
