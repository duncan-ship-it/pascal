# pascal

## Description

Will generate and print `n` number of rows in Pascal's Triangle to the terminal, with the following colour scheme for each number:

| Multiple of...    | Colour  							       |
|-------------------|------------------------------------------|
| Neither 2 nor 3   | None	  							       |
| 2, not 3          |<span style="color:blue">Blue</span>      |
| 3, not 2   		|<span style="color:red">Red</span>	       |
| Both 2 and 3    	|<span style="color:purple">Purple</span>  |

## Display settings

By default, the terminal window width will be used to calculate the spacing for each line. This can be overridden by specifying the terminal's buffer width:

    > main.py 9999

which will provide more columns for rows to be displayed.

## Result

150 rows should look like this:

<img src="/assets/images/pascal.png" alt="Console view of result"/>