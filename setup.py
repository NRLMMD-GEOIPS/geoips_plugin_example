# # # Distribution Statement A. Approved for public release. Distribution unlimited.
# # #
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # #
# # # This program is free software: you can redistribute it and/or modify it under
# # # the terms of the NRLMMD License included with this program. This program is
# # # distributed WITHOUT ANY WARRANTY; without even the implied warranty of
# # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the included license
# # # for more details. If you did not receive the license, for more information see:
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/

'''
This is a template to use as a starting point for your setup.py.
To get this working corectly, set `name` to the name of your packages,
add any installation requirements to the `install_requires` array, and
add any required `entry_points`.
'''

from numpy.distutils.core import setup, Extension

# If you have no required compiled code, you can remove "ext1" from setup.py - only required for compileable source code
ext1 = Extension(name='geoips_plugin_example.lib.constants',
                 sources=['src/constants.f90'])

setup(
      ext_modules=[ext1],  # If no required compiled code, remove "ext_modules" from setup
  )
