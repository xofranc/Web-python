def narcisista(numero):
    return numero == sum(int(x) ** len(str(numero)) for x in str(numero))
        
print(narcisista(153))