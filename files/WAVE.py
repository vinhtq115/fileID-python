from files import Base


class WAVE(Base):
    def __init__(self):
        self.NAME = 'Waveform Audio File Format'
        self.EXTS = ['.wav', '.wave']

        # Used for matching
        self.RIFF_SIGNATURE = b'RIFF'  # Signature at the beginning of file
        self.WAVE_SIGNATURE = b'WAVE'  # b'WAVE' signature indicate Waveform

        self.TOTAL_SCORE = 2

    def get_score(self, f):
        f.seek(0, 0)
        match = 0

        # Check first four bytes
        header = f.read(4)
        if header != self.RIFF_SIGNATURE:
            # WAVE must begin with b'RIFF' marker
            return 0
        match += 1
        del self.RIFF_SIGNATURE

        # Check four bytes from offset 0x8
        f.seek(4)
        header = f.read(4)
        if header != self.WAVE_SIGNATURE:
            # WAVE must have b'WAVE' signature at offset 8
            return 0
        match += 1
        del self.RIFF_SIGNATURE

        result = match / self.TOTAL_SCORE
        return result * 100