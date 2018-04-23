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
"""
This repository is the elit SDK for python language. Your NLP tools implemented
the abstract class and method of this SDK can be hosted on elit.cloud.

See http://elitsdk.rtfd.io for documentation.
"""

from __future__ import absolute_import
from .sdk import Component
from .api import Client

__author__ = "Gary Lai"

__all__ = [
    'Component',
    'Client'
]