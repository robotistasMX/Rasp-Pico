import machine
import utime

# Definir los pines que se van a utilizar
# para cada uno de los colores de cada LED

#RGB LED1
lr1 = machine.PWM(machine.Pin(1))
lg1 = machine.PWM(machine.Pin(2))
lb1 = machine.PWM(machine.Pin(3))
#RGB LED2
lr2 = machine.PWM(machine.Pin(4))
lg2 = machine.PWM(machine.Pin(5))
lb2 = machine.PWM(machine.Pin(6))
#RGB LED3
lr3 = machine.PWM(machine.Pin(7))
lg3 = machine.PWM(machine.Pin(8))
lb3 = machine.PWM(machine.Pin(9))
#RGB LED4
lr4 = machine.PWM(machine.Pin(10))
lg4 = machine.PWM(machine.Pin(11))
lb4 = machine.PWM(machine.Pin(12))
#RGB LED5
lr5 = machine.PWM(machine.Pin(13))
lg5 = machine.PWM(machine.Pin(14))
lb5 = machine.PWM(machine.Pin(15))

#Pines de LDR
ldrr =machine.ADC(28)
ldrg =machine.ADC(27)
ldrb =machine.ADC(26)


while True:
    
    # Lectura de cada fotoresistencia
    r = round (ldrr.read_u16())
    g = round (ldrg.read_u16())
    b = round (ldrb.read_u16())
    
    #Imprimir valor de las fotoresistencias
    print ("r: " + str(r))
    print ("g: " + str(g))
    print ("b: " + str(b))
    print (" ")
    
    utime.sleep(0.1)

    #Control color rojo
    lr1.duty_u16(r)
    lr2.duty_u16(r)
    lr3.duty_u16(r)
    lr4.duty_u16(r)
    lr5.duty_u16(r)
    
    #Control color verde
    lg1.duty_u16(g)
    lg2.duty_u16(g)
    lg3.duty_u16(g)
    lg4.duty_u16(g)
    lg5.duty_u16(g)
    
    #Control color azul
    lb1.duty_u16(b)
    lb2.duty_u16(b)
    lb3.duty_u16(b)
    lb4.duty_u16(b)
    lb5.duty_u16(b)
