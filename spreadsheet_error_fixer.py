class ErrorFixer:
    def __init__(self, spreadsheet):
        self.spreadsheet = spreadsheet

    @classmethod
    def cpf_fixer(cls, cpf):
        cpf_clean = cls.numeric_filter(cpf).strip(".0")
        if len(cpf_clean) == 11:
            return cpf_clean[:3] + "." +\
                   cpf_clean[3:6] + "." +\
                   cpf_clean[6:9] + "-" +\
                   cpf_clean[9:]
        else:
            return "000.000.000-00"

    @classmethod
    def telephone_fixer(cls, telephone):
        telephone_clean = cls.numeric_filter(telephone).strip(".0")
        if 8 < len(telephone_clean) < 15:
            return "(" + telephone_clean[:2] + ") " +\
                         telephone_clean[2:6] + "-" +\
                         telephone_clean[6:]
        else:
            return "(00) 0000-0000"

    @classmethod
    def birthday_fixer(cls, birthday):
        birthday_clean = cls.numeric_filter(birthday)
        if len(birthday_clean) == 19:
            return birthday_clean[8:10] + "/" +\
                   birthday_clean[5:7] + "/" +\
                   birthday_clean[0:4]
        else:
            return "00/00/0000"

    def numeric_filter(data):
        if data is None:
            return '00000000000'
        else:
            numeric_clean = filter(lambda x: x.isdigit, str(data))
            return "".join(numeric_clean)
