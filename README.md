# Substituir-Acento-Til-por-Trema
Substituir Til por Trema é um utilitário Python com uma GUI Tkinter que substitui caracteres acentuados específicos (ã→ä, õ→ö, Ã→Ä, Õ→Ö) em arquivos de texto. Ele suporta vários formatos de texto, preserva a codificação UTF-8 original e está disponível como um executável (.exe) para uso fácil. 

### 📌 Sobre a Ferramenta  
"Substituir Til por Trema" é uma ferramenta essencial para quem trabalha com **tradução de jogos** e **edição de fontes**. Quando traduzimos um jogo para **português do Brasil**, um dos desafios é a adaptação da **fonte do jogo**, pois muitas delas não incluem o **acento til (~)**.  

Geralmente, as fontes dos jogos vêm com o **trema (¨)**, mas sem o til. Para resolver isso, editamos a **imagem da fonte** do jogo, substituindo os **dois pontinhos do trema** pelo **til (~)**. Dessa forma, quando o jogo exibe um caractere como "ä", ele aparece como "ã", porque editamos a imagem da fonte para fazer essa substituição visual.  

No entanto, dentro dos arquivos de texto do jogo, os textos traduzidos **geralmente são feitos com o til primeiro** para garantir a fidelidade da tradução. Depois que a tradução está pronta, precisamos substituir todos os caracteres com til pelos equivalentes com trema para que o jogo exiba corretamente os textos na fonte modificada. **Fazer essa substituição manualmente em vários arquivos pode ser demorado e propenso a erros, e é exatamente para isso que essa ferramenta existe: para automatizar esse processo de forma rápida e eficiente.**  

### 🔹 Como Funciona?  
✅ Substitui automaticamente:  
- `ã` → `ä`  
- `õ` → `ö`  
- `Ã` → `Ä`  
- `Õ` → `Ö`  

✅ **Mantém a codificação original** dos arquivos (UTF-8 ou fallback para latin-1).  
✅ **Suporta múltiplos tipos de arquivos** de texto (`.q`, `.txt`, `.csv`, `.ini`, `.log`, etc.).  
✅ **Permite processar vários arquivos ou uma pasta inteira de uma vez**.  
✅ **Interface gráfica fácil de usar** (sem necessidade de comandos complicados).  
✅ Disponível também como **executável (.exe)** para facilitar o uso sem precisar instalar Python.  

Essa ferramenta **economiza tempo** e **evita erros manuais**, tornando-se indispensável para quem traduz jogos e precisa adaptar textos para fontes personalizadas.
