"""Configuration helpers."""

# Copyright 2016-2019 ASI Data Science
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os

import click

import faculty.config


_PROFILE_CACHE = None

def get_profile():
    global _PROFILE_CACHE
    if _PROFILE_CACHE is None:
        _PROFILE_CACHE = faculty.config.resolve_profile()
    return _PROFILE_CACHE


def _url_for_service(service):
    """Return URL for the given service."""
    profile = get_profile()
    return "{}://{}.{}".format(profile.protocol, service, profile.domain)


def casebook_url():
    """Return URL for Casebook."""
    return _url_for_service("casebook")


def hudson_url():
    """Return URL for Hudson"""
    return _url_for_service("hudson")


def galleon_url():
    """Return URL for Galleon."""
    return _url_for_service("galleon")


def baskerville_url():
    """Return URL for Baskerville."""
    return _url_for_service("baskerville")
