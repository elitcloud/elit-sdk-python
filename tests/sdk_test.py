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

from elitsdk.benchmark import Timer
from elitsdk.sdk import Component
from example.example import SpaceTokenizer

__author__ = "Gary Lai"


def test_sdk():

    class TestSDK(Component):
        pass

    with pytest.raises(TypeError):
        TestSDK()


def test_abstract_class():

    class TestSDK(Component):

        def __init__(self):
            super().__init__()

        def init(self):
            super().init()

        def decode(self, input_data, **kwargs):
            super().decode(input_data, **kwargs)

        def load(self, model_path, **kwargs):
            super().load(model_path, **kwargs)

        def train(self, trn_data, dev_data, model_path, **kwargs):
            super().train(trn_data, dev_data, model_path, **kwargs)

        def save(self, model_path, **kwargs):
            super().save(model_path, **kwargs)
        
    with pytest.raises(NotImplementedError):
        test_task = TestSDK()
        test_task.decode("test")


def test_space_tokenizer():
    space_tokenizer = SpaceTokenizer()
    tokens, offset = space_tokenizer.decode("Hello, world")
    assert tokens == ['Hello,', 'world']
    assert offset == [(0, 6), (7, 12)]


def test_benchmark():
    space_tokenizer = SpaceTokenizer()
    with Timer() as time1:
        space_tokenizer.decode("Hello, world")
    with Timer() as time2:
        space_tokenizer.decode("This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers.")

    assert isinstance(time1.runtime, float)
    assert isinstance(time2.runtime, float)
    assert time1.runtime > 0.0
    assert time2.runtime > 0.0
