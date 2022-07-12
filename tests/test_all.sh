# # # Distribution Statement A. Approved for public release. Distribution unlimited.
# # # 
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # # 
# # # This program is free software:
# # # you can redistribute it and/or modify it under the terms
# # # of the NRLMMD License included with this program.
# # # 
# # # If you did not receive the license, see
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/
# # # for more information.
# # # 
# # # This program is distributed WITHOUT ANY WARRANTY;
# # # without even the implied warranty of MERCHANTABILITY
# # # or FITNESS FOR A PARTICULAR PURPOSE.
# # # See the included license for more details.

#!/bin/bash

# This should contain test calls to cover ALL required functionality tests for the geoips_template_plugin repo.

# The $GEOIPS tests modules sourced within this script handle:
   # setting up the appropriate associative arrays for tracking the overall return value,
   # calling the test scripts appropriately, and 
   # setting the final return value.

# Note you must use the variable "call" in the for the loop

. $GEOIPS/tests/utils/test_all_pre.sh geoips_template_plugin

echo ""
# "call" used in test_all_run.sh
for call in \
            "$GEOIPS_PACKAGES_DIR/geoips_template_plugin/tests/scripts/abi_aws.sh"
do
    . $GEOIPS/tests/utils/test_all_run.sh
done

. $GEOIPS/tests/utils/test_all_post.sh
