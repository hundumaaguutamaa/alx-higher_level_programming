#include <Python.h>
#include <stdio.h>
#include <float.h>

void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list = (PyListObject *)p;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_GET_SIZE(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);
    for (i = 0; i < size; i++)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}

void print_python_bytes(PyObject *p)
{
    long int size, i;
    char *str;

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    if (size > 10)
        size = 10;
    printf("  first %ld bytes:", size + 1);
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", str[i]);
    printf("\n");
}

void print_python_float(PyObject *p)
{
    double val;

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    val = PyFloat_AsDouble(p);
    printf("[.] float object info\n");
    if ((long int)val == val)
        printf("  value: %.16g.0\n", val);
    else
        printf("  value: %.16g\n", val);
}
