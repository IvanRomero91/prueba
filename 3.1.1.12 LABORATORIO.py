ingreso=float(input("Ingrese el ingreso anual:"))

if ingreso<0.00:
    impuesto=0.00
elif ingreso<=556.02:
    impuesto=0.00
elif ingreso <= 85528.00:
    impuesto= (ingreso*0.18)-556.02 #exencion fiscal
elif ingreso> 85528.00 :
    impuesto= 14839.02 + ((ingreso-85528)*0.32)

if impuesto<0.00:
    impuesto=0.0

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")