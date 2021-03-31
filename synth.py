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

"""This script is used to synthesize generated parts of this library."""
import os

import synthtool as s
import synthtool.gcp as gcp
from synthtool.languages import python

gapic = gcp.GAPICBazel()
common = gcp.CommonTemplates()

# ----------------------------------------------------------------------------
# Generate OS Config GAPIC layer
# ----------------------------------------------------------------------------
versions = ["v1"]

for version in versions:
    library = gapic.py_library(
        service="osconfig",
        version=version,
        bazel_target=f"//google/cloud/osconfig/{version}:osconfig-{version}-py"
    )

    s.move(library, excludes=["nox.py", "setup.py", "README.rst", "docs/index.rst"])

# rename to google-cloud-os-config
s.replace(["google/**/*.py", "tests/**/*.py"], "google-cloud-osconfig", "google-cloud-os-config")

# Add newline after last item in list
s.replace("google/cloud/**/*client.py",
"(-  Must be unique within the project\.)",
"\g<1>\n")


# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(
    samples=False,
    microgenerator=True,
    cov_level=98,
)
s.move(
    templated_files, excludes=[".coveragerc"]
)  # the microgenerator has a good coveragerc file


s.shell.run(["nox", "-s", "blacken"], hide_output=False)
