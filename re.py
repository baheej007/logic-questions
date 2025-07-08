text = "Card: 1234567890, Phone: 9876543210"

match = re.search(r"[Pp]hone[:\s]*([0-9]{10})", text)
if match:
    print("Phone number:", match.group(1))
else:
    print("Not found")
