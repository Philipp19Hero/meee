
import os

def patch_orbit_sprx(file_path):
    with open(file_path, 'rb') as f:
        data = bytearray(f.read())

    patched = False

    # Patch 1: Ersetze Pfad zur orbit.key Datei
    key_check_str = b'/dev_hdd0/tmp/Orbit/orbit.key'
    if key_check_str in data:
        index = data.find(key_check_str)
        print(f'[+] KeyCheck-String gefunden bei Offset: 0x{index:X}')
        data[index:index+len(key_check_str)] = b'/dev_usb000/DUMMY/BYPASS.key\x00'
        patched = True

    # Patch 2: Fehlerhafte Verbindung zu "Success"
    err_str = b'Error Connection'
    if err_str in data:
        index = data.find(err_str)
        print(f'[+] Error-Meldung gefunden bei Offset: 0x{index:X}')
        data[index:index+len(err_str)] = b'Success Injected! '
        patched = True

    if patched:
        output_path = file_path.replace('.sprx', '_Cracked.sprx')
        with open(output_path, 'wb') as f:
            f.write(data)
        print(f'[✔] Patch erfolgreich! Neue Datei gespeichert unter: {output_path}')
    else:
        print('[!] Keine Patch-Stellen gefunden. Manuelle Analyse nötig.')

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Verwendung: python orbit_crack_patcher_flex.py <Orbit.sprx>")
    else:
        patch_orbit_sprx(sys.argv[1])
