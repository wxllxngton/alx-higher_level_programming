#include <Python.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the PyObject representing the list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}


/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  [.] size: %ld\n", size);
	printf("  [.] trying string: %s\n", str);

	printf("  [.] first %ld bytes: ", (size < 10) ? size : 10);
	for (i = 0; i < size && i < 10; i++)
		printf("%02hhx ", str[i]);
	printf("\n");
}


/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to the PyObject representing the float object
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  [.] value: %.17g\n", value);
}


