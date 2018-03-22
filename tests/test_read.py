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

def authentication_headers():
    url = "{}/oauth2/token?username={}&password={}&client_id={}&grant_type=password&scope=ALL:ALL" \
        .format(TEST_AUTH_URL, MICROSHARE_USERNAME, MICROSHARE_PASSWORD, MICROSHARE_API_KEY)

    response = post(url)
    json = response.json()

    token = json.get('access_token')
    headers = {
        "Authorization": "Bearer {}".format(token)
    }

    return headers


def cleantags(tags):
    if tags:
        tags = "tags/{}".format(tags)
        if tags.endswith('/'):
            tags = tags[:-1]
    return tags


class TestDataLake(unittest.TestCase):

    def test_get(self):
        url = "{}/share/com.hackforthesea.global.location".format(TEST_URL)
        response = get(url, headers=authentication_headers())
        print(response.json())
        pass

if __name__ == '__main__':
    unittest.main()



'''

class MicroshareGetDeleteView(ProtectedResourceView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MicroshareGetDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, rec_type, id):
        url = "https://dapi.microshare.io/share/{}/{}".format(rec_type, id)
        response = get(url, headers=authentication_headers())
        return JsonResponse(response.json())

    def delete(self, request, id, rec_type):
        url = "https://dapi.microshare.io/share/{}/{}".format(rec_type, id)
        response = delete(url, headers=authentication_headers())
        return JsonResponse(response.json())


class MicroshareListCreateView(ProtectedResourceView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MicroshareListCreateView, self).dispatch(request, *args, **kwargs)

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

    def post(self, request, rec_type=None, tags=''):
        url = "https://dapi.microshare.io/share/{}/{}".format(rec_type, cleantagsx(tags))
        response = post(url, request.body, headers=authentication_headers())
        return JsonResponse(response.json())
'''
