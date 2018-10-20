# Evaluation of chess libraries for Python

## Description

This project is in the context of a study project for a scientific approach for developing a chess AI. Therefore we will evaluate needed technologies, realize our project and document our used technologies and theoretical backgrounds as well as the implementation itself. Finally we will evaluate our results on the basis of our defined requirements and criteria.

This repository serves the purpose of evaluating chess libraries for Python with the aim of developing a chess AI.

Therefore the necessary functions for the chess game should be tested with different scripts. They should be stored, so that they can be reused later if necessary.

## Needed libraries

For completing all of our requirements, we need to find libraries for following purposes:

- chess core library for creating a chess board, calculating legal moves, push moves to board etc.
- library for game opening
- _(Optional)_ library for graphical user interface
- _(Optional)_ Implementation of chess.com API or similiar

Thereby we will search such libraries and evaluate them for following purposes:

*Chess Core:*
- Create chessboard
- Print chess board as ASCII
- Push moves to the chessboard 
- Calculating legal moves 
- Check for check / check mate 
- Test, if chess core recognize Rochade, En passant etc. as legal moves 
- Print chessboard as SVG to JupyterNotebook
- Test possibilities to save unique boards into csv
	
Furthermore we will test how following actions / calculations could be realized using the specific library:
- Calculate & print legal moves for one special figure
- Alternate user and ai input 
- Calculating board value & attacked figures
- Save moves / board progression with game context as csv
	
*Opening strategy library:*
- Having a list of possible opening strategies
- Choose a random opening strategy 
- Execute the choosen opening strategy turn by turn 
- implement this library in Chess Core library

*_(Optional)_ Chess.com API or similiar:*
- Access game engine via API
- get moves from user / current chessboard
- push moves to board 

*_(Optional)_ GUI library:*
- Print chessboard onto GUI
- Control user moves via GUI 
- Refresh board after every turn
	
Of course, a good documentation of the used libraries would also be very welcomned

## Organization

One python notebook will be created for every evaluated library. In those notebooks, all the necessary functions will be tested the belonging code snippets will be stored in it along with an explanation of the code as well as its purpose.

The different tests will be splitted between the development team. Therefore we will create Issued for every library and every purpose to test. Those issues will be organized with ZenHub.
To use this everyone has to download the Browser extension for either Chrome or Firefox. As soon as the plugin is installed you can switch to the ZenHub Board of our repository.

After every necessary library is evaluated and for every purpose a way to implement it has been found, the main project of the development of a chess AI with python can be started as well as the theoretical elaboration of the used methods, scientific backgrounds and used technologies.
 