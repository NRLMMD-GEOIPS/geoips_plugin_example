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

'''
This is a template to use as a starting point for your setup.py.
To get this working corectly, set `name` to the name of your packages,
add any installation requirements to the `install_requires` array, and
add any required `entry_points`.
'''

from os.path import realpath, join, dirname

from setuptools import find_packages
from numpy.distutils.core import setup, Extension

# This ensures .__version__ is set on the package, based on value in VERSION file.
with open(join(dirname(realpath(__file__)), 'VERSION'), encoding='utf-8') as version_file:
    version = version_file.read().strip()

# If you have no required compiled code, you can remove "ext1" from setup.py - only required for compileable source code
ext1 = Extension(name='geoips_template_plugin.lib.constants',
                 sources=['src/constants.f90'])

setup(
      name='geoips_template_plugin',
      version=version,
      packages=find_packages(),
      python_requires='>=3.6',
      build_requires=['numpy'],
      install_requires=['numpy'],
      ext_modules=[ext1],  # If no required compiled code, remove "ext_modules" from setup
      entry_points={
          'geoips.filename_formats': [
              'test_fname=geoips_template_plugin.interface_modules.filename_formats.test_fname:test_fname',
          ],
          'geoips.output_formats': [
              'imagery_test=geoips_template_plugin.interface_modules.output_formats.imagery_test:imagery_test',
          ],
          'geoips.algorithms': [
              'single_channel_test=geoips_template_plugin.interface_modules.algorithms.single_channel_test:' +
              'single_channel_test',
          ],
          'geoips.interpolation': [
              'pyresample_wrappers.interp_gauss_test=geoips_template_plugin.interface_modules.interpolation.' +
              'pyresample_wrappers.interp_gauss_test:interp_gauss_test',
          ],
          'geoips.user_colormaps': [
              'visir.Infrared_Test=geoips_template_plugin.interface_modules.user_colormaps.' +
              'visir.Infrared_Test:Infrared_Test',
          ],
      }
  )
