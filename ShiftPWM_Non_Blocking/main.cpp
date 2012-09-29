/*
 * Copyright 2012 Elco Jacobs.
 *
 * This file is part of ShiftPWM.
 * 
 * ShiftPWM is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * ShiftPWM is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with ShiftPWM.  If not, see <http://www.gnu.org/licenses/>.
 */

/*
 * This Atmel Studio 6 project automatically includes all needed Arduino source files, you just have to point it to the right directories.
 * To compile this project on your computer, take the following steps:
 * 1. Go the the project properties and change the following options:
 *		In AVR/GNU C++ Compiler --> Directories.
 *			Change the two directories to point to your local Arduino installation. For the second directory, choose the Arduino variant that you are using.
 *			Also add any Arduino libraries that you are using. My directories are:
 *			D:\arduino-1.0.1\hardware\arduino\cores\arduino
 *			D:\arduino-1.0.1\hardware\arduino\variants\leonardo
 *			D:\arduino-1.0.1\libraries\ShiftPWM
 *		If you are using an 8 MHz Arduino, also change F_CPU in AVR/GNU C++ Compiler --> Symbols
 * 2. ArduinoFunctions.cpp includes all the source files from Arduino that are used. By including all the Arduino source files in this file, 
 *	  you don't have to add them separately. You will have to edit this file if you get errors that functions are 'unreferenced'.
 * 
 * That is all that is needed! No hassle with makefiles and compiling libraries. You can find all the files that are automatically included under 'Dependencies'.
 */

#include <Arduino.h>

int main(void)
{
	init();

	#if defined(USBCON)
	USBDevice.attach();
	#endif
	
	setup();
	
	for (;;) {
		loop();
		if (serialEventRun) serialEventRun();
	}
	return 0;
}
