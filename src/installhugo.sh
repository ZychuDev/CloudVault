#!/bin/bash

#
# Copyright 2022 Google Inc. All rights reserved.
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
#
_HUGO_VERSION=0.96.0
# echo Downloading Hugo version $_HUGO_VERSION...
# curl -L https://github.com/gohugoio/hugo/releases/download/v${_HUGO_VERSION}/hugo_${_HUGO_VERSION}_Linux-64bit.tar.gz | tar -xz -C /tmp/
# echo Downloading Hugo version $_HUGO_VERSION...
curl -L https://github.com/gohugoio/hugo/releases/download/v${_HUGO_VERSION}/hugo_extended_${_HUGO_VERSION}_Linux-64bit.tar.gz | tar -xz -C /tmp/
# echo The Hugo binary is now at /tmp/hugo.