"""
Defines the module for the Photo class
"""

from os import path
import methods

class Photo(object):
    """
    Photo class to describe input of a photo
    """
    def __init__(self, filename, method):
        """
        Accepts the path to the filename of the photo to process and the method,
        a subclassed instance of BaseRecognitionMethod
        """
        # Assertions for init to pass
        assert path.isfile(filename), \
            "Filename %s does not exist" % filename
        assert "#" in filename, \
            "Filename %s is missing hash tag in name" % filename
        assert isinstance(method, methods.base.BaseRecognitionMethod), \
            "Method provided to photo should be subclassed from BaseRecognitionMethod"
        self.filename = filename
        filename_string, label_string = self.filename.split("#")
        self.name = path.basename(filename_string)
        self.labels = set(filter(None, label_string.split('.')[0].split(" ")))
        self.candidates = method.process(self)
        # https://stats.stackexchange.com/a/8026
        self.true_positives = self.candidates & self.labels
        self.false_positives = self.candidates - self.labels
        self.false_negatives = self.labels - self.candidates
        num_tp = len(self.true_positives)
        num_fp = len(self.false_positives)
        num_fn = len(self.false_negatives)
        self.precision = num_tp / (num_tp + num_fp) if (num_tp + num_fp) != 0 else 0
        self.recall = num_tp / (num_tp + num_fn) if (num_tp + num_fn) != 0 else 0

    def csv(self):
        """
        Returns a CSV representation of the labels
        """
        ','.join([
            self.name,
            ' '.join(map(str, self.candidates)),
            ' '.join(map(str, self.labels)),
            str(self.precision),
            str(self.recall)
        ])
