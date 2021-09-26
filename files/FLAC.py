from files import Base


class FLAC(Base):
    def __init__(self):
        self.NAME = 'Free Lossless Audio Codec'
        self.EXTS = ['.flac']

        # Used for matching
        self.FLAC_HEADER = b'fLaC'  # Marker at the beginning of file

        self.TOTAL_SCORE = 1

    def get_score(self, f):
        f.seek(0, 0)
        match = 0

        # Check first four bytes
        header = f.read(4)
        if header != self.FLAC_HEADER:
            # FLAC must begin with b'fLaC' marker
            return 0
        match += 1
        del self.FLAC_HEADER

        result = match / self.TOTAL_SCORE
        return result * 100
