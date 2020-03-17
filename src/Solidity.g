// Copyright 2016-2019 Federico Bond <federicobond@gmail.com>
// Licensed under the MIT license. See LICENSE file in the project root for details.

grammar Solidity;


options
{
    language=Python;
	output=AST;
	k=2;
	backtrack=true;
	memoize=true;
}

tokens {
    Functioncall        ;     This                  ;     RegEx                   ;
    If                  ;     Regexchar             ;     Regexpid                ;
    Listarguments       ;     Var                   ;     Each                    ;
    Ident               ;     Function              ;     While                   ;
    Program             ;     VarDeclaration        ;     Expr                    ;
    Statements          ;     String                ;
    Integer             ;     List                  ;     Assignment              ;
    Return              ;     Number          	    ;
    DoWhile             ;     Break                 ;     For                     ;
    Continue            ;     Throw                 ;
    DefaultBlock        ;     With                  ;
    Label               ;     PropertyName          ;     Or                      ;
    And                 ;     Property              ;     New                     ;
    Ternary             ;     Index                 ;     Try                     ;
    BOr                 ;     BAnd                  ;     BXor                    ;
    MemberExpr          ;     Suffix                ;     Null                    ;
    Ltrue               ;     Lfalse                ;
    EmptyStatement      ;     ExpressionStatement   ;     VariableDeclarationList ;
    VariableStatement   ;     UnaryExpr             ;     FunctionExpr            ;
    Delete              ;     CatchClause           ;     FinallyClause           ;
    Void                ;     Typeof                ;     ObjectLiteral           ;
    ListCreation        ;     PropertyGet           ;     PropertySet             ;
    DebuggerStatement   ;     Contract              ;     Mapping                 ;
    Emit                ;     Tuple                 ;     Hex                     ;
    Array               ;     Modifier              ;     Constructor             ;
    Enum                ;     Struct                ;     State                   ;
    Scope               ;
}


sourceUnit
  : (pragmaDirective | importDirective | contractDefinition)* EOF;

pragmaDirective
  : 'pragma' pragmaName pragmaValue ';' ;

pragmaName
  : identifier ;

pragmaValue
  : version | expression ;

version
  : versionConstraint versionConstraint? ;

versionOperator
  : '^' | '~' | '>=' | '>' | '<' | '<=' | '=' ;

versionConstraint
  : versionOperator? VersionLiteral ;

importDeclaration
  : identifier ('as' identifier)? ;

importDirective
  : 'import' StringLiteral ('as' identifier)? ';'
  | 'import' ('*' | identifier) ('as' identifier)? 'from' StringLiteral ';'
  | 'import' '{' importDeclaration ( ',' importDeclaration )* '}' 'from' StringLiteral ';' ;

contractDefinition
  : ( 'contract' | 'interface' | 'library' ) identifier
    ( 'is' inheritanceSpecifier (',' inheritanceSpecifier )* )?
    '{' contractPart* '}' -> ^(Contract inheritanceSpecifier ^(Statements contractPart*) ^(Ident identifier));

inheritanceSpecifier
  : userDefinedTypeName ( '(' expression ( ',' expression )* ')' )? ;

//enumDefinition
//  : 'enum' identifier '{' enumValue? (',' enumValue)* '}' -> ^(Enum ^(Ident identifier) enumValue?);


contractPart
  : stateVariableDeclaration
  | usingForDeclaration
  | structDefinition
  | constructorDefinition
  | modifierDefinition
  | functionDefinition
  | eventDefinition
  | enumDefinition ;


stateVariableDeclaration
  : typeName
    ( PublicKeyword | InternalKeyword | PrivateKeyword | ConstantKeyword )*
    identifier ('=' expression)? ';'  -> ^(State typeName   ^(Ident identifier) expression);

usingForDeclaration
  : 'using' identifier 'for' ('*' | typeName) ';' ;

structDefinition
  : 'struct' identifier
    '{' ( variableDeclaration ';' (variableDeclaration ';')* )? '}'  -> ^(Struct ^(Ident identifier) variableDeclaration*);

constructorDefinition
  : 'constructor' parameterList modifierList block -> ^(Constructor parameterList modifierList ^(Statements block));

modifierDefinition
  : 'modifier' identifier parameterList? block -> ^(Modifier ^(Ident identifier parameterList? ^(Statements block)));

modifierInvocation
  : identifier ( '(' expressionList? ')' )? -> ^(Ident identifier expressionList?);

functionDefinition
  : 'function' identifier? parameterList modifierList returnParameters? ( ';' | block )  -> ^(Function ^(Ident identifier) parameterList );

returnParameters
  : 'returns' parameterList ;

modifierList
  : ( modifierInvocation | stateMutability | ExternalKeyword
    | PublicKeyword | InternalKeyword | PrivateKeyword )* ;

eventDefinition
  : 'event' identifier eventParameterList AnonymousKeyword? ';' ;

enumValue
  : identifier ;

enumDefinition
  : 'enum' identifier '{' enumValue? (',' enumValue)* '}' -> ^(Enum ^(Ident identifier) enumValue);

parameterList
  : '(' ( parameter (',' parameter)* )? ')' ;

parameter
  : typeName storageLocation? identifier? ;

eventParameterList
  : '(' ( eventParameter (',' eventParameter)* )? ')' ;

eventParameter
  : typeName IndexedKeyword? identifier? ;

functionTypeParameterList
  : '(' ( functionTypeParameter (',' functionTypeParameter)* )? ')' ;

functionTypeParameter
  : typeName storageLocation? ;

variableDeclaration
  : typeName storageLocation? identifier -> ^(Var storageLocation? ^(Ident identifier));

typeName
  : (elementaryTypeName | userDefinedTypeName | mapping -> ^(Mapping) | functionTypeName | 'address' 'payable') ('[' expression? ']')* ;

userDefinedTypeName
  : identifier ( '.' identifier )* ;

mapping
  : 'mapping' '(' elementaryTypeName '=>' typeName ')' ;

functionTypeName
  : 'function' functionTypeParameterList
    ( InternalKeyword | ExternalKeyword | stateMutability )*
    ( 'returns' functionTypeParameterList )? ;

storageLocation
  : 'memory' | 'storage' | 'calldata';

stateMutability
  : PureKeyword | ConstantKeyword | ViewKeyword | PayableKeyword ;

block
  : '{' statement* '}' ;

statement
  : ifStatement
  | whileStatement
  | forStatement
  | block
  | inlineAssemblyStatement
  | doWhileStatement
  | continueStatement
  | breakStatement
  | returnStatement
  | throwStatement
  | emitStatement
  | simpleStatement ;

expressionStatement
  : expression ';' -> expression;

//ifStatement
//  : 'if' '(' expression ')' statement ( 'else' statement )? ;

ifStatement:
  'if'  '('  expression  ')'  s1=statement ( 'else'  s2=statement)? -> ^(If expression $s1? $s2?) ;

whileStatement
  : 'while' '(' expression ')' statement -> ^(While expression statement);

simpleStatement
  : ( variableDeclarationStatement | expressionStatement ) ;

//forStatement
//  : 'for' '(' ( simpleStatement | ';' ) ( expressionStatement | ';' ) expression? ')' statement ;

forStatement:
   'for' LT* '(' ( LT* simpleStatement)? LT*  ';' ( LT* e1=expression)? LT* ';' ( LT* e2=expression)? LT* ')' LT* statement -> ^(For  ^(Expr  simpleStatement?)   ^(Expr $e1?) ^(Expr $e2?) statement )
	;

inlineAssemblyStatement
  : 'assembly' StringLiteral? assemblyBlock ;

doWhileStatement
  : 'do' statement 'while' '(' expression ')' ';' -> ^(DoWhile statement expression) ;

continueStatement
  : 'continue' ';' -> ^(Continue) ;

breakStatement
  : 'break' ';' -> ^(Break) ;

returnStatement
  : 'return' expression? ';' -> ^(Return expression?) ;

throwStatement
  : 'throw' ';' -> ^(Throw  expression ) ;

emitStatement
  : 'emit' functionCall ';' -> ^(Emit ^(Functioncall functionCall));

variableDeclarationStatement
  : ( 'var' identifierList | variableDeclaration | '(' variableDeclarationList ')' ) ( '=' expression )? ';';

variableDeclarationList
  : variableDeclaration? (',' variableDeclaration? )* ;


identifierList
  : '(' ( identifier? ',' )* identifier? ')' ;


Eexpression
	:(a=assignmentExpression->$a)
		(
			LT* ',' LT* b=assignmentExpression
			->   ^(ExpressionStatement $expression $b)
		)*
	;

expressionNoIn
	:(a=assignmentExpressionNoIn->$a)
		(
			LT* ',' LT* b=assignmentExpressionNoIn
			->   ^(ExpressionStatement $expressionNoIn $b)
		)*
	;

assignmentExpression:
   conditionalExpression
	| leftHandSideExpression LT* assignmentOperator LT* assignmentExpression -> ^(Assignment leftHandSideExpression assignmentOperator assignmentExpression)
	;

assignmentExpressionNoIn:
   conditionalExpressionNoIn
	| leftHandSideExpression LT* assignmentOperator LT* assignmentExpressionNoIn -> ^(Assignment leftHandSideExpression assignmentOperator assignmentExpressionNoIn)
	;

leftHandSideExpression:
    callExpression
	| newExpression
	;

NEW : 'new';

newExpression:
   memberExpression
	|  NEW LT* newExpression -> ^(New newExpression)
	;

pexp:
  primaryExpression                             -> ^(Expr primaryExpression)
  | 'new' LT* memberExpression LT* arguments    -> ^(New memberExpression arguments)

  ;


memberExpression:
   (p=pexp ->$p  )
   (
		(LT* memberExpressionSuffix)
		->
		 ^( MemberExpr $memberExpression  memberExpressionSuffix )
	)*
  ;



memberExpressionSuffix
	: indexSuffix
	| propertyReferenceSuffix
	;

callExpression
	: memberExpression LT* arguments (LT* callExpressionSuffix)* ->  ^(Functioncall memberExpression arguments callExpressionSuffix*)
	;

callExpressionSuffix
	: arguments
	| indexSuffix
	| propertyReferenceSuffix
	;

arguments
	: '(' (LT* assignmentExpression (LT* ',' LT* assignmentExpression)*)* LT* ')' -> ^(Listarguments assignmentExpression* )
	;

indexSuffix
	: '[' LT* expression LT* ']'  -> ^(Index expression)
	;


propertyReferenceSuffix
	: '.' LT* identifier -> ^(Property ^(Ident identifier ))
	;

assignmentOperator
	: '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|='
	;


conditionalExpression
	:(a=logicalORExpression->^(Expr $a))
		(
			LT* '?' LT* a1=assignmentExpression LT* ':' LT* a2=assignmentExpression
			->   ^(Ternary $conditionalExpression $a1 $a2)
		)?
	;


conditionalExpressionNoIn
	:(a=logicalORExpressionNoIn-> ^(Expr $a))
		(
			LT* '?' LT* a1=assignmentExpressionNoIn LT* ':' LT* a2=assignmentExpressionNoIn
			->   ^(Ternary $conditionalExpressionNoIn $a1 $a2)
		)?
	;

logicalORExpression
	:(a=logicalANDExpression->$a)
		(
			LT* '||' LT* b=logicalANDExpression
			->   ^(Expr $logicalORExpression Or $b)
		)*
	;


logicalORExpressionNoIn
	:(a=logicalANDExpressionNoIn->$a)
		(
			LT* '||' LT* b=logicalANDExpressionNoIn
			->   ^(Expr $logicalORExpressionNoIn Or $b)
		)*
	;




logicalANDExpression
	:(a=bitwiseORExpression->$a)
		(
			LT* '&&' LT* b=bitwiseORExpression
			->   ^(Expr $logicalANDExpression And $b)
		)*
	;


logicalANDExpressionNoIn
	:(a=bitwiseORExpressionNoIn->$a)
		(
			LT* '&&' LT* b=bitwiseORExpressionNoIn
			->   ^(Expr $logicalANDExpressionNoIn And $b)
		)*
	;

bitwiseORExpression
	:(a=bitwiseXORExpression->$a)
		(
			LT* '|' LT* b=bitwiseXORExpression
			->   ^(Expr $bitwiseORExpression BOr $b)
		)*
	;


bitwiseORExpressionNoIn
	:(a=bitwiseXORExpressionNoIn->$a)
		(
			LT* '|' LT* b=bitwiseXORExpressionNoIn
			->   ^(Expr $bitwiseORExpressionNoIn BOr $b)
		)*
	;



bitwiseXORExpression
	:(a=bitwiseANDExpression->$a)
		(
			LT* '^' LT* b=bitwiseANDExpression
			->   ^(Expr $bitwiseXORExpression BXor $b)
		)*
	;


bitwiseXORExpressionNoIn
	:(a=bitwiseANDExpressionNoIn->$a)
		(
			LT* '^' LT* b=bitwiseANDExpressionNoIn
			->   ^(Expr $bitwiseXORExpressionNoIn BXor $b)
		)*
	;



bitwiseANDExpression
	:(a=equalityExpression->$a)
		(
			LT* '&' LT* b=equalityExpression
			->   ^(Expr $bitwiseANDExpression BAnd $b)
		)*
	;


bitwiseANDExpressionNoIn
	:(a=equalityExpressionNoIn->$a)
		(
			LT* '&' LT* b=equalityExpressionNoIn
			->   ^(Expr $bitwiseANDExpressionNoIn BAnd $b)
		)*
	;


EQUSING:  ('==' | '!=' | '===' | '!==') ;


equalityExpression
	:(a=relationalExpression->$a)
		(
			LT* EQUSING LT* b=relationalExpression
			->   ^(Expr $equalityExpression EQUSING $b)
		)*
	;


equalityExpressionNoIn
	:(a=relationalExpressionNoIn->$a)
		(
			LT* EQUSING LT* b=relationalExpressionNoIn
			->   ^(Expr $equalityExpressionNoIn EQUSING $b)
		)*
	;


COMPSIGNOIN: ('<' | '>' | '<=' | '>=' | 'instanceof' );

TIN : 'in';

compsig : COMPSIGNOIN | TIN;

relationalExpression
	:(a=shiftExpression->$a)
		(
			LT* compsig LT* b=shiftExpression
			->   ^(Expr $relationalExpression compsig  $b)
		)*
	;

relationalExpressionNoIn
	:(a=shiftExpression->$a)
		(
			LT* COMPSIGNOIN LT* b=shiftExpression
			->   ^(Expr $relationalExpressionNoIn COMPSIGNOIN $b)
		)*
	;


SHIFTSIG: ('<<' | '>>' | '>>>');
shiftExpression
	:(a=additiveExpression->$a)
		(
			LT* SHIFTSIG LT* b=additiveExpression
			->   ^(Expr $shiftExpression SHIFTSIG $b)
		)*
	;

additiveExpression


	:	(a=multiplicativeExpression->$a)
                (  LT*  PLUSMINUS LT* b=multiplicativeExpression
                     -> ^(Expr $additiveExpression PLUSMINUS $b) // use previous rule result
                )*
	;

MULSIG:('*' | '/' | '%');

multiplicativeExpression
	:	(a=unaryExpression->$a)
                (  LT* MULSIG LT* b=unaryExpression
                     -> ^(Expr $multiplicativeExpression MULSIG  $b) // use previous rule result
                )*
	;

PLUSMINUS: ('+' | '-');

INCDEC:  ('++' | '--');


TDELETE :  'delete';
TVOID : 'void' ;
TTYPEOF : 'typeof';

fragment preunary :
	  TDELETE
	| TVOID
	| TTYPEOF
	| INCDEC
	| PLUSMINUS
	|  '~'
	| '!' ;

unaryExpression
	: postfixExpression
	| preunary LT* unaryExpression -> ^(UnaryExpr preunary unaryExpression )
	;

postfixExpression
	: (l=leftHandSideExpression -> $l)
		(  INCDEC -> ^(Expr $postfixExpression  INCDEC))?
	;

elementaryTypeName
  : 'address'  | 'bool' | 'string' | 'var' | Int | Uint | 'byte' | Byte | Fixed | Ufixed ;

Int
  : 'int' | 'int8' | 'int16' | 'int24' | 'int32' | 'int40' | 'int48' | 'int56' | 'int64' | 'int72' | 'int80' | 'int88' | 'int96' | 'int104' | 'int112' | 'int120' | 'int128' | 'int136' | 'int144' | 'int152' | 'int160' | 'int168' | 'int176' | 'int184' | 'int192' | 'int200' | 'int208' | 'int216' | 'int224' | 'int232' | 'int240' | 'int248' | 'int256' ;

Uint
  : 'uint' | 'uint8' | 'uint16' | 'uint24' | 'uint32' | 'uint40' | 'uint48' | 'uint56' | 'uint64' | 'uint72' | 'uint80' | 'uint88' | 'uint96' | 'uint104' | 'uint112' | 'uint120' | 'uint128' | 'uint136' | 'uint144' | 'uint152' | 'uint160' | 'uint168' | 'uint176' | 'uint184' | 'uint192' | 'uint200' | 'uint208' | 'uint216' | 'uint224' | 'uint232' | 'uint240' | 'uint248' | 'uint256' ;

Byte
  : 'bytes' | 'bytes1' | 'bytes2' | 'bytes3' | 'bytes4' | 'bytes5' | 'bytes6' | 'bytes7' | 'bytes8' | 'bytes9' | 'bytes10' | 'bytes11' | 'bytes12' | 'bytes13' | 'bytes14' | 'bytes15' | 'bytes16' | 'bytes17' | 'bytes18' | 'bytes19' | 'bytes20' | 'bytes21' | 'bytes22' | 'bytes23' | 'bytes24' | 'bytes25' | 'bytes26' | 'bytes27' | 'bytes28' | 'bytes29' | 'bytes30' | 'bytes31' | 'bytes32' ;

Fixed
  : 'fixed' | ( 'fixed' DecimalDigit+ 'x' DecimalDigit+ ) ;

Ufixed
  : 'ufixed' | ( 'ufixed' DecimalDigit+ 'x' DecimalDigit+ ) ;


expression
  : (Eexpression | 'new' typeName | '(' expression ')' | ('++' | '--') expression | ('+' | '-') expression | ('after' | 'delete') expression | '!' expression | '~' expression | primaryExpression) (('++' | '--') | '[' expression ']' | '(' functionCallArguments ')' | '.' identifier | '**' expression | ('*' | '/' | '%') expression | ('+' | '-') expression | ('<<' | '>>') expression | '&' expression | '^' expression | '|' expression | ('<' | '>' | '<=' | '>=') expression | ('==' | '!=') expression | '&&' expression | '||' expression | '?' expression ':' expression | ('=' | '|=' | '^=' | '&=' | '<<=' | '>>=' | '+=' | '-=' | '*=' | '/=' | '%=') expression)* ;

Msg : 'msg';

Block : 'block';

Abi : 'abi';

TTRUE : 'true';

TFALSE : 'false';

primaryExpression
  : TTRUE    -> ^(Ltrue )
  | TFALSE   -> ^(Lfalse )
  | numberLiteral   -> ^(Number numberLiteral)
  | HexLiteral      -> ^(Hex HexLiteral)
  | StringLiteral   -> ^(String StringLiteral)
  | tupleExpression -> ^(Tuple tupleExpression)
  | arrayLiteral -> ^(Array arrayLiteral)
  ;


arrayLiteral
  : identifier ('[' ']')?
  | elementaryTypeNameExpression ('[' ']')? ;

expressionList
  : expression (',' expression)* ;

nameValueList
  : nameValue (',' nameValue)* ','? ;

nameValue
  : identifier ':' expression -> ^(Ident identifier expression);

functionCallArguments
  : '{' nameValueList? '}'
  | expressionList? ;

functionCall
  : expression '(' functionCallArguments ')' -> ^(Functioncall expression  functionCallArguments);

assemblyBlock
  : '{' assemblyItem* '}' ;

assemblyItem
  : identifier
  | assemblyBlock
  | assemblyExpression
  | assemblyLocalDefinition
  | assemblyAssignment
  | assemblyStackAssignment
  | labelDefinition
  | assemblySwitch
  | assemblyFunctionDefinition
  | assemblyFor
  | assemblyIf
  | BreakKeyword
  | ContinueKeyword
  | subAssembly
  | numberLiteral
  | StringLiteral
  | HexLiteral ;

assemblyExpression
  : assemblyCall | assemblyLiteral ;

assemblyCall
  : ( 'return' | 'address' | 'byte' | identifier ) ( '(' assemblyExpression? ( ',' assemblyExpression )* ')' )? ;

assemblyLocalDefinition
  : 'let' assemblyIdentifierOrList ( ':=' assemblyExpression )? ;

assemblyAssignment
  : assemblyIdentifierOrList ':=' assemblyExpression ;

assemblyIdentifierOrList
  : identifier | '(' assemblyIdentifierList ')' ;

assemblyIdentifierList
  : identifier ( ',' identifier )* ;

assemblyStackAssignment
  : '=:' identifier ;

labelDefinition
  : identifier ':' ;

assemblySwitch
  : 'switch' assemblyExpression assemblyCase* ;

assemblyCase
  : 'case' assemblyLiteral assemblyBlock
  | 'default' assemblyBlock ;

assemblyFunctionDefinition
  : 'function' identifier '(' assemblyIdentifierList? ')'
    assemblyFunctionReturns? assemblyBlock ;

assemblyFunctionReturns
  : ( '->' assemblyIdentifierList ) ;

assemblyFor
  : 'for' ( assemblyBlock | assemblyExpression )
    assemblyExpression ( assemblyBlock | assemblyExpression ) assemblyBlock ;

assemblyIf
  : 'if' assemblyExpression assemblyBlock ;

assemblyLiteral
  : StringLiteral | DecimalNumber | HexNumber | HexLiteral ;

subAssembly
  : 'assembly' identifier assemblyBlock ;

tupleExpression
  : '(' ( expression? ( ',' expression? )* ) ')'
  | '[' ( expression ( ',' expression )* )? ']' ;

elementaryTypeNameExpression
  : elementaryTypeName ;

numberLiteral
  : (DecimalNumber | HexNumber) NumberUnit? ;

identifier
  : ('from' | 'calldata' | Identifier) ;

VersionLiteral
  : DecimalDigit+ '.' DecimalDigit+ '.' DecimalDigit+ ;

BooleanLiteral
  : 'true' | 'false' ;

DecimalNumber
  : (DecimalDigit+ | (DecimalDigit* '.' DecimalDigit+) ) ( ('e'|'E') DecimalDigit+ )? ;

HexNumber
  : '0' '[xX]' HexDigit+ ;

NumberUnit
  : 'wei' | 'szabo' | 'finney' | 'ether'
  | 'seconds' | 'minutes' | 'hours' | 'days' | 'weeks' | 'years' ;

HexLiteral : 'hex' ('"' HexPair* '"' | '\'' HexPair* '\'') ;

fragment HexPair
  : HexDigit HexDigit ;

//fragment HexCharacter
//  : '[0-9A-Fa-f]' ;

ReservedKeyword
  : 'abstract'
  | 'after'
  | 'case'
  | 'catch'
  | 'default'
  | 'final'
  | 'in'
  | 'inline'
  | 'let'
  | 'match'
  | 'null'
  | 'of'
  | 'relocatable'
  | 'static'
  | 'switch'
  | 'try'
  | 'type'
  | 'typeof' ;

AnonymousKeyword : 'anonymous' ;
BreakKeyword : 'break' ;
ConstantKeyword : 'constant' ;
ContinueKeyword : 'continue' ;
ExternalKeyword : 'external' ;
IndexedKeyword : 'indexed' ;
InternalKeyword : 'internal' ;
PayableKeyword : 'payable' ;
PrivateKeyword : 'private' ;
PublicKeyword : 'public' ;
PureKeyword : 'pure' ;
ViewKeyword : 'view' ;

Identifier
  : IdentifierStart IdentifierPart* ;

fragment IdentifierStart
//  : '[a-zA-Z$_]';
    : Char
    | '$'
    | '_' ;

fragment IdentifierPart
//    : '[a-zA-Z0-9$_]' ;
    : '$'
    | '_'
    | Char
    | DecimalDigit ;

StringLiteral
    : '"' DoubleStringCharacter* '"'
    | '\'' SingleStringCharacter* '\''
    ;

fragment DoubleStringCharacter
	: ~('"' | '\\' | LT)
	| '\\' EscapeSequence
	;

fragment SingleStringCharacter
	: ~('\'' | '\\' | LT)
	| '\\' EscapeSequence
	;

fragment EscapeSequence
	: CharacterEscapeSequence
	| '0'
	| HexEscapeSequence
	| UnicodeEscapeSequence
	;

fragment CharacterEscapeSequence
	: SingleEscapeCharacter
	| NonEscapeCharacter
	;

fragment SingleEscapeCharacter
	: '\'' | '"' | '\\' | 'b' | 'f' | 'n' | 'r' | 't' | 'v'
	;

fragment NonEscapeCharacter
	: ~(EscapeCharacter | LT)
	;

fragment EscapeCharacter
	: SingleEscapeCharacter
	| DecimalDigit
	| 'x'
	| 'u'
	;

fragment HexEscapeSequence
	: 'x' HexDigit HexDigit
	;

fragment UnicodeEscapeSequence
	: 'u' HexDigit HexDigit HexDigit HexDigit
	;

fragment HexDigit
	: DecimalDigit | ('a'..'f') | ('A'..'F')
	;

fragment DecimalDigit
	: ('0'..'9')
	;

fragment Char
    : ('a'..'z')
    | ('A'..'Z')
    ;

Comment:
	'/*' (options {greedy=false;} : .)* '*/' {$channel=HIDDEN;}
	;

LineComment:
	'//' ~(LT)* {$channel=HIDDEN;}
	;

LT:
	'\n'		// Line feed.
	| '\r'		// Carriage return.
	| '\u2028'	// Line separator.
	| '\u2029'	// Paragraph separator.
	;

WhiteSpace:
	('\t' | '\r' | '\n' | ' ' | '\u000C')	{$channel=HIDDEN;}
	;
