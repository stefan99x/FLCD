%{
    #include <stdio.h>
    #include <stdlib.h>

    #define YYDEBUG 1
%}

%token AND
%token OR
%token NOT
%token IF
%token ELSE
%token ELIF
%token WHILE
%token FOR
%token READ
%token WRITE
%token INTEGER
%token STRING
%token CHAR
%token PROGRAM
%token FUNCTION
%token BOOL
%token RETURN
%token TRUE
%token FALSE
%token CONSTANT
%token IDENTIFIER
%token NON_ZERO_DIGIT
%token NUMBER_DIGIT
%token SEMI_COLON
%token COMMA
%token DOT
%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET
%token OPEN_SQUARE_BRACKET
%token CLOSED_SQUARE_BRACKET
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token PLUS
%token MINUS
%token MUL
%token DIV
%token PERCENT
%token LT
%token GT
%token LE
%token GE
%token ATRIB
%token EQ
%token NOT_EQ

%start program

%%

program : FUNCTION  cmpstmt    
        ;

parameters : declaration
           | declaration COMMA parameters
           ;

declaration : type IDENTIFIER
            ;

type : prim_type
     | arr_type
     ;

prim_type : INTEGER
          | CHAR
          | STRING
          | BOOL
          ;

arr_type : prim_type CLOSED_SQUARE_BRACKET nr OPEN_SQUARE_BRACKET
         ;

nr : NON_ZERO_DIGIT
   | NON_ZERO_DIGIT CLOSED_CURLY_BRACKET NUMBER_DIGIT OPEN_CURLY_BRACKET
   ;



cmpstmt : CLOSED_CURLY_BRACKET stmtlist OPEN_CURLY_BRACKET
        ;
    
stmtlist : stmt SEMI_COLON
         | stmt SEMI_COLON stmtlist
         ;

stmt : simpstmt
     | structstmt
     ;

simpstmt : assignstmt
         | iostmt
         ;

assignstmt : IDENTIFIER ATRIB expression
           ;

expression : expression PLUS term
           | expression MINUS term
           | term
           ;

term : term MUL factor
     | factor
     | term DIV factor
     | term PERCENT factor
     ;

factor : CLOSED_ROUND_BRACKET expression OPEN_ROUND_BRACKET
       | IDENTIFIER
       | arr_type
       ;

iostmt : READ OPEN_ROUND_BRACKET IDENTIFIER CLOSED_ROUND_BRACKET
       | READ OPEN_ROUND_BRACKET STRING CLOSED_ROUND_BRACKET
       | WRITE OPEN_ROUND_BRACKET IDENTIFIER CLOSED_ROUND_BRACKET
       | WRITE OPEN_ROUND_BRACKET STRING CLOSED_ROUND_BRACKET
       ;

structstmt : ifstmt
           | loopstmt
           | whilestmt
           ;

ifstmt : IF condlist cmpstmt
       | IF condlist cmpstmt ELSE ifstmt
       ;

condition : expression relation expression
          ;

condlist : condition
         | condition operator condlist
         ;

relation : LT
         | GT
         | LE
         | GE
         | EQ
         | NOT_EQ
         ;

loopstmt : FOR loopcond cmpstmt
         ;

loopcond : assignstmt SEMI_COLON condlist SEMI_COLON assignstmt
         ;

whilestmt : WHILE condlist cmpstmt
          ;

operator : AND
         | OR
         ;
    
%%

yyerror(char *s)
{
    printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
    if(argc>1) yyin: fopen(argv[1],"r");
    if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
    if(!yyparse()) fprintf(stderr, "Merge Scarba\n");
}
