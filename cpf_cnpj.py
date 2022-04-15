from validate_docbr import CPF
from validate_docbr import CNPJ

class documentos:

     @staticmethod
     def cria_documento(documento):
         if len(documento) == 11:
             return doc_cpf(documento)
         elif len(documento) == 14:
             return doc_cnpj(documento)

class doc_cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("Documento Inválido!")

    def __str__(self):
        return self.cpf_formatado()

    def cpf_valido(self, cpf):
        validador_cpf = CPF()
        return validador_cpf.validate(cpf)

    def cpf_formatado(self):
        mascara_cpf = CPF()
        return mascara_cpf.mask(self.cpf)


class doc_cnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.cnpj_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("Documento Inválido!")

    def __str__(self):
        return self.cnpj_formatado()

    def cnpj_valido(self, cnpj):
        validador_cnpj = CNPJ()
        return validador_cnpj.validate(cnpj)


    def cnpj_formatado(self):
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.cnpj)

'''
class cpf_cnpj_class:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if tipo_documento == "cpf":
            if self.cpf_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif tipo_documento == "cnpj":
            if self.cnpj_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")


    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.cpf_formatado()
        elif self.tipo_documento == "cnpj":
            return self.cnpj_formatado()
        else:
            raise ValueError("Documento Inválido!")



    def cnpj_valido(self, cnpj):
        if len(cnpj) == 14:
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos Inválida!")



    def cnpj_formatado(self):
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.cnpj)
'''
