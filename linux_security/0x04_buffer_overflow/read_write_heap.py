#!/usr/bin/python3
import sys

def error(msg):
    print(msg)
    sys.exit(1)

def get_heap_range(pid):
    try:
        with open(f"/proc/{pid}/maps", "r") as f:
            for line in f:
                if "[heap]" in line:
                    parts = line.split()
                    addr = parts[0]
                    start, end = addr.split("-")
                    return int(start, 16), int(end, 16)
    except Exception:
        pass
    return None, None

def main():
    if len(sys.argv) != 4:
        error("Usage: read_write_heap.py pid search_string replace_string")

    pid = sys.argv[1]
    search = sys.argv[2].encode()
    replace = sys.argv[3].encode()

    if len(replace) != len(search):
        error("Error: replace string must be same length as search string")

    start, end = get_heap_range(pid)
    if start is None:
        error("Error: cannot find heap")

    try:
        with open(f"/proc/{pid}/mem", "rb+") as mem:
            mem.seek(start)
            heap = mem.read(end - start)

            index = heap.find(search)
            if index == -1:
                error("Error: string not found in heap")

            real_addr = start + index

            mem.seek(real_addr)
            mem.write(replace)

            print("SUCCESS!")

    except PermissionError:
        error("Error: permission denied (try sudo)")
    except Exception as e:
        error(f"Error: {e}")

if __name__ == "__main__":
    main()
