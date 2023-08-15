#include <Python.h>

/**
 * print_python_list_info - print list of python using c code.
 * @p: pointer to list object.
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size, i, size_allocate;
	PyObject *ob;

	size_allocate = ((PyListObject *)p)->allocated;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", size_allocate);
	i = 0;
	while (i < size)
	{
		ob = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(ob)->tp_name);
		i++;
	}
}
