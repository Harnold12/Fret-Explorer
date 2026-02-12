# 🎸 Fret Explorer **por Henrique Arnold**

![Fretboard Preview](assets/Fmin%20Pentatonic%20Print.png)

Este documento também está disponível em [Inglês (English)](README.md).

Um visualizador de braço de instrumentos de cordas desenvolvido inteiramente em **Python**.

---

## 📖 Descrição
O **Fret Explorer** é uma ferramenta para músicos que permite a visualização de escalas, tríades e intervalos em diversos instrumentos (Guitarra, Baixo, Ukulele, etc.). Suporta de 4 a 12 cordas com uma interface que se adapta em tempo real às necessidades do usuário.

---

## 🚀 Principais Recursos

* **Suporte Multi-Instrumento:** Ajuste dinâmico de 4 a 12 cordas. O app reconhece automaticamente afinações padrão do mercado para 4 a 9 cordas.
* **Modo Canhoto (Lefty Mode):** Inversão horizontal completa do braço, trastes e marcações.
* **Visualização Avançada de Notas:**
    * Labels dinâmicos (Notação Padrão vs. Intervalos).
    * **Sistema bicolor** (arcos) para identificar funções harmônicas duplas na mesma nota.
    * Limpeza rápida de cores secundárias com o botão direito.
* **Biblioteca de Escalas:** Acesso rápido a padrões como Maior, Menor Natural, Pentatônicas, Modos Gregos e Menor Harmônica.
* **Internacionalização:** Interface totalmente bilíngue (**Português** e **Inglês**) com troca instantânea.
* **Sistema de Presets:** Salve suas configurações favoritas em arquivos JSON para consulta posterior.
* **Validação de Dados:** Proteção contra notas inválidas e tratamento de caracteres 'X' para afinações personalizadas acima de 10 cordas.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12.9
* **GUI:** Tkinter (Interface Gráfica Nativa)
* **Persistência:** JSON (Armazenamento de Presets)

---

## 📋 Como Executar

> **Nota:** Estas instruções são baseadas em ambientes **Windows e macOS** e não incluem direções específicas para distribuições Linux.

0. **Para não programadores:** Baixe o executável diretamente na seção de [Releases](https://github.com/Harnold12/Fret-Explorer/releases) e execute-o. Caso o Windows avise sobre um "arquivo desconhecido", clique em *Mais informações* e *Executar assim mesmo*.
1. **Para rodar o código-fonte:** Certifique-se de ter o **Python 3.12.9** instalado em sua máquina.
2. Baixe o arquivo `fret.py`.
3. Execute o arquivo `fret.py` diretamente ou através da sua IDE de preferência.
4. O arquivo `guitar_presets.json` será criado automaticamente na mesma pasta ao salvar o primeiro preset.

---

## ⌨️ Atalhos e Dicas de Uso
* **Clique Esquerdo (na caixa de cor):** Abre o seletor de cores para a nota/intervalo.
* **Clique Direito (na caixa de cor secundária):** Limpa a cor secundária, retornando a nota para uma cor sólida.
* **⚙ Ajustes:** Abre a janela de configuração (apenas uma instância por vez).
* **Aplicar Alterações:** Atualiza afinação e cordas. Substitua todos os 'X' por notas válidas antes de aplicar.

---

## 📜 Resumo do Dev Log
O desenvolvimento seguiu uma sequência lógica de 26 etapas, partindo do mapeamento da escala cromática de 12 notas e renderização bimodal no Canvas do Tkinter, até a refatoração final para compactação do código e implementação das diferentes lógicas durante o processo de criação do executável.

---

## 👤 Autor
**Henrique Arnold**
* Estudante de Engenharia da Computação - SENAI CIMATEC
* Fret Explorer © 2026
