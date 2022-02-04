# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for GetOSPolicyAssignmentReport
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-os-config


# [START osconfig_generated_osconfig_v1_OsConfigZonalService_GetOSPolicyAssignmentReport_async]
from google.cloud import osconfig_v1


async def sample_get_os_policy_assignment_report():
    # Create a client
    client = osconfig_v1.OsConfigZonalServiceAsyncClient()

    # Initialize request argument(s)
    request = osconfig_v1.GetOSPolicyAssignmentReportRequest(
        name="name_value",
    )

    # Make the request
    response = await client.get_os_policy_assignment_report(request=request)

    # Handle response
    print(response)

# [END osconfig_generated_osconfig_v1_OsConfigZonalService_GetOSPolicyAssignmentReport_async]
