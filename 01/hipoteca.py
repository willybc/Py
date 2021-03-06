# hipoteca.py
#1.8
##Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca
##Modificar el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.

#1.9
##¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?
##Modificá tu programa de forma que la información sobre pagos extras sea incorporada de manera versatil. 
##Agregá las siguientes variables antes del ciclo, para definir el comienzo, fin y monto de los pagos extras:

#1.10
#Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante. La salida debería verse aproximadamente así:

#1.13
#Corregir el codigo para que el pago del ultimo mes se ajuste a lo adecuado.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
total_pagado_interes = 0.0

pago_extra = 1000
duracion_extra = 12

contador_mes = 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

saldo_anterior = 0.0

while saldo > 0:
    contador_mes= contador_mes + 1

    saldo = (saldo * (1+tasa/12) ) - pago_mensual
    #condicion problema 1.8 Adelantos
    if duracion_extra > 0:
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra
        duracion_extra = duracion_extra -1

    #condicion 1.9 Calculadora de adelantos
    if contador_mes >= 61 and contador_mes <= 108:
        saldo = saldo -pago_extra
        total_pagado = total_pagado + pago_extra

    #condicion 1.11 Bonus
    if 0 >= saldo:
        saldo = saldo - saldo
        total_pagado = total_pagado + saldo_anterior 
    else:
        total_pagado = total_pagado + pago_mensual

    saldo_anterior = saldo
    print(contador_mes, total_pagado, saldo)
    #nota: si entra en la condicion , le sumo al total_pagado el saldo anterior con el interes incluido

print(f'total pagado sin interes:{total_pagado} en {contador_mes} meses')
