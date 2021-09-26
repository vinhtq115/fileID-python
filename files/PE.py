from files import Base
import re


class PE(Base):
    def __init__(self):
        self.NAME = 'Portable Executable'
        self.EXTS = ['.exe']

        # Used for matching
        self.IMAGE_DOS_SIGNATURE = b'MZ'
        self.CANNOT_RUN_IN_DOS_MODE_REGEXS = [
            re.compile(b'!This program cannot be run in DOS mode.'),  # Exists in most, if not all, modern programs
            re.compile(b'This program must be run under Win32'),  # 90s programs, games
            re.compile(b'!This program requires Microsoft Windows.')  # Same as above
                                              ]
        self.PE_SIGNATURE = b'PE\x00\x00'

        self.TOTAL_SCORE = 3

    def get_score(self, f):
        f.seek(0, 0)
        match = 0

        # Check first two bytes
        header = f.read(2)
        if header != self.IMAGE_DOS_SIGNATURE:
            # PE must begin with "4D 5A"
            return 0
        match += 1
        del self.IMAGE_DOS_SIGNATURE

        # Read PE header's address (1 byte) and check if PE_SIGNATURE is at the address
        f.seek(0x3C, 0)
        pe_header_address = int.from_bytes(f.read(4), 'little')
        f.seek(pe_header_address, 0)
        pe_signature = f.read(4)

        if pe_signature != self.PE_SIGNATURE:
            return 0
        match += 1
        del self.PE_SIGNATURE

        # Find the infamous string "!This program cannot be run in DOS mode".
        # This string should be between 0x3C and PE_SIGNATURE location since it's in DOS stub.
        f.seek(0x40, 0)  # 0x40: beginning of DOS stub
        DOS_stub = f.read(pe_header_address - 0x40)
        for regex in self.CANNOT_RUN_IN_DOS_MODE_REGEXS:
            if regex.search(DOS_stub) is not None:
                match += 1
                break
        del self.CANNOT_RUN_IN_DOS_MODE_REGEXS

        result = match / self.TOTAL_SCORE
        return result * 100
