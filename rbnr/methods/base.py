"""
Defines the module to define the base recognition method.
"""
class BaseRecognitionMethod(object):
    """
    Abstract class for base recognition method, to be overidden by concrete
    recognition methods.
    """

    def _process(self, filename):
        """
        Processes the filename, to be overridden by implemented recognition
        methods. Returns a set type containing each of the identified
        candidates.
        """
        raise NotImplementedError("Private method '_process' called on BaseRecognitionMethod")

    def process(self, photo):
        """
        Processes the recognition method on the given file, as specified by
        filename. Returns a set type containing each of the identified
        candidates.
        """
        print "Processing %s using %s..." % (photo.name, self.__class__.__name__)
        candidates = self._process(photo.filename)
        print "Candidates found: %s" % ','.join(candidates)
        assert isinstance(candidates, set), "Candidates returned by '_process' must be a set type"

        return candidates
