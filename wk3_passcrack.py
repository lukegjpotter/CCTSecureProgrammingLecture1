import hashlib

def crackHash(inputPass):
    try:
        passFile = open("wk3_passlist.txt", "r")
    except:
        print("File Not Found")

    for password in passFile:
        encodedPassword = password.encode("utf-8").strip()
        print(f"[info] Checking {password.strip()} | MD5: {hashlib.md5(encodedPassword).hexdigest()}")
        digest = hashlib.md5(encodedPassword).hexdigest()

        if digest == inputPass:
            print(f"[success] Password Found: {password}")


if __name__ == "__main__":
    crackHash("21232f297a57a5a743894a0e4a801fc3")