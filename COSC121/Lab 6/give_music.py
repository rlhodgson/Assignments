import os.path
def main():
    fn = None
    while fn is None:
        fn = input("Enter a file name: ")
        if not os.path.isfile(fn):
            print(fn, "DOES NOT EXIST!")
            fn = None
    
    f = open(fn, encoding="utf-8")
    lines = f.readlines()
    f.close()
    
    # pull out the header data
    st = "<head>"   # Start tag
    et = "</head>"  # End tag
    i = 0
    found = False
    while i < len(lines) and not found:
        l = lines[i]
        if l.strip().startswith(st):
            sl = i  # Start line index
            found = True
        else:
            i += 1
    
    i = 0
    found = False
    while i < len(lines) and not found:
        l = lines[i]
        if l.strip().startswith(et):
            el = i  # End line index
            found = True
        else:
            i += 1
    
    
    h_lines = lines[sl+1:el]
    _, name = h_lines[0].strip().split(':')
    _, status = h_lines[1].strip().split(':')
    
    
    
    # pull out the data block
    st = "<data>"   # Start tag
    et = "</data>"  # End tag
    i = 0
    found = False
    while i < len(lines) and not found:
        l = lines[i]
        if l.strip().startswith(st):
            sl = i  # Start line index
            found = True
        else:
            i += 1
    
    i = 0
    found = False
    while i < len(lines) and not found:
        l = lines[i]
        if l.strip().startswith(et):
            el = i  # End line index
            found = True
        else:
            i += 1
    
    
    data_lines = lines[sl+1:el]
    data = []
    for line in data_lines:
        _, band_name, amount = line.strip().split(',')
        amount = float(amount)
        data.append((band_name, amount))
    
    total = 0
    for band_name, amount in data:
        total += amount
    
    
    # Print the report
    print("-" * 40)
    print("Donation Summary")
    print("-" * 40)
    print("User name: {}".format(name.title()))
    print("Account Status: {}".format(status))
    
    if status in ["suspended", "deleted"]:
        print("*** WARNING ***")
        print("*** User can't access their account ***")
    print("-" * 40)
    
    for band_name, amount in sorted(data):
        print("{} ({:.2f})".format(band_name, amount))
    print("-" * 40)
    print("Count: {}".format(len(data)))
    print("Total: {:.2f}".format(total))
    print("-" * 40)

main()
