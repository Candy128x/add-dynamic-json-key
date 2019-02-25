190225
# Python (Note)


---
@Description:
- Append dynamic JSON key value according key
- Eg: IFSC Code: SBIN0001537
	Our key is SBI & value 0001537
- Suppose we have one key & multi value in application 
- If new cust add in System. We need to add thier IFSC code in json file.
- Our py script did this task quickly & save developoer time :)


---
@ExectionEnvironment:
- py 3.7


---
@Specification:
- Python 3.7 [lib: json, re]


---
@Working-of-Script
=> py IFSCappendScript2.py
- During execution it takes IFSC code from user.
- seperate Key (bank short code) & value cust IFSC code.
- Read all data from IFSCdata.json file & append new/unique IFSC code in specific place according 
	key value mapping in IFSCappendData.json file. 
- At the end for stability/consistency we copy appended data file content to old json file.
