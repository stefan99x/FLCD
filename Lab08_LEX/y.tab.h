/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    AND = 258,
    OR = 259,
    NOT = 260,
    IF = 261,
    ELSE = 262,
    ELIF = 263,
    WHILE = 264,
    FOR = 265,
    READ = 266,
    WRITE = 267,
    INTEGER = 268,
    STRING = 269,
    CHAR = 270,
    PROGRAM = 271,
    FUNCTION = 272,
    BOOL = 273,
    RETURN = 274,
    TRUE = 275,
    FALSE = 276,
    CONSTANT = 277,
    IDENTIFIER = 278,
    NON_ZERO_DIGIT = 279,
    NUMBER_DIGIT = 280,
    SEMI_COLON = 281,
    COMMA = 282,
    DOT = 283,
    OPEN_CURLY_BRACKET = 284,
    CLOSED_CURLY_BRACKET = 285,
    OPEN_SQUARE_BRACKET = 286,
    CLOSED_SQUARE_BRACKET = 287,
    OPEN_ROUND_BRACKET = 288,
    CLOSED_ROUND_BRACKET = 289,
    PLUS = 290,
    MINUS = 291,
    MUL = 292,
    DIV = 293,
    PERCENT = 294,
    LT = 295,
    GT = 296,
    LE = 297,
    GE = 298,
    ATRIB = 299,
    EQ = 300,
    NOT_EQ = 301
  };
#endif
/* Tokens.  */
#define AND 258
#define OR 259
#define NOT 260
#define IF 261
#define ELSE 262
#define ELIF 263
#define WHILE 264
#define FOR 265
#define READ 266
#define WRITE 267
#define INTEGER 268
#define STRING 269
#define CHAR 270
#define PROGRAM 271
#define FUNCTION 272
#define BOOL 273
#define RETURN 274
#define TRUE 275
#define FALSE 276
#define CONSTANT 277
#define IDENTIFIER 278
#define NON_ZERO_DIGIT 279
#define NUMBER_DIGIT 280
#define SEMI_COLON 281
#define COMMA 282
#define DOT 283
#define OPEN_CURLY_BRACKET 284
#define CLOSED_CURLY_BRACKET 285
#define OPEN_SQUARE_BRACKET 286
#define CLOSED_SQUARE_BRACKET 287
#define OPEN_ROUND_BRACKET 288
#define CLOSED_ROUND_BRACKET 289
#define PLUS 290
#define MINUS 291
#define MUL 292
#define DIV 293
#define PERCENT 294
#define LT 295
#define GT 296
#define LE 297
#define GE 298
#define ATRIB 299
#define EQ 300
#define NOT_EQ 301

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
