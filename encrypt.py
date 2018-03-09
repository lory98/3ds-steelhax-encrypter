from secrets import Secrets
import disa_extract
import cmac
import key_engine
import io
import hashlib
import sys

def main():
    secretsDb = Secrets()
    keyEngine = key_engine.KeyEngine(secretsDb)
    f = open(sys.argv[1], 'rb')
    disa = io.BytesIO(f.read())
    f.close()
    game_id = int(sys.argv[2], 16)
    disa.seek(0x100, 0)
    header = disa.read(0x100)
    digest = hashlib.sha256(disa_extract.getDigestBlock("sd", game_id, header)).digest()
    disa.seek(0x00, 0)
    disa.write(cmac.AesCmac(digest, keyEngine.getKeySdNandCmac()))
    disa.seek(0x00, 0)
    disa = disa_extract.cryptoUnwrap(disa, "sd", game_id, keyEngine.getKeySdDecrypt())   
    with open("./out/00000001.sav", 'wb') as save:
        save.write(disa.getbuffer())

if __name__ == '__main__':
    main()
