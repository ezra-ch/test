import pythoncom, pyWinhook

def OnKeyboardEvent(event):
    count = time
    print ('MessageName:',event.MessageName)
    print ('Message:',event.Message)
    print ('Time:',event.Time)
    print ('Window:',event.Window)
    print ('WindowName:',event.WindowName)
    print ('Ascii:', event.Ascii, chr(event.Ascii))
    print ('Key:', event.Key)
    print ('KeyID:', event.KeyID)
    print ('ScanCode:', event.ScanCode)
    print ('Extended:', event.Extended)
    print ('Injected:', event.Injected)
    print ('Alt', event.Alt)
    print ('Transition', event.Transition)
    print ('---')

    # return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyWinhook.HookManager()

# watch for key press events
hm.KeyDown = OnKeyboardEvent

# set the hook
hm.HookKeyboard()

# wait forever
pythoncom.PumpMessages() 