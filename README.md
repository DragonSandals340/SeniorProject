# SeniorProject
Senior Project Code.


## MCP23017 Directory

This will hold all code for the MCP device that we are using for the I/O expander.  This device is 16 pin so ideally we will need 4 of these to run the 64 read switches that are required to sense the chess pieces.

## Chess Board Options
-Stockfish

-Chessboard

### Stockfish

This will serve as the directory that we are using for the chess engine.  Stockfish is open source (GPL license). That means you can read the code, modify it, contribute back, and even use it in your own projects.  You can use Stockfish on your computer running Windows, macOS, or Linux, or on your iOS or Android device. So you can get world-class chess analysis, wherever you are.  Stockfish is one of the strongest chess engines in the world. It is also much stronger than the best human chess grandmasters. Stockfish is useful because there are a tone of resources and examples that use it.

### GameBoard

ChessBoard is an implementation of the laws of chess. It validates moves, tests game states, tests for checkmate etc. It is not a chess engine.  Unfortunately the original writer does not support it anymore.  ChessBoard is a Python implementation of the FIDE laws of chess. The main goal is to implement all applicable rules in a simple, straightforward way. The intention is not to be fast but to be easy to understand and to be complete. Many other implementation has known problems with castling, stalemate or other more or less special rules.Features:
- The moves of the pieces
- Castling
- En passant
- Check detection
- Checkmate detection
- Stalemate detection
- Draw by the fifty moves rule detection
- Draw by the three repetitions rule detection
- Get valid locations support
- Imoprt and export of Forsyth-Edwards Notation strings.
- Add text moves in the AN, SAN and LAN standards.
- Export moves in the AN, SAN and LAN standards.
- Undo and Redo.
- Goto a specified move.
