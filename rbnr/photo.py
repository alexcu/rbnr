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
            "Filename is missing hash tag in name"
        assert isinstance(method, methods.base.BaseRecognitionMethod), \
            "Method provided to photo should be subclassed from BaseRecognitionMethod"
        self.filename = filename
        filename_string, label_string = self.filename.split("#")
        self.name = path.basename(filename_string)
        self.labels = set(filter(None, label_string.split('.')[0].split(" ")))
        self.candidates = method.process(self.filename)
        self.true_positives = tp = self.candidates & self.labels
        self.false_positives = fp = self.candidates - self.labels
        self.false_negatives = fn = self.labels - self.candidates
        self.precision = tp / (tp + fp)
        self.recall = tp / (tp + fn)

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
