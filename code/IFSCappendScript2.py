import json, re

print("Ex: SBIN0040991");
ifscCode = input("Enter IFSC Code -> BANK CODE:")

bankShortCode = ifscCode[:4]
print("bankShortCode = ",bankShortCode)

custIFSCcode = ifscCode[4:]
print("custIFSCcode = ",custIFSCcode)


# -> type cast if string -> char has int
if re.match("^[0-9_]*$", custIFSCcode):
	custIFSCcode = int(custIFSCcode)
else:
	custIFSCcode = str(custIFSCcode)


# -> append IFSC code if not present in file
with open('IFSCdata.json') as in_file, open('IFSCappendData.json', 'w') as out_file:
    data = json.load(in_file)
    if custIFSCcode not in data[bankShortCode]:
        data[bankShortCode].append(custIFSCcode)

    json.dump(data, out_file, indent=4, sort_keys=True) # -> Make it in proper format


# -> make it in single line. Remove whitespace.
with open('IFSCappendData.json', 'r') as f:
    json_data = json.load(f)
with open('IFSCappendData.json', 'w') as f:
    f.write(json.dumps(json_data, separators=(',', ':')))


# -> copy content of file IFSCappendData.json to IFSCdata.json
with open("IFSCappendData.json") as f:
    with open("IFSCdata.json", "w") as f1:
        for line in f:
            f1.write(line)
