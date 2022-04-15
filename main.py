from cpf_cnpj import documentos

def main():
    cpf_1 = "35844295870"
    documento = documentos.cria_documento(cpf_1)
    print(documento)

    cnpj_1 = "30455375000107"
    documento2 = documentos.cria_documento(cnpj_1)
    print(documento2)

    #cpf_2 = cpf_class("12344295870")
    #print(cpf_2)

    #cpf_3 = cpf_class("44444295870")
    #print(cpf_3)

if __name__ == '__main__':
    main()
