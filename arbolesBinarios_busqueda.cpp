#include <iostream>

using namespace std;

class Nodo
{
public:
    int dato;
    Nodo *izquierdoPtr;
    Nodo *derechoPtr;
};
class Arbol
{
private:
    Nodo *raizPtr;
    bool esVacio();
    void gotoxy(int x, int y);

public:
    Arbol();
    ~Arbol();
    Nodo *regresaRaiz();
    void insertarNodo(int valor, Nodo *&nodoPtr);
    void muestraAcostado(int nivel, Nodo *nodoPtr);
    void graficarArbol(Nodo *nodoPtr, int x, int n);
    bool busqueda(int x, Nodo *nodoPtr);
    Nodo *buscaMenor(Nodo *nodoPtr);
    Nodo *buscaMayor(Nodo *nodorPtr);
    void eliminarPredecesor(int x, Nodo *&nodoPtr);
    void eliminarSucesor(int x, Nodo *&nodoPtr);
    void preOrden(Nodo *nodoPtr);
    void postOrden(Nodo *nodoPtr);
    void inOrden(Nodo *nodoPtr);

    void recorridoNiveles(Nodo *nodoPtr);
    int altura(Nodo *nodoPtr);
    int contarHojas(Nodo *nodoPtr);
    int contarNodos(Nodo *nodoPtr);
    void arbolEspejo(Nodo *nodoPtr);
    bool esCompleto(Nodo *nodoPtr);
    bool esLleno(Nodo *nodoPtr);
    void podarArbol(Nodo *&nodoPtr);
};
Arbol::Arbol()
{
    raizPtr = NULL;
}
Arbol::~Arbol()
{
    podarArbol(raizPtr);
}
bool Arbol::esVacio()
{
    return raizPtr == NULL;
}
Nodo *Arbol::regresaRaiz()
{
    return raizPtr;
}
void Arbol::insertarNodo(int valor, Nodo *&nodoPtr)
{
    if (nodoPtr == NULL)
    {
        nodoPtr = new Nodo();
        nodoPtr->dato = valor;
        nodoPtr->izquierdoPtr = NULL;
        nodoPtr->derechoPtr = NULL;
    }
    else if (valor < nodoPtr->dato)
    {
        insertarNodo(valor, nodoPtr->izquierdoPtr);
    }
    else if (valor > nodoPtr->dato)
    {
        insertarNodo(valor, nodoPtr->derechoPtr);
    }
}
void Arbol::muestraAcostado(int nivel, Nodo *nodoPtr)
{
    if (nodoPtr == NULL)

        return;
    muestraAcostado(nivel + 1, nodoPtr->derechoPtr);
    for (int i = 0; i < nivel; i++)
        cout << "  ";
    cout << nodoPtr->dato << endl;
    muestraAcostado(nivel + 1, nodoPtr->izquierdoPtr);
}
void Arbol::inOrden(Nodo *nodoPtr)
{
    if (nodoPtr = NULL)
    {
        return;
        inOrden(nodoPtr->izquerdoPtr);
        cout << nodoPtr->dato << " - ";
        inOrden(nodoPtr->derechoPtr);
    }
}
void Arbol::preOrden(Nodo *nodoPtr)
{
    if (nodoPtr = NULL)
    {
        return;
        cout << nodoPtr->dato << "-";
        preOrden(nodoPtr->izquierdoPtr);
        preOdern(nodoPtr->derechoPtr);
    }
}
void Arbol::postOrden(Nodo *nodoPtr)
{
    if (nodoPtr N == NULL)
    {
        return;
        postOrden(nodoPtr->izquierdoPtr);
        postOrden(nodoPtr->derechoPtr);
        cout << nodoPtr->dato << "-";
    }
    bool Arbol::busqueda(int x, Nodo *nodoPtr)
    {
        if (nodoPtr == NULL)
        {
            return false;
        }
        else if (x < nodoPtr->dato)
        {
            return busqueda(x, nodoPtr->izquierdoPtr);
        }
        else if (x > nodoPtr->dato)
        {
            return busqueda(x, nodoPtr->derechoPtr);
        }
        else
        {
            return true;
        }
    }
}
void Arbol::podarArbol(Nodo *&nodoPtr)
{
    if (NodoPtr == NULL)
    {
        return;
        podarArbol(nodoPtr->izquierdoPtr);
        podarArbol(nodoPtr->derechoPtr);

        delete nodoPtr;
        nodoPtr = NULL;
    }
}
Nodo *Arbol::buscaMenor(Nodo *nodoPtr)
{
    if (nodoPtr == NULL)
    {
        return NULL;
    }
    else if (nodoPtr->izquierdoPtr == NULL)
    {
        return nodoPtr;
    }
    else
    {
        return buscaMenor(nodoPtr->izquierdoPtr);
    }
}
Nodo *Arbol::buscaMayor(Nodo *nodoPtr)
{
    if (nodoPtr NULL)
    {
        return NULL;
    }
    else if (nodoPtr->derechoPtr == NULL)
    {
        return nodoPtr;
    }
    else
    {
        return buscaMayor(nodoPtr->derechoPtr);
    }
}
void Arbol::eliminarPredecesor(int x, Nodo *&nodoPtr)
{
    if (nodoPtr == NULL)
    {
        return;
    }
    else if (x < nodoPtr->dato)
    {
        eliminarPredecesor(x, nodo->izquierdoPtr);
    }
    else if (x > nodoPtr->dato)
    {
        eliminarPredecesor(x nodoPtr->derechoPtr);
    }
    else if (nodoPtr->izquierdoPtr && nodoPtr->derecho->derechoPtr)
        ;
    {
        Nodo *mayor = buscaMayor(nodoPtr->izquierdoPtr);
        nodoPtr->dato = mayor->dato;
        eliminarPredecesor(mayor->dato, nodoPtr->izquierdoPtr);
    }
    else
    {
        Nodo *temp = nodoPtr;
        if (nodo->izquierdo == NULL)
        {
            nodoPtr = nodoPtr->derechoPtr;
        }
        else if (nodoPtr->derechoPtr == NULL)
        {
            nodoPtr = nodoPtr->izquierdoPtr;
        }
        delete temp;
    }
}
void Arbol::eliminarSucesor(int x, Nodo *&nodoPtr)
{
    if (nodoPtr == NULL)
    {
        return;
    }
    else if (x < nodoPtr->dato)
    {
        eliminarSucesor(x, nodoPtr->izquierdoPtr);
    }
    else if (x > nodoPtr->dato)
    {
        eliminarSucesor(x, nodoPtr->derechoPtr);
    }
    else if (nodoPtr->izquierdoPtr && nodoPtr->derechoPtr)
    {
        Nodo *menor = buscaMenor(nodoPtr->derecho);
        nodoPtr->= menor->dato;
        eliminarSucesor(menor->dato, nodoPtr->derchoPtr);
    }
    else
    {
        Nodo *temp = nodoPtr;
        if (nodoPtr->izquierdoPtr == NULL)
        {
            nodoPtr = nodoPtr->derechoPtr;
        }
        else if (nodoPtr->derechoPtr == NULL)
        {
            nodoPtr = nodoPtr->izquierdoPtr;
            delete temp;
        }
    }
}
int Arbol::altura(Nodo *nodoPtr)
{
    if (nodoPtr == NULL)
    {
        return = 0;
    }
    return (1 + max(altura(nodoPtr->izquierdoPtr), altura(nodoPtr->derechoPtr)));
}
int Arbol::contarHojas(Nodo *nodoPtr)
{
    if (nodoPtr = NULL)
        return = 0;

    if (nodoPtr->derechoPtr == NULL && nodoPtr->izquierdoPtr == NULL)
        return 1;
    else
        return contarHojas(nodoPtr->izquierdoPtr) + contarHojas(nodoPtr->derechoPtr);
}
int Arbol::contarNodos(Nodo *nodoPtr)
{
    if (nodoPtr == NULL)
    {
        return 0;
    }
    return 1 + contarNodos(nodoPtr->izquierdoPtr) + contarNodos(nodoPtr->derechoPtr);
}
void Arbol::recorridoNiveles(Nodo *nodoPtr)
{
    Nodo *nodoAuxiliar;
    queue<Nodo> colaAuxiliar;
    colaAuxilar.push(nodoPtr);

    while (!colaAuxiliar.empty())
    {
        cout << nodoAuxiliar->dato << "-";
        colaAuxiliar.pop();

        if (nodoAuxiliar->izquierdoPtr != NULL)
        {
            colaAuxiliar.push(nodoAuxiliar->izquierdoPtr);
        }
        if (nodoAuxiliar->derechoPtr != NULL)
        {
            colaAuxiliar.push(nodoAuxiliar->derechoPtr);
        }
    }
}
bool Arbol::esLleno(Nodo *nodoPtr)
{
    if (nodoPtr == NULL)

        return true;

    //
    if (nodoPtr->derechoPtr == NULL && nodoPtr->izquierdoPtr == NULL)

        return true;

    //
    if (nodoPtr->derechoPtr && nodoPtr->izquierdoPtr)
        return (esLleno(nodoPtr->izquierdo) && esLleno(nodoPtr->derechoPtr));

    //
    return false;
}
bool Arbol::esCompleto(nodo *nodoPtr)
{
    if (nodoPtr == NULL)
        return true;

    Nodo *nodoAuxiliar;
    queue<Nodo *> colaAuxiliar;
    colaAuxiliar.push(nodoPtr);
    bool nodoNoLleno = false;
    while (!colaAuxiliar.empty())
    {
        nodoAuxiliar = colaAuxiliar.front();
        colaAuxiliar.pop();

        if (nodoAuxiliar->izquierdoPtr)
        {
            if (nodoNoLleno == true)
                return false;
            colaAuxiliar.push(nodoAuxiliar->izquierdoPtr);
        }
        else
        {
            nodoLleno = true;
        }
        if (nodoAuxiliar->derechoPtr)
        {
            if (nodoNoLleno == true)
                return false;
            colaAuxiliar.push(nodoAuxiliar->derechoPtr);
        }
        else
        {
            nodoNoLleno = true;
        }
    }
    return true;
}

void Arbol::graficarArbol(Nodo *nodoPtr, int x, int y, int n)
{
    if (nodoPtr == NULL)
    {
        return;
    }
    gotoxy(x, y);
    cout << nodoPtr->dato;
    graficarArbol(nodoPtr->izquierdo, x - 15 + n * 6, y + 2, n + 1);
    graficarArbol(nodo->derecho, x + 15 - n * 6, y + 2, n + 1);
}
void Arbol::gotoxy(int x, int y)
{
    COORD coord;
    coord.x = x;
    coord.y = y;
    setConsoleCursorPosition(getStdHandle(STD_OUTPUT_HANDLE), coord);
}
void menu()
{
    system("cls");
    cout << "\n     ...[ARBOL BINARIO DE BUSQUEDA]...";
    cout << "\n ..[Erika mneses riko]..";
    cout << "[1] Insertar elemento\n";
    cout << "[2] Imprime el valor de la raiz\n";
    cout << "[3] Mostrar el arbol completo acostado con la raiz a la izquieda \n";
    cout << "[4] Graficar arbol completo\n";
    cout << "[5]buscar un elemento el el arbol\n";
    cout << "[6] Recorrer el arbol en preorden\n";
    cout << "[7] Recorrer el arbol en Inorden \n";
    cout << "[8] Recorrer el arbol en PostOrden\n";
    cout << "[9] Eliminar un nodo del arbol PRESWCESOR \n";
    cout << "[10] Eliminar un nodo del arbol SUCESOR \n";
    cout << "-----------------------------------------------------\n";
    cout << "[11] Recorrer el arbol por niveles (Amplitud) \n";
    cout << "[12] Altura del arbol \n";
    cout << "[13] cantidad de hojas del arbol\n";
    cout << "[14] Cantidad de nodos del arbol\n";
    cout << "[15] Mostar arbol espejo\n";
    cout << "[16] Revisa si es un arbol binario completo\n";
    cout << "[17]Revisa si es un arbol binario lleno\n ";
    cout << "[18] Construir el arbol 8,3,1,20,1,5,10,7,4 \n ";
    cout << "[19] Eliminar el arbol\n";
    cout << "[20] SALIR \n";
    cout << "\nIngrese opcion :";
}

int main()
{
    int opcion;
    int valor;
    int x;

    Arbol arbolEnteros;
    Nodo *raizArbolPtr = arbolEnteros.regresaRaiz();
    Arbol arbolCopiaEnteros;
    Nodo *raizArbolCopiaPtr = arbolCopiaEnteros.regresaRaiz();

    system("color 1f");

    do
    {
        menu();
        cin >> opcion;
        switch (opcion)
        {
        case 1:
            cout << "\nIngresa valor enteros:";
            cin >> valor;
            arbolEnteros.insertarNodo(valor, raizArbolPtr);
            cout << "\nLos elementos del arbol acostado con la raiz ala izquierda son: \n";
            arbolEnteros.muestraAcostado(0, raizArbolPtr);
            cout << "\n\n";
            system("pause");
            break;
        case 2:
            if (raizArbolPtr == NULL)
            {
                cout << "\nEl arbol esta vacio.\n\n";
                system("pause");
                break;
            }
            cout << "\nEl valor del nodo de raiz es :" << raizArbolPtr->dato << "\n\n";
            system("pause");
            break;
        case 3:
            if (raizArbolPtr == NULL)
            {
                cout << "\nEl arbo, esta vacio.\n\n";
                system("pause");
                break;
            }
            cout << "\nEl elementos del arbol acostado con la raiz a la izquierda son:\n\n ";
            arbolEnteros.muestraAcostado(0, raizArbolPtr);
            cout << "\n\n";
            system("pause");
            break;
        case 4:
            if (raizArbol == NULL)
            {
                cout << "\nEl arbol esta vacio.\n\n";
                system("pause");
                break;
            }
            system("cls");
            arbolEnteros.graficarArbol(raizArbolPtr, 45, 2, 0);
            cout << "\n\n\n\n\n\n";
            system("pause");
            break;
        case 5:
            if (raizArbol == NULL)
            {
                cout << "\nEl arbol esta vacio.\n\n";
                system("pause");
                break;
            }
            cout << "\nIngrese valor entero";
            cin >> x;
            if (arbolEnteros.busqyeda(x, raizArbolPtr) == true)

                cout << "\nElemento " << x << "ha sido encontrado en el arbol\n";
            else
                cout << "\nElemento no encontrado\n";

            //
            cout << "\nLos elementos del arbol acostado con la raiz a ala izquierda son: ";
            arbolEnteros.muestraAcostado(0, raizArbolPtr);
            cout << "\n\n";
            system("pause");
            break;
        case 6:
            if (raizArbol == NULL)
            {
                cout << "\nEl arbol esta vacio.\n\n";
                system("pause");
                break;
            }
            cout << "\nRecorrido en Preorden: ";
            arbolEnteros.preOrden(raizArbolPtr);
            cout << "\n\n";
            system("pause");
            break;
        case 7:
            if (raizArbol == NULL)
            {
                cout << "\nEl arbol esta vacio.\n\n";
                system("pause");
                break;
            }
            cout << "\nRecorrido de elementos en inOrden: ";
            arbolEnteros.inOrden(raizArbolPtr);
            cout << "\n\n";
            system("pause");
            break;
        case 8:
            if (raizArbol == NULL)
            {
                cout << "\nEl arbol esta vacio.\n\n";
                system("pause");
                break;
            }
            cout << "\nRecorrido en PostOrden: ";
            arbolEnteros.postOrden(raizArbolPtr);
            cout << "\n\n";
            system("pause");
            break;
        case 8:
            if (raizArbol == NULL)
            {
                cout << "\nEl arbol esta vacio.\n\n";
                system("pause");
                break;
            }
            cout << "\nIngrese el valor enetero a liminar PREDECESOR: ";
            cin >> x;
            arbolEnteros.eliminarPredecesor(x, raizArbolPtr);
            cout << "\nLos elementos del arbol acostado con la raiz izquieda son: ";
            arbolEnteros.muestraAcostado(0, raizArbolPtr);
            cout << "\n\n";
            system("pause");
            break;
        case 10:
            if (raizArbol == NULL)
            {
                cout << "\nEl arbol esta vacio.\n\n";
                system("pause");
                break;
            }
            cout << "\nIngrese el valor entero a liminar SUCESOR: ";
            cin >> x;
            arbolEnteros.eliminarSucesor(x, raizArbolPtr);
            cout << "\n\n";
            system("pause");
            break;
        case 11:
            cout << "\nRecorrido por niveles: ";
            arbolEnteros.recorridoNiveles(raizArbolPtr);
            cout << "\n\n";
            system("pause");
            break;

        case 12:

            cout << "\nLa altura del arbol es: " << arbolEnteros.altura(raizArbolPtr);

            cout << "\n\n";
            system("pause");
            break;
        case 13:
            cout << "\nEl numero de hojas del arbol es: " << arbolEnteros.contarNodos(raizArbolPtr);

            cout << "\n\n";
            system("pause");
            break;
        case 14:
            cout << "\nEl numero de nodos del arbol es: " << arbolEnteros.contarNodos(raizArbolPtr);

            cout << "\n\n";
            system("pause");
            break;
        case 15:
            cout << "\nLos elementos del arbol acostado son la raiz a la izquieda son: \n\n";
            arbolEnteros.muestraAcostado(0, raizArbolPtr);
            cout << "\n\n";
            if (arbolEnteros.esCompleto(raizArbolPtr))
            {
                cout << "\nSI es un arbol binario completo";
            }
            else
                cout << "\nNo es un arbol binario completo";

            //
            cout << "\n\n";
            system("pause");
            break;
        case 16:
            cout << "\nLos elementos del arbol con la raiz a ala izquierda son: \n\n";
            arbolEnteros.muestraAcostado(0, raizArbolPtr);
            cout << "\n\n";

            if (arbolEnteros.esLleno(raizArbolPtr))
            {
                cout << "\nSI es una arbol lleno";
            }
            else
            {
                cout << "\nNO es un arbol lleno";
            }
            cout << "\n\n";
            system("pause");
            break;

        case 17:
            arbolEnteros.insertarNodo(8, raizArbolPtr);
            arbolEnteros.insertarNodo(3, raizArbolPtr);
            arbolEnteros.insertarNodo(1, raizArbolPtr);
            arbolEnteros.insertarNodo(20, raizArbolPtr);
            arbolEnteros.insertarNodo(1, raizArbolPtr);
            arbolEnteros.insertarNodo(5, raizArbolPtr);
            arbolEnteros.insertarNodo(10, raizArbolPtr);
            arbolEnteros.insertarNodo(7, raizArbolPtr);
            arbolEnteros.insertarNodo(4, raizArbolPtr);
            std::cout << "\nLos elementos del arbol acostado con la raiz ala izquierda son: \n";
            arbolEnteros.muestraAcostado(0, , raizArbolPtr);
            std::cout << "\n\n";
            system("pause");
            break;
        case 18:
            arbolEnteros.podarArbol(raizArbolPtr);
            std::cout << "\nEl arbol ha sido podado.";
            std::cout << "\n\n";
            std::cout << "\n\n";
            system("pause");
            break;

        default:
            break;
        }
    } while (opcion != 19);
    return = 0;
}