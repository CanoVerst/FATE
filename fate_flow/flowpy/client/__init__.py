#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from fate_flow.flowpy.client.base import BaseFlowClient
from fate_flow.flowpy.client import api
from arch.api.utils import file_utils
from arch.api.utils.core_utils import get_lan_ip
from fate_flow.settings import SERVERS, ROLE, API_VERSION

server_conf = file_utils.load_json_conf("arch/conf/server_conf.json")


default_ip = server_conf.get(SERVERS).get(ROLE).get('host')
if default_ip in ['localhost', '127.0.0.1']:
    default_ip = get_lan_ip()
default_port = server_conf.get(SERVERS).get(ROLE).get('http.port')
default_version = API_VERSION


class FlowClient(BaseFlowClient):
    job = api.Job()
    component = api.Component()
    data = api.Data()
    queue = api.Queue()
    table = api.Table()
    task = api.Task()
    model = api.Model()
    priviledge = api.Priviledge()

    def __init__(self, ip=default_ip, port=default_port, version=default_version):
        super().__init__(ip, port, version)
        self.API_BASE_URL = 'http://%s:%s/%s/' % (ip, port, version)