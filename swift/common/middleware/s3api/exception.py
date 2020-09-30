# Copyright (c) 2014 OpenStack Foundation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class S3Exception(Exception):
    pass


class NotS3Request(S3Exception):
    pass


class BadSwiftRequest(S3Exception):
    pass


class ACLError(S3Exception):
    pass


class InvalidSubresource(S3Exception):
    def __init__(self, resource, cause):
        self.resource = resource
        self.cause = cause


class IAMException(S3Exception):
    pass
