# This script will look up function names found at the currently selected address and opens a man page to it.
# If man page cannot be found, it will automatically start a google query for the function.
# Change BROWSER and TERMINAL variables accordindly to your system/preferences.

#@author 
#@category Helper
#@keybinding SHIFT-G
#@menupath 
#@toolbar 

BROWSER  = 'firefox'
TERMINAL = 'st'
GOOGLE_SEARCH_PREFIX = "https://www.google.com/search?btnI&q="
DUCKDUCKGO_SEARCH_PREFIX = "https://duckduckgo.com/?q=!ducky "

from subprocess import Popen

def lookUpFunction():
	for r in getReferencesFrom(currentAddress):
		if r.isExternalReference():
			func_name = r.getLibraryName() + " " + r.getLabel()
			return func_name
			break
		else:
			func_name = getFunctionAt(r.getToAddress())
			if func_name:
				return func_name
				break

func_name = lookUpFunction()

if func_name == None:
	print("Failed to get function name from current address.")
else:
	handle = Popen(["man", str(func_name)])
	ret = handle.wait()
	if (ret == 0):
		Popen([TERMINAL, "man", str(func_name)])
	else:
		Popen([BROWSER, GOOGLE_SEARCH_PREFIX+str(func_name)])
