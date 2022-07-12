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

from default_package import default_algorithm
from default_package import constants

def test_algorithm():
    assert default_algorithm() == 1
    assert default_algorithm() == default_algorithm(constants.test1)
    assert default_algorithm(constants.test2) == default_algorithm(constants.test2)
    assert default_algorithm(2) == 4
