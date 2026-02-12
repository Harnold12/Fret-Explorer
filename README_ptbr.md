\# 🎸 Fret Explorer \*\*por Henrique Arnold\*\*

Um visualizador de braço de instrumentos de corda desenvolvido
inteiramente em \*\*Python\*\*.

\-\--

\## 📖 Descrição O \*\*Fret Explorer\*\* é uma ferramenta para músicos
que permite visualizar escalas, tríades e intervalos em diversos
instrumentos (Guitarra, Baixo, Ukulele, etc.). Suporta de 4 a 12 cordas
com uma interface que se adapta em tempo real às necessidades do
usuário.

\-\--

\## 🚀 Funcionalidades Principais

\* \*\*Suporte Multi-Instrumento:\*\* Ajuste dinâmico de 4 a 12 cordas.
O app reconhece padrões industriais de afinação para 4 a 9 cordas
automaticamente. \* \*\*Modo Canhoto (Lefty Mode):\*\* Inversão
horizontal completa do braço, trastes e marcações. \* \*\*Visualização
Avançada de Notas:\*\* \* Labels dinâmicos (Cifras Americanas vs.
Intervalos). \* Sistema de \*\*Cores Bicolores\*\* (arcos) para
identificar funções harmônicas duplas na mesma nota. \* Limpeza rápida
de cores secundárias com o botão direito do mouse. \* \*\*Biblioteca de
Escalas:\*\* Acesso rápido a padrões como Maior, Menor Natural,
Pentatônicas, Modos Gregos e Menor Harmônica. \*
\*\*Internacionalização:\*\* Interface totalmente bilíngue
(\*\*Português\*\* e \*\*Inglês\*\*) com troca instantânea. \*
\*\*Sistema de Presets:\*\* Salve suas configurações favoritas em
arquivos JSON para consulta posterior. \* \*\*Validação de Dados:\*\*
Proteção contra notas inválidas e tratamento de caracteres \'X\' para
afinações personalizadas acima de 10 cordas.

\-\--

\## 🛠️ Tecnologias Utilizadas \* \*\*Linguagem:\*\* Python 3.12.9 \*
\*\*GUI:\*\* Tkinter (Interface Gráfica Nativa) \* \*\*Persistência:\*\*
JSON (Armazenamento de Presets)

\-\--

\## 📋 Como Executar

\> \*\*Nota:\*\* Estas instruções são baseadas em ambientes \*\*Windows
e macOS\*\* e não incluem direcionamentos específicos para distribuições
Linux.

0\. \*\*Para usuários não-programadores:\*\* Baixe o executável
diretamente e execute-o. Caso o Windows alerte sobre um \"arquivo
desconhecido\", clique em \*Mais informações\* e \*Executar assim
mesmo\*. 1. \*\*Para rodar o código-fonte:\*\* Certifique-se de ter o
\*\*Python 3.12.9\*\* instalado em sua máquina. 2. Baixe o arquivo
\`fret.py\`. 3. Execute o arquivo \`fret.py\` diretamente ou através de
sua IDE de preferência (a maioria já deve possuir as bibliotecas
necessárias, visto que são nativas). 4. O arquivo
\`guitar_presets.json\` será criado automaticamente na mesma pasta ao
salvar o primeiro preset.

\-\--

\## ⌨️ Atalhos e Dicas de Uso \* \*\*Clique Esquerdo (na caixa de
cor):\*\* Abre o seletor de cores para a nota/intervalo. \* \*\*Clique
Direito (na caixa de cor secundária):\*\* Limpa a cor secundária,
voltando a nota para cor sólida. \* \*\*⚙ Ajustes:\*\* Abre a janela de
configurações (apenas uma instância por vez). \* \*\*Aplicar
Mudanças:\*\* Atualiza afinação e cordas. Substitua todos os \'X\' por
notas válidas antes de aplicar.

\-\--

\## 📜 Resumo do Dev Log O desenvolvimento seguiu uma ordem lógica de 26
etapas, partindo do mapeamento da escala cromática de 12 notas e
renderização bimodal no Canvas do Tkinter, até a refatoração final para
compactação de código e implementação de diferentes lógicas ao longo do
processo para a criação do executável.

\-\--

\## 👤 Autor \*\*Henrique Arnold\*\* \* Estudante de Engenharia da
Computação \* Fret Explorer © 2026
