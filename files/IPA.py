import re
from zipfile import ZipFile
from files import Base
from files.ZIP import ZIP


class IPA(Base):
    def __init__(self):
        self.NAME = 'iOS App Store Package (ZIP-based)'
        self.EXTS = ['.ipa']

        self.zip_check = ZIP()
        self.app_name_re = re.compile('^Payload/([^/])+.app/$')

        self.TOTAL_SCORE = 2

    def get_score(self, f):
        f.seek(0, 0)
        match = 0

        # Check if f is zip file
        zip_score = self.zip_check.get_score(f)
        if zip_score < 1.0:
            return 0

        # Check for Payload folder
        f.seek(0, 0)
        zip_file = ZipFile(f)
        list_files = zip_file.namelist()
        if 'Payload/' in list_files:
            match += 1

        # Check for Payload/ApplicationName.app/ folder
        for i in list_files:
            if self.app_name_re.search(i):
                match += 1

        result = match / self.TOTAL_SCORE
        return result * 100
