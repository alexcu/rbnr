"""
Method using the Bibnumber (https://github.com/gheinrich/bibnumber) open source
framework.
"""
import os
import tempfile
import subprocess
import shutil
import re
from methods.base import BaseRecognitionMethod

class BibnumberMethod(BaseRecognitionMethod):
    """
    Processing using the Bibnumber open source method
    (https://github.com/gheinrich/bibnumber)
    """

    def __init__(self):
        self.bibnumber_working_directory = tempfile.mkdtemp()

    def __del__(self):
        shutil.rmtree(self.bibnumber_working_directory)

    def _process(self, filename):
        """
        Processes the filename using the Bibnumber method
        """
        bibnumber_dir = os.path.realpath('bin/bibnumber/bibnumber/Debug')
        assert os.path.isdir(bibnumber_dir), "Bibnumber is not installed!"
        bibnumber_exec = os.path.join(bibnumber_dir, 'bibnumber')
        exec_args = [bibnumber_exec, filename]
        output = subprocess.check_output(exec_args, cwd=self.bibnumber_working_directory)
        candidates_read_line = output.split("\n")[-2]
        candidates_list = re.search(r"Read: \[([^\]]+)?\]", candidates_read_line).group(1)
        if candidates_list is None:
            candidates_list = ''
        candidates = filter(None, candidates_list.split(","))
        return set(candidates)
