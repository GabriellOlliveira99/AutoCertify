import openpyxl;
from PIL import Image, ImageDraw, ImageFont;
from datetime import datetime;

workbook_alunos = openpyxl.load_workbook('nameFicticios.xlsx')
sheet_alunos = workbook_alunos['Planilha1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2, max_row=2)):
    name_alunos = linha[0].value #NOME ALUNOS
    date_curso = linha[1].value #DATA DO CURSO
    emissao_cert = linha[2].value #DATA DE EMISSÃO
    
    font_nome = ImageFont.truetype('./Courgette-Regular.ttf',90)
    font_geral = ImageFont.truetype('./georgia.ttf', 40)

    image = Image.open('./certificado.png')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((700,600), name_alunos, fill='black', font=font_nome)
    desenhar.text((1050,823), date_curso, fill='black', font=font_geral)
    # desenhar.text((1050,823), emissao_cert, fill='black', font=font_geral)

    image.save(f'./{indice}{name_alunos} certificado.png')