# Simple PDF Merger (Unificador de PDFs) 📄🤝

Um script Python extremamente simples e leve para juntar dois ou mais arquivos PDF em um único documento. Ideal para uso rápido no Kaggle, Google Colab ou localmente.

## 🚀 Como funciona
O script utiliza a biblioteca `PyPDF2` para ler os arquivos PDF fornecidos e mesclá-los em um novo arquivo de saída, mantendo a ordem desejada.

## 🛠️ Pré-requisitos
Antes de rodar o script, você precisará ter o Python instalado e a biblioteca `PyPDF2`.

```bash
pip install PyPDF2
```

## 💻 Como usar
No Kaggle / Google Colab:
1 - Faça o upload dos PDFs que deseja juntar.
2 - Copie o código do arquivo main.py para uma célula.
3 - Altere os nomes das variáveis arquivo1 e arquivo2 para os nomes dos seus arquivos.
4 - Execute a célula e baixe o arquivo gerado.

## Localmente (Terminal):
1 - Clone este repositório:
 git clone https://github.com/seu-usuario/nome-do-repositorio.git
2 - Coloque seus PDFs na mesma pasta do script.
3 - Execute o script:
 python main.py

## 📜 Código Principal
Python

from PyPDF2 import PdfWriter

merger = PdfWriter()

 Adicione quantos arquivos quiser na lista abaixo
arquivos = ["arquivo1.pdf", "arquivo2.pdf"]

for pdf in arquivos:
    merger.append(pdf)

merger.write("pdf_final_unificado.pdf")
merger.close()
