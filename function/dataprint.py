def printsimples(x,y):
    '''
    função para imprimir DataFrame em linhas
    x = dataframe
    y = alinhamento:
    opções: (l = left, r = right, c = center)
    by: Romerito morais
    '''  
    import os
    from prettytable import from_csv
    export = 'temp.csv'
    dataframe = x
    alinhamento = y
    dataframe.to_csv(export)       
    arquivo = open(export)
    table = from_csv(arquivo)
    table.align = alinhamento
    arquivo.close()
    path = os.getcwd()
    dir = os.listdir(path)
    for file in dir:
        if file == export:
            os.remove(file)
    return print(table)