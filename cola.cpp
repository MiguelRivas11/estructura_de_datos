
class Nodo
{
	public:
		int dato;
		Nodo *siguientePtr;
};
class Cola
{
private:
		Nodo *inicioPtr;
		Nodo *finalPtr;
		bool estaVacia();
		
public:
Cola();
~Cola();
void mete(int valor);
void saca();
int nodoInicio();
int nodoFinal();
void muestra();
void mueve(Cola c);
int cantidadElementos();
int nodoMayor();
void eliminaNodo(int referencia);
void mezcla(Cola c1, Cola c2);		
};

bool Cola::estaVacia()
{
	if(inicioPtr == NULL && finalPtr == NULL)
     return 1;
    else
        return 0;

	
}
Cola::Cola()
{
    inicioPtr = NULL;
    finalPtr = NULL;


}
Cola::~Cola()
{
    while (!estaVacia())
    {
        saca();
    }
    
}
void Cola::saca()
{
    if (estaVacia())
    {
        std::cout <<"Error en saca(). La cola esta vacia\n\n";
        exit(1);
        return;
    }
    Nodo *tempPtr = inicioPtr;
    inicioPtr = inicioPtr -> siguientePtr;
     if (inicioPtr == NULL)
     {
        finalPtr = NULL;
     }
     delete tempPtr;
     
    
}
void Cola:: mete(int valor)
{
    Nodo *nuevoPtr = new Nodo();
    nuevoPtr -> dato = valor;
    nuevoPtr -> siguientePtr = NULL;

    if (finalPtr != NULL)
    {
        finalPtr -> siguientePtr = nuevoPtr;
    }
    finalPtr = nuevoPtr;
    if (inicioPtr == NULL)
    {
        inicioPtr = nuevoPtr;
    }
    
    
}
 int Cola:: nodoInicio()
 {
    if (inicioPtr == NULL)
    {
        std::cout<<"Error en nodoInicio(). La cola esta vacia";
        exit(1);

    }
    return inicioPtr -> dato;
    
 }
 void Cola::muestra()
 {
    if (estaVacia())
    {
        std::cout<<"\nLa cola esta vacia";
        system("pause");
        return;
    }
    Cola aux;
    int x;
    std::cout<<"\nLos elementos de la cola son:";

    while (!estaVacia())
    {
        x = nodoIncio();
        std::<< x << " ->";
        saca();
        aux.mete(x);
    }
    while (!aux.estaVacia())
    {
        x = aux.nodoInicio();
        aux.saca();
        mete(x);
    }
    std::cout<<"\n\n";
    system("pause");
    
    
    
 }
 void Cola::mueve(Cola & c)
 {
    int x;
    while (!c.estaVacia())
    {
        x = c.nodoInicio();
        c.saca();
        mueve(x);
    }
    
 }
  void Cola::eliminaNodo(int referencia)
  {
    if (estaVacia())
    {
        std::cout<<"\nEl nodo dado como referencia no se encuentra en la cola.\n";
        return;
    }
    Cola aux;
    int x;
    bool encotrado = false;

    while (!estaVacia())
    {
        x = nodoInicio();
        saca();
        if (referencia == x)
        {
            std::cout<<"\nEliminado nodo: "<< x << "\n";
            encotrado = true;
        }
        else
            aux.mete(x);

        
    }
mueve(aux);
if (!encotrado)
{
    std::cout<<"\nEl nodo dado como referencia no se encuentra en la cola.\n";

}
  
}
int Cola::cantidadElementos()
{
    if (estaVacia())
    {
        return 0;
    }
    Cola aux;
    int x ;
    int cout =0;

    while (!estaVacia())
    {
        x = nodoInicio();
        saca();
        aux.mete(x);
        cout++;
    }
    mueve(aux);
    return cout;
    
    
}