url = input("Enter a URL: ")

cleaned_url = url.replace("https://", "")

print("Cleaned URL:", cleaned_url)

parts = cleaned_url.split(".")

domain = parts[1]
print("Domain:", domain)

TLD = parts[2]

# We might get a trailing / character, so we need to remove it.
#TLD_clean = TLD.strip("/")
TLD_clean = TLD.replace
print("Top-Level Domain:", TLD_clean)




