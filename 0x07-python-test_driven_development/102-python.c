#include <Python.h>
#include <stdio.h>

/**
 * Prints information about a Python string object.
 *
 * This function prints the data and length of a Python string object.
 * It checks if the given PyObject pointer is a valid Python string (unicode object)
 * using PyUnicode_Check. If it is a valid string, the UTF-8 representation and the
 * length of the string are obtained using PyUnicode_AsUTF8 and PyUnicode_GET_LENGTH
 * respectively. The function then prints the string data and its length.
 *
 * @param p (PyObject*): The Python string object to be printed.
 *
 * @return None.
 */
void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        Py_ssize_t size = PyUnicode_GET_LENGTH(p);
        const char *str = PyUnicode_AsUTF8(p);

        printf("String data: %s\n", str);
        printf("  Length: %zd\n", size);
    } else {
        printf("Invalid Python string.\n");
    }
}
