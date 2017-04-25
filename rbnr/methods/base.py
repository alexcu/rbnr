class BaseRecognitionMethod:
    '''
    Abstract class for base recognition method
    '''
    def _process(self, filename):
        '''
        Internal processing for subclass to be overidden
        '''
        raise NotImplementedError("Private method '_process' called on BaseRecognitionMethod")

    def process(self, filename):
        '''
        Processes the recognition method on the given file
        '''
        candidates = _process(filename)
        assert isinstance(candidates, set), "Candidates returned by '_process' must be a set type"
        return candidates
