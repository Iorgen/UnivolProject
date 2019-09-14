import time

import numpy
import requests
# tomsk 144, nsk 99, omsk 104, kras 73


class VKUserFetcher:
    VK_TOKEN = '81cc3c5e7876d2d571d8edf668a3cc667d9a3b7aeb91a2aeefb8a2b3048fd73a3feba730f6aca0426e405'

    def get_result_volunteers_from_vk(self, keyword: list, city_key: int = None) -> list:
        result_dict_set = []
        for group_id in self.get_id_group(keyword, city_key):
            members_ids = self.get_members_id(group_id)
            result_dict_set.extend(members_ids)
        return set(result_dict_set)

    def compare_result(self, result_dict):
        result_set = result_dict.pop()
        for key in result_dict.keys():
            result_set = key.intersection(result_set)

        vk_url = 'http://vk.com/id'

        return list(map(lambda x: vk_url+str(x), list(result_set)))

    def get_request_members(self, group_id_, offset_=0):
        t = requests.get(
            'https://api.vk.com/method/groups.getMembers?group_id={}&offset={}&v=5.52&access_token={}'.format(
                group_id_,
                offset_ * 1000,
                self.VK_TOKEN
            )
        )
        return t

    def how_much_members(self, group_id):
        try:
            t = self.get_request_members(group_id)
            return t.json()['response']['count']
        except Exception:
            print('Нинаю')
            return None

    # 1 count = 0.33 sec
    def get_members_id(self, group, count_of_id=1):
        current_count = 0
        list_id = None
        total_members = self.how_much_members(group)
        time.sleep(1 / 3)
        while (current_count < count_of_id) and (current_count + 1 < total_members):
            t = self.get_request_members(group, current_count)
            if list_id is None:
                list_id = numpy.asarray(t.json()['response']['items'])
            else:
                list_id = numpy.append(list_id, numpy.asarray(t.json()['response']['items']))
            time.sleep(1 / 3)
            current_count += 1
        return list_id

    def create_vk_id(self, id_):
        return 'https://vk.com/id' + str(id_)

    def get_request_search(self, search_, city_id=None, count_=1000):
        if city_id is None:
            t = requests.get(
                'https://api.vk.com/method/groups.search?q={}&count={}&v=5.52&access_token={}'.format(
                    search_,
                    count_,
                    self.VK_TOKEN
                )
            )
            return t

        t = requests.get(
            'https://api.vk.com/method/groups.search?q={}&count={}&city_id={}&v=5.52&access_token={}'.format(
                search_,
                count_,
                city_id,
                self.VK_TOKEN
            )
        )
        return t

    # искать только открытые группы
    def get_id_group(self, search, city_id=None):
        t = self.get_request_search(search, city_id)
        res = [gro['screen_name'] for gro in t.json()['response']['items'] if gro['is_closed'] == 0]
        return res
