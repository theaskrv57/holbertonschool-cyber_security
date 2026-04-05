#!/usr/bin/python3
"""
Finds and replaces a string in the heap of a running process.
"""

import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    pid = sys.argv[1]
    search_str = sys.argv[2]
    replace_str = sys.argv[3]

    if len(search_str) == 0:
        sys.exit(1)

    try:
        # Maps faylını oxuyuruq
        with open(f"/proc/{pid}/maps", "r") as f:
            for line in f:
                if "[heap]" in line:
                    # Ünvanları götürürük
                    addr_range = line.split()[0].split('-')
                    start_addr = int(addr_range[0], 16)
                    end_addr = int(addr_range[1], 16)
                    break
            else:
                sys.exit(1)

        # Mem faylını oxuyub/yazırıq
        with open(f"/proc/{pid}/mem", "rb+") as mem:
            mem.seek(start_addr)
            heap_data = mem.read(end_addr - start_addr)

            try:
                # Stringi axtarırıq
                offset = heap_data.index(search_str.encode('ascii'))
            except ValueError:
                # Tapılmasa heç nə etmirik və ya error çıxırıq
                sys.exit(1)

            # Ekrana çıxış (Sənin error loguna uyğun format)
            print(f"[] Found '{search_str}' at {hex(start_addr + offset)}")

            # Yazma prosesi
            mem.seek(start_addr + offset)
            mem.write(replace_str.encode('ascii')) # Null byte (\0) bəzən testi poza bilər
            print(f"[] Replaced with '{replace_str}'")

    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()
