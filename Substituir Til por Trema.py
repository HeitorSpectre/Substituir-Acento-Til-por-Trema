import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Extensões de arquivos suportadas
EXTENSOES_SUPORTADAS = (".q", ".txt", ".csv", ".ini", ".log")

# Mapeamento das substituições: de til para trema
substituicoes = {
    'ã': 'ä',
    'õ': 'ö',
    'Ã': 'Ä',
    'Õ': 'Ö'
}

def processar_arquivo(caminho_arquivo):
    encoding_utilizado = 'utf-8'
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except UnicodeDecodeError:
        try:
            encoding_utilizado = 'latin-1'
            with open(caminho_arquivo, 'r', encoding='latin-1') as f:
                conteudo = f.read()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo {caminho_arquivo}:\n{e}")
            return

    # Realiza as substituições
    for original, novo in substituicoes.items():
        conteudo = conteudo.replace(original, novo)

    try:
        with open(caminho_arquivo, 'w', encoding=encoding_utilizado) as f:
            f.write(conteudo)
        print(f"Processado: {caminho_arquivo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao escrever o arquivo {caminho_arquivo}:\n{e}")

def processar_arquivos(lista_arquivos):
    if not lista_arquivos:
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado!")
        return

    for caminho_arquivo in lista_arquivos:
        processar_arquivo(caminho_arquivo)

    messagebox.showinfo("Concluído", "Todos os arquivos foram processados com sucesso!")

def selecionar_arquivos():
    arquivos = filedialog.askopenfilenames(filetypes=[("Arquivos de Texto", ["*" + ext for ext in EXTENSOES_SUPORTADAS])])
    if arquivos:
        lista_arquivos.extend(arquivos)
        atualizar_lista()

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        arquivos_pasta = [
            os.path.join(pasta, f) for f in os.listdir(pasta) 
            if f.lower().endswith(EXTENSOES_SUPORTADAS)
        ]
        if arquivos_pasta:
            lista_arquivos.extend(arquivos_pasta)
            atualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo de texto encontrado na pasta selecionada.")

def limpar_lista():
    lista_arquivos.clear()
    atualizar_lista()

def atualizar_lista():
    lista_arquivos_box.delete(0, tk.END)
    for arquivo in lista_arquivos:
        lista_arquivos_box.insert(tk.END, arquivo)

# Criar janela principal
root = tk.Tk()
root.title("Substituir Til por Trema")
root.geometry("600x400")

lista_arquivos = []

# Frame para botões
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

btn_selecionar_arquivos = tk.Button(frame_botoes, text="Selecionar Arquivos", command=selecionar_arquivos)
btn_selecionar_arquivos.pack(side=tk.LEFT, padx=5)

btn_selecionar_pasta = tk.Button(frame_botoes, text="Selecionar Pasta", command=selecionar_pasta)
btn_selecionar_pasta.pack(side=tk.LEFT, padx=5)

btn_limpar = tk.Button(frame_botoes, text="Limpar Lista", command=limpar_lista)
btn_limpar.pack(side=tk.LEFT, padx=5)

btn_processar = tk.Button(root, text="Processar Arquivos", command=lambda: processar_arquivos(lista_arquivos))
btn_processar.pack(pady=10)

# Lista de arquivos
lista_arquivos_box = tk.Listbox(root, width=80, height=15)
lista_arquivos_box.pack(pady=10)

# Executa a interface
root.mainloop()
