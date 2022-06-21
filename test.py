#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Display an image on Vector's face
"""

import os
import sys
import time

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import anki_vector
from anki_vector.util import degrees


def main():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:

        ## SAY 'Happy Birthday'
        print("Say 'Happy Birthday'...")
        robot.behavior.say_text("happy birthday, tito christian")
        
        # If necessary, move Vector's Head and Lift to make it easy to see his face
        # robot.behavior.set_head_angle(degrees(45.0))
        # robot.behavior.set_lift_height(0.0)
       
        ## FIREWORKS
        #animation = "anim_holiday_hny_fireworks_01"
        #robot.anim.play_animation("anim_holiday_hny_fireworks_01")


if __name__ == "__main__":
    main()
