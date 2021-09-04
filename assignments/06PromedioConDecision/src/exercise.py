def main():
    #escribe tu código abajo de esta línea
x=0
z=0
y=0
while True:
    x=float(input())
    if x < 0:
        break
    else:
        y=y+x
        z=z+1
  
promedio=y/z
print(str(promedio))

    pass
if __name__=='__main__':
    main()
