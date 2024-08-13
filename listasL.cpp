class Nodo{
public:
    int datos;
    Nodo *siguientePtr;
};
class Lista
{
private:
    Nodo *primeroPtr;
    bool estaVacia();
public:
    Lista();
    ~Lista();
    void insertarAlInicio(int valor);
    void recorfreIterativo();
    
};
bool Lista::estaVacia()
{
    return primeroPtr == NULL;
}
Lista::Lista()
{
    primeroPtr=NULL;
}
Lista::~Lista()
{
    if (!estaVacia())
    {
        std::cout<<"\n\nDestruyendo nodos... \n\n";
        Nodo *actualPtr=primeroPtr;
        Nodo *temPtr;
        
        while (actualPtr !=NULL)
        {
            temPtr=actualPtr;
            std::<<temPtr->datos<<'';
            actualPtr=actualPtr->siguientePtr;
            delete temPtr;
        }
        
    }
    std::<<"\n\nSe destruyeron todos los nodos\n\n";
    
}
void Lista::insertarAlInicio(int valor)
{
    Nodo *nuevoPtr=new Nodo();
    nuevoPtr->datos=valor;
    if (estaVacia())
    {
        nuevoPtr->siguientePtr=NULL;
    }
    else
    {
        nuevoPtr->siguientePtr=primeroPtr;
    }
    primeroPtr = nuevoPtr;
    
}
void Lista::recorfreIterativo()
{
    if (estaVacia())
    {
        std::cout<<"\nLa lista esta vacia\n\n";
        system("pause");
        return;
    }
    Nodo *actualPtr=primeroPtr;
    std::cout<<"\nLos elementos de la lista son: ";

    while (actualPtr!=NULL)
    {
        std::<<actualPtr->datos<<"->";
        actualPtr=actualPtr->siguientePtr;
    }
    std::cout<<"\n\n";
    system("pause");
    
    
}
void menu()
{
    system("cls");
    std::cout<<"\n ..[LISTA SIMPPLEMENTE LIGADA]";
    std::cout<<"\n Insertar elemento al inicio\n";
    std::cout<<"[1] inseetar elemento al inicio \n";
    std::cout<<"[2] Imprimir los valores de la lista \n";
    std::cout<<"\nIngrese opcion :";
}
int main()
{
    int opcion;
    int valor;
    Lista ListaEnteros;

    system("color 1F");
    do
    {
        menu();
        cin >> opcion
        switch (opcion)
        {
        case 1: /* constant-expression */:
              std::cout<<"\nIngrese valor entero: ";
              cin>>valor;
              ListaEnteros.insertarAlInicio(valor);
              ListaEnteros.recorreIterativo();

            break;
        case 2:
            ListaEnteros.recorreIterativo();
            break;
        
        
        }
    } while (opcion != 3);
    return 0;
    
}