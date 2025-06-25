# 🗃️ Packer and Decrypt

**Packer and Decrypt** is a lightweight, proof-of-concept encryption and execution toolkit built for educational purposes. It allows users to encrypt Python scripts into a binary format and then decrypt and execute them using a custom stub loader or a standalone decryption tool.

---

## 📦 Components

### `encryptor.py` / `encryptor.exe`
Encrypts any Python file (`.py`) into a binary payload using AES encryption.

- Uses ECB mode with a static 16-byte key
- Produces a `payload.bin` file containing the encrypted content

### `stubLoader.exe`
A minimal loader that dynamically decrypts `payload.bin` at runtime and executes it. This acts as the stub that loads packed code.

---

## 🛠️ Usage

### 🔐 Encrypting a File
Run the encryption script:

```bash
python encryptor.py
```

Or use the standalone `.exe`:

```bash
encryptor.exe
```

A file dialog will open. Select a `.py` file to encrypt. The tool will output `payload.bin`.

### 🚀 Running Encrypted File
Use `stubLoader.exe` to execute the encrypted payload:

```bash
stubLoader.exe
```

Make sure `payload.bin` is in the same directory.

### 🔓 Decrypting a File
To reverse the encryption and restore the original file:

```bash
python stubLoader.py
```

A dialog will open to select the `payload.bin` file. The tool will save the decrypted output as `[file-name].py`.

---

## 🧩 Example: `decrypter.py`

```python
from Crypto.Cipher import AES
from tkinter import filedialog, Tk

def unpad(data):
    return data.rstrip(b' ')

key = b'ThisIsA16ByteKey'
cipher = AES.new(key, AES.MODE_ECB)

Tk().withdraw()
src_file = filedialog.askopenfilename(filetypes=[("Binary files", "*.bin")])

if src_file:
    with open(src_file, "rb") as f:
        encrypted = f.read()

    decrypted = unpad(cipher.decrypt(encrypted))

    with open("restored_output.py", "wb") as out:
        out.write(decrypted)

    print("✅ Decrypted and saved as [file-name].py")
else:
    print("No file selected.")
```

---

## ⚠️ Disclaimer

This project is for educational, ethical, and research purposes only.

- Do not use it for malicious purposes such as malware packing or unauthorized code execution.
- The developer is not liable for any misuse of this tool.

---

## 📁 Folder Structure

```
packer-and-decrypt/
├── encryptor.py         # Python script to encrypt files into payload.bin
├── encryptor.exe        # Compiled version of encryptor.py
├── stubLoader.exe       # Loader to execute the encrypted binary
├── payload.bin          # Encrypted binary output (generated at runtime)
```

---

## ✅ Requirements

- Python 3.x (for running `encryptor.py`)
- `pycryptodome` library:  
  ```
  pip install pycryptodome
  ```

---

## 📚 License
```
MIT License — free to use, modify, and share with proper attribution.
```
