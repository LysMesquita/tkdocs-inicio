from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get()) # ENTRADA
        #essa parte pega valor, "insere" no "feet" e converte a String para Float
        result = int(0.3048 * value * 10000.0 + 0.5)/10000.0 # PROCESSAMENTO
        #só a conta p/ conversão mesmo
        meters.set(result) # SAÍDA
        #ele pega e 'seta' o resultado nos metros (na variavel Meters)
    except ValueError:
        pass
# Ele imprime o erro (função do Pass)

#isso tudo acima é referente ao comando de converter (converter=) da linha 30

#Criando janela TK
root = Tk()
#Configurando título do app 
root.title("Pés para metros")

# criando o container (nossa "div")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
# nosso input (ttk.Entry):
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
#mainframe "inputa" ele na nossa div
# o width faz com que ele cresça até 7 pixeis. Quando puxarmos/expandrimos a janela, ele cresce junto ,as trava no 7 nesse caso
feet_entry.grid(column=2, row=1, sticky=(W, E))
# localiza essa "parte" no nosso grid (div). O sticky faz com que ele se expanda ao máximo que puder nas respectivas cardinalidades informadas. Precisa de pelo menos unma (mas podemos definir um limite de pixeis como acima)

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) #o Label é nosso texto (uma espécie de <p>)
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W) #quando for só uma cardinalidade no sticky, não precisamos de parenteses a mais

ttk.Label(mainframe, text="pés").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    #ele faz um For por todos os "filhos" do codigo (como se fossem varias divs em uma classe) 
    child.grid_configure(padx=5, pady=5)
    #aqui ele pega as "divs" e configura elas com um espaçamento entre si, horizontalmente e verticalmente de forma respectiva. Como se deixassemos uma margem entre os filhos para melhor organização
feet_entry.focus()
#para quando entrarmos no app/janela, a área de input ficar com aquele foco/barrinha piscando, para já abrirmos e inserirmos os valores (não temos que ficar clicando na área quando entrarmos)
root.bind("<Return>", calculate)
#aqui é para o Enter do nosso teclado fazer o mesmo papel que o ato de clicar no botão "Calcular"

# Gerando loop para renderização intermitente.
root.mainloop()