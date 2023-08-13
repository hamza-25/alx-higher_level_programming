#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints lists object of python.
 * @p: p is Pointer to the list.
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
  
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
  i = 0;
	while (i < size)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    i++;
	}
}
