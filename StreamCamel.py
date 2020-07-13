#!/usr/bin/python3
import requests

class StreamCamel:
    def __fetch(self, url):
        max_retry = 3
        attempt = 1
        while True:
            try:
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

    def top_companies(self):
        return self.__fetch('https://api.streamcamel.com/companies?limit=5000')

    def top_games(self):
        return self.__fetch('https://api.streamcamel.com/games?limit=5000')

    def top_streamers(self):
        return self.__fetch('https://api.streamcamel.com/users?limit=5000')

    def missing_games(self):
        return self.__fetch('https://api.streamcamel.com/games_without_igdb?limit=5000')

    def users_stats(self):
        return self.__fetch('https://api.streamcamel.com/users_stats?limit=5000')
