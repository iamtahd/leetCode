import collections


class GoogleChallenges:
    def __init__(self):
        pass

    @staticmethod
    def challengeSolution1(data, n):
        if n == 0:
            return []
        dataFrequency = collections.Counter(data)
        for key, value in dataFrequency.items():
            if value > n:
                data = list(filter(lambda a: a != key, data))

        return data
