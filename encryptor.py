from Crypto.Cipher import AES
from tkinter import filedialog, Tk

def pad(data):
    return data + b' ' * (16 - len(data) % 16)

key = b'ThisIsA16ByteKey'
cipher = AES.new(key, AES.MODE_ECB)

Tk().withdraw()
src_file = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])

if src_file:
    with open(src_file, "rb") as f:
        data = pad(f.read())

    encrypted = cipher.encrypt(data)

    with open("payload.bin", "wb") as out:
        out.write(encrypted)

    print("✅ Encrypted and saved as payload.bin")
else:
    print("No file selected.")
