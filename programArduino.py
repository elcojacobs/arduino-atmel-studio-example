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

import subprocess as sub
from time import sleep


def programArduino(boardType, hexFile, port, eraseEEPROM, arduinoPath):
    if(boardType == 'leonardo'):
        import serial

    avrconf = arduinoPath + 'hardware/tools/avr/etc/avrdude.conf'
    avrdude = arduinoPath + 'hardware/tools/avr/bin/avrdude'
    avrsize = arduinoPath + 'hardware/tools/avr/bin/avr-size'

    boardsFile = open(arduinoPath + 'hardware/arduino/boards.txt',
        'rb').readlines()

    boardSettings = {}

    for line in boardsFile:
        if(line.startswith(boardType)):
              # strip board name, period and \n
            setting = line.replace(boardType + '.', '', 1).strip()
            [key, sign, val] = setting.rpartition('=')
            boardSettings[key] = val

    avrsizeCommand = avrsize + ' ' + hexFile
    # check program size against maximum size
    p = sub.Popen(avrsizeCommand, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
    output, errors = p.communicate()
    if errors != "":
        print 'avr-size error: ' + errors + '\n'
        return

    print ('Progam size: ' + output.split()[7] +
        ' bytes out of max ' + boardSettings['upload.maximum_size'] + '\n')

    programCommand = (avrdude +
                ' -F ' +
                ' -p ' + boardSettings['build.mcu'] +
                ' -c ' + boardSettings['upload.protocol'] +
                ' -b ' + boardSettings['upload.speed'] +
                ' -P ' + port +
                ' -U ' + 'flash:w:' + hexFile +
                ' -C ' + avrconf)

    if(eraseEEPROM):
        programCommand = programCommand + ' -e'

    # open and close serial port at 1200 baud. This resets the Arduino Leonardo
    if(boardType == 'leonardo'):
        ser = serial.Serial(port, 1200)
        ser.close()
        sleep(1)  # give the bootloader time to start up

    p = sub.Popen(programCommand, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
    output, errors = p.communicate()
    # avrdude only uses stderr, append it
    print errors
    return
