import sys

def main():
    with open(sys.argv[1], "rb") as file:
        file_data = file.read()
        file_data = file_data.replace(
            b"\xc6\x45\xb7\x00",
            b"\xc6\x45\xb7\x01"
        )

        # MyTestX 10.1
        file_data = file_data.replace(
            b"\x3a\xd0\x74\x04\xc6\x45\xb7\x01",
            b"\x38\xda\x75\x04\xc6\x45\xb7\x00"
        )

        # MyTestX 10.2
        file_data = file_data.replace(
            b"\xe8\x23\x0c\xee\xff\x3a\xd8\x74\x04\xc6\x45\xb7\x01",
            b"\x90\x90\x8b\x45\xc4\x38\xc3\x75\x04\xc6\x45\xb7\x00"
        )

        file_data = file_data.replace(
            b"\xff\xff\x8b\x83\x10\x0b\x00\x00\x80\x78\x37\x00\x74\x07\x8b\xc3\xe8",
            b"\xff\xff\x8b\x83\x10\x0b\x00\x00\x80\x78\x37\xFF\x7f\x07\x8b\xc3\xe8"
        )
        with open("Cracked.exe", "wb") as output:
            output.write(file_data)

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print(f"Usage: {sys.argv[0]} filename")
        exit(1)

    main()