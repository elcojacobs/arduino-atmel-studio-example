# Copyright 2012 Elco Jacobs.
# This file is part of ShiftPWM.

# ShiftPWM is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# ShiftPWM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with ShiftPWM.  If not, see <http://www.gnu.org/licenses/>.

import programArduino as programmer

hexFile = 'ShiftPWM_Non_Blocking/Debug/ShiftPWM_Non_Blocking.hex'
arduinoPath = 'D:/arduino-1.0.1/'
# check https://github.com/arduino/Arduino/blob/master/hardware/arduino/boards.txt for the correct name
boardType = 'nano328'
port = 'COM7'
eraseEEPROM = True

programmer.programArduino(boardType, hexFile, port, eraseEEPROM, arduinoPath)
