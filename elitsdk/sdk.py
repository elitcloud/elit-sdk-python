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
import abc

__author__ = "Gary Lai"


class ElitSDK(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def decode(self, input_data, *args, **kwargs):
        """
        :param input_data: expect input for the decode function
        :param args: args for the decode method if needed
        :param kwargs: kwargs for the decode method if needed
        :return:
        """
        return NotImplemented

    @abc.abstractmethod
    def load_model(self, model_root):
        """
        Implement the method how to load your models.
        :type model_root: str
        :param model_root: the root directory contains all models you need
        :return: None
        """
