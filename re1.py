text = "My password is 1234"
masked = re.sub(r"\d{4}", "****", text)
print(masked)  # ➜ My password is ****
