# ========================================================================
# Copyright 2018 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
import http.client
import json

__author__ = "Gary Lai"


class Client(object):
    def __init__(self):
        self.server_url = "https://elit.cloud/api"
        self.endpoint = '{}/{}'.format('public', 'decode')

    def decode(self, payload):
        """

        :type payload: dict
        :param payload:
        :return: result from given payload
        :rtype: json
        """

        params = json.dumps(payload)
        headers = {'Content-type': 'application/json'}
        connection = http.client.HTTPConnection(self.server_url)
        connection.request("POST", self.endpoint, params, headers)
        response = connection.getresponse()
        result = response.read()
        if response.status == 200:
            return json.loads(result)
        else:
            return {
                'status': response.status,
                'message': result
            }
