# Tests

import os

from tests.base import BaseTestZSTD, raise_skip

class TestZSTD(BaseTestZSTD):

    def setUp(self):
        self.VERSION = os.getenv("VERSION")
        self.PKG_VERSION = os.getenv("PKG_VERSION")
        v = [int(n) for n in self.VERSION.split(".")]
        v = sorted(v, reverse=True)
        self.VERSION_INT = 0
        i = 0
        for n in v:
            self.VERSION_INT += n * 100**i
            i += 1

    def test_module_version(self):
        BaseTestZSTD.helper_version(self)

    def test_library_version(self):
        BaseTestZSTD.helper_zstd_version(self)

    def test_library_version_number(self):
        BaseTestZSTD.helper_zstd_version_number(self)

if __name__ == '__main__':
    unittest.main()
