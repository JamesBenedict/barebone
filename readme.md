# Barebone
A simple starting point to develop javascript programs or media. 

## Featutres
* Server with live reload 
* Sass compiler
* D3 and handlebars included

## Getting started
The program was developed for python 3 but should run with python 2.7, which is installed by default on Macs. 

Navigate into the project directory  
```
cd barebone
```

Install dependencies  
```
python install.py
```

Launch the program   
``` 
python barebone.py 
 ```

## Compiling notes
The program looks for changes to `./style/sass/styles.scss` and then compiles it into `./style/css/style.css`. You can add more files to watch in `barebone.py` by repeating the following line in the `sever()` function.
```
server.watch('<PATH TO FILE TO WATCH>', compile_sass)
```

## Server notes
The sever runs from port 8080 by default. If you are trying to run multiple instances of a server, alter the port number on one of your files. 

