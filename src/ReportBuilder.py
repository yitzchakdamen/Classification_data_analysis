

class ReportBuilder:
    
    
    @staticmethod
    def bild(*args) -> dict:
        dict_result = {}
        for arg in args:
            dict_result.update(arg)
        return dict_result