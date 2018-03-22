# -*- coding: utf-8 -*-
from __future__ import unicode_literals

'''
Read from the data lake
'''
import os
import unittest
from requests import get, post, delete

MICROSHARE_USERNAME = os.environ["MICROSHARE_USERNAME"]
MICROSHARE_PASSWORD = os.environ["MICROSHARE_PASSWORD"]
MICROSHARE_API_KEY = os.environ["MICROSHARE_API_KEY"]
MICROSHARE_SECRET = os.environ["MICROSHARE_SECRET"]

TEST_AUTH_URL="https://dauth.microshare.io"
TEST_URL="https://dapi.microshare.io"


def cleantags(tags):
    if tags:
        tags = "tags/{}".format(tags)
        if tags.endswith('/'):
            tags = tags[:-1]
    return tags


class TestDataLake(unittest.TestCase):
    def setUp(self):
        url = "{}/oauth2/token?username={}&password={}&client_id={}&grant_type=password&scope=ALL:ALL" \
        .format(TEST_AUTH_URL, MICROSHARE_USERNAME, MICROSHARE_PASSWORD, MICROSHARE_API_KEY)

        response = post(url)
        json = response.json()

        token = json.get('access_token')
        self.auth_headers = {
            "Authorization": "Bearer {}".format(token)
        }

    def test_get(self):
        url = "{}/share/com.hackforthesea.global.location".format(TEST_URL)
        response = get(url, headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['meta']['totalCount'] > 0)
        
    def test_append_no_tags(self):
        url = "{}/share/com.hackforthesea.tests.functional.tmp".format(TEST_URL)
        response = post(url, '{ "Test": "Null" }', headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        obj_url = "{}{}?details=true".format(TEST_URL, response.json()['objs'][0]["url"])
        echo_response = get(url, headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['meta']['totalCount'] > 0)
        # TODO: Did the data carry over?
        
    #~ def test_append_with_tags(self):
        #~ pass
       
    #~ def test_delete(self):
        #~ url = "https://dapi.microshare.io/share/{}/{}".format(rec_type, id)
        #~ response = delete(url, headers=self.auth_headers)
        #~ print(response.json())
        #~ pass

if __name__ == '__main__':
    unittest.main()



'''

def delete(self, request, id, rec_type):
	


class MicroshareListCreateView(ProtectedResourceView):
    def get(self, request, rec_type=None, tags=''):
        # @type boolean
        # Will return matching objects with their details, false will only return main information
        details = request.GET.get('details', "false")

        # @type int
        # Specifies the requested page, defaults to 1
        page = request.GET.get('page', 1)

        # @type int
        # Specifies the number of objects to be returned per page, defaults to 999
        perPage = request.GET.get('perPage', 999)

        # @type string
        # Specifies if sorting needs to be applied and to which field in the data
        sort = request.GET.get('sort', '')
        if sort != '':
            sort = '&sort={}'.format(sort)

        params = "?details={}&page={}&perPage={}{}".format(details,page,perPage, sort)
        url = "https://dapi.microshare.io/share/{}/{}{}".format(rec_type, cleantags(tags), params)
        response = get(url, headers=authentication_headers())
        return JsonResponse(response.json())
'''
