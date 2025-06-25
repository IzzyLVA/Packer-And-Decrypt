from Crypto.Cipher import AES
from tkinter import filedialog, Tk, messagebox

key = b'ThisIsA16ByteKey'
cipher = AES.new(key, AES.MODE_ECB)

def unpad(data):
    return data.rstrip(b' ')


Tk().withdraw()
payload_path = filedialog.askopenfilename(filetypes=[("Binary files", "*.bin")])

if payload_path:
    with open(payload_path, "rb") as f:
        encrypted = f.read()
    
    decrypted = unpad(cipher.decrypt(encrypted))
    exec(decrypted.decode())
else:
    messagebox.showerror("Error", "No payload selected.")