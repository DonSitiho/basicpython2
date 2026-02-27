#Agregamos librería para ejecutar comandos
import os
import subprocess

os.system("ls")

#Llamamos la función subprocess.run(), que es más eficiente, para eso tenemos que importar import subprocess.
#Lista completa de argumentos subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

subprocess.run(["ls"])

#Subprocess con dos argumentos
subprocess.run(["ls","-l"])

#Ahora vamos con trres argumentos
subprocess.run(["ls","-l","README.md"])

#La función subprocess es eficiente por que puede utilizar para ejcutar cualquier bash.
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#Ahora vamos a obtener información del disco
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
