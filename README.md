# Instruction how to use Rounded Calculate Module

## How to install package 
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

### Calculator methods
<br/>
<p>All Calculator methods returns calculation result where operand 1 is current value of last memory entry calculation and operand 2 is called method parameter.</p><br/>
<br/>

<p>calculator.add(n)<br/>
Adds parameter n to last calculation of calculator outcome and returns new value.</p><br/>
<br/>
<p>calculator.substract(n)<br/>
Substracts parameter n to last calculation of calculator outcome.</p><br/>
<br/>
<p>calculator.multiply(n)<br/>
Multiplies last calculation of calculator outcome by power of parameter n.</p><br/>
<br/>
<p>calculator.divide(n)<br/>
Divides last calculation of calculator outcome by power of parameter n.</p><br/>
<br/>
<p>calculator.root(n)<br/>
Adds parameter n to last calculation of calculator outcome.</p><br/>
<br/>
<p>calculator.undo(n)<br/>
Removes last entry of calculator history.</p><br/>
<br/>
<p>calculator.reset_memory(n)<br/>
Deletes all calculations history, sets next calculation base to 0.</p><br/>