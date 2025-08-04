

class ReportBuilder:
    
    
    @staticmethod
    def bild(*args) -> dict:
        """
        Accepts arguments of dictionary
        returns a large dictionary containing all the dictionaries
        """
        dict_result = {}
        for arg in args:
            dict_result.update(arg)
        return dict_result