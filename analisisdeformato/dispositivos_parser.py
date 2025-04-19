import json

with open('dispositivos.json', 'r') as json_file:
    dispositivos_data = json.load(json_file)

print('\n\nInformación de cada dispositivo: \n\n')

for i in dispositivos_data['dispositivos']:
    print('------------------')
    print(i['nombre'])
    print(i['ip'])
    print(i['estado'])
print('------------------')


