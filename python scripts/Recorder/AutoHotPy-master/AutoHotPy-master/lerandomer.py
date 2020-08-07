# -*- coding: utf-8 -*-
"""
@author: Emilio Moretti
Copyright 2013 Emilio Moretti <emilio.morettiATgmailDOTcom>
This program is distributed under the terms of the GNU Lesser General Public License.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

#The example starts here
from AutoHotPy import AutoHotPy  # we need to tell python that we are going to use the library
import random
import time

# The following function is called when you press ESC.
#autohotpy is the instance that controlls the library, you should do everything through it.
def exitAutoHotKey(autohotpy,event):
    """
    exit the program when you press ESC
    """
    autohotpy.stop() #makes the program finish successfully. Thisis the right way to stop it
    
def superCombo(autohotpy,event):
    """
    This function is called when you press "A" key.
    It executes the combo: A -> S -> move left -> move up -> A -> S
    """

    while 1:
        count=random.randint(0,100)
        print(count)
        time.sleep(random.randint(4000,8000)/1000)
        if count>60:
            autohotpy.V.down()
            time.sleep(random.randint(80,200)/1000)  # press() method simulates a key press by sending first the key down, and later the key up events
            autohotpy.V.up()
            time.sleep(random.randint(80,200)/1000)
        if count<60>10:
            autohotpy.N6.down()
            time.sleep(random.randint(60,200)/1000)  # press() method simulates a key press by sending first the key down, and later the key up events
            autohotpy.N6.up()
            time.sleep(random.randint(80,200)/1000)
        if count<10:
            autohotpy.N5.down()
            time.sleep(random.randint(70,200)/1000)  # press() method simulates a key press by sending first the key down, and later the key up events
            autohotpy.N5.up()
            time.sleep(random.randint(60,200)/1000)


# THIS IS WERE THE PROGRAM STARTS EXECUTING!!!!!!!!
if __name__=="__main__":
    auto = AutoHotPy()  #Initialize the library
    auto.registerExit(auto.ESC, exitAutoHotKey)   # Registering an end key is mandatory to be able to stop the program gracefully
    auto.registerForKeyDown(auto.F1,superCombo) # This method lets you say: "when I press A in the keyboard, then execute "superCombo"
    auto.start()                                #Now that everything is registered we should start runnin the program
