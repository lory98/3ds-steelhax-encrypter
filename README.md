# 3ds-save-reencrypter
ReEncrypts a 3DS save, allowing you to move it to another console (Only Steel Diver: Sub Wars supported now)

Requires: https://github.com/wwylele/3ds-save-tool

Usage:

Place `encrypt.py` in the `3ds-save-tool` folder and rename `disa-extract.py` to `disa_extract.py`.

Configure 3ds-save-tool (add your keys in `secrets.py`)

Then `$ python encrypt.py <YOUR-SAVE>` to encrypt your plaintext save.

The encrypted file will be `./out/00000001.sav`
