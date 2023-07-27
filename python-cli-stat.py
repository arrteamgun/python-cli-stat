import urllib.request
url = "http://ftp.uk.debian.org/debian/dists/stable/main/"
try:
    urllib.request.urlretrieve(url, "")
    print("success")
except Exception as e:
    print(f"error {e}")

arch = input()
