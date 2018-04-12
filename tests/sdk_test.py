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
import pytest
from elitsdk.sdk import Component

__author__ = "Gary Lai"


def test_sdk():

    class TestSDK(Component):
        pass

    with pytest.raises(TypeError):
        test_task = TestSDK()


def test_abstract_class():

    class TestSDK(Component):

        def __init__(self):
            super(TestSDK, self).__init__()

        def decode(self, input_data, *args, **kwargs):
            super(TestSDK, self).decode(input_data, *args, **kwargs)

        def load(self, model_path, *args, **kwargs):
            super(TestSDK, self).load(model_path, *args, **kwargs)

        def train(self, trn_data, dev_data, *args, **kwargs):
            super(TestSDK, self).train(trn_data, dev_data, *args, **kwargs)

        def save(self, model_path, *args, **kwargs):
            super(TestSDK, self).save(model_path, *args, **kwargs)

    with pytest.raises(NotImplementedError):
        test_task = TestSDK()
        test_task.decode("test")
