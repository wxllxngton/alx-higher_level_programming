## 0x08-python-more_classes

**Requirements for `rectangle.py`:**

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area

<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<li>Class method <code>def square(cls, size=0):</code> that returns a new Rectangle instance with <code>width == height == size</code></li>
<li>You are not allowed to import any module</li>
</ul>

**Requirements for `101-nqueens.py`:**
<ul>
<li>Usage: <code>nqueens N</code>

<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<li>where N must be an integer greater or equal to <code>4</code>

<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<li>The program should print every possible solution to the problem

<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don’t have to print the solutions in a specific order</li>
</ul></li>
<li>You are only allowed to import the <code>sys</code> module</li>
</ul>
