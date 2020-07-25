#!/usr/bin/python3
import requests
import logging

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
                    print('giving up')
                    print("HTTP Exception: {}".format(err))
                    fakeData = ""
                    return fakeData
                else:
                    print('retrying')
                    print("(Going to retry) HTTP Exception: {}".format(err))

        return r.json()

    def top_companies(self):
        return self.__fetch('https://api.streamcamel.com/companies?limit=500')

    def top_games(self):
        return self.__fetch('https://api.streamcamel.com/games?limit=500')

    def top_streamers(self):
        return self.__fetch('https://api.streamcamel.com/users?limit=500')

    def missing_games(self):
        return self.__fetch('https://api.streamcamel.com/games_without_igdb?limit=500')

    def users_stats(self):
        return self.__fetch('https://api.streamcamel.com/users_stats?limit=500')
