solicitapuerto = int(input('Ingrese su número de puerto: '))

if solicitapuerto >= 0 and solicitapuerto <= 1023:
    print(f'Su puerto {solicitapuerto} corresponde al rango de puertos bien conocidos (0-1023)')

elif solicitapuerto >= 1024 and solicitapuerto <= 49151:
    print(f'Su puerto {solicitapuerto} corresponde al rango de puertos registrados (1024-49151)')

elif solicitapuerto >= 49152 and solicitapuerto <= 65535:
    print(f'Su puerto {solicitapuerto} corresponde al rango de puertos dinámicos o privados (49152-65535)')

else:
    print(f'El número {solicitapuerto} no corresponde a ningún rango de puertos válido')

