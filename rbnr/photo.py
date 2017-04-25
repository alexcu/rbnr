from os import path

class Photo:
    def __init__(self, filename, method):
        assert path.isfile(filename), "Filename %s does not exist" % filename
        # Must have hash to get tags out
        assert "#" in filename, "Filename is missing hash tag in name"
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

    def csv():
        ','.join([
            self.name,
            ' '.join(map(str, self.candidates)),
            ' '.join(map(str, self.labels)),
            str(self.precision),
            str(self.recall)
        ])
