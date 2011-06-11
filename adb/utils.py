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
		""" Return a list of attached devices."""
	    result = self.call_adb("devices")
	    devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
	    return [device for device in devices if len(device) > 2]
	    
	def get_state(self):
		result = self.call_adb("get-state")
                result = result.strip(' \t\n\r')
		return result or None
		
	def install(self, device_id, path_to_app, **kwargs):
		# check to see if correct device is connected
		# ensure path to app exists and is .apk
		# command = "install"
		# check for options in kwargs
		
		# result = self.call_adb(command)
		pass
		
	def reboot(self, option):
		command = "reboot"
		if len(option) > 7 and option in ("bootloader", "recovery",):
			command = "%s %s" % (command, option.strip())
		self.call_adb(command)
		
	def push(self, local, remote):
		result = self.call_adb("push %s %s" % (local, remote))
		return result
		
	def pull(self, remote, local):
		result = self.call_adb("pull %s %s" % (remote, local))
		return result
	
	def sync(self, directory, **kwargs):
		command = "sync %s" % directory
		if 'list' in kwargs:
			command += " -l"
		result = self.call_adb(command)
		return result
	
		
	
	    
	    
	    
	 
	


