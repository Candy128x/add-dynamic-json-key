import json, re

# print "Hello py developer :]"

ifscCode = input("Enter IFSC Code -> BANK CODE:")

bankShortCode = ifscCode[:4]
print("bankShortCode = ",bankShortCode)

custIFSCcode = ifscCode[4:]
print("custIFSCcode = ",custIFSCcode)


print("Type:",type(custIFSCcode))

if re.match("^[0-9_]*$", custIFSCcode):
	custIFSCcode = int(custIFSCcode)
else:
	custIFSCcode = str(custIFSCcode)

print("--After Type:",type(custIFSCcode))


# f = open('IFSCdataWhiteSpace.json', 'r')
# for line in f:
# 	line = line.rstrip()
# f.close()

with open('IFSCdataWhiteSpace.json', 'r') as f:
    json_data = json.load(f)

with open('IFSCdataWhiteSpace.json', 'w') as f:
    f.write(json.dumps(json_data, separators=(',', ':')))