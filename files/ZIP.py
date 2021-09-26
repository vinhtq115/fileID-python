from files import Base


class ZIP(Base):
    def __init__(self):
        self.NAME = 'ZIP'
        self.EXTS = ['.zip']

        # Used for matching
        self.HEADER_SIGNATURE = b'PK\x03\x04'  # Signature at the beginning of file

        self.TOTAL_SCORE = 1

    def get_score(self, f):
        f.seek(0, 0)
        match = 0

        # Check first four bytes
        header = f.read(4)
        if header != self.HEADER_SIGNATURE:
            # ZIP must begin with b'PK\x03\x04' marker
            return 0
        match += 1
        del self.HEADER_SIGNATURE

        result = match / self.TOTAL_SCORE
        return result * 100
