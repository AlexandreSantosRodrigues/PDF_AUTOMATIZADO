!pip install PyPDF2 -q

from PyPDF2 import PdfWriter

arquivo1 = "cole aqui o caminho"
arquivo2 = "cole aqui o caminho2"
nome_saida = "pdf_final_unificado.pdf"

merger = PdfWriter()

for pdf in [arquivo1, arquivo2]:
    merger.append(pdf)

merger.write(nome_saida)
merger.close()

print(f"Sucesso! O arquivo '{nome_saida}' foi gerado.")
