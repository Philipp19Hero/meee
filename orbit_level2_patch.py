
import os

def patch_level2(file_path):
    with open(file_path, 'rb') as f:
        data = bytearray(f.read())

    # Offset für vermuteten Key-/Servercheck (aus Analyse)
    offset = 0x9FDDB
    patch_bytes = bytes.fromhex('60000000')  # NOP in PowerPC (PS3)

    if data[offset:offset+4] != patch_bytes:
        print(f'[+] Patching Offset 0x{offset:X} mit NOPs...')
        data[offset:offset+4] = patch_bytes
        output_path = file_path.replace('.sprx', '_Level2Cracked.sprx')
        with open(output_path, 'wb') as f:
            f.write(data)
        print(f'[✔] Level-2 Patch erfolgreich! Gespeichert unter: {output_path}')
    else:
        print('[!] Patch wurde bereits angewendet oder Stelle ist schon neutralisiert.')

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Verwendung: python orbit_level2_patch.py <Orbit.sprx>")
    else:
        patch_level2(sys.argv[1])
