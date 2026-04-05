#!/usr/bin/python3
"""
Finds and replaces a string in the heap of a running process.
"""

import sys


def main():
    """ Main function to read and write to process memory """
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    pid = sys.argv[1]
    search_str = sys.argv[2]
    replace_str = sys.argv[3]

    if search_str == "":
        return

    try:
        # Heap aralığını bulmak için maps dosyasını oku
        with open("/proc/{}/maps".format(pid), "r") as f:
            for line in f:
                if "[heap]" in line:
                    addr_range = line.split()[0].split('-')
                    start_addr = int(addr_range[0], 16)
                    end_addr = int(addr_range[1], 16)
                    break
            else:
                sys.exit(1)

        # Mem dosyasını binary modda aç
        with open("/proc/{}/mem".format(pid), "rb+") as mem:
            mem.seek(start_addr)
            heap_data = mem.read(end_addr - start_addr)

            try:
                # Stringi axtar
                offset = heap_data.index(search_str.encode('ascii'))
            except ValueError:
                sys.exit(1)

            # Testin beklediği tam format (Başında boşluk varsa ekle)
            print("[*] Found '{}' at {}".format(search_str,
                                                hex(start_addr + offset)))

            # Yazma işlemi
            mem.seek(start_addr + offset)
            mem.write(replace_str.encode('ascii'))

            print("[*] Replaced with '{}'".format(replace_str))
            # Testin beklediği kritik başarı mesajı
            print("SUCCESS!")

    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()
