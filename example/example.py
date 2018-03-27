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
from elit.sdk import Component


__author__ = "Gary Lai"


class Example(Component):

    def __init__(self):
        super().__init__()

    def decode(self, input_data, *args, **kwargs):
        """

        :param input_data:
        :param args:
        :param kwargs:
        """
        pass

    def load_model(self, model_root, *args, **kwargs):
        """

        :param model_root:
        :param args:
        :param kwargs:
        """
        pass

    def train(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        pass

    def save_model(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        pass


if __name__ == '__main__':
    example = Example()
    example.decode("Hello, world")