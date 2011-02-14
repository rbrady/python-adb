# python module for interacting with adb
import os

class AndroidDebugBridge(object):

    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
	    results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        return command_result

    # check for any fastboot device
    def fastboot(self, device_id):
	    pass
	    
	def attached_devices(self):
	    result = self.call_adb("devices")
	    devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
	    return [device for device in devices if len(device) > 2]
	    
	    
	    
	 
	


