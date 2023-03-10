# Rounded calculator

## Features
<p> This package allows users to calculate addition, substraction, division, multiplication and power of n root of active memory value. Also package users can print history of calculations and undo last actions to access specific history values. All calculations made with this package are rounded to 8 decimal points.</p> 

### Getting started 
<p>Instalation of the Rounded Calculate package is done by running command <br/>
pip install rounded-calculate</p>

## Package usage

### Init Calculator
<p>Assign Calculator class to desired variable <br/>
calculator = Calculator()<br/>
<br/>
All the calculations made by the Calculator is based on value of the Calculator memory.<br/>
<br/>
Calculator class contains class of Memory which is storing all the history of calculations performed by using this package.   <br/>
</p>

### Calculator functions
<br/>
<p>All Calculator methods returns calculation result where operand 1 is current value of calculator memory and operand 2 is called method parameter. This do not apply for memory related methods.</p><br/>
<br/>

<p>calculator.add(n)<br/>
Adds parameter n to calculator memory value. Returns new calculator memory value.</p><br/>

<p>calculator.substract(n)<br/>
Substracts parameter n from calculator memory value. Returns new calculator memory value.</p><br/>

<p>calculator.multiply(n)<br/>
Multiplies calculator memory value by power of parameter n. Returns new calculator memory value.</p><br/>

<p>calculator.divide(n)<br/>
Divides calculator memory value by power of parameter n. Returns new calculator memory value.</p><br/>

<p>calculator.root(n)<br/>
Adds parameter n to last calculation of calculator outcome. Returns new calculator memory value.</p><br/>

<p>calculator.undo()<br/>
Removes last entry of calculator history.</p><br/>

<p>calculator.reset_memory()<br/>
Deletes all calculations history, sets next calculation base to 0.</p><br/>

<p>calculator.print_history()<br/>
Prints all calculations history.</p><br/>

## License

<p>Licensed under the MIT License.</p>