#!/usr/bin/python3
"""
Python script that finds and replaces a string in the heap of a running process.
"""

import sys

def main():
    # Argumentlərin sayını yoxlayırıq
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    pid = sys.argv[1]
    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    # /proc/[pid]/maps faylını oxuyub heap-in harada olduğunu tapırıq
    try:
        maps_file_path = f"/proc/{pid}/maps"
        with open(maps_file_path, 'r') as maps_file:
            for line in maps_file:
                if "[heap]" in line:
                    # Heap sətrindən başlanğıc və son ünvanları götürürük
                    parts = line.split()
                    addr_range = parts[0].split('-')
                    start_addr = int(addr_range[0], 16)
                    end_addr = int(addr_range[1], 16)
                    break
            else:
                print("Error: Could not find [heap] in /proc/{}/maps".format(pid))
                sys.exit(1)

        # /proc/[pid]/mem faylına daxil olub axtarış və əvəzetmə edirik
        mem_file_path = f"/proc/{pid}/mem"
        with open(mem_file_path, 'rb+') as mem_file:
            # Heap hissəsinə keçid edirik
            mem_file.seek(start_addr)
            heap = mem_file.read(end_addr - start_addr)

            # Stringi axtarırıq (ASCII formatında)
            try:
                index = heap.index(search_string.encode('ascii'))
            except ValueError:
                print(f"Error: String '{search_string}' not found in heap.")
                sys.exit(1)

            # Tapılan yerə qayıdırıq və yeni stringi yazırıq
            print(f"[*] Found '{search_string}' at {hex(start_addr + index)}")
            mem_file.seek(start_addr + index)
            mem_file.write(replace_string.encode('ascii') + b'\0')
            print(f"[*] Replaced with '{replace_string}'")

    except PermissionError:
        print("Error: Permission denied. Run as sudo.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
