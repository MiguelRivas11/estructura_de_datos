import sys
    sys. path. append(* ../../')
from Stack import Stack
def inverseFile(file_path:str) → None:
11Invertir los contenidos de un archivo
S = Stack@
with Copen(file_path, 'r')) as f:
for lige iOf Dylines():
S. push(Tine)
with Copen( 'output.txt', 'w')) as n:
while not S.is_emptyO:
n. write(S. pop)