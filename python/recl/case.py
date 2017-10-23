from ecl.ecl import EclFile, EclGrid, EclRestartFile, EclRegion
from os.path import isfile, expanduser

def load_case(path):
    return Case(expanduser(path))


class Case(object):
    def __init__(self, path):
        self._grid_file = path + '.EGRID'
        self._init_file = path + '.INIT'
        self._smry_file = path + '.UNSMRY'
        self._rst_file = path + '.UNRST'
        self._grid = None
        self._init = None
        self._smry = None
        self._rst = None

    def _region(self, preselect=False):
        return EclRegion(self.grid, preselect=preselect)

    @property
    def grid(self):
        if self._grid:
            return self._grid
        if isfile(self._grid_file):
            self._grid = EclGrid(self._grid_file)
            self._grid.init = self.init

            self._grid.region = self._region
            return self._grid
        return None

    @property
    def init(self):
        if self._init:
            return self._init
        if isfile(self._init_file):
            self._init = EclFile(self._init_file)
            return self._init
        return None


    @property
    def summary(self):
        if self._smry:
            return self._smry
        if isfile(self._smry_file):
            self._smry = EclFile(self._smry_file)
            return self._smry
        return None

    @property
    def restart(self):
        if self._rst:
            return self._rst
        if isfile(self._rst_file):
            self._rst = EclRestartFile(self._rst_file)
            return self._rst
        return None
