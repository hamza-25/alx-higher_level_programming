#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints lists object of python.
 * @p: p is Pointer to the list.
*/

void print_python_list_info(PyObject *p)
{
	PyListObject *object;
	long int size;
	int i;

	size =  = PyList_Size(p);
	object = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", object->allocated);
	i = 0;
	while (i < size)
	{
		printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[i])->tp_name);
		i++;
	}
}
