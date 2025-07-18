
import os

def patch_orbit_sprx(file_path, output_path):
    with open(file_path, 'rb') as f:
        data = bytearray(f.read())

    # Beispielhafte Dummy-Patch-Positionen
    # Diese müssten mit echten Offsets ersetzt werden, wenn Ghidra die Stellen findet

    patched = False

    # Suche nach typischen Strings oder Platzhaltern, die gepatcht werden sollen
    key_check_str = b'/dev_hdd0/tmp/Orbit/orbit.key'
    if key_check_str in data:
        index = data.find(key_check_str)
        print(f'[+] KeyCheck-String gefunden bei Offset: 0x{index:X}')
        # Überschreibe den Pfad mit Dummywerten
        data[index:index+len(key_check_str)] = b'/dev_usb000/DUMMY/BYPASS.key '
        patched = True

    # Dummy-Patch: ersetze "Error Connection" mit "Success Injected"
    err_str = b'Error Connection'
    if err_str in data:
        index = data.find(err_str)
        print(f'[+] Error-Meldung gefunden bei Offset: 0x{index:X}')
        data[index:index+len(err_str)] = b'Success Injected! '

        patched = True

    if patched:
        with open(output_path, 'wb') as f:
            f.write(data)
        print(f'[✔] Patch erfolgreich! Neue Datei gespeichert unter: {output_path}')
    else:
        print('[!] Keine Patch-Stellen gefunden. Manuelle Analyse nötig.')

if __name__ == "__main__":
    input_path = "Orbit.sprx"
    output_path = "Orbit_Cracked.sprx"

    if not os.path.exists(input_path):
        print(f"[!] Datei {input_path} nicht gefunden.")
    else:
        patch_orbit_sprx(input_path, output_path)
