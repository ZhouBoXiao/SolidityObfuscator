# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g 2019-04-11 18:34:54

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__50=50
NonEscapeCharacter=44
DecimalNumber=27
T__59=59
T__55=55
InternalKeyword=7
T__56=56
T__57=57
T__58=58
T__51=51
T__137=137
T__52=52
T__136=136
T__53=53
T__54=54
T__138=138
T__133=133
T__132=132
T__60=60
T__135=135
T__61=61
T__134=134
T__131=131
T__130=130
ViewKeyword=15
HexDigit=31
LINE_COMMENT=47
StringLiteral=5
Byte=19
T__66=66
CharacterEscapeSequence=40
T__67=67
T__129=129
T__68=68
T__69=69
T__62=62
T__126=126
T__63=63
T__125=125
T__64=64
T__128=128
T__65=65
T__127=127
UnicodeEscapeSequence=42
DecimalDigit=22
COMMENT=46
PrivateKeyword=8
IdentifierPart=35
Uint=18
Char=36
BreakKeyword=25
PublicKeyword=6
Fixed=20
VersionLiteral=4
T__49=49
HexLiteral=24
T__91=91
T__100=100
T__92=92
T__93=93
T__102=102
T__94=94
T__101=101
T__90=90
LT=10
ReservedKeyword=33
Identifier=30
T__99=99
HexNumber=28
T__95=95
T__96=96
T__97=97
T__98=98
ContinueKeyword=26
HexEscapeSequence=41
SingleEscapeCharacter=43
HexPair=32
PayableKeyword=16
PureKeyword=14
T__122=122
T__70=70
T__121=121
T__71=71
T__124=124
T__72=72
T__123=123
T__120=120
ConstantKeyword=9
BooleanLiteral=23
Int=17
AnonymousKeyword=12
T__77=77
T__119=119
T__78=78
T__118=118
IdentifierStart=34
T__79=79
T__73=73
T__115=115
WS=48
EOF=-1
T__74=74
T__114=114
T__75=75
T__117=117
T__76=76
T__116=116
T__80=80
T__111=111
T__81=81
T__110=110
T__82=82
T__113=113
IndexedKeyword=13
T__83=83
T__112=112
Ufixed=21
EscapeSequence=39
ExternalKeyword=11
DoubleStringCharacter=37
T__88=88
T__108=108
T__89=89
T__107=107
T__109=109
T__84=84
T__104=104
T__85=85
T__103=103
T__86=86
T__106=106
SingleStringCharacter=38
EscapeCharacter=45
T__87=87
T__105=105
NumberUnit=29

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "VersionLiteral", "StringLiteral", "PublicKeyword", "InternalKeyword", 
    "PrivateKeyword", "ConstantKeyword", "LT", "ExternalKeyword", "AnonymousKeyword", 
    "IndexedKeyword", "PureKeyword", "ViewKeyword", "PayableKeyword", "Int", 
    "Uint", "Byte", "Fixed", "Ufixed", "DecimalDigit", "BooleanLiteral", 
    "HexLiteral", "BreakKeyword", "ContinueKeyword", "DecimalNumber", "HexNumber", 
    "NumberUnit", "Identifier", "HexDigit", "HexPair", "ReservedKeyword", 
    "IdentifierStart", "IdentifierPart", "Char", "DoubleStringCharacter", 
    "SingleStringCharacter", "EscapeSequence", "CharacterEscapeSequence", 
    "HexEscapeSequence", "UnicodeEscapeSequence", "SingleEscapeCharacter", 
    "NonEscapeCharacter", "EscapeCharacter", "COMMENT", "LINE_COMMENT", 
    "WS", "'pragma'", "';'", "'^'", "'~'", "'>='", "'>'", "'<'", "'<='", 
    "'='", "'as'", "'import'", "'*'", "'from'", "'{'", "','", "'}'", "'contract'", 
    "'interface'", "'library'", "'is'", "'('", "')'", "'using'", "'for'", 
    "'struct'", "'constructor'", "'modifier'", "'function'", "'returns'", 
    "'event'", "'enum'", "'address'", "'['", "']'", "'.'", "'mapping'", 
    "'=>'", "'memory'", "'storage'", "'calldata'", "'if'", "'else'", "'while'", 
    "'assembly'", "'do'", "'return'", "'throw'", "'emit'", "'var'", "'bool'", 
    "'string'", "'byte'", "'new'", "'++'", "'--'", "'+'", "'-'", "'after'", 
    "'delete'", "'!'", "'**'", "'/'", "'%'", "'<<'", "'>>'", "'&'", "'|'", 
    "'=='", "'!='", "'&&'", "'||'", "'?'", "':'", "'|='", "'^='", "'&='", 
    "'<<='", "'>>='", "'+='", "'-='", "'*='", "'/='", "'%='", "'let'", "':='", 
    "'=:'", "'switch'", "'case'", "'default'", "'->'"
]




class solParser(Parser):
    grammarFileName = "D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(solParser, self).__init__(input, state, *args, **kwargs)

        self._state.ruleMemo = {}
        self.dfa2 = self.DFA2(
            self, 2,
            eot = self.DFA2_eot,
            eof = self.DFA2_eof,
            min = self.DFA2_min,
            max = self.DFA2_max,
            accept = self.DFA2_accept,
            special = self.DFA2_special,
            transition = self.DFA2_transition
            )

        self.dfa13 = self.DFA13(
            self, 13,
            eot = self.DFA13_eot,
            eof = self.DFA13_eof,
            min = self.DFA13_min,
            max = self.DFA13_max,
            accept = self.DFA13_accept,
            special = self.DFA13_special,
            transition = self.DFA13_transition
            )

        self.dfa16 = self.DFA16(
            self, 16,
            eot = self.DFA16_eot,
            eof = self.DFA16_eof,
            min = self.DFA16_min,
            max = self.DFA16_max,
            accept = self.DFA16_accept,
            special = self.DFA16_special,
            transition = self.DFA16_transition
            )

        self.dfa24 = self.DFA24(
            self, 24,
            eot = self.DFA24_eot,
            eof = self.DFA24_eof,
            min = self.DFA24_min,
            max = self.DFA24_max,
            accept = self.DFA24_accept,
            special = self.DFA24_special,
            transition = self.DFA24_transition
            )

        self.dfa23 = self.DFA23(
            self, 23,
            eot = self.DFA23_eot,
            eof = self.DFA23_eof,
            min = self.DFA23_min,
            max = self.DFA23_max,
            accept = self.DFA23_accept,
            special = self.DFA23_special,
            transition = self.DFA23_transition
            )

        self.dfa28 = self.DFA28(
            self, 28,
            eot = self.DFA28_eot,
            eof = self.DFA28_eof,
            min = self.DFA28_min,
            max = self.DFA28_max,
            accept = self.DFA28_accept,
            special = self.DFA28_special,
            transition = self.DFA28_transition
            )

        self.dfa29 = self.DFA29(
            self, 29,
            eot = self.DFA29_eot,
            eof = self.DFA29_eof,
            min = self.DFA29_min,
            max = self.DFA29_max,
            accept = self.DFA29_accept,
            special = self.DFA29_special,
            transition = self.DFA29_transition
            )

        self.dfa36 = self.DFA36(
            self, 36,
            eot = self.DFA36_eot,
            eof = self.DFA36_eof,
            min = self.DFA36_min,
            max = self.DFA36_max,
            accept = self.DFA36_accept,
            special = self.DFA36_special,
            transition = self.DFA36_transition
            )

        self.dfa45 = self.DFA45(
            self, 45,
            eot = self.DFA45_eot,
            eof = self.DFA45_eof,
            min = self.DFA45_min,
            max = self.DFA45_max,
            accept = self.DFA45_accept,
            special = self.DFA45_special,
            transition = self.DFA45_transition
            )

        self.dfa46 = self.DFA46(
            self, 46,
            eot = self.DFA46_eot,
            eof = self.DFA46_eof,
            min = self.DFA46_min,
            max = self.DFA46_max,
            accept = self.DFA46_accept,
            special = self.DFA46_special,
            transition = self.DFA46_transition
            )

        self.dfa48 = self.DFA48(
            self, 48,
            eot = self.DFA48_eot,
            eof = self.DFA48_eof,
            min = self.DFA48_min,
            max = self.DFA48_max,
            accept = self.DFA48_accept,
            special = self.DFA48_special,
            transition = self.DFA48_transition
            )

        self.dfa47 = self.DFA47(
            self, 47,
            eot = self.DFA47_eot,
            eof = self.DFA47_eof,
            min = self.DFA47_min,
            max = self.DFA47_max,
            accept = self.DFA47_accept,
            special = self.DFA47_special,
            transition = self.DFA47_transition
            )

        self.dfa49 = self.DFA49(
            self, 49,
            eot = self.DFA49_eot,
            eof = self.DFA49_eof,
            min = self.DFA49_min,
            max = self.DFA49_max,
            accept = self.DFA49_accept,
            special = self.DFA49_special,
            transition = self.DFA49_transition
            )

        self.dfa50 = self.DFA50(
            self, 50,
            eot = self.DFA50_eot,
            eof = self.DFA50_eof,
            min = self.DFA50_min,
            max = self.DFA50_max,
            accept = self.DFA50_accept,
            special = self.DFA50_special,
            transition = self.DFA50_transition
            )

        self.dfa51 = self.DFA51(
            self, 51,
            eot = self.DFA51_eot,
            eof = self.DFA51_eof,
            min = self.DFA51_min,
            max = self.DFA51_max,
            accept = self.DFA51_accept,
            special = self.DFA51_special,
            transition = self.DFA51_transition
            )

        self.dfa52 = self.DFA52(
            self, 52,
            eot = self.DFA52_eot,
            eof = self.DFA52_eof,
            min = self.DFA52_min,
            max = self.DFA52_max,
            accept = self.DFA52_accept,
            special = self.DFA52_special,
            transition = self.DFA52_transition
            )

        self.dfa53 = self.DFA53(
            self, 53,
            eot = self.DFA53_eot,
            eof = self.DFA53_eof,
            min = self.DFA53_min,
            max = self.DFA53_max,
            accept = self.DFA53_accept,
            special = self.DFA53_special,
            transition = self.DFA53_transition
            )

        self.dfa54 = self.DFA54(
            self, 54,
            eot = self.DFA54_eot,
            eof = self.DFA54_eof,
            min = self.DFA54_min,
            max = self.DFA54_max,
            accept = self.DFA54_accept,
            special = self.DFA54_special,
            transition = self.DFA54_transition
            )

        self.dfa55 = self.DFA55(
            self, 55,
            eot = self.DFA55_eot,
            eof = self.DFA55_eof,
            min = self.DFA55_min,
            max = self.DFA55_max,
            accept = self.DFA55_accept,
            special = self.DFA55_special,
            transition = self.DFA55_transition
            )

        self.dfa56 = self.DFA56(
            self, 56,
            eot = self.DFA56_eot,
            eof = self.DFA56_eof,
            min = self.DFA56_min,
            max = self.DFA56_max,
            accept = self.DFA56_accept,
            special = self.DFA56_special,
            transition = self.DFA56_transition
            )

        self.dfa57 = self.DFA57(
            self, 57,
            eot = self.DFA57_eot,
            eof = self.DFA57_eof,
            min = self.DFA57_min,
            max = self.DFA57_max,
            accept = self.DFA57_accept,
            special = self.DFA57_special,
            transition = self.DFA57_transition
            )

        self.dfa58 = self.DFA58(
            self, 58,
            eot = self.DFA58_eot,
            eof = self.DFA58_eof,
            min = self.DFA58_min,
            max = self.DFA58_max,
            accept = self.DFA58_accept,
            special = self.DFA58_special,
            transition = self.DFA58_transition
            )

        self.dfa60 = self.DFA60(
            self, 60,
            eot = self.DFA60_eot,
            eof = self.DFA60_eof,
            min = self.DFA60_min,
            max = self.DFA60_max,
            accept = self.DFA60_accept,
            special = self.DFA60_special,
            transition = self.DFA60_transition
            )

        self.dfa61 = self.DFA61(
            self, 61,
            eot = self.DFA61_eot,
            eof = self.DFA61_eof,
            min = self.DFA61_min,
            max = self.DFA61_max,
            accept = self.DFA61_accept,
            special = self.DFA61_special,
            transition = self.DFA61_transition
            )

        self.dfa69 = self.DFA69(
            self, 69,
            eot = self.DFA69_eot,
            eof = self.DFA69_eof,
            min = self.DFA69_min,
            max = self.DFA69_max,
            accept = self.DFA69_accept,
            special = self.DFA69_special,
            transition = self.DFA69_transition
            )

        self.dfa70 = self.DFA70(
            self, 70,
            eot = self.DFA70_eot,
            eof = self.DFA70_eof,
            min = self.DFA70_min,
            max = self.DFA70_max,
            accept = self.DFA70_accept,
            special = self.DFA70_special,
            transition = self.DFA70_transition
            )

        self.dfa71 = self.DFA71(
            self, 71,
            eot = self.DFA71_eot,
            eof = self.DFA71_eof,
            min = self.DFA71_min,
            max = self.DFA71_max,
            accept = self.DFA71_accept,
            special = self.DFA71_special,
            transition = self.DFA71_transition
            )

        self.dfa72 = self.DFA72(
            self, 72,
            eot = self.DFA72_eot,
            eof = self.DFA72_eof,
            min = self.DFA72_min,
            max = self.DFA72_max,
            accept = self.DFA72_accept,
            special = self.DFA72_special,
            transition = self.DFA72_transition
            )

        self.dfa79 = self.DFA79(
            self, 79,
            eot = self.DFA79_eot,
            eof = self.DFA79_eof,
            min = self.DFA79_min,
            max = self.DFA79_max,
            accept = self.DFA79_accept,
            special = self.DFA79_special,
            transition = self.DFA79_transition
            )

        self.dfa78 = self.DFA78(
            self, 78,
            eot = self.DFA78_eot,
            eof = self.DFA78_eof,
            min = self.DFA78_min,
            max = self.DFA78_max,
            accept = self.DFA78_accept,
            special = self.DFA78_special,
            transition = self.DFA78_transition
            )

        self.dfa80 = self.DFA80(
            self, 80,
            eot = self.DFA80_eot,
            eof = self.DFA80_eof,
            min = self.DFA80_min,
            max = self.DFA80_max,
            accept = self.DFA80_accept,
            special = self.DFA80_special,
            transition = self.DFA80_transition
            )

        self.dfa81 = self.DFA81(
            self, 81,
            eot = self.DFA81_eot,
            eof = self.DFA81_eof,
            min = self.DFA81_min,
            max = self.DFA81_max,
            accept = self.DFA81_accept,
            special = self.DFA81_special,
            transition = self.DFA81_transition
            )

        self.dfa86 = self.DFA86(
            self, 86,
            eot = self.DFA86_eot,
            eof = self.DFA86_eof,
            min = self.DFA86_min,
            max = self.DFA86_max,
            accept = self.DFA86_accept,
            special = self.DFA86_special,
            transition = self.DFA86_transition
            )

        self.dfa87 = self.DFA87(
            self, 87,
            eot = self.DFA87_eot,
            eof = self.DFA87_eof,
            min = self.DFA87_min,
            max = self.DFA87_max,
            accept = self.DFA87_accept,
            special = self.DFA87_special,
            transition = self.DFA87_transition
            )

        self.dfa90 = self.DFA90(
            self, 90,
            eot = self.DFA90_eot,
            eof = self.DFA90_eof,
            min = self.DFA90_min,
            max = self.DFA90_max,
            accept = self.DFA90_accept,
            special = self.DFA90_special,
            transition = self.DFA90_transition
            )

        self.dfa96 = self.DFA96(
            self, 96,
            eot = self.DFA96_eot,
            eof = self.DFA96_eof,
            min = self.DFA96_min,
            max = self.DFA96_max,
            accept = self.DFA96_accept,
            special = self.DFA96_special,
            transition = self.DFA96_transition
            )

        self.dfa97 = self.DFA97(
            self, 97,
            eot = self.DFA97_eot,
            eof = self.DFA97_eof,
            min = self.DFA97_min,
            max = self.DFA97_max,
            accept = self.DFA97_accept,
            special = self.DFA97_special,
            transition = self.DFA97_transition
            )

        self.dfa100 = self.DFA100(
            self, 100,
            eot = self.DFA100_eot,
            eof = self.DFA100_eof,
            min = self.DFA100_min,
            max = self.DFA100_max,
            accept = self.DFA100_accept,
            special = self.DFA100_special,
            transition = self.DFA100_transition
            )

        self.dfa102 = self.DFA102(
            self, 102,
            eot = self.DFA102_eot,
            eof = self.DFA102_eof,
            min = self.DFA102_min,
            max = self.DFA102_max,
            accept = self.DFA102_accept,
            special = self.DFA102_special,
            transition = self.DFA102_transition
            )

        self.dfa113 = self.DFA113(
            self, 113,
            eot = self.DFA113_eot,
            eof = self.DFA113_eof,
            min = self.DFA113_min,
            max = self.DFA113_max,
            accept = self.DFA113_accept,
            special = self.DFA113_special,
            transition = self.DFA113_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class sourceUnit_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.sourceUnit_return, self).__init__()

            self.tree = None




    # $ANTLR start "sourceUnit"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:13:1: sourceUnit : ( pragmaDirective | importDirective | contractDefinition )* EOF ;
    def sourceUnit(self, ):

        retval = self.sourceUnit_return()
        retval.start = self.input.LT(1)
        sourceUnit_StartIndex = self.input.index()
        root_0 = None

        EOF4 = None
        pragmaDirective1 = None

        importDirective2 = None

        contractDefinition3 = None


        EOF4_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:14:3: ( ( pragmaDirective | importDirective | contractDefinition )* EOF )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:14:5: ( pragmaDirective | importDirective | contractDefinition )* EOF
                pass 
                root_0 = self._adaptor.nil()

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:14:5: ( pragmaDirective | importDirective | contractDefinition )*
                while True: #loop1
                    alt1 = 4
                    LA1 = self.input.LA(1)
                    if LA1 == 49:
                        alt1 = 1
                    elif LA1 == 59:
                        alt1 = 2
                    elif LA1 == 65 or LA1 == 66 or LA1 == 67:
                        alt1 = 3

                    if alt1 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:14:6: pragmaDirective
                        pass 
                        self._state.following.append(self.FOLLOW_pragmaDirective_in_sourceUnit52)
                        pragmaDirective1 = self.pragmaDirective()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, pragmaDirective1.tree)


                    elif alt1 == 2:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:14:24: importDirective
                        pass 
                        self._state.following.append(self.FOLLOW_importDirective_in_sourceUnit56)
                        importDirective2 = self.importDirective()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, importDirective2.tree)


                    elif alt1 == 3:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:14:42: contractDefinition
                        pass 
                        self._state.following.append(self.FOLLOW_contractDefinition_in_sourceUnit60)
                        contractDefinition3 = self.contractDefinition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, contractDefinition3.tree)


                    else:
                        break #loop1
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_sourceUnit64)
                if self._state.backtracking == 0:

                    EOF4_tree = self._adaptor.createWithPayload(EOF4)
                    self._adaptor.addChild(root_0, EOF4_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 1, sourceUnit_StartIndex, success)

            pass
        return retval

    # $ANTLR end "sourceUnit"

    class pragmaDirective_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.pragmaDirective_return, self).__init__()

            self.tree = None




    # $ANTLR start "pragmaDirective"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:16:1: pragmaDirective : 'pragma' pragmaName pragmaValue ';' ;
    def pragmaDirective(self, ):

        retval = self.pragmaDirective_return()
        retval.start = self.input.LT(1)
        pragmaDirective_StartIndex = self.input.index()
        root_0 = None

        string_literal5 = None
        char_literal8 = None
        pragmaName6 = None

        pragmaValue7 = None


        string_literal5_tree = None
        char_literal8_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:17:3: ( 'pragma' pragmaName pragmaValue ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:17:5: 'pragma' pragmaName pragmaValue ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal5=self.match(self.input, 49, self.FOLLOW_49_in_pragmaDirective75)
                if self._state.backtracking == 0:

                    string_literal5_tree = self._adaptor.createWithPayload(string_literal5)
                    self._adaptor.addChild(root_0, string_literal5_tree)

                self._state.following.append(self.FOLLOW_pragmaName_in_pragmaDirective77)
                pragmaName6 = self.pragmaName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, pragmaName6.tree)
                self._state.following.append(self.FOLLOW_pragmaValue_in_pragmaDirective79)
                pragmaValue7 = self.pragmaValue()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, pragmaValue7.tree)
                char_literal8=self.match(self.input, 50, self.FOLLOW_50_in_pragmaDirective81)
                if self._state.backtracking == 0:

                    char_literal8_tree = self._adaptor.createWithPayload(char_literal8)
                    self._adaptor.addChild(root_0, char_literal8_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 2, pragmaDirective_StartIndex, success)

            pass
        return retval

    # $ANTLR end "pragmaDirective"

    class pragmaName_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.pragmaName_return, self).__init__()

            self.tree = None




    # $ANTLR start "pragmaName"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:19:1: pragmaName : identifier ;
    def pragmaName(self, ):

        retval = self.pragmaName_return()
        retval.start = self.input.LT(1)
        pragmaName_StartIndex = self.input.index()
        root_0 = None

        identifier9 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:20:3: ( identifier )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:20:5: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_pragmaName92)
                identifier9 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier9.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 3, pragmaName_StartIndex, success)

            pass
        return retval

    # $ANTLR end "pragmaName"

    class pragmaValue_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.pragmaValue_return, self).__init__()

            self.tree = None




    # $ANTLR start "pragmaValue"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:22:1: pragmaValue : ( version | expression );
    def pragmaValue(self, ):

        retval = self.pragmaValue_return()
        retval.start = self.input.LT(1)
        pragmaValue_StartIndex = self.input.index()
        root_0 = None

        version10 = None

        expression11 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:23:3: ( version | expression )
                alt2 = 2
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:23:5: version
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_version_in_pragmaValue103)
                    version10 = self.version()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, version10.tree)


                elif alt2 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:23:15: expression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expression_in_pragmaValue107)
                    expression11 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression11.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 4, pragmaValue_StartIndex, success)

            pass
        return retval

    # $ANTLR end "pragmaValue"

    class version_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.version_return, self).__init__()

            self.tree = None




    # $ANTLR start "version"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:25:1: version : versionConstraint ( versionConstraint )? ;
    def version(self, ):

        retval = self.version_return()
        retval.start = self.input.LT(1)
        version_StartIndex = self.input.index()
        root_0 = None

        versionConstraint12 = None

        versionConstraint13 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:26:3: ( versionConstraint ( versionConstraint )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:26:5: versionConstraint ( versionConstraint )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_versionConstraint_in_version118)
                versionConstraint12 = self.versionConstraint()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, versionConstraint12.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:26:23: ( versionConstraint )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == VersionLiteral or (51 <= LA3_0 <= 57)) :
                    alt3 = 1
                if alt3 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: versionConstraint
                    pass 
                    self._state.following.append(self.FOLLOW_versionConstraint_in_version120)
                    versionConstraint13 = self.versionConstraint()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, versionConstraint13.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 5, version_StartIndex, success)

            pass
        return retval

    # $ANTLR end "version"

    class versionOperator_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.versionOperator_return, self).__init__()

            self.tree = None




    # $ANTLR start "versionOperator"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:28:1: versionOperator : ( '^' | '~' | '>=' | '>' | '<' | '<=' | '=' );
    def versionOperator(self, ):

        retval = self.versionOperator_return()
        retval.start = self.input.LT(1)
        versionOperator_StartIndex = self.input.index()
        root_0 = None

        set14 = None

        set14_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:29:3: ( '^' | '~' | '>=' | '>' | '<' | '<=' | '=' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:
                pass 
                root_0 = self._adaptor.nil()

                set14 = self.input.LT(1)
                if (51 <= self.input.LA(1) <= 57):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set14))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 6, versionOperator_StartIndex, success)

            pass
        return retval

    # $ANTLR end "versionOperator"

    class versionConstraint_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.versionConstraint_return, self).__init__()

            self.tree = None




    # $ANTLR start "versionConstraint"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:31:1: versionConstraint : ( versionOperator )? VersionLiteral ;
    def versionConstraint(self, ):

        retval = self.versionConstraint_return()
        retval.start = self.input.LT(1)
        versionConstraint_StartIndex = self.input.index()
        root_0 = None

        VersionLiteral16 = None
        versionOperator15 = None


        VersionLiteral16_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:32:3: ( ( versionOperator )? VersionLiteral )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:32:5: ( versionOperator )? VersionLiteral
                pass 
                root_0 = self._adaptor.nil()

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:32:5: ( versionOperator )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((51 <= LA4_0 <= 57)) :
                    alt4 = 1
                if alt4 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: versionOperator
                    pass 
                    self._state.following.append(self.FOLLOW_versionOperator_in_versionConstraint167)
                    versionOperator15 = self.versionOperator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, versionOperator15.tree)



                VersionLiteral16=self.match(self.input, VersionLiteral, self.FOLLOW_VersionLiteral_in_versionConstraint170)
                if self._state.backtracking == 0:

                    VersionLiteral16_tree = self._adaptor.createWithPayload(VersionLiteral16)
                    self._adaptor.addChild(root_0, VersionLiteral16_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 7, versionConstraint_StartIndex, success)

            pass
        return retval

    # $ANTLR end "versionConstraint"

    class importDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.importDeclaration_return, self).__init__()

            self.tree = None




    # $ANTLR start "importDeclaration"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:34:1: importDeclaration : identifier ( 'as' identifier )? ;
    def importDeclaration(self, ):

        retval = self.importDeclaration_return()
        retval.start = self.input.LT(1)
        importDeclaration_StartIndex = self.input.index()
        root_0 = None

        string_literal18 = None
        identifier17 = None

        identifier19 = None


        string_literal18_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:35:3: ( identifier ( 'as' identifier )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:35:5: identifier ( 'as' identifier )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_importDeclaration181)
                identifier17 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier17.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:35:16: ( 'as' identifier )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 58) :
                    alt5 = 1
                if alt5 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:35:17: 'as' identifier
                    pass 
                    string_literal18=self.match(self.input, 58, self.FOLLOW_58_in_importDeclaration184)
                    if self._state.backtracking == 0:

                        string_literal18_tree = self._adaptor.createWithPayload(string_literal18)
                        self._adaptor.addChild(root_0, string_literal18_tree)

                    self._state.following.append(self.FOLLOW_identifier_in_importDeclaration186)
                    identifier19 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier19.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 8, importDeclaration_StartIndex, success)

            pass
        return retval

    # $ANTLR end "importDeclaration"

    class importDirective_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.importDirective_return, self).__init__()

            self.tree = None




    # $ANTLR start "importDirective"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:37:1: importDirective : ( 'import' StringLiteral ( 'as' identifier )? ';' | 'import' ( '*' | identifier ) ( 'as' identifier )? 'from' StringLiteral ';' | 'import' '{' importDeclaration ( ',' importDeclaration )* '}' 'from' StringLiteral ';' );
    def importDirective(self, ):

        retval = self.importDirective_return()
        retval.start = self.input.LT(1)
        importDirective_StartIndex = self.input.index()
        root_0 = None

        string_literal20 = None
        StringLiteral21 = None
        string_literal22 = None
        char_literal24 = None
        string_literal25 = None
        char_literal26 = None
        string_literal28 = None
        string_literal30 = None
        StringLiteral31 = None
        char_literal32 = None
        string_literal33 = None
        char_literal34 = None
        char_literal36 = None
        char_literal38 = None
        string_literal39 = None
        StringLiteral40 = None
        char_literal41 = None
        identifier23 = None

        identifier27 = None

        identifier29 = None

        importDeclaration35 = None

        importDeclaration37 = None


        string_literal20_tree = None
        StringLiteral21_tree = None
        string_literal22_tree = None
        char_literal24_tree = None
        string_literal25_tree = None
        char_literal26_tree = None
        string_literal28_tree = None
        string_literal30_tree = None
        StringLiteral31_tree = None
        char_literal32_tree = None
        string_literal33_tree = None
        char_literal34_tree = None
        char_literal36_tree = None
        char_literal38_tree = None
        string_literal39_tree = None
        StringLiteral40_tree = None
        char_literal41_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:38:3: ( 'import' StringLiteral ( 'as' identifier )? ';' | 'import' ( '*' | identifier ) ( 'as' identifier )? 'from' StringLiteral ';' | 'import' '{' importDeclaration ( ',' importDeclaration )* '}' 'from' StringLiteral ';' )
                alt10 = 3
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 59) :
                    LA10 = self.input.LA(2)
                    if LA10 == StringLiteral:
                        alt10 = 1
                    elif LA10 == 62:
                        alt10 = 3
                    elif LA10 == Identifier or LA10 == 60 or LA10 == 61 or LA10 == 88:
                        alt10 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 10, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:38:5: 'import' StringLiteral ( 'as' identifier )? ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal20=self.match(self.input, 59, self.FOLLOW_59_in_importDirective199)
                    if self._state.backtracking == 0:

                        string_literal20_tree = self._adaptor.createWithPayload(string_literal20)
                        self._adaptor.addChild(root_0, string_literal20_tree)

                    StringLiteral21=self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_importDirective201)
                    if self._state.backtracking == 0:

                        StringLiteral21_tree = self._adaptor.createWithPayload(StringLiteral21)
                        self._adaptor.addChild(root_0, StringLiteral21_tree)

                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:38:28: ( 'as' identifier )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == 58) :
                        alt6 = 1
                    if alt6 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:38:29: 'as' identifier
                        pass 
                        string_literal22=self.match(self.input, 58, self.FOLLOW_58_in_importDirective204)
                        if self._state.backtracking == 0:

                            string_literal22_tree = self._adaptor.createWithPayload(string_literal22)
                            self._adaptor.addChild(root_0, string_literal22_tree)

                        self._state.following.append(self.FOLLOW_identifier_in_importDirective206)
                        identifier23 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier23.tree)



                    char_literal24=self.match(self.input, 50, self.FOLLOW_50_in_importDirective210)
                    if self._state.backtracking == 0:

                        char_literal24_tree = self._adaptor.createWithPayload(char_literal24)
                        self._adaptor.addChild(root_0, char_literal24_tree)



                elif alt10 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:39:5: 'import' ( '*' | identifier ) ( 'as' identifier )? 'from' StringLiteral ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal25=self.match(self.input, 59, self.FOLLOW_59_in_importDirective216)
                    if self._state.backtracking == 0:

                        string_literal25_tree = self._adaptor.createWithPayload(string_literal25)
                        self._adaptor.addChild(root_0, string_literal25_tree)

                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:39:14: ( '*' | identifier )
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 60) :
                        alt7 = 1
                    elif (LA7_0 == Identifier or LA7_0 == 61 or LA7_0 == 88) :
                        alt7 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 7, 0, self.input)

                        raise nvae

                    if alt7 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:39:15: '*'
                        pass 
                        char_literal26=self.match(self.input, 60, self.FOLLOW_60_in_importDirective219)
                        if self._state.backtracking == 0:

                            char_literal26_tree = self._adaptor.createWithPayload(char_literal26)
                            self._adaptor.addChild(root_0, char_literal26_tree)



                    elif alt7 == 2:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:39:21: identifier
                        pass 
                        self._state.following.append(self.FOLLOW_identifier_in_importDirective223)
                        identifier27 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier27.tree)



                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:39:33: ( 'as' identifier )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 58) :
                        alt8 = 1
                    if alt8 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:39:34: 'as' identifier
                        pass 
                        string_literal28=self.match(self.input, 58, self.FOLLOW_58_in_importDirective227)
                        if self._state.backtracking == 0:

                            string_literal28_tree = self._adaptor.createWithPayload(string_literal28)
                            self._adaptor.addChild(root_0, string_literal28_tree)

                        self._state.following.append(self.FOLLOW_identifier_in_importDirective229)
                        identifier29 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier29.tree)



                    string_literal30=self.match(self.input, 61, self.FOLLOW_61_in_importDirective233)
                    if self._state.backtracking == 0:

                        string_literal30_tree = self._adaptor.createWithPayload(string_literal30)
                        self._adaptor.addChild(root_0, string_literal30_tree)

                    StringLiteral31=self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_importDirective235)
                    if self._state.backtracking == 0:

                        StringLiteral31_tree = self._adaptor.createWithPayload(StringLiteral31)
                        self._adaptor.addChild(root_0, StringLiteral31_tree)

                    char_literal32=self.match(self.input, 50, self.FOLLOW_50_in_importDirective237)
                    if self._state.backtracking == 0:

                        char_literal32_tree = self._adaptor.createWithPayload(char_literal32)
                        self._adaptor.addChild(root_0, char_literal32_tree)



                elif alt10 == 3:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:40:5: 'import' '{' importDeclaration ( ',' importDeclaration )* '}' 'from' StringLiteral ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal33=self.match(self.input, 59, self.FOLLOW_59_in_importDirective243)
                    if self._state.backtracking == 0:

                        string_literal33_tree = self._adaptor.createWithPayload(string_literal33)
                        self._adaptor.addChild(root_0, string_literal33_tree)

                    char_literal34=self.match(self.input, 62, self.FOLLOW_62_in_importDirective245)
                    if self._state.backtracking == 0:

                        char_literal34_tree = self._adaptor.createWithPayload(char_literal34)
                        self._adaptor.addChild(root_0, char_literal34_tree)

                    self._state.following.append(self.FOLLOW_importDeclaration_in_importDirective247)
                    importDeclaration35 = self.importDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, importDeclaration35.tree)
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:40:36: ( ',' importDeclaration )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == 63) :
                            alt9 = 1


                        if alt9 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:40:38: ',' importDeclaration
                            pass 
                            char_literal36=self.match(self.input, 63, self.FOLLOW_63_in_importDirective251)
                            if self._state.backtracking == 0:

                                char_literal36_tree = self._adaptor.createWithPayload(char_literal36)
                                self._adaptor.addChild(root_0, char_literal36_tree)

                            self._state.following.append(self.FOLLOW_importDeclaration_in_importDirective253)
                            importDeclaration37 = self.importDeclaration()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, importDeclaration37.tree)


                        else:
                            break #loop9
                    char_literal38=self.match(self.input, 64, self.FOLLOW_64_in_importDirective258)
                    if self._state.backtracking == 0:

                        char_literal38_tree = self._adaptor.createWithPayload(char_literal38)
                        self._adaptor.addChild(root_0, char_literal38_tree)

                    string_literal39=self.match(self.input, 61, self.FOLLOW_61_in_importDirective260)
                    if self._state.backtracking == 0:

                        string_literal39_tree = self._adaptor.createWithPayload(string_literal39)
                        self._adaptor.addChild(root_0, string_literal39_tree)

                    StringLiteral40=self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_importDirective262)
                    if self._state.backtracking == 0:

                        StringLiteral40_tree = self._adaptor.createWithPayload(StringLiteral40)
                        self._adaptor.addChild(root_0, StringLiteral40_tree)

                    char_literal41=self.match(self.input, 50, self.FOLLOW_50_in_importDirective264)
                    if self._state.backtracking == 0:

                        char_literal41_tree = self._adaptor.createWithPayload(char_literal41)
                        self._adaptor.addChild(root_0, char_literal41_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 9, importDirective_StartIndex, success)

            pass
        return retval

    # $ANTLR end "importDirective"

    class contractDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.contractDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "contractDefinition"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:42:1: contractDefinition : ( 'contract' | 'interface' | 'library' ) identifier ( 'is' inheritanceSpecifier ( ',' inheritanceSpecifier )* )? '{' ( contractPart )* '}' ;
    def contractDefinition(self, ):

        retval = self.contractDefinition_return()
        retval.start = self.input.LT(1)
        contractDefinition_StartIndex = self.input.index()
        root_0 = None

        set42 = None
        string_literal44 = None
        char_literal46 = None
        char_literal48 = None
        char_literal50 = None
        identifier43 = None

        inheritanceSpecifier45 = None

        inheritanceSpecifier47 = None

        contractPart49 = None


        set42_tree = None
        string_literal44_tree = None
        char_literal46_tree = None
        char_literal48_tree = None
        char_literal50_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:43:3: ( ( 'contract' | 'interface' | 'library' ) identifier ( 'is' inheritanceSpecifier ( ',' inheritanceSpecifier )* )? '{' ( contractPart )* '}' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:43:5: ( 'contract' | 'interface' | 'library' ) identifier ( 'is' inheritanceSpecifier ( ',' inheritanceSpecifier )* )? '{' ( contractPart )* '}'
                pass 
                root_0 = self._adaptor.nil()

                set42 = self.input.LT(1)
                if (65 <= self.input.LA(1) <= 67):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set42))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self._state.following.append(self.FOLLOW_identifier_in_contractDefinition289)
                identifier43 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier43.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:44:5: ( 'is' inheritanceSpecifier ( ',' inheritanceSpecifier )* )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 68) :
                    alt12 = 1
                if alt12 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:44:7: 'is' inheritanceSpecifier ( ',' inheritanceSpecifier )*
                    pass 
                    string_literal44=self.match(self.input, 68, self.FOLLOW_68_in_contractDefinition297)
                    if self._state.backtracking == 0:

                        string_literal44_tree = self._adaptor.createWithPayload(string_literal44)
                        self._adaptor.addChild(root_0, string_literal44_tree)

                    self._state.following.append(self.FOLLOW_inheritanceSpecifier_in_contractDefinition299)
                    inheritanceSpecifier45 = self.inheritanceSpecifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, inheritanceSpecifier45.tree)
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:44:33: ( ',' inheritanceSpecifier )*
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == 63) :
                            alt11 = 1


                        if alt11 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:44:34: ',' inheritanceSpecifier
                            pass 
                            char_literal46=self.match(self.input, 63, self.FOLLOW_63_in_contractDefinition302)
                            if self._state.backtracking == 0:

                                char_literal46_tree = self._adaptor.createWithPayload(char_literal46)
                                self._adaptor.addChild(root_0, char_literal46_tree)

                            self._state.following.append(self.FOLLOW_inheritanceSpecifier_in_contractDefinition304)
                            inheritanceSpecifier47 = self.inheritanceSpecifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, inheritanceSpecifier47.tree)


                        else:
                            break #loop11



                char_literal48=self.match(self.input, 62, self.FOLLOW_62_in_contractDefinition316)
                if self._state.backtracking == 0:

                    char_literal48_tree = self._adaptor.createWithPayload(char_literal48)
                    self._adaptor.addChild(root_0, char_literal48_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:45:9: ( contractPart )*
                while True: #loop13
                    alt13 = 2
                    alt13 = self.dfa13.predict(self.input)
                    if alt13 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: contractPart
                        pass 
                        self._state.following.append(self.FOLLOW_contractPart_in_contractDefinition318)
                        contractPart49 = self.contractPart()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, contractPart49.tree)


                    else:
                        break #loop13
                char_literal50=self.match(self.input, 64, self.FOLLOW_64_in_contractDefinition321)
                if self._state.backtracking == 0:

                    char_literal50_tree = self._adaptor.createWithPayload(char_literal50)
                    self._adaptor.addChild(root_0, char_literal50_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 10, contractDefinition_StartIndex, success)

            pass
        return retval

    # $ANTLR end "contractDefinition"

    class inheritanceSpecifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.inheritanceSpecifier_return, self).__init__()

            self.tree = None




    # $ANTLR start "inheritanceSpecifier"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:47:1: inheritanceSpecifier : userDefinedTypeName ( '(' expression ( ',' expression )* ')' )? ;
    def inheritanceSpecifier(self, ):

        retval = self.inheritanceSpecifier_return()
        retval.start = self.input.LT(1)
        inheritanceSpecifier_StartIndex = self.input.index()
        root_0 = None

        char_literal52 = None
        char_literal54 = None
        char_literal56 = None
        userDefinedTypeName51 = None

        expression53 = None

        expression55 = None


        char_literal52_tree = None
        char_literal54_tree = None
        char_literal56_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:48:3: ( userDefinedTypeName ( '(' expression ( ',' expression )* ')' )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:48:5: userDefinedTypeName ( '(' expression ( ',' expression )* ')' )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_userDefinedTypeName_in_inheritanceSpecifier332)
                userDefinedTypeName51 = self.userDefinedTypeName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, userDefinedTypeName51.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:48:25: ( '(' expression ( ',' expression )* ')' )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 69) :
                    alt15 = 1
                if alt15 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:48:27: '(' expression ( ',' expression )* ')'
                    pass 
                    char_literal52=self.match(self.input, 69, self.FOLLOW_69_in_inheritanceSpecifier336)
                    if self._state.backtracking == 0:

                        char_literal52_tree = self._adaptor.createWithPayload(char_literal52)
                        self._adaptor.addChild(root_0, char_literal52_tree)

                    self._state.following.append(self.FOLLOW_expression_in_inheritanceSpecifier338)
                    expression53 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression53.tree)
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:48:42: ( ',' expression )*
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == 63) :
                            alt14 = 1


                        if alt14 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:48:44: ',' expression
                            pass 
                            char_literal54=self.match(self.input, 63, self.FOLLOW_63_in_inheritanceSpecifier342)
                            if self._state.backtracking == 0:

                                char_literal54_tree = self._adaptor.createWithPayload(char_literal54)
                                self._adaptor.addChild(root_0, char_literal54_tree)

                            self._state.following.append(self.FOLLOW_expression_in_inheritanceSpecifier344)
                            expression55 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, expression55.tree)


                        else:
                            break #loop14
                    char_literal56=self.match(self.input, 70, self.FOLLOW_70_in_inheritanceSpecifier349)
                    if self._state.backtracking == 0:

                        char_literal56_tree = self._adaptor.createWithPayload(char_literal56)
                        self._adaptor.addChild(root_0, char_literal56_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 11, inheritanceSpecifier_StartIndex, success)

            pass
        return retval

    # $ANTLR end "inheritanceSpecifier"

    class contractPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.contractPart_return, self).__init__()

            self.tree = None




    # $ANTLR start "contractPart"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:50:1: contractPart : ( stateVariableDeclaration | usingForDeclaration | structDefinition | constructorDefinition | modifierDefinition | functionDefinition | eventDefinition | enumDefinition );
    def contractPart(self, ):

        retval = self.contractPart_return()
        retval.start = self.input.LT(1)
        contractPart_StartIndex = self.input.index()
        root_0 = None

        stateVariableDeclaration57 = None

        usingForDeclaration58 = None

        structDefinition59 = None

        constructorDefinition60 = None

        modifierDefinition61 = None

        functionDefinition62 = None

        eventDefinition63 = None

        enumDefinition64 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:51:3: ( stateVariableDeclaration | usingForDeclaration | structDefinition | constructorDefinition | modifierDefinition | functionDefinition | eventDefinition | enumDefinition )
                alt16 = 8
                alt16 = self.dfa16.predict(self.input)
                if alt16 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:51:5: stateVariableDeclaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_stateVariableDeclaration_in_contractPart363)
                    stateVariableDeclaration57 = self.stateVariableDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, stateVariableDeclaration57.tree)


                elif alt16 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:52:5: usingForDeclaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_usingForDeclaration_in_contractPart369)
                    usingForDeclaration58 = self.usingForDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, usingForDeclaration58.tree)


                elif alt16 == 3:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:53:5: structDefinition
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_structDefinition_in_contractPart375)
                    structDefinition59 = self.structDefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, structDefinition59.tree)


                elif alt16 == 4:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:54:5: constructorDefinition
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_constructorDefinition_in_contractPart381)
                    constructorDefinition60 = self.constructorDefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, constructorDefinition60.tree)


                elif alt16 == 5:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:55:5: modifierDefinition
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_modifierDefinition_in_contractPart387)
                    modifierDefinition61 = self.modifierDefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, modifierDefinition61.tree)


                elif alt16 == 6:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:56:5: functionDefinition
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_functionDefinition_in_contractPart393)
                    functionDefinition62 = self.functionDefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, functionDefinition62.tree)


                elif alt16 == 7:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:57:5: eventDefinition
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_eventDefinition_in_contractPart399)
                    eventDefinition63 = self.eventDefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, eventDefinition63.tree)


                elif alt16 == 8:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:58:5: enumDefinition
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_enumDefinition_in_contractPart405)
                    enumDefinition64 = self.enumDefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, enumDefinition64.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 12, contractPart_StartIndex, success)

            pass
        return retval

    # $ANTLR end "contractPart"

    class stateVariableDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.stateVariableDeclaration_return, self).__init__()

            self.tree = None




    # $ANTLR start "stateVariableDeclaration"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:60:1: stateVariableDeclaration : typeName ( PublicKeyword | InternalKeyword | PrivateKeyword | ConstantKeyword )* identifier ( '=' expression )? ';' ;
    def stateVariableDeclaration(self, ):

        retval = self.stateVariableDeclaration_return()
        retval.start = self.input.LT(1)
        stateVariableDeclaration_StartIndex = self.input.index()
        root_0 = None

        set66 = None
        char_literal68 = None
        char_literal70 = None
        typeName65 = None

        identifier67 = None

        expression69 = None


        set66_tree = None
        char_literal68_tree = None
        char_literal70_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:61:3: ( typeName ( PublicKeyword | InternalKeyword | PrivateKeyword | ConstantKeyword )* identifier ( '=' expression )? ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:61:5: typeName ( PublicKeyword | InternalKeyword | PrivateKeyword | ConstantKeyword )* identifier ( '=' expression )? ';'
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_typeName_in_stateVariableDeclaration416)
                typeName65 = self.typeName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, typeName65.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:62:5: ( PublicKeyword | InternalKeyword | PrivateKeyword | ConstantKeyword )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if ((PublicKeyword <= LA17_0 <= ConstantKeyword)) :
                        alt17 = 1


                    if alt17 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:
                        pass 
                        set66 = self.input.LT(1)
                        if (PublicKeyword <= self.input.LA(1) <= ConstantKeyword):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set66))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        break #loop17
                self._state.following.append(self.FOLLOW_identifier_in_stateVariableDeclaration445)
                identifier67 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier67.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:63:16: ( '=' expression )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == 57) :
                    alt18 = 1
                if alt18 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:63:17: '=' expression
                    pass 
                    char_literal68=self.match(self.input, 57, self.FOLLOW_57_in_stateVariableDeclaration448)
                    if self._state.backtracking == 0:

                        char_literal68_tree = self._adaptor.createWithPayload(char_literal68)
                        self._adaptor.addChild(root_0, char_literal68_tree)

                    self._state.following.append(self.FOLLOW_expression_in_stateVariableDeclaration450)
                    expression69 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression69.tree)



                char_literal70=self.match(self.input, 50, self.FOLLOW_50_in_stateVariableDeclaration454)
                if self._state.backtracking == 0:

                    char_literal70_tree = self._adaptor.createWithPayload(char_literal70)
                    self._adaptor.addChild(root_0, char_literal70_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 13, stateVariableDeclaration_StartIndex, success)

            pass
        return retval

    # $ANTLR end "stateVariableDeclaration"

    class usingForDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.usingForDeclaration_return, self).__init__()

            self.tree = None




    # $ANTLR start "usingForDeclaration"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:65:1: usingForDeclaration : 'using' identifier 'for' ( '*' | typeName ) ';' ;
    def usingForDeclaration(self, ):

        retval = self.usingForDeclaration_return()
        retval.start = self.input.LT(1)
        usingForDeclaration_StartIndex = self.input.index()
        root_0 = None

        string_literal71 = None
        string_literal73 = None
        char_literal74 = None
        char_literal76 = None
        identifier72 = None

        typeName75 = None


        string_literal71_tree = None
        string_literal73_tree = None
        char_literal74_tree = None
        char_literal76_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:66:3: ( 'using' identifier 'for' ( '*' | typeName ) ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:66:5: 'using' identifier 'for' ( '*' | typeName ) ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal71=self.match(self.input, 71, self.FOLLOW_71_in_usingForDeclaration465)
                if self._state.backtracking == 0:

                    string_literal71_tree = self._adaptor.createWithPayload(string_literal71)
                    self._adaptor.addChild(root_0, string_literal71_tree)

                self._state.following.append(self.FOLLOW_identifier_in_usingForDeclaration467)
                identifier72 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier72.tree)
                string_literal73=self.match(self.input, 72, self.FOLLOW_72_in_usingForDeclaration469)
                if self._state.backtracking == 0:

                    string_literal73_tree = self._adaptor.createWithPayload(string_literal73)
                    self._adaptor.addChild(root_0, string_literal73_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:66:30: ( '*' | typeName )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == 60) :
                    alt19 = 1
                elif ((Int <= LA19_0 <= Ufixed) or LA19_0 == Identifier or LA19_0 == 61 or LA19_0 == 76 or LA19_0 == 80 or LA19_0 == 84 or LA19_0 == 88 or (97 <= LA19_0 <= 100)) :
                    alt19 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:66:31: '*'
                    pass 
                    char_literal74=self.match(self.input, 60, self.FOLLOW_60_in_usingForDeclaration472)
                    if self._state.backtracking == 0:

                        char_literal74_tree = self._adaptor.createWithPayload(char_literal74)
                        self._adaptor.addChild(root_0, char_literal74_tree)



                elif alt19 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:66:37: typeName
                    pass 
                    self._state.following.append(self.FOLLOW_typeName_in_usingForDeclaration476)
                    typeName75 = self.typeName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeName75.tree)



                char_literal76=self.match(self.input, 50, self.FOLLOW_50_in_usingForDeclaration479)
                if self._state.backtracking == 0:

                    char_literal76_tree = self._adaptor.createWithPayload(char_literal76)
                    self._adaptor.addChild(root_0, char_literal76_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 14, usingForDeclaration_StartIndex, success)

            pass
        return retval

    # $ANTLR end "usingForDeclaration"

    class structDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.structDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "structDefinition"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:68:1: structDefinition : 'struct' identifier '{' ( variableDeclaration ';' ( variableDeclaration ';' )* )? '}' ;
    def structDefinition(self, ):

        retval = self.structDefinition_return()
        retval.start = self.input.LT(1)
        structDefinition_StartIndex = self.input.index()
        root_0 = None

        string_literal77 = None
        char_literal79 = None
        char_literal81 = None
        char_literal83 = None
        char_literal84 = None
        identifier78 = None

        variableDeclaration80 = None

        variableDeclaration82 = None


        string_literal77_tree = None
        char_literal79_tree = None
        char_literal81_tree = None
        char_literal83_tree = None
        char_literal84_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:69:3: ( 'struct' identifier '{' ( variableDeclaration ';' ( variableDeclaration ';' )* )? '}' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:69:5: 'struct' identifier '{' ( variableDeclaration ';' ( variableDeclaration ';' )* )? '}'
                pass 
                root_0 = self._adaptor.nil()

                string_literal77=self.match(self.input, 73, self.FOLLOW_73_in_structDefinition490)
                if self._state.backtracking == 0:

                    string_literal77_tree = self._adaptor.createWithPayload(string_literal77)
                    self._adaptor.addChild(root_0, string_literal77_tree)

                self._state.following.append(self.FOLLOW_identifier_in_structDefinition492)
                identifier78 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier78.tree)
                char_literal79=self.match(self.input, 62, self.FOLLOW_62_in_structDefinition498)
                if self._state.backtracking == 0:

                    char_literal79_tree = self._adaptor.createWithPayload(char_literal79)
                    self._adaptor.addChild(root_0, char_literal79_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:70:9: ( variableDeclaration ';' ( variableDeclaration ';' )* )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if ((Int <= LA21_0 <= Ufixed) or LA21_0 == Identifier or LA21_0 == 61 or LA21_0 == 76 or LA21_0 == 80 or LA21_0 == 84 or LA21_0 == 88 or (97 <= LA21_0 <= 100)) :
                    alt21 = 1
                if alt21 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:70:11: variableDeclaration ';' ( variableDeclaration ';' )*
                    pass 
                    self._state.following.append(self.FOLLOW_variableDeclaration_in_structDefinition502)
                    variableDeclaration80 = self.variableDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variableDeclaration80.tree)
                    char_literal81=self.match(self.input, 50, self.FOLLOW_50_in_structDefinition504)
                    if self._state.backtracking == 0:

                        char_literal81_tree = self._adaptor.createWithPayload(char_literal81)
                        self._adaptor.addChild(root_0, char_literal81_tree)

                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:70:35: ( variableDeclaration ';' )*
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if ((Int <= LA20_0 <= Ufixed) or LA20_0 == Identifier or LA20_0 == 61 or LA20_0 == 76 or LA20_0 == 80 or LA20_0 == 84 or LA20_0 == 88 or (97 <= LA20_0 <= 100)) :
                            alt20 = 1


                        if alt20 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:70:36: variableDeclaration ';'
                            pass 
                            self._state.following.append(self.FOLLOW_variableDeclaration_in_structDefinition507)
                            variableDeclaration82 = self.variableDeclaration()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, variableDeclaration82.tree)
                            char_literal83=self.match(self.input, 50, self.FOLLOW_50_in_structDefinition509)
                            if self._state.backtracking == 0:

                                char_literal83_tree = self._adaptor.createWithPayload(char_literal83)
                                self._adaptor.addChild(root_0, char_literal83_tree)



                        else:
                            break #loop20



                char_literal84=self.match(self.input, 64, self.FOLLOW_64_in_structDefinition516)
                if self._state.backtracking == 0:

                    char_literal84_tree = self._adaptor.createWithPayload(char_literal84)
                    self._adaptor.addChild(root_0, char_literal84_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 15, structDefinition_StartIndex, success)

            pass
        return retval

    # $ANTLR end "structDefinition"

    class constructorDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.constructorDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "constructorDefinition"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:72:1: constructorDefinition : 'constructor' parameterList modifierList block ;
    def constructorDefinition(self, ):

        retval = self.constructorDefinition_return()
        retval.start = self.input.LT(1)
        constructorDefinition_StartIndex = self.input.index()
        root_0 = None

        string_literal85 = None
        parameterList86 = None

        modifierList87 = None

        block88 = None


        string_literal85_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:73:3: ( 'constructor' parameterList modifierList block )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:73:5: 'constructor' parameterList modifierList block
                pass 
                root_0 = self._adaptor.nil()

                string_literal85=self.match(self.input, 74, self.FOLLOW_74_in_constructorDefinition527)
                if self._state.backtracking == 0:

                    string_literal85_tree = self._adaptor.createWithPayload(string_literal85)
                    self._adaptor.addChild(root_0, string_literal85_tree)

                self._state.following.append(self.FOLLOW_parameterList_in_constructorDefinition529)
                parameterList86 = self.parameterList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, parameterList86.tree)
                self._state.following.append(self.FOLLOW_modifierList_in_constructorDefinition531)
                modifierList87 = self.modifierList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, modifierList87.tree)
                self._state.following.append(self.FOLLOW_block_in_constructorDefinition533)
                block88 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block88.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 16, constructorDefinition_StartIndex, success)

            pass
        return retval

    # $ANTLR end "constructorDefinition"

    class modifierDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.modifierDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "modifierDefinition"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:75:1: modifierDefinition : 'modifier' identifier ( parameterList )? block ;
    def modifierDefinition(self, ):

        retval = self.modifierDefinition_return()
        retval.start = self.input.LT(1)
        modifierDefinition_StartIndex = self.input.index()
        root_0 = None

        string_literal89 = None
        identifier90 = None

        parameterList91 = None

        block92 = None


        string_literal89_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:76:3: ( 'modifier' identifier ( parameterList )? block )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:76:5: 'modifier' identifier ( parameterList )? block
                pass 
                root_0 = self._adaptor.nil()

                string_literal89=self.match(self.input, 75, self.FOLLOW_75_in_modifierDefinition544)
                if self._state.backtracking == 0:

                    string_literal89_tree = self._adaptor.createWithPayload(string_literal89)
                    self._adaptor.addChild(root_0, string_literal89_tree)

                self._state.following.append(self.FOLLOW_identifier_in_modifierDefinition546)
                identifier90 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier90.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:76:27: ( parameterList )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == 69) :
                    alt22 = 1
                if alt22 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: parameterList
                    pass 
                    self._state.following.append(self.FOLLOW_parameterList_in_modifierDefinition548)
                    parameterList91 = self.parameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parameterList91.tree)



                self._state.following.append(self.FOLLOW_block_in_modifierDefinition551)
                block92 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block92.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 17, modifierDefinition_StartIndex, success)

            pass
        return retval

    # $ANTLR end "modifierDefinition"

    class modifierInvocation_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.modifierInvocation_return, self).__init__()

            self.tree = None




    # $ANTLR start "modifierInvocation"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:78:1: modifierInvocation : identifier ( '(' ( expressionList )? ')' )? ;
    def modifierInvocation(self, ):

        retval = self.modifierInvocation_return()
        retval.start = self.input.LT(1)
        modifierInvocation_StartIndex = self.input.index()
        root_0 = None

        char_literal94 = None
        char_literal96 = None
        identifier93 = None

        expressionList95 = None


        char_literal94_tree = None
        char_literal96_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:79:3: ( identifier ( '(' ( expressionList )? ')' )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:79:5: identifier ( '(' ( expressionList )? ')' )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_modifierInvocation562)
                identifier93 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier93.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:79:16: ( '(' ( expressionList )? ')' )?
                alt24 = 2
                alt24 = self.dfa24.predict(self.input)
                if alt24 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:79:18: '(' ( expressionList )? ')'
                    pass 
                    char_literal94=self.match(self.input, 69, self.FOLLOW_69_in_modifierInvocation566)
                    if self._state.backtracking == 0:

                        char_literal94_tree = self._adaptor.createWithPayload(char_literal94)
                        self._adaptor.addChild(root_0, char_literal94_tree)

                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:79:22: ( expressionList )?
                    alt23 = 2
                    alt23 = self.dfa23.predict(self.input)
                    if alt23 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: expressionList
                        pass 
                        self._state.following.append(self.FOLLOW_expressionList_in_modifierInvocation568)
                        expressionList95 = self.expressionList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expressionList95.tree)



                    char_literal96=self.match(self.input, 70, self.FOLLOW_70_in_modifierInvocation571)
                    if self._state.backtracking == 0:

                        char_literal96_tree = self._adaptor.createWithPayload(char_literal96)
                        self._adaptor.addChild(root_0, char_literal96_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 18, modifierInvocation_StartIndex, success)

            pass
        return retval

    # $ANTLR end "modifierInvocation"

    class functionDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.functionDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionDefinition"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:84:1: functionDefinition : 'function' ( LT )* identifier ( LT )* parameterList ( LT )* '{' ( LT )* ( statement )* '}' ;
    def functionDefinition(self, ):

        retval = self.functionDefinition_return()
        retval.start = self.input.LT(1)
        functionDefinition_StartIndex = self.input.index()
        root_0 = None

        string_literal97 = None
        LT98 = None
        LT100 = None
        LT102 = None
        char_literal103 = None
        LT104 = None
        char_literal106 = None
        identifier99 = None

        parameterList101 = None

        statement105 = None


        string_literal97_tree = None
        LT98_tree = None
        LT100_tree = None
        LT102_tree = None
        char_literal103_tree = None
        LT104_tree = None
        char_literal106_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:85:3: ( 'function' ( LT )* identifier ( LT )* parameterList ( LT )* '{' ( LT )* ( statement )* '}' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:85:5: 'function' ( LT )* identifier ( LT )* parameterList ( LT )* '{' ( LT )* ( statement )* '}'
                pass 
                root_0 = self._adaptor.nil()

                string_literal97=self.match(self.input, 76, self.FOLLOW_76_in_functionDefinition588)
                if self._state.backtracking == 0:

                    string_literal97_tree = self._adaptor.createWithPayload(string_literal97)
                    self._adaptor.addChild(root_0, string_literal97_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:85:16: ( LT )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == LT) :
                        alt25 = 1


                    if alt25 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: LT
                        pass 
                        LT98=self.match(self.input, LT, self.FOLLOW_LT_in_functionDefinition590)
                        if self._state.backtracking == 0:

                            LT98_tree = self._adaptor.createWithPayload(LT98)
                            self._adaptor.addChild(root_0, LT98_tree)



                    else:
                        break #loop25
                self._state.following.append(self.FOLLOW_identifier_in_functionDefinition593)
                identifier99 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier99.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:85:31: ( LT )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == LT) :
                        alt26 = 1


                    if alt26 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: LT
                        pass 
                        LT100=self.match(self.input, LT, self.FOLLOW_LT_in_functionDefinition595)
                        if self._state.backtracking == 0:

                            LT100_tree = self._adaptor.createWithPayload(LT100)
                            self._adaptor.addChild(root_0, LT100_tree)



                    else:
                        break #loop26
                self._state.following.append(self.FOLLOW_parameterList_in_functionDefinition598)
                parameterList101 = self.parameterList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, parameterList101.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:85:49: ( LT )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == LT) :
                        alt27 = 1


                    if alt27 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: LT
                        pass 
                        LT102=self.match(self.input, LT, self.FOLLOW_LT_in_functionDefinition600)
                        if self._state.backtracking == 0:

                            LT102_tree = self._adaptor.createWithPayload(LT102)
                            self._adaptor.addChild(root_0, LT102_tree)



                    else:
                        break #loop27
                char_literal103=self.match(self.input, 62, self.FOLLOW_62_in_functionDefinition604)
                if self._state.backtracking == 0:

                    char_literal103_tree = self._adaptor.createWithPayload(char_literal103)
                    self._adaptor.addChild(root_0, char_literal103_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:85:58: ( LT )*
                while True: #loop28
                    alt28 = 2
                    alt28 = self.dfa28.predict(self.input)
                    if alt28 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: LT
                        pass 
                        LT104=self.match(self.input, LT, self.FOLLOW_LT_in_functionDefinition606)
                        if self._state.backtracking == 0:

                            LT104_tree = self._adaptor.createWithPayload(LT104)
                            self._adaptor.addChild(root_0, LT104_tree)



                    else:
                        break #loop28
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:85:62: ( statement )*
                while True: #loop29
                    alt29 = 2
                    alt29 = self.dfa29.predict(self.input)
                    if alt29 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_functionDefinition609)
                        statement105 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, statement105.tree)


                    else:
                        break #loop29
                char_literal106=self.match(self.input, 64, self.FOLLOW_64_in_functionDefinition612)
                if self._state.backtracking == 0:

                    char_literal106_tree = self._adaptor.createWithPayload(char_literal106)
                    self._adaptor.addChild(root_0, char_literal106_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 19, functionDefinition_StartIndex, success)

            pass
        return retval

    # $ANTLR end "functionDefinition"

    class returnParameters_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.returnParameters_return, self).__init__()

            self.tree = None




    # $ANTLR start "returnParameters"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:88:1: returnParameters : 'returns' parameterList ;
    def returnParameters(self, ):

        retval = self.returnParameters_return()
        retval.start = self.input.LT(1)
        returnParameters_StartIndex = self.input.index()
        root_0 = None

        string_literal107 = None
        parameterList108 = None


        string_literal107_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:89:3: ( 'returns' parameterList )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:89:5: 'returns' parameterList
                pass 
                root_0 = self._adaptor.nil()

                string_literal107=self.match(self.input, 77, self.FOLLOW_77_in_returnParameters624)
                if self._state.backtracking == 0:

                    string_literal107_tree = self._adaptor.createWithPayload(string_literal107)
                    self._adaptor.addChild(root_0, string_literal107_tree)

                self._state.following.append(self.FOLLOW_parameterList_in_returnParameters626)
                parameterList108 = self.parameterList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, parameterList108.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 20, returnParameters_StartIndex, success)

            pass
        return retval

    # $ANTLR end "returnParameters"

    class modifierList_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.modifierList_return, self).__init__()

            self.tree = None




    # $ANTLR start "modifierList"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:91:1: modifierList : ( modifierInvocation | stateMutability | ExternalKeyword | PublicKeyword | InternalKeyword | PrivateKeyword )* ;
    def modifierList(self, ):

        retval = self.modifierList_return()
        retval.start = self.input.LT(1)
        modifierList_StartIndex = self.input.index()
        root_0 = None

        ExternalKeyword111 = None
        PublicKeyword112 = None
        InternalKeyword113 = None
        PrivateKeyword114 = None
        modifierInvocation109 = None

        stateMutability110 = None


        ExternalKeyword111_tree = None
        PublicKeyword112_tree = None
        InternalKeyword113_tree = None
        PrivateKeyword114_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:92:3: ( ( modifierInvocation | stateMutability | ExternalKeyword | PublicKeyword | InternalKeyword | PrivateKeyword )* )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:92:5: ( modifierInvocation | stateMutability | ExternalKeyword | PublicKeyword | InternalKeyword | PrivateKeyword )*
                pass 
                root_0 = self._adaptor.nil()

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:92:5: ( modifierInvocation | stateMutability | ExternalKeyword | PublicKeyword | InternalKeyword | PrivateKeyword )*
                while True: #loop30
                    alt30 = 7
                    LA30 = self.input.LA(1)
                    if LA30 == Identifier or LA30 == 61 or LA30 == 88:
                        alt30 = 1
                    elif LA30 == ConstantKeyword or LA30 == PureKeyword or LA30 == ViewKeyword or LA30 == PayableKeyword:
                        alt30 = 2
                    elif LA30 == ExternalKeyword:
                        alt30 = 3
                    elif LA30 == PublicKeyword:
                        alt30 = 4
                    elif LA30 == InternalKeyword:
                        alt30 = 5
                    elif LA30 == PrivateKeyword:
                        alt30 = 6

                    if alt30 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:92:7: modifierInvocation
                        pass 
                        self._state.following.append(self.FOLLOW_modifierInvocation_in_modifierList639)
                        modifierInvocation109 = self.modifierInvocation()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, modifierInvocation109.tree)


                    elif alt30 == 2:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:92:28: stateMutability
                        pass 
                        self._state.following.append(self.FOLLOW_stateMutability_in_modifierList643)
                        stateMutability110 = self.stateMutability()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, stateMutability110.tree)


                    elif alt30 == 3:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:92:46: ExternalKeyword
                        pass 
                        ExternalKeyword111=self.match(self.input, ExternalKeyword, self.FOLLOW_ExternalKeyword_in_modifierList647)
                        if self._state.backtracking == 0:

                            ExternalKeyword111_tree = self._adaptor.createWithPayload(ExternalKeyword111)
                            self._adaptor.addChild(root_0, ExternalKeyword111_tree)



                    elif alt30 == 4:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:93:7: PublicKeyword
                        pass 
                        PublicKeyword112=self.match(self.input, PublicKeyword, self.FOLLOW_PublicKeyword_in_modifierList655)
                        if self._state.backtracking == 0:

                            PublicKeyword112_tree = self._adaptor.createWithPayload(PublicKeyword112)
                            self._adaptor.addChild(root_0, PublicKeyword112_tree)



                    elif alt30 == 5:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:93:23: InternalKeyword
                        pass 
                        InternalKeyword113=self.match(self.input, InternalKeyword, self.FOLLOW_InternalKeyword_in_modifierList659)
                        if self._state.backtracking == 0:

                            InternalKeyword113_tree = self._adaptor.createWithPayload(InternalKeyword113)
                            self._adaptor.addChild(root_0, InternalKeyword113_tree)



                    elif alt30 == 6:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:93:41: PrivateKeyword
                        pass 
                        PrivateKeyword114=self.match(self.input, PrivateKeyword, self.FOLLOW_PrivateKeyword_in_modifierList663)
                        if self._state.backtracking == 0:

                            PrivateKeyword114_tree = self._adaptor.createWithPayload(PrivateKeyword114)
                            self._adaptor.addChild(root_0, PrivateKeyword114_tree)



                    else:
                        break #loop30



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 21, modifierList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "modifierList"

    class eventDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.eventDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "eventDefinition"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:95:1: eventDefinition : 'event' identifier eventParameterList ( AnonymousKeyword )? ';' ;
    def eventDefinition(self, ):

        retval = self.eventDefinition_return()
        retval.start = self.input.LT(1)
        eventDefinition_StartIndex = self.input.index()
        root_0 = None

        string_literal115 = None
        AnonymousKeyword118 = None
        char_literal119 = None
        identifier116 = None

        eventParameterList117 = None


        string_literal115_tree = None
        AnonymousKeyword118_tree = None
        char_literal119_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:96:3: ( 'event' identifier eventParameterList ( AnonymousKeyword )? ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:96:5: 'event' identifier eventParameterList ( AnonymousKeyword )? ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal115=self.match(self.input, 78, self.FOLLOW_78_in_eventDefinition677)
                if self._state.backtracking == 0:

                    string_literal115_tree = self._adaptor.createWithPayload(string_literal115)
                    self._adaptor.addChild(root_0, string_literal115_tree)

                self._state.following.append(self.FOLLOW_identifier_in_eventDefinition679)
                identifier116 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier116.tree)
                self._state.following.append(self.FOLLOW_eventParameterList_in_eventDefinition681)
                eventParameterList117 = self.eventParameterList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, eventParameterList117.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:96:43: ( AnonymousKeyword )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == AnonymousKeyword) :
                    alt31 = 1
                if alt31 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: AnonymousKeyword
                    pass 
                    AnonymousKeyword118=self.match(self.input, AnonymousKeyword, self.FOLLOW_AnonymousKeyword_in_eventDefinition683)
                    if self._state.backtracking == 0:

                        AnonymousKeyword118_tree = self._adaptor.createWithPayload(AnonymousKeyword118)
                        self._adaptor.addChild(root_0, AnonymousKeyword118_tree)




                char_literal119=self.match(self.input, 50, self.FOLLOW_50_in_eventDefinition686)
                if self._state.backtracking == 0:

                    char_literal119_tree = self._adaptor.createWithPayload(char_literal119)
                    self._adaptor.addChild(root_0, char_literal119_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 22, eventDefinition_StartIndex, success)

            pass
        return retval

    # $ANTLR end "eventDefinition"

    class enumValue_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.enumValue_return, self).__init__()

            self.tree = None




    # $ANTLR start "enumValue"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:98:1: enumValue : identifier ;
    def enumValue(self, ):

        retval = self.enumValue_return()
        retval.start = self.input.LT(1)
        enumValue_StartIndex = self.input.index()
        root_0 = None

        identifier120 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:99:3: ( identifier )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:99:5: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_enumValue697)
                identifier120 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier120.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 23, enumValue_StartIndex, success)

            pass
        return retval

    # $ANTLR end "enumValue"

    class enumDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.enumDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "enumDefinition"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:101:1: enumDefinition : 'enum' identifier '{' ( enumValue )? ( ',' enumValue )* '}' ;
    def enumDefinition(self, ):

        retval = self.enumDefinition_return()
        retval.start = self.input.LT(1)
        enumDefinition_StartIndex = self.input.index()
        root_0 = None

        string_literal121 = None
        char_literal123 = None
        char_literal125 = None
        char_literal127 = None
        identifier122 = None

        enumValue124 = None

        enumValue126 = None


        string_literal121_tree = None
        char_literal123_tree = None
        char_literal125_tree = None
        char_literal127_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:102:3: ( 'enum' identifier '{' ( enumValue )? ( ',' enumValue )* '}' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:102:5: 'enum' identifier '{' ( enumValue )? ( ',' enumValue )* '}'
                pass 
                root_0 = self._adaptor.nil()

                string_literal121=self.match(self.input, 79, self.FOLLOW_79_in_enumDefinition708)
                if self._state.backtracking == 0:

                    string_literal121_tree = self._adaptor.createWithPayload(string_literal121)
                    self._adaptor.addChild(root_0, string_literal121_tree)

                self._state.following.append(self.FOLLOW_identifier_in_enumDefinition710)
                identifier122 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier122.tree)
                char_literal123=self.match(self.input, 62, self.FOLLOW_62_in_enumDefinition712)
                if self._state.backtracking == 0:

                    char_literal123_tree = self._adaptor.createWithPayload(char_literal123)
                    self._adaptor.addChild(root_0, char_literal123_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:102:27: ( enumValue )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == Identifier or LA32_0 == 61 or LA32_0 == 88) :
                    alt32 = 1
                if alt32 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: enumValue
                    pass 
                    self._state.following.append(self.FOLLOW_enumValue_in_enumDefinition714)
                    enumValue124 = self.enumValue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, enumValue124.tree)



                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:102:38: ( ',' enumValue )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == 63) :
                        alt33 = 1


                    if alt33 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:102:39: ',' enumValue
                        pass 
                        char_literal125=self.match(self.input, 63, self.FOLLOW_63_in_enumDefinition718)
                        if self._state.backtracking == 0:

                            char_literal125_tree = self._adaptor.createWithPayload(char_literal125)
                            self._adaptor.addChild(root_0, char_literal125_tree)

                        self._state.following.append(self.FOLLOW_enumValue_in_enumDefinition720)
                        enumValue126 = self.enumValue()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, enumValue126.tree)


                    else:
                        break #loop33
                char_literal127=self.match(self.input, 64, self.FOLLOW_64_in_enumDefinition724)
                if self._state.backtracking == 0:

                    char_literal127_tree = self._adaptor.createWithPayload(char_literal127)
                    self._adaptor.addChild(root_0, char_literal127_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 24, enumDefinition_StartIndex, success)

            pass
        return retval

    # $ANTLR end "enumDefinition"

    class parameterList_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.parameterList_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameterList"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:104:1: parameterList : '(' ( parameter ( ',' parameter )* )? ')' ;
    def parameterList(self, ):

        retval = self.parameterList_return()
        retval.start = self.input.LT(1)
        parameterList_StartIndex = self.input.index()
        root_0 = None

        char_literal128 = None
        char_literal130 = None
        char_literal132 = None
        parameter129 = None

        parameter131 = None


        char_literal128_tree = None
        char_literal130_tree = None
        char_literal132_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:105:3: ( '(' ( parameter ( ',' parameter )* )? ')' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:105:5: '(' ( parameter ( ',' parameter )* )? ')'
                pass 
                root_0 = self._adaptor.nil()

                char_literal128=self.match(self.input, 69, self.FOLLOW_69_in_parameterList735)
                if self._state.backtracking == 0:

                    char_literal128_tree = self._adaptor.createWithPayload(char_literal128)
                    self._adaptor.addChild(root_0, char_literal128_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:105:9: ( parameter ( ',' parameter )* )?
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if ((Int <= LA35_0 <= Ufixed) or LA35_0 == Identifier or LA35_0 == 61 or LA35_0 == 76 or LA35_0 == 80 or LA35_0 == 84 or LA35_0 == 88 or (97 <= LA35_0 <= 100)) :
                    alt35 = 1
                if alt35 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:105:11: parameter ( ',' parameter )*
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_parameterList739)
                    parameter129 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parameter129.tree)
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:105:21: ( ',' parameter )*
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == 63) :
                            alt34 = 1


                        if alt34 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:105:22: ',' parameter
                            pass 
                            char_literal130=self.match(self.input, 63, self.FOLLOW_63_in_parameterList742)
                            if self._state.backtracking == 0:

                                char_literal130_tree = self._adaptor.createWithPayload(char_literal130)
                                self._adaptor.addChild(root_0, char_literal130_tree)

                            self._state.following.append(self.FOLLOW_parameter_in_parameterList744)
                            parameter131 = self.parameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, parameter131.tree)


                        else:
                            break #loop34



                char_literal132=self.match(self.input, 70, self.FOLLOW_70_in_parameterList751)
                if self._state.backtracking == 0:

                    char_literal132_tree = self._adaptor.createWithPayload(char_literal132)
                    self._adaptor.addChild(root_0, char_literal132_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 25, parameterList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "parameterList"

    class parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.parameter_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameter"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:107:1: parameter : typeName ( storageLocation )? ( identifier )? ;
    def parameter(self, ):

        retval = self.parameter_return()
        retval.start = self.input.LT(1)
        parameter_StartIndex = self.input.index()
        root_0 = None

        typeName133 = None

        storageLocation134 = None

        identifier135 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:108:3: ( typeName ( storageLocation )? ( identifier )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:108:5: typeName ( storageLocation )? ( identifier )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_typeName_in_parameter762)
                typeName133 = self.typeName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, typeName133.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:108:14: ( storageLocation )?
                alt36 = 2
                alt36 = self.dfa36.predict(self.input)
                if alt36 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: storageLocation
                    pass 
                    self._state.following.append(self.FOLLOW_storageLocation_in_parameter764)
                    storageLocation134 = self.storageLocation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, storageLocation134.tree)



                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:108:31: ( identifier )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == Identifier or LA37_0 == 61 or LA37_0 == 88) :
                    alt37 = 1
                if alt37 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_parameter767)
                    identifier135 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier135.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 26, parameter_StartIndex, success)

            pass
        return retval

    # $ANTLR end "parameter"

    class eventParameterList_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.eventParameterList_return, self).__init__()

            self.tree = None




    # $ANTLR start "eventParameterList"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:110:1: eventParameterList : '(' ( eventParameter ( ',' eventParameter )* )? ')' ;
    def eventParameterList(self, ):

        retval = self.eventParameterList_return()
        retval.start = self.input.LT(1)
        eventParameterList_StartIndex = self.input.index()
        root_0 = None

        char_literal136 = None
        char_literal138 = None
        char_literal140 = None
        eventParameter137 = None

        eventParameter139 = None


        char_literal136_tree = None
        char_literal138_tree = None
        char_literal140_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:111:3: ( '(' ( eventParameter ( ',' eventParameter )* )? ')' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:111:5: '(' ( eventParameter ( ',' eventParameter )* )? ')'
                pass 
                root_0 = self._adaptor.nil()

                char_literal136=self.match(self.input, 69, self.FOLLOW_69_in_eventParameterList779)
                if self._state.backtracking == 0:

                    char_literal136_tree = self._adaptor.createWithPayload(char_literal136)
                    self._adaptor.addChild(root_0, char_literal136_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:111:9: ( eventParameter ( ',' eventParameter )* )?
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if ((Int <= LA39_0 <= Ufixed) or LA39_0 == Identifier or LA39_0 == 61 or LA39_0 == 76 or LA39_0 == 80 or LA39_0 == 84 or LA39_0 == 88 or (97 <= LA39_0 <= 100)) :
                    alt39 = 1
                if alt39 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:111:11: eventParameter ( ',' eventParameter )*
                    pass 
                    self._state.following.append(self.FOLLOW_eventParameter_in_eventParameterList783)
                    eventParameter137 = self.eventParameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, eventParameter137.tree)
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:111:26: ( ',' eventParameter )*
                    while True: #loop38
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == 63) :
                            alt38 = 1


                        if alt38 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:111:27: ',' eventParameter
                            pass 
                            char_literal138=self.match(self.input, 63, self.FOLLOW_63_in_eventParameterList786)
                            if self._state.backtracking == 0:

                                char_literal138_tree = self._adaptor.createWithPayload(char_literal138)
                                self._adaptor.addChild(root_0, char_literal138_tree)

                            self._state.following.append(self.FOLLOW_eventParameter_in_eventParameterList788)
                            eventParameter139 = self.eventParameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, eventParameter139.tree)


                        else:
                            break #loop38



                char_literal140=self.match(self.input, 70, self.FOLLOW_70_in_eventParameterList795)
                if self._state.backtracking == 0:

                    char_literal140_tree = self._adaptor.createWithPayload(char_literal140)
                    self._adaptor.addChild(root_0, char_literal140_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 27, eventParameterList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "eventParameterList"

    class eventParameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.eventParameter_return, self).__init__()

            self.tree = None




    # $ANTLR start "eventParameter"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:113:1: eventParameter : typeName ( IndexedKeyword )? ( identifier )? ;
    def eventParameter(self, ):

        retval = self.eventParameter_return()
        retval.start = self.input.LT(1)
        eventParameter_StartIndex = self.input.index()
        root_0 = None

        IndexedKeyword142 = None
        typeName141 = None

        identifier143 = None


        IndexedKeyword142_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:114:3: ( typeName ( IndexedKeyword )? ( identifier )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:114:5: typeName ( IndexedKeyword )? ( identifier )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_typeName_in_eventParameter806)
                typeName141 = self.typeName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, typeName141.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:114:14: ( IndexedKeyword )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == IndexedKeyword) :
                    alt40 = 1
                if alt40 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: IndexedKeyword
                    pass 
                    IndexedKeyword142=self.match(self.input, IndexedKeyword, self.FOLLOW_IndexedKeyword_in_eventParameter808)
                    if self._state.backtracking == 0:

                        IndexedKeyword142_tree = self._adaptor.createWithPayload(IndexedKeyword142)
                        self._adaptor.addChild(root_0, IndexedKeyword142_tree)




                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:114:30: ( identifier )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == Identifier or LA41_0 == 61 or LA41_0 == 88) :
                    alt41 = 1
                if alt41 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_eventParameter811)
                    identifier143 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier143.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 28, eventParameter_StartIndex, success)

            pass
        return retval

    # $ANTLR end "eventParameter"

    class functionTypeParameterList_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.functionTypeParameterList_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionTypeParameterList"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:116:1: functionTypeParameterList : '(' ( functionTypeParameter ( ',' functionTypeParameter )* )? ')' ;
    def functionTypeParameterList(self, ):

        retval = self.functionTypeParameterList_return()
        retval.start = self.input.LT(1)
        functionTypeParameterList_StartIndex = self.input.index()
        root_0 = None

        char_literal144 = None
        char_literal146 = None
        char_literal148 = None
        functionTypeParameter145 = None

        functionTypeParameter147 = None


        char_literal144_tree = None
        char_literal146_tree = None
        char_literal148_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:117:3: ( '(' ( functionTypeParameter ( ',' functionTypeParameter )* )? ')' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:117:5: '(' ( functionTypeParameter ( ',' functionTypeParameter )* )? ')'
                pass 
                root_0 = self._adaptor.nil()

                char_literal144=self.match(self.input, 69, self.FOLLOW_69_in_functionTypeParameterList823)
                if self._state.backtracking == 0:

                    char_literal144_tree = self._adaptor.createWithPayload(char_literal144)
                    self._adaptor.addChild(root_0, char_literal144_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:117:9: ( functionTypeParameter ( ',' functionTypeParameter )* )?
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if ((Int <= LA43_0 <= Ufixed) or LA43_0 == Identifier or LA43_0 == 61 or LA43_0 == 76 or LA43_0 == 80 or LA43_0 == 84 or LA43_0 == 88 or (97 <= LA43_0 <= 100)) :
                    alt43 = 1
                if alt43 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:117:11: functionTypeParameter ( ',' functionTypeParameter )*
                    pass 
                    self._state.following.append(self.FOLLOW_functionTypeParameter_in_functionTypeParameterList827)
                    functionTypeParameter145 = self.functionTypeParameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, functionTypeParameter145.tree)
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:117:33: ( ',' functionTypeParameter )*
                    while True: #loop42
                        alt42 = 2
                        LA42_0 = self.input.LA(1)

                        if (LA42_0 == 63) :
                            alt42 = 1


                        if alt42 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:117:34: ',' functionTypeParameter
                            pass 
                            char_literal146=self.match(self.input, 63, self.FOLLOW_63_in_functionTypeParameterList830)
                            if self._state.backtracking == 0:

                                char_literal146_tree = self._adaptor.createWithPayload(char_literal146)
                                self._adaptor.addChild(root_0, char_literal146_tree)

                            self._state.following.append(self.FOLLOW_functionTypeParameter_in_functionTypeParameterList832)
                            functionTypeParameter147 = self.functionTypeParameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, functionTypeParameter147.tree)


                        else:
                            break #loop42



                char_literal148=self.match(self.input, 70, self.FOLLOW_70_in_functionTypeParameterList839)
                if self._state.backtracking == 0:

                    char_literal148_tree = self._adaptor.createWithPayload(char_literal148)
                    self._adaptor.addChild(root_0, char_literal148_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 29, functionTypeParameterList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "functionTypeParameterList"

    class functionTypeParameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.functionTypeParameter_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionTypeParameter"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:119:1: functionTypeParameter : typeName ( storageLocation )? ;
    def functionTypeParameter(self, ):

        retval = self.functionTypeParameter_return()
        retval.start = self.input.LT(1)
        functionTypeParameter_StartIndex = self.input.index()
        root_0 = None

        typeName149 = None

        storageLocation150 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:120:3: ( typeName ( storageLocation )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:120:5: typeName ( storageLocation )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_typeName_in_functionTypeParameter850)
                typeName149 = self.typeName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, typeName149.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:120:14: ( storageLocation )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if ((86 <= LA44_0 <= 88)) :
                    alt44 = 1
                if alt44 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: storageLocation
                    pass 
                    self._state.following.append(self.FOLLOW_storageLocation_in_functionTypeParameter852)
                    storageLocation150 = self.storageLocation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, storageLocation150.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 30, functionTypeParameter_StartIndex, success)

            pass
        return retval

    # $ANTLR end "functionTypeParameter"

    class variableDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.variableDeclaration_return, self).__init__()

            self.tree = None




    # $ANTLR start "variableDeclaration"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:122:1: variableDeclaration : typeName ( storageLocation )? identifier ;
    def variableDeclaration(self, ):

        retval = self.variableDeclaration_return()
        retval.start = self.input.LT(1)
        variableDeclaration_StartIndex = self.input.index()
        root_0 = None

        typeName151 = None

        storageLocation152 = None

        identifier153 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:123:3: ( typeName ( storageLocation )? identifier )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:123:5: typeName ( storageLocation )? identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_typeName_in_variableDeclaration864)
                typeName151 = self.typeName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, typeName151.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:123:14: ( storageLocation )?
                alt45 = 2
                alt45 = self.dfa45.predict(self.input)
                if alt45 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: storageLocation
                    pass 
                    self._state.following.append(self.FOLLOW_storageLocation_in_variableDeclaration866)
                    storageLocation152 = self.storageLocation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, storageLocation152.tree)



                self._state.following.append(self.FOLLOW_identifier_in_variableDeclaration869)
                identifier153 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier153.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 31, variableDeclaration_StartIndex, success)

            pass
        return retval

    # $ANTLR end "variableDeclaration"

    class typeName_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.typeName_return, self).__init__()

            self.tree = None




    # $ANTLR start "typeName"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:125:1: typeName : ( elementaryTypeName | userDefinedTypeName | mapping | functionTypeName | 'address' 'payable' ) ( '[' ( expression )? ']' )* ;
    def typeName(self, ):

        retval = self.typeName_return()
        retval.start = self.input.LT(1)
        typeName_StartIndex = self.input.index()
        root_0 = None

        string_literal158 = None
        string_literal159 = None
        char_literal160 = None
        char_literal162 = None
        elementaryTypeName154 = None

        userDefinedTypeName155 = None

        mapping156 = None

        functionTypeName157 = None

        expression161 = None


        string_literal158_tree = None
        string_literal159_tree = None
        char_literal160_tree = None
        char_literal162_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:3: ( ( elementaryTypeName | userDefinedTypeName | mapping | functionTypeName | 'address' 'payable' ) ( '[' ( expression )? ']' )* )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:5: ( elementaryTypeName | userDefinedTypeName | mapping | functionTypeName | 'address' 'payable' ) ( '[' ( expression )? ']' )*
                pass 
                root_0 = self._adaptor.nil()

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:5: ( elementaryTypeName | userDefinedTypeName | mapping | functionTypeName | 'address' 'payable' )
                alt46 = 5
                alt46 = self.dfa46.predict(self.input)
                if alt46 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:6: elementaryTypeName
                    pass 
                    self._state.following.append(self.FOLLOW_elementaryTypeName_in_typeName881)
                    elementaryTypeName154 = self.elementaryTypeName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementaryTypeName154.tree)


                elif alt46 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:27: userDefinedTypeName
                    pass 
                    self._state.following.append(self.FOLLOW_userDefinedTypeName_in_typeName885)
                    userDefinedTypeName155 = self.userDefinedTypeName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, userDefinedTypeName155.tree)


                elif alt46 == 3:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:49: mapping
                    pass 
                    self._state.following.append(self.FOLLOW_mapping_in_typeName889)
                    mapping156 = self.mapping()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, mapping156.tree)


                elif alt46 == 4:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:59: functionTypeName
                    pass 
                    self._state.following.append(self.FOLLOW_functionTypeName_in_typeName893)
                    functionTypeName157 = self.functionTypeName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, functionTypeName157.tree)


                elif alt46 == 5:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:78: 'address' 'payable'
                    pass 
                    string_literal158=self.match(self.input, 80, self.FOLLOW_80_in_typeName897)
                    if self._state.backtracking == 0:

                        string_literal158_tree = self._adaptor.createWithPayload(string_literal158)
                        self._adaptor.addChild(root_0, string_literal158_tree)

                    string_literal159=self.match(self.input, PayableKeyword, self.FOLLOW_PayableKeyword_in_typeName899)
                    if self._state.backtracking == 0:

                        string_literal159_tree = self._adaptor.createWithPayload(string_literal159)
                        self._adaptor.addChild(root_0, string_literal159_tree)




                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:99: ( '[' ( expression )? ']' )*
                while True: #loop48
                    alt48 = 2
                    alt48 = self.dfa48.predict(self.input)
                    if alt48 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:100: '[' ( expression )? ']'
                        pass 
                        char_literal160=self.match(self.input, 81, self.FOLLOW_81_in_typeName903)
                        if self._state.backtracking == 0:

                            char_literal160_tree = self._adaptor.createWithPayload(char_literal160)
                            self._adaptor.addChild(root_0, char_literal160_tree)

                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:104: ( expression )?
                        alt47 = 2
                        alt47 = self.dfa47.predict(self.input)
                        if alt47 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: expression
                            pass 
                            self._state.following.append(self.FOLLOW_expression_in_typeName905)
                            expression161 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, expression161.tree)



                        char_literal162=self.match(self.input, 82, self.FOLLOW_82_in_typeName908)
                        if self._state.backtracking == 0:

                            char_literal162_tree = self._adaptor.createWithPayload(char_literal162)
                            self._adaptor.addChild(root_0, char_literal162_tree)



                    else:
                        break #loop48



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 32, typeName_StartIndex, success)

            pass
        return retval

    # $ANTLR end "typeName"

    class userDefinedTypeName_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.userDefinedTypeName_return, self).__init__()

            self.tree = None




    # $ANTLR start "userDefinedTypeName"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:128:1: userDefinedTypeName : identifier ( '.' identifier )* ;
    def userDefinedTypeName(self, ):

        retval = self.userDefinedTypeName_return()
        retval.start = self.input.LT(1)
        userDefinedTypeName_StartIndex = self.input.index()
        root_0 = None

        char_literal164 = None
        identifier163 = None

        identifier165 = None


        char_literal164_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:129:3: ( identifier ( '.' identifier )* )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:129:5: identifier ( '.' identifier )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_userDefinedTypeName921)
                identifier163 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier163.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:129:16: ( '.' identifier )*
                while True: #loop49
                    alt49 = 2
                    alt49 = self.dfa49.predict(self.input)
                    if alt49 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:129:18: '.' identifier
                        pass 
                        char_literal164=self.match(self.input, 83, self.FOLLOW_83_in_userDefinedTypeName925)
                        if self._state.backtracking == 0:

                            char_literal164_tree = self._adaptor.createWithPayload(char_literal164)
                            self._adaptor.addChild(root_0, char_literal164_tree)

                        self._state.following.append(self.FOLLOW_identifier_in_userDefinedTypeName927)
                        identifier165 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier165.tree)


                    else:
                        break #loop49



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 33, userDefinedTypeName_StartIndex, success)

            pass
        return retval

    # $ANTLR end "userDefinedTypeName"

    class mapping_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.mapping_return, self).__init__()

            self.tree = None




    # $ANTLR start "mapping"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:131:1: mapping : 'mapping' '(' elementaryTypeName '=>' typeName ')' ;
    def mapping(self, ):

        retval = self.mapping_return()
        retval.start = self.input.LT(1)
        mapping_StartIndex = self.input.index()
        root_0 = None

        string_literal166 = None
        char_literal167 = None
        string_literal169 = None
        char_literal171 = None
        elementaryTypeName168 = None

        typeName170 = None


        string_literal166_tree = None
        char_literal167_tree = None
        string_literal169_tree = None
        char_literal171_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:132:3: ( 'mapping' '(' elementaryTypeName '=>' typeName ')' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:132:5: 'mapping' '(' elementaryTypeName '=>' typeName ')'
                pass 
                root_0 = self._adaptor.nil()

                string_literal166=self.match(self.input, 84, self.FOLLOW_84_in_mapping941)
                if self._state.backtracking == 0:

                    string_literal166_tree = self._adaptor.createWithPayload(string_literal166)
                    self._adaptor.addChild(root_0, string_literal166_tree)

                char_literal167=self.match(self.input, 69, self.FOLLOW_69_in_mapping943)
                if self._state.backtracking == 0:

                    char_literal167_tree = self._adaptor.createWithPayload(char_literal167)
                    self._adaptor.addChild(root_0, char_literal167_tree)

                self._state.following.append(self.FOLLOW_elementaryTypeName_in_mapping945)
                elementaryTypeName168 = self.elementaryTypeName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, elementaryTypeName168.tree)
                string_literal169=self.match(self.input, 85, self.FOLLOW_85_in_mapping947)
                if self._state.backtracking == 0:

                    string_literal169_tree = self._adaptor.createWithPayload(string_literal169)
                    self._adaptor.addChild(root_0, string_literal169_tree)

                self._state.following.append(self.FOLLOW_typeName_in_mapping949)
                typeName170 = self.typeName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, typeName170.tree)
                char_literal171=self.match(self.input, 70, self.FOLLOW_70_in_mapping951)
                if self._state.backtracking == 0:

                    char_literal171_tree = self._adaptor.createWithPayload(char_literal171)
                    self._adaptor.addChild(root_0, char_literal171_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 34, mapping_StartIndex, success)

            pass
        return retval

    # $ANTLR end "mapping"

    class functionTypeName_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.functionTypeName_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionTypeName"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:134:1: functionTypeName : 'function' functionTypeParameterList ( InternalKeyword | ExternalKeyword | stateMutability )* ( 'returns' functionTypeParameterList )? ;
    def functionTypeName(self, ):

        retval = self.functionTypeName_return()
        retval.start = self.input.LT(1)
        functionTypeName_StartIndex = self.input.index()
        root_0 = None

        string_literal172 = None
        InternalKeyword174 = None
        ExternalKeyword175 = None
        string_literal177 = None
        functionTypeParameterList173 = None

        stateMutability176 = None

        functionTypeParameterList178 = None


        string_literal172_tree = None
        InternalKeyword174_tree = None
        ExternalKeyword175_tree = None
        string_literal177_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:135:3: ( 'function' functionTypeParameterList ( InternalKeyword | ExternalKeyword | stateMutability )* ( 'returns' functionTypeParameterList )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:135:5: 'function' functionTypeParameterList ( InternalKeyword | ExternalKeyword | stateMutability )* ( 'returns' functionTypeParameterList )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal172=self.match(self.input, 76, self.FOLLOW_76_in_functionTypeName962)
                if self._state.backtracking == 0:

                    string_literal172_tree = self._adaptor.createWithPayload(string_literal172)
                    self._adaptor.addChild(root_0, string_literal172_tree)

                self._state.following.append(self.FOLLOW_functionTypeParameterList_in_functionTypeName964)
                functionTypeParameterList173 = self.functionTypeParameterList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, functionTypeParameterList173.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:136:5: ( InternalKeyword | ExternalKeyword | stateMutability )*
                while True: #loop50
                    alt50 = 4
                    alt50 = self.dfa50.predict(self.input)
                    if alt50 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:136:7: InternalKeyword
                        pass 
                        InternalKeyword174=self.match(self.input, InternalKeyword, self.FOLLOW_InternalKeyword_in_functionTypeName972)
                        if self._state.backtracking == 0:

                            InternalKeyword174_tree = self._adaptor.createWithPayload(InternalKeyword174)
                            self._adaptor.addChild(root_0, InternalKeyword174_tree)



                    elif alt50 == 2:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:136:25: ExternalKeyword
                        pass 
                        ExternalKeyword175=self.match(self.input, ExternalKeyword, self.FOLLOW_ExternalKeyword_in_functionTypeName976)
                        if self._state.backtracking == 0:

                            ExternalKeyword175_tree = self._adaptor.createWithPayload(ExternalKeyword175)
                            self._adaptor.addChild(root_0, ExternalKeyword175_tree)



                    elif alt50 == 3:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:136:43: stateMutability
                        pass 
                        self._state.following.append(self.FOLLOW_stateMutability_in_functionTypeName980)
                        stateMutability176 = self.stateMutability()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, stateMutability176.tree)


                    else:
                        break #loop50
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:137:5: ( 'returns' functionTypeParameterList )?
                alt51 = 2
                alt51 = self.dfa51.predict(self.input)
                if alt51 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:137:7: 'returns' functionTypeParameterList
                    pass 
                    string_literal177=self.match(self.input, 77, self.FOLLOW_77_in_functionTypeName991)
                    if self._state.backtracking == 0:

                        string_literal177_tree = self._adaptor.createWithPayload(string_literal177)
                        self._adaptor.addChild(root_0, string_literal177_tree)

                    self._state.following.append(self.FOLLOW_functionTypeParameterList_in_functionTypeName993)
                    functionTypeParameterList178 = self.functionTypeParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, functionTypeParameterList178.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 35, functionTypeName_StartIndex, success)

            pass
        return retval

    # $ANTLR end "functionTypeName"

    class storageLocation_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.storageLocation_return, self).__init__()

            self.tree = None




    # $ANTLR start "storageLocation"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:139:1: storageLocation : ( 'memory' | 'storage' | 'calldata' );
    def storageLocation(self, ):

        retval = self.storageLocation_return()
        retval.start = self.input.LT(1)
        storageLocation_StartIndex = self.input.index()
        root_0 = None

        set179 = None

        set179_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:140:3: ( 'memory' | 'storage' | 'calldata' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:
                pass 
                root_0 = self._adaptor.nil()

                set179 = self.input.LT(1)
                if (86 <= self.input.LA(1) <= 88):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set179))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 36, storageLocation_StartIndex, success)

            pass
        return retval

    # $ANTLR end "storageLocation"

    class stateMutability_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.stateMutability_return, self).__init__()

            self.tree = None




    # $ANTLR start "stateMutability"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:142:1: stateMutability : ( PureKeyword | ConstantKeyword | ViewKeyword | PayableKeyword );
    def stateMutability(self, ):

        retval = self.stateMutability_return()
        retval.start = self.input.LT(1)
        stateMutability_StartIndex = self.input.index()
        root_0 = None

        set180 = None

        set180_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:143:3: ( PureKeyword | ConstantKeyword | ViewKeyword | PayableKeyword )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:
                pass 
                root_0 = self._adaptor.nil()

                set180 = self.input.LT(1)
                if self.input.LA(1) == ConstantKeyword or (PureKeyword <= self.input.LA(1) <= PayableKeyword):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set180))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 37, stateMutability_StartIndex, success)

            pass
        return retval

    # $ANTLR end "stateMutability"

    class block_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.block_return, self).__init__()

            self.tree = None




    # $ANTLR start "block"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:145:1: block : '{' ( statement )* '}' ;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)
        block_StartIndex = self.input.index()
        root_0 = None

        char_literal181 = None
        char_literal183 = None
        statement182 = None


        char_literal181_tree = None
        char_literal183_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:146:3: ( '{' ( statement )* '}' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:146:5: '{' ( statement )* '}'
                pass 
                root_0 = self._adaptor.nil()

                char_literal181=self.match(self.input, 62, self.FOLLOW_62_in_block1048)
                if self._state.backtracking == 0:

                    char_literal181_tree = self._adaptor.createWithPayload(char_literal181)
                    self._adaptor.addChild(root_0, char_literal181_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:146:9: ( statement )*
                while True: #loop52
                    alt52 = 2
                    alt52 = self.dfa52.predict(self.input)
                    if alt52 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_block1050)
                        statement182 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, statement182.tree)


                    else:
                        break #loop52
                char_literal183=self.match(self.input, 64, self.FOLLOW_64_in_block1053)
                if self._state.backtracking == 0:

                    char_literal183_tree = self._adaptor.createWithPayload(char_literal183)
                    self._adaptor.addChild(root_0, char_literal183_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 38, block_StartIndex, success)

            pass
        return retval

    # $ANTLR end "block"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "statement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:148:1: statement : ( ifStatement | whileStatement | forStatement | block | inlineAssemblyStatement | doWhileStatement | continueStatement | breakStatement | returnStatement | throwStatement | emitStatement | simpleStatement );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)
        statement_StartIndex = self.input.index()
        root_0 = None

        ifStatement184 = None

        whileStatement185 = None

        forStatement186 = None

        block187 = None

        inlineAssemblyStatement188 = None

        doWhileStatement189 = None

        continueStatement190 = None

        breakStatement191 = None

        returnStatement192 = None

        throwStatement193 = None

        emitStatement194 = None

        simpleStatement195 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:149:3: ( ifStatement | whileStatement | forStatement | block | inlineAssemblyStatement | doWhileStatement | continueStatement | breakStatement | returnStatement | throwStatement | emitStatement | simpleStatement )
                alt53 = 12
                alt53 = self.dfa53.predict(self.input)
                if alt53 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:149:5: ifStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ifStatement_in_statement1064)
                    ifStatement184 = self.ifStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ifStatement184.tree)


                elif alt53 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:150:5: whileStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_whileStatement_in_statement1070)
                    whileStatement185 = self.whileStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, whileStatement185.tree)


                elif alt53 == 3:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:151:5: forStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_forStatement_in_statement1076)
                    forStatement186 = self.forStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, forStatement186.tree)


                elif alt53 == 4:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:152:5: block
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_block_in_statement1082)
                    block187 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block187.tree)


                elif alt53 == 5:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:153:5: inlineAssemblyStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_inlineAssemblyStatement_in_statement1088)
                    inlineAssemblyStatement188 = self.inlineAssemblyStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, inlineAssemblyStatement188.tree)


                elif alt53 == 6:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:154:5: doWhileStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_doWhileStatement_in_statement1094)
                    doWhileStatement189 = self.doWhileStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, doWhileStatement189.tree)


                elif alt53 == 7:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:155:5: continueStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_continueStatement_in_statement1100)
                    continueStatement190 = self.continueStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, continueStatement190.tree)


                elif alt53 == 8:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:156:5: breakStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_breakStatement_in_statement1106)
                    breakStatement191 = self.breakStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, breakStatement191.tree)


                elif alt53 == 9:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:157:5: returnStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_returnStatement_in_statement1112)
                    returnStatement192 = self.returnStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, returnStatement192.tree)


                elif alt53 == 10:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:158:5: throwStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_throwStatement_in_statement1118)
                    throwStatement193 = self.throwStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, throwStatement193.tree)


                elif alt53 == 11:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:159:5: emitStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_emitStatement_in_statement1124)
                    emitStatement194 = self.emitStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, emitStatement194.tree)


                elif alt53 == 12:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:160:5: simpleStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_simpleStatement_in_statement1130)
                    simpleStatement195 = self.simpleStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simpleStatement195.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 39, statement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "statement"

    class expressionStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.expressionStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "expressionStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:162:1: expressionStatement : expression ';' ;
    def expressionStatement(self, ):

        retval = self.expressionStatement_return()
        retval.start = self.input.LT(1)
        expressionStatement_StartIndex = self.input.index()
        root_0 = None

        char_literal197 = None
        expression196 = None


        char_literal197_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:163:3: ( expression ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:163:5: expression ';'
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expression_in_expressionStatement1141)
                expression196 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression196.tree)
                char_literal197=self.match(self.input, 50, self.FOLLOW_50_in_expressionStatement1143)
                if self._state.backtracking == 0:

                    char_literal197_tree = self._adaptor.createWithPayload(char_literal197)
                    self._adaptor.addChild(root_0, char_literal197_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 40, expressionStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "expressionStatement"

    class ifStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.ifStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "ifStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:165:1: ifStatement : 'if' '(' expression ')' statement ( 'else' statement )? ;
    def ifStatement(self, ):

        retval = self.ifStatement_return()
        retval.start = self.input.LT(1)
        ifStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal198 = None
        char_literal199 = None
        char_literal201 = None
        string_literal203 = None
        expression200 = None

        statement202 = None

        statement204 = None


        string_literal198_tree = None
        char_literal199_tree = None
        char_literal201_tree = None
        string_literal203_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:166:3: ( 'if' '(' expression ')' statement ( 'else' statement )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:166:5: 'if' '(' expression ')' statement ( 'else' statement )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal198=self.match(self.input, 89, self.FOLLOW_89_in_ifStatement1154)
                if self._state.backtracking == 0:

                    string_literal198_tree = self._adaptor.createWithPayload(string_literal198)
                    self._adaptor.addChild(root_0, string_literal198_tree)

                char_literal199=self.match(self.input, 69, self.FOLLOW_69_in_ifStatement1156)
                if self._state.backtracking == 0:

                    char_literal199_tree = self._adaptor.createWithPayload(char_literal199)
                    self._adaptor.addChild(root_0, char_literal199_tree)

                self._state.following.append(self.FOLLOW_expression_in_ifStatement1158)
                expression200 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression200.tree)
                char_literal201=self.match(self.input, 70, self.FOLLOW_70_in_ifStatement1160)
                if self._state.backtracking == 0:

                    char_literal201_tree = self._adaptor.createWithPayload(char_literal201)
                    self._adaptor.addChild(root_0, char_literal201_tree)

                self._state.following.append(self.FOLLOW_statement_in_ifStatement1162)
                statement202 = self.statement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, statement202.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:166:39: ( 'else' statement )?
                alt54 = 2
                alt54 = self.dfa54.predict(self.input)
                if alt54 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:166:41: 'else' statement
                    pass 
                    string_literal203=self.match(self.input, 90, self.FOLLOW_90_in_ifStatement1166)
                    if self._state.backtracking == 0:

                        string_literal203_tree = self._adaptor.createWithPayload(string_literal203)
                        self._adaptor.addChild(root_0, string_literal203_tree)

                    self._state.following.append(self.FOLLOW_statement_in_ifStatement1168)
                    statement204 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement204.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 41, ifStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "ifStatement"

    class whileStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.whileStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "whileStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:168:1: whileStatement : 'while' '(' expression ')' statement ;
    def whileStatement(self, ):

        retval = self.whileStatement_return()
        retval.start = self.input.LT(1)
        whileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal205 = None
        char_literal206 = None
        char_literal208 = None
        expression207 = None

        statement209 = None


        string_literal205_tree = None
        char_literal206_tree = None
        char_literal208_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:169:3: ( 'while' '(' expression ')' statement )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:169:5: 'while' '(' expression ')' statement
                pass 
                root_0 = self._adaptor.nil()

                string_literal205=self.match(self.input, 91, self.FOLLOW_91_in_whileStatement1182)
                if self._state.backtracking == 0:

                    string_literal205_tree = self._adaptor.createWithPayload(string_literal205)
                    self._adaptor.addChild(root_0, string_literal205_tree)

                char_literal206=self.match(self.input, 69, self.FOLLOW_69_in_whileStatement1184)
                if self._state.backtracking == 0:

                    char_literal206_tree = self._adaptor.createWithPayload(char_literal206)
                    self._adaptor.addChild(root_0, char_literal206_tree)

                self._state.following.append(self.FOLLOW_expression_in_whileStatement1186)
                expression207 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression207.tree)
                char_literal208=self.match(self.input, 70, self.FOLLOW_70_in_whileStatement1188)
                if self._state.backtracking == 0:

                    char_literal208_tree = self._adaptor.createWithPayload(char_literal208)
                    self._adaptor.addChild(root_0, char_literal208_tree)

                self._state.following.append(self.FOLLOW_statement_in_whileStatement1190)
                statement209 = self.statement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, statement209.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 42, whileStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "whileStatement"

    class simpleStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.simpleStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "simpleStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:171:1: simpleStatement : ( variableDeclarationStatement | expressionStatement ) ;
    def simpleStatement(self, ):

        retval = self.simpleStatement_return()
        retval.start = self.input.LT(1)
        simpleStatement_StartIndex = self.input.index()
        root_0 = None

        variableDeclarationStatement210 = None

        expressionStatement211 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:172:3: ( ( variableDeclarationStatement | expressionStatement ) )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:172:5: ( variableDeclarationStatement | expressionStatement )
                pass 
                root_0 = self._adaptor.nil()

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:172:5: ( variableDeclarationStatement | expressionStatement )
                alt55 = 2
                alt55 = self.dfa55.predict(self.input)
                if alt55 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:172:7: variableDeclarationStatement
                    pass 
                    self._state.following.append(self.FOLLOW_variableDeclarationStatement_in_simpleStatement1203)
                    variableDeclarationStatement210 = self.variableDeclarationStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variableDeclarationStatement210.tree)


                elif alt55 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:172:38: expressionStatement
                    pass 
                    self._state.following.append(self.FOLLOW_expressionStatement_in_simpleStatement1207)
                    expressionStatement211 = self.expressionStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expressionStatement211.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 43, simpleStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "simpleStatement"

    class forStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.forStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "forStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:174:1: forStatement : 'for' '(' ( simpleStatement | ';' ) ( expressionStatement | ';' ) ( expression )? ')' statement ;
    def forStatement(self, ):

        retval = self.forStatement_return()
        retval.start = self.input.LT(1)
        forStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal212 = None
        char_literal213 = None
        char_literal215 = None
        char_literal217 = None
        char_literal219 = None
        simpleStatement214 = None

        expressionStatement216 = None

        expression218 = None

        statement220 = None


        string_literal212_tree = None
        char_literal213_tree = None
        char_literal215_tree = None
        char_literal217_tree = None
        char_literal219_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:175:3: ( 'for' '(' ( simpleStatement | ';' ) ( expressionStatement | ';' ) ( expression )? ')' statement )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:175:5: 'for' '(' ( simpleStatement | ';' ) ( expressionStatement | ';' ) ( expression )? ')' statement
                pass 
                root_0 = self._adaptor.nil()

                string_literal212=self.match(self.input, 72, self.FOLLOW_72_in_forStatement1220)
                if self._state.backtracking == 0:

                    string_literal212_tree = self._adaptor.createWithPayload(string_literal212)
                    self._adaptor.addChild(root_0, string_literal212_tree)

                char_literal213=self.match(self.input, 69, self.FOLLOW_69_in_forStatement1222)
                if self._state.backtracking == 0:

                    char_literal213_tree = self._adaptor.createWithPayload(char_literal213)
                    self._adaptor.addChild(root_0, char_literal213_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:175:15: ( simpleStatement | ';' )
                alt56 = 2
                alt56 = self.dfa56.predict(self.input)
                if alt56 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:175:17: simpleStatement
                    pass 
                    self._state.following.append(self.FOLLOW_simpleStatement_in_forStatement1226)
                    simpleStatement214 = self.simpleStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simpleStatement214.tree)


                elif alt56 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:175:35: ';'
                    pass 
                    char_literal215=self.match(self.input, 50, self.FOLLOW_50_in_forStatement1230)
                    if self._state.backtracking == 0:

                        char_literal215_tree = self._adaptor.createWithPayload(char_literal215)
                        self._adaptor.addChild(root_0, char_literal215_tree)




                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:175:41: ( expressionStatement | ';' )
                alt57 = 2
                alt57 = self.dfa57.predict(self.input)
                if alt57 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:175:43: expressionStatement
                    pass 
                    self._state.following.append(self.FOLLOW_expressionStatement_in_forStatement1236)
                    expressionStatement216 = self.expressionStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expressionStatement216.tree)


                elif alt57 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:175:65: ';'
                    pass 
                    char_literal217=self.match(self.input, 50, self.FOLLOW_50_in_forStatement1240)
                    if self._state.backtracking == 0:

                        char_literal217_tree = self._adaptor.createWithPayload(char_literal217)
                        self._adaptor.addChild(root_0, char_literal217_tree)




                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:175:71: ( expression )?
                alt58 = 2
                alt58 = self.dfa58.predict(self.input)
                if alt58 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_forStatement1244)
                    expression218 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression218.tree)



                char_literal219=self.match(self.input, 70, self.FOLLOW_70_in_forStatement1247)
                if self._state.backtracking == 0:

                    char_literal219_tree = self._adaptor.createWithPayload(char_literal219)
                    self._adaptor.addChild(root_0, char_literal219_tree)

                self._state.following.append(self.FOLLOW_statement_in_forStatement1249)
                statement220 = self.statement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, statement220.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 44, forStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "forStatement"

    class inlineAssemblyStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.inlineAssemblyStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "inlineAssemblyStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:177:1: inlineAssemblyStatement : 'assembly' ( StringLiteral )? assemblyBlock ;
    def inlineAssemblyStatement(self, ):

        retval = self.inlineAssemblyStatement_return()
        retval.start = self.input.LT(1)
        inlineAssemblyStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal221 = None
        StringLiteral222 = None
        assemblyBlock223 = None


        string_literal221_tree = None
        StringLiteral222_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:178:3: ( 'assembly' ( StringLiteral )? assemblyBlock )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:178:5: 'assembly' ( StringLiteral )? assemblyBlock
                pass 
                root_0 = self._adaptor.nil()

                string_literal221=self.match(self.input, 92, self.FOLLOW_92_in_inlineAssemblyStatement1260)
                if self._state.backtracking == 0:

                    string_literal221_tree = self._adaptor.createWithPayload(string_literal221)
                    self._adaptor.addChild(root_0, string_literal221_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:178:16: ( StringLiteral )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == StringLiteral) :
                    alt59 = 1
                if alt59 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: StringLiteral
                    pass 
                    StringLiteral222=self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_inlineAssemblyStatement1262)
                    if self._state.backtracking == 0:

                        StringLiteral222_tree = self._adaptor.createWithPayload(StringLiteral222)
                        self._adaptor.addChild(root_0, StringLiteral222_tree)




                self._state.following.append(self.FOLLOW_assemblyBlock_in_inlineAssemblyStatement1265)
                assemblyBlock223 = self.assemblyBlock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyBlock223.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 45, inlineAssemblyStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "inlineAssemblyStatement"

    class doWhileStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.doWhileStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "doWhileStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:180:1: doWhileStatement : 'do' statement 'while' '(' expression ')' ';' ;
    def doWhileStatement(self, ):

        retval = self.doWhileStatement_return()
        retval.start = self.input.LT(1)
        doWhileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal224 = None
        string_literal226 = None
        char_literal227 = None
        char_literal229 = None
        char_literal230 = None
        statement225 = None

        expression228 = None


        string_literal224_tree = None
        string_literal226_tree = None
        char_literal227_tree = None
        char_literal229_tree = None
        char_literal230_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:181:3: ( 'do' statement 'while' '(' expression ')' ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:181:5: 'do' statement 'while' '(' expression ')' ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal224=self.match(self.input, 93, self.FOLLOW_93_in_doWhileStatement1276)
                if self._state.backtracking == 0:

                    string_literal224_tree = self._adaptor.createWithPayload(string_literal224)
                    self._adaptor.addChild(root_0, string_literal224_tree)

                self._state.following.append(self.FOLLOW_statement_in_doWhileStatement1278)
                statement225 = self.statement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, statement225.tree)
                string_literal226=self.match(self.input, 91, self.FOLLOW_91_in_doWhileStatement1280)
                if self._state.backtracking == 0:

                    string_literal226_tree = self._adaptor.createWithPayload(string_literal226)
                    self._adaptor.addChild(root_0, string_literal226_tree)

                char_literal227=self.match(self.input, 69, self.FOLLOW_69_in_doWhileStatement1282)
                if self._state.backtracking == 0:

                    char_literal227_tree = self._adaptor.createWithPayload(char_literal227)
                    self._adaptor.addChild(root_0, char_literal227_tree)

                self._state.following.append(self.FOLLOW_expression_in_doWhileStatement1284)
                expression228 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression228.tree)
                char_literal229=self.match(self.input, 70, self.FOLLOW_70_in_doWhileStatement1286)
                if self._state.backtracking == 0:

                    char_literal229_tree = self._adaptor.createWithPayload(char_literal229)
                    self._adaptor.addChild(root_0, char_literal229_tree)

                char_literal230=self.match(self.input, 50, self.FOLLOW_50_in_doWhileStatement1288)
                if self._state.backtracking == 0:

                    char_literal230_tree = self._adaptor.createWithPayload(char_literal230)
                    self._adaptor.addChild(root_0, char_literal230_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 46, doWhileStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "doWhileStatement"

    class continueStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.continueStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "continueStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:183:1: continueStatement : 'continue' ';' ;
    def continueStatement(self, ):

        retval = self.continueStatement_return()
        retval.start = self.input.LT(1)
        continueStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal231 = None
        char_literal232 = None

        string_literal231_tree = None
        char_literal232_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:184:3: ( 'continue' ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:184:5: 'continue' ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal231=self.match(self.input, ContinueKeyword, self.FOLLOW_ContinueKeyword_in_continueStatement1299)
                if self._state.backtracking == 0:

                    string_literal231_tree = self._adaptor.createWithPayload(string_literal231)
                    self._adaptor.addChild(root_0, string_literal231_tree)

                char_literal232=self.match(self.input, 50, self.FOLLOW_50_in_continueStatement1301)
                if self._state.backtracking == 0:

                    char_literal232_tree = self._adaptor.createWithPayload(char_literal232)
                    self._adaptor.addChild(root_0, char_literal232_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 47, continueStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "continueStatement"

    class breakStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.breakStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "breakStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:186:1: breakStatement : 'break' ';' ;
    def breakStatement(self, ):

        retval = self.breakStatement_return()
        retval.start = self.input.LT(1)
        breakStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal233 = None
        char_literal234 = None

        string_literal233_tree = None
        char_literal234_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:187:3: ( 'break' ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:187:5: 'break' ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal233=self.match(self.input, BreakKeyword, self.FOLLOW_BreakKeyword_in_breakStatement1312)
                if self._state.backtracking == 0:

                    string_literal233_tree = self._adaptor.createWithPayload(string_literal233)
                    self._adaptor.addChild(root_0, string_literal233_tree)

                char_literal234=self.match(self.input, 50, self.FOLLOW_50_in_breakStatement1314)
                if self._state.backtracking == 0:

                    char_literal234_tree = self._adaptor.createWithPayload(char_literal234)
                    self._adaptor.addChild(root_0, char_literal234_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 48, breakStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "breakStatement"

    class returnStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.returnStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "returnStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:189:1: returnStatement : 'return' ( expression )? ';' ;
    def returnStatement(self, ):

        retval = self.returnStatement_return()
        retval.start = self.input.LT(1)
        returnStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal235 = None
        char_literal237 = None
        expression236 = None


        string_literal235_tree = None
        char_literal237_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:190:3: ( 'return' ( expression )? ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:190:5: 'return' ( expression )? ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal235=self.match(self.input, 94, self.FOLLOW_94_in_returnStatement1325)
                if self._state.backtracking == 0:

                    string_literal235_tree = self._adaptor.createWithPayload(string_literal235)
                    self._adaptor.addChild(root_0, string_literal235_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:190:14: ( expression )?
                alt60 = 2
                alt60 = self.dfa60.predict(self.input)
                if alt60 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_returnStatement1327)
                    expression236 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression236.tree)



                char_literal237=self.match(self.input, 50, self.FOLLOW_50_in_returnStatement1330)
                if self._state.backtracking == 0:

                    char_literal237_tree = self._adaptor.createWithPayload(char_literal237)
                    self._adaptor.addChild(root_0, char_literal237_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 49, returnStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "returnStatement"

    class throwStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.throwStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "throwStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:192:1: throwStatement : 'throw' ';' ;
    def throwStatement(self, ):

        retval = self.throwStatement_return()
        retval.start = self.input.LT(1)
        throwStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal238 = None
        char_literal239 = None

        string_literal238_tree = None
        char_literal239_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:193:3: ( 'throw' ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:193:5: 'throw' ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal238=self.match(self.input, 95, self.FOLLOW_95_in_throwStatement1341)
                if self._state.backtracking == 0:

                    string_literal238_tree = self._adaptor.createWithPayload(string_literal238)
                    self._adaptor.addChild(root_0, string_literal238_tree)

                char_literal239=self.match(self.input, 50, self.FOLLOW_50_in_throwStatement1343)
                if self._state.backtracking == 0:

                    char_literal239_tree = self._adaptor.createWithPayload(char_literal239)
                    self._adaptor.addChild(root_0, char_literal239_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 50, throwStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "throwStatement"

    class emitStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.emitStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "emitStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:195:1: emitStatement : 'emit' functionCall ';' ;
    def emitStatement(self, ):

        retval = self.emitStatement_return()
        retval.start = self.input.LT(1)
        emitStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal240 = None
        char_literal242 = None
        functionCall241 = None


        string_literal240_tree = None
        char_literal242_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:196:3: ( 'emit' functionCall ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:196:5: 'emit' functionCall ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal240=self.match(self.input, 96, self.FOLLOW_96_in_emitStatement1354)
                if self._state.backtracking == 0:

                    string_literal240_tree = self._adaptor.createWithPayload(string_literal240)
                    self._adaptor.addChild(root_0, string_literal240_tree)

                self._state.following.append(self.FOLLOW_functionCall_in_emitStatement1356)
                functionCall241 = self.functionCall()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, functionCall241.tree)
                char_literal242=self.match(self.input, 50, self.FOLLOW_50_in_emitStatement1358)
                if self._state.backtracking == 0:

                    char_literal242_tree = self._adaptor.createWithPayload(char_literal242)
                    self._adaptor.addChild(root_0, char_literal242_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 51, emitStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "emitStatement"

    class variableDeclarationStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.variableDeclarationStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "variableDeclarationStatement"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:198:1: variableDeclarationStatement : ( 'var' identifierList | variableDeclaration | '(' variableDeclarationList ')' ) ( '=' expression )? ';' ;
    def variableDeclarationStatement(self, ):

        retval = self.variableDeclarationStatement_return()
        retval.start = self.input.LT(1)
        variableDeclarationStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal243 = None
        char_literal246 = None
        char_literal248 = None
        char_literal249 = None
        char_literal251 = None
        identifierList244 = None

        variableDeclaration245 = None

        variableDeclarationList247 = None

        expression250 = None


        string_literal243_tree = None
        char_literal246_tree = None
        char_literal248_tree = None
        char_literal249_tree = None
        char_literal251_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:199:3: ( ( 'var' identifierList | variableDeclaration | '(' variableDeclarationList ')' ) ( '=' expression )? ';' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:199:5: ( 'var' identifierList | variableDeclaration | '(' variableDeclarationList ')' ) ( '=' expression )? ';'
                pass 
                root_0 = self._adaptor.nil()

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:199:5: ( 'var' identifierList | variableDeclaration | '(' variableDeclarationList ')' )
                alt61 = 3
                alt61 = self.dfa61.predict(self.input)
                if alt61 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:199:7: 'var' identifierList
                    pass 
                    string_literal243=self.match(self.input, 97, self.FOLLOW_97_in_variableDeclarationStatement1371)
                    if self._state.backtracking == 0:

                        string_literal243_tree = self._adaptor.createWithPayload(string_literal243)
                        self._adaptor.addChild(root_0, string_literal243_tree)

                    self._state.following.append(self.FOLLOW_identifierList_in_variableDeclarationStatement1373)
                    identifierList244 = self.identifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifierList244.tree)


                elif alt61 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:199:30: variableDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationStatement1377)
                    variableDeclaration245 = self.variableDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variableDeclaration245.tree)


                elif alt61 == 3:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:199:52: '(' variableDeclarationList ')'
                    pass 
                    char_literal246=self.match(self.input, 69, self.FOLLOW_69_in_variableDeclarationStatement1381)
                    if self._state.backtracking == 0:

                        char_literal246_tree = self._adaptor.createWithPayload(char_literal246)
                        self._adaptor.addChild(root_0, char_literal246_tree)

                    self._state.following.append(self.FOLLOW_variableDeclarationList_in_variableDeclarationStatement1383)
                    variableDeclarationList247 = self.variableDeclarationList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variableDeclarationList247.tree)
                    char_literal248=self.match(self.input, 70, self.FOLLOW_70_in_variableDeclarationStatement1385)
                    if self._state.backtracking == 0:

                        char_literal248_tree = self._adaptor.createWithPayload(char_literal248)
                        self._adaptor.addChild(root_0, char_literal248_tree)




                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:199:86: ( '=' expression )?
                alt62 = 2
                LA62_0 = self.input.LA(1)

                if (LA62_0 == 57) :
                    alt62 = 1
                if alt62 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:199:88: '=' expression
                    pass 
                    char_literal249=self.match(self.input, 57, self.FOLLOW_57_in_variableDeclarationStatement1391)
                    if self._state.backtracking == 0:

                        char_literal249_tree = self._adaptor.createWithPayload(char_literal249)
                        self._adaptor.addChild(root_0, char_literal249_tree)

                    self._state.following.append(self.FOLLOW_expression_in_variableDeclarationStatement1393)
                    expression250 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression250.tree)



                char_literal251=self.match(self.input, 50, self.FOLLOW_50_in_variableDeclarationStatement1398)
                if self._state.backtracking == 0:

                    char_literal251_tree = self._adaptor.createWithPayload(char_literal251)
                    self._adaptor.addChild(root_0, char_literal251_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 52, variableDeclarationStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "variableDeclarationStatement"

    class variableDeclarationList_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.variableDeclarationList_return, self).__init__()

            self.tree = None




    # $ANTLR start "variableDeclarationList"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:201:1: variableDeclarationList : ( variableDeclaration )? ( ',' ( variableDeclaration )? )* ;
    def variableDeclarationList(self, ):

        retval = self.variableDeclarationList_return()
        retval.start = self.input.LT(1)
        variableDeclarationList_StartIndex = self.input.index()
        root_0 = None

        char_literal253 = None
        variableDeclaration252 = None

        variableDeclaration254 = None


        char_literal253_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:202:3: ( ( variableDeclaration )? ( ',' ( variableDeclaration )? )* )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:202:5: ( variableDeclaration )? ( ',' ( variableDeclaration )? )*
                pass 
                root_0 = self._adaptor.nil()

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:202:5: ( variableDeclaration )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if ((Int <= LA63_0 <= Ufixed) or LA63_0 == Identifier or LA63_0 == 61 or LA63_0 == 76 or LA63_0 == 80 or LA63_0 == 84 or LA63_0 == 88 or (97 <= LA63_0 <= 100)) :
                    alt63 = 1
                if alt63 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: variableDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList1408)
                    variableDeclaration252 = self.variableDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variableDeclaration252.tree)



                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:202:26: ( ',' ( variableDeclaration )? )*
                while True: #loop65
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if (LA65_0 == 63) :
                        alt65 = 1


                    if alt65 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:202:27: ',' ( variableDeclaration )?
                        pass 
                        char_literal253=self.match(self.input, 63, self.FOLLOW_63_in_variableDeclarationList1412)
                        if self._state.backtracking == 0:

                            char_literal253_tree = self._adaptor.createWithPayload(char_literal253)
                            self._adaptor.addChild(root_0, char_literal253_tree)

                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:202:31: ( variableDeclaration )?
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if ((Int <= LA64_0 <= Ufixed) or LA64_0 == Identifier or LA64_0 == 61 or LA64_0 == 76 or LA64_0 == 80 or LA64_0 == 84 or LA64_0 == 88 or (97 <= LA64_0 <= 100)) :
                            alt64 = 1
                        if alt64 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: variableDeclaration
                            pass 
                            self._state.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList1414)
                            variableDeclaration254 = self.variableDeclaration()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, variableDeclaration254.tree)





                    else:
                        break #loop65



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 53, variableDeclarationList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "variableDeclarationList"

    class identifierList_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.identifierList_return, self).__init__()

            self.tree = None




    # $ANTLR start "identifierList"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:204:1: identifierList : '(' ( ( identifier )? ',' )* ( identifier )? ')' ;
    def identifierList(self, ):

        retval = self.identifierList_return()
        retval.start = self.input.LT(1)
        identifierList_StartIndex = self.input.index()
        root_0 = None

        char_literal255 = None
        char_literal257 = None
        char_literal259 = None
        identifier256 = None

        identifier258 = None


        char_literal255_tree = None
        char_literal257_tree = None
        char_literal259_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:205:3: ( '(' ( ( identifier )? ',' )* ( identifier )? ')' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:205:5: '(' ( ( identifier )? ',' )* ( identifier )? ')'
                pass 
                root_0 = self._adaptor.nil()

                char_literal255=self.match(self.input, 69, self.FOLLOW_69_in_identifierList1429)
                if self._state.backtracking == 0:

                    char_literal255_tree = self._adaptor.createWithPayload(char_literal255)
                    self._adaptor.addChild(root_0, char_literal255_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:205:9: ( ( identifier )? ',' )*
                while True: #loop67
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if (LA67_0 == Identifier or LA67_0 == 61 or LA67_0 == 88) :
                        LA67_1 = self.input.LA(2)

                        if (LA67_1 == 63) :
                            alt67 = 1


                    elif (LA67_0 == 63) :
                        alt67 = 1


                    if alt67 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:205:11: ( identifier )? ','
                        pass 
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:205:11: ( identifier )?
                        alt66 = 2
                        LA66_0 = self.input.LA(1)

                        if (LA66_0 == Identifier or LA66_0 == 61 or LA66_0 == 88) :
                            alt66 = 1
                        if alt66 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: identifier
                            pass 
                            self._state.following.append(self.FOLLOW_identifier_in_identifierList1433)
                            identifier256 = self.identifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, identifier256.tree)



                        char_literal257=self.match(self.input, 63, self.FOLLOW_63_in_identifierList1436)
                        if self._state.backtracking == 0:

                            char_literal257_tree = self._adaptor.createWithPayload(char_literal257)
                            self._adaptor.addChild(root_0, char_literal257_tree)



                    else:
                        break #loop67
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:205:30: ( identifier )?
                alt68 = 2
                LA68_0 = self.input.LA(1)

                if (LA68_0 == Identifier or LA68_0 == 61 or LA68_0 == 88) :
                    alt68 = 1
                if alt68 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_identifierList1441)
                    identifier258 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier258.tree)



                char_literal259=self.match(self.input, 70, self.FOLLOW_70_in_identifierList1444)
                if self._state.backtracking == 0:

                    char_literal259_tree = self._adaptor.createWithPayload(char_literal259)
                    self._adaptor.addChild(root_0, char_literal259_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 54, identifierList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "identifierList"

    class elementaryTypeName_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.elementaryTypeName_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementaryTypeName"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:207:1: elementaryTypeName : ( 'address' | 'bool' | 'string' | 'var' | Int | Uint | 'byte' | Byte | Fixed | Ufixed );
    def elementaryTypeName(self, ):

        retval = self.elementaryTypeName_return()
        retval.start = self.input.LT(1)
        elementaryTypeName_StartIndex = self.input.index()
        root_0 = None

        set260 = None

        set260_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:208:3: ( 'address' | 'bool' | 'string' | 'var' | Int | Uint | 'byte' | Byte | Fixed | Ufixed )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:
                pass 
                root_0 = self._adaptor.nil()

                set260 = self.input.LT(1)
                if (Int <= self.input.LA(1) <= Ufixed) or self.input.LA(1) == 80 or (97 <= self.input.LA(1) <= 100):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set260))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 55, elementaryTypeName_StartIndex, success)

            pass
        return retval

    # $ANTLR end "elementaryTypeName"

    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.expression_return, self).__init__()

            self.tree = None




    # $ANTLR start "expression"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:226:1: expression : ( 'new' typeName | '(' expression ')' | ( '++' | '--' ) expression | ( '+' | '-' ) expression | ( 'after' | 'delete' ) expression | '!' expression | '~' expression | primaryExpression ) ( ( '++' | '--' ) | '[' expression ']' | '(' functionCallArguments ')' | '.' identifier | '**' expression | ( '*' | '/' | '%' ) expression | ( '+' | '-' ) expression | ( '<<' | '>>' ) expression | '&' expression | '^' expression | '|' expression | ( '<' | '>' | '<=' | '>=' ) expression | ( '==' | '!=' ) expression | '&&' expression | '||' expression | '?' expression ':' expression | ( '=' | '|=' | '^=' | '&=' | '<<=' | '>>=' | '+=' | '-=' | '*=' | '/=' | '%=' ) expression )* ;
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)
        expression_StartIndex = self.input.index()
        root_0 = None

        string_literal261 = None
        char_literal263 = None
        char_literal265 = None
        set266 = None
        set268 = None
        set270 = None
        char_literal272 = None
        char_literal274 = None
        set277 = None
        char_literal278 = None
        char_literal280 = None
        char_literal281 = None
        char_literal283 = None
        char_literal284 = None
        string_literal286 = None
        set288 = None
        set290 = None
        set292 = None
        char_literal294 = None
        char_literal296 = None
        char_literal298 = None
        set300 = None
        set302 = None
        string_literal304 = None
        string_literal306 = None
        char_literal308 = None
        char_literal310 = None
        set312 = None
        typeName262 = None

        expression264 = None

        expression267 = None

        expression269 = None

        expression271 = None

        expression273 = None

        expression275 = None

        primaryExpression276 = None

        expression279 = None

        functionCallArguments282 = None

        identifier285 = None

        expression287 = None

        expression289 = None

        expression291 = None

        expression293 = None

        expression295 = None

        expression297 = None

        expression299 = None

        expression301 = None

        expression303 = None

        expression305 = None

        expression307 = None

        expression309 = None

        expression311 = None

        expression313 = None


        string_literal261_tree = None
        char_literal263_tree = None
        char_literal265_tree = None
        set266_tree = None
        set268_tree = None
        set270_tree = None
        char_literal272_tree = None
        char_literal274_tree = None
        set277_tree = None
        char_literal278_tree = None
        char_literal280_tree = None
        char_literal281_tree = None
        char_literal283_tree = None
        char_literal284_tree = None
        string_literal286_tree = None
        set288_tree = None
        set290_tree = None
        set292_tree = None
        char_literal294_tree = None
        char_literal296_tree = None
        char_literal298_tree = None
        set300_tree = None
        set302_tree = None
        string_literal304_tree = None
        string_literal306_tree = None
        char_literal308_tree = None
        char_literal310_tree = None
        set312_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:3: ( ( 'new' typeName | '(' expression ')' | ( '++' | '--' ) expression | ( '+' | '-' ) expression | ( 'after' | 'delete' ) expression | '!' expression | '~' expression | primaryExpression ) ( ( '++' | '--' ) | '[' expression ']' | '(' functionCallArguments ')' | '.' identifier | '**' expression | ( '*' | '/' | '%' ) expression | ( '+' | '-' ) expression | ( '<<' | '>>' ) expression | '&' expression | '^' expression | '|' expression | ( '<' | '>' | '<=' | '>=' ) expression | ( '==' | '!=' ) expression | '&&' expression | '||' expression | '?' expression ':' expression | ( '=' | '|=' | '^=' | '&=' | '<<=' | '>>=' | '+=' | '-=' | '*=' | '/=' | '%=' ) expression )* )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:5: ( 'new' typeName | '(' expression ')' | ( '++' | '--' ) expression | ( '+' | '-' ) expression | ( 'after' | 'delete' ) expression | '!' expression | '~' expression | primaryExpression ) ( ( '++' | '--' ) | '[' expression ']' | '(' functionCallArguments ')' | '.' identifier | '**' expression | ( '*' | '/' | '%' ) expression | ( '+' | '-' ) expression | ( '<<' | '>>' ) expression | '&' expression | '^' expression | '|' expression | ( '<' | '>' | '<=' | '>=' ) expression | ( '==' | '!=' ) expression | '&&' expression | '||' expression | '?' expression ':' expression | ( '=' | '|=' | '^=' | '&=' | '<<=' | '>>=' | '+=' | '-=' | '*=' | '/=' | '%=' ) expression )*
                pass 
                root_0 = self._adaptor.nil()

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:5: ( 'new' typeName | '(' expression ')' | ( '++' | '--' ) expression | ( '+' | '-' ) expression | ( 'after' | 'delete' ) expression | '!' expression | '~' expression | primaryExpression )
                alt69 = 8
                alt69 = self.dfa69.predict(self.input)
                if alt69 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:6: 'new' typeName
                    pass 
                    string_literal261=self.match(self.input, 101, self.FOLLOW_101_in_expression1975)
                    if self._state.backtracking == 0:

                        string_literal261_tree = self._adaptor.createWithPayload(string_literal261)
                        self._adaptor.addChild(root_0, string_literal261_tree)

                    self._state.following.append(self.FOLLOW_typeName_in_expression1977)
                    typeName262 = self.typeName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeName262.tree)


                elif alt69 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:23: '(' expression ')'
                    pass 
                    char_literal263=self.match(self.input, 69, self.FOLLOW_69_in_expression1981)
                    if self._state.backtracking == 0:

                        char_literal263_tree = self._adaptor.createWithPayload(char_literal263)
                        self._adaptor.addChild(root_0, char_literal263_tree)

                    self._state.following.append(self.FOLLOW_expression_in_expression1983)
                    expression264 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression264.tree)
                    char_literal265=self.match(self.input, 70, self.FOLLOW_70_in_expression1985)
                    if self._state.backtracking == 0:

                        char_literal265_tree = self._adaptor.createWithPayload(char_literal265)
                        self._adaptor.addChild(root_0, char_literal265_tree)



                elif alt69 == 3:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:44: ( '++' | '--' ) expression
                    pass 
                    set266 = self.input.LT(1)
                    if (102 <= self.input.LA(1) <= 103):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set266))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    self._state.following.append(self.FOLLOW_expression_in_expression1997)
                    expression267 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression267.tree)


                elif alt69 == 4:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:71: ( '+' | '-' ) expression
                    pass 
                    set268 = self.input.LT(1)
                    if (104 <= self.input.LA(1) <= 105):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set268))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    self._state.following.append(self.FOLLOW_expression_in_expression2009)
                    expression269 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression269.tree)


                elif alt69 == 5:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:96: ( 'after' | 'delete' ) expression
                    pass 
                    set270 = self.input.LT(1)
                    if (106 <= self.input.LA(1) <= 107):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set270))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    self._state.following.append(self.FOLLOW_expression_in_expression2021)
                    expression271 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression271.tree)


                elif alt69 == 6:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:130: '!' expression
                    pass 
                    char_literal272=self.match(self.input, 108, self.FOLLOW_108_in_expression2025)
                    if self._state.backtracking == 0:

                        char_literal272_tree = self._adaptor.createWithPayload(char_literal272)
                        self._adaptor.addChild(root_0, char_literal272_tree)

                    self._state.following.append(self.FOLLOW_expression_in_expression2027)
                    expression273 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression273.tree)


                elif alt69 == 7:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:147: '~' expression
                    pass 
                    char_literal274=self.match(self.input, 52, self.FOLLOW_52_in_expression2031)
                    if self._state.backtracking == 0:

                        char_literal274_tree = self._adaptor.createWithPayload(char_literal274)
                        self._adaptor.addChild(root_0, char_literal274_tree)

                    self._state.following.append(self.FOLLOW_expression_in_expression2033)
                    expression275 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression275.tree)


                elif alt69 == 8:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:164: primaryExpression
                    pass 
                    self._state.following.append(self.FOLLOW_primaryExpression_in_expression2037)
                    primaryExpression276 = self.primaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, primaryExpression276.tree)



                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:183: ( ( '++' | '--' ) | '[' expression ']' | '(' functionCallArguments ')' | '.' identifier | '**' expression | ( '*' | '/' | '%' ) expression | ( '+' | '-' ) expression | ( '<<' | '>>' ) expression | '&' expression | '^' expression | '|' expression | ( '<' | '>' | '<=' | '>=' ) expression | ( '==' | '!=' ) expression | '&&' expression | '||' expression | '?' expression ':' expression | ( '=' | '|=' | '^=' | '&=' | '<<=' | '>>=' | '+=' | '-=' | '*=' | '/=' | '%=' ) expression )*
                while True: #loop70
                    alt70 = 18
                    alt70 = self.dfa70.predict(self.input)
                    if alt70 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:184: ( '++' | '--' )
                        pass 
                        set277 = self.input.LT(1)
                        if (102 <= self.input.LA(1) <= 103):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set277))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    elif alt70 == 2:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:200: '[' expression ']'
                        pass 
                        char_literal278=self.match(self.input, 81, self.FOLLOW_81_in_expression2051)
                        if self._state.backtracking == 0:

                            char_literal278_tree = self._adaptor.createWithPayload(char_literal278)
                            self._adaptor.addChild(root_0, char_literal278_tree)

                        self._state.following.append(self.FOLLOW_expression_in_expression2053)
                        expression279 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression279.tree)
                        char_literal280=self.match(self.input, 82, self.FOLLOW_82_in_expression2055)
                        if self._state.backtracking == 0:

                            char_literal280_tree = self._adaptor.createWithPayload(char_literal280)
                            self._adaptor.addChild(root_0, char_literal280_tree)



                    elif alt70 == 3:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:221: '(' functionCallArguments ')'
                        pass 
                        char_literal281=self.match(self.input, 69, self.FOLLOW_69_in_expression2059)
                        if self._state.backtracking == 0:

                            char_literal281_tree = self._adaptor.createWithPayload(char_literal281)
                            self._adaptor.addChild(root_0, char_literal281_tree)

                        self._state.following.append(self.FOLLOW_functionCallArguments_in_expression2061)
                        functionCallArguments282 = self.functionCallArguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, functionCallArguments282.tree)
                        char_literal283=self.match(self.input, 70, self.FOLLOW_70_in_expression2063)
                        if self._state.backtracking == 0:

                            char_literal283_tree = self._adaptor.createWithPayload(char_literal283)
                            self._adaptor.addChild(root_0, char_literal283_tree)



                    elif alt70 == 4:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:253: '.' identifier
                        pass 
                        char_literal284=self.match(self.input, 83, self.FOLLOW_83_in_expression2067)
                        if self._state.backtracking == 0:

                            char_literal284_tree = self._adaptor.createWithPayload(char_literal284)
                            self._adaptor.addChild(root_0, char_literal284_tree)

                        self._state.following.append(self.FOLLOW_identifier_in_expression2069)
                        identifier285 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier285.tree)


                    elif alt70 == 5:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:270: '**' expression
                        pass 
                        string_literal286=self.match(self.input, 109, self.FOLLOW_109_in_expression2073)
                        if self._state.backtracking == 0:

                            string_literal286_tree = self._adaptor.createWithPayload(string_literal286)
                            self._adaptor.addChild(root_0, string_literal286_tree)

                        self._state.following.append(self.FOLLOW_expression_in_expression2075)
                        expression287 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression287.tree)


                    elif alt70 == 6:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:288: ( '*' | '/' | '%' ) expression
                        pass 
                        set288 = self.input.LT(1)
                        if self.input.LA(1) == 60 or (110 <= self.input.LA(1) <= 111):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set288))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_expression_in_expression2091)
                        expression289 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression289.tree)


                    elif alt70 == 7:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:319: ( '+' | '-' ) expression
                        pass 
                        set290 = self.input.LT(1)
                        if (104 <= self.input.LA(1) <= 105):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set290))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_expression_in_expression2103)
                        expression291 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression291.tree)


                    elif alt70 == 8:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:344: ( '<<' | '>>' ) expression
                        pass 
                        set292 = self.input.LT(1)
                        if (112 <= self.input.LA(1) <= 113):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set292))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_expression_in_expression2115)
                        expression293 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression293.tree)


                    elif alt70 == 9:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:371: '&' expression
                        pass 
                        char_literal294=self.match(self.input, 114, self.FOLLOW_114_in_expression2119)
                        if self._state.backtracking == 0:

                            char_literal294_tree = self._adaptor.createWithPayload(char_literal294)
                            self._adaptor.addChild(root_0, char_literal294_tree)

                        self._state.following.append(self.FOLLOW_expression_in_expression2121)
                        expression295 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression295.tree)


                    elif alt70 == 10:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:388: '^' expression
                        pass 
                        char_literal296=self.match(self.input, 51, self.FOLLOW_51_in_expression2125)
                        if self._state.backtracking == 0:

                            char_literal296_tree = self._adaptor.createWithPayload(char_literal296)
                            self._adaptor.addChild(root_0, char_literal296_tree)

                        self._state.following.append(self.FOLLOW_expression_in_expression2127)
                        expression297 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression297.tree)


                    elif alt70 == 11:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:405: '|' expression
                        pass 
                        char_literal298=self.match(self.input, 115, self.FOLLOW_115_in_expression2131)
                        if self._state.backtracking == 0:

                            char_literal298_tree = self._adaptor.createWithPayload(char_literal298)
                            self._adaptor.addChild(root_0, char_literal298_tree)

                        self._state.following.append(self.FOLLOW_expression_in_expression2133)
                        expression299 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression299.tree)


                    elif alt70 == 12:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:422: ( '<' | '>' | '<=' | '>=' ) expression
                        pass 
                        set300 = self.input.LT(1)
                        if (53 <= self.input.LA(1) <= 56):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set300))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_expression_in_expression2153)
                        expression301 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression301.tree)


                    elif alt70 == 13:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:461: ( '==' | '!=' ) expression
                        pass 
                        set302 = self.input.LT(1)
                        if (116 <= self.input.LA(1) <= 117):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set302))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_expression_in_expression2165)
                        expression303 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression303.tree)


                    elif alt70 == 14:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:488: '&&' expression
                        pass 
                        string_literal304=self.match(self.input, 118, self.FOLLOW_118_in_expression2169)
                        if self._state.backtracking == 0:

                            string_literal304_tree = self._adaptor.createWithPayload(string_literal304)
                            self._adaptor.addChild(root_0, string_literal304_tree)

                        self._state.following.append(self.FOLLOW_expression_in_expression2171)
                        expression305 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression305.tree)


                    elif alt70 == 15:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:506: '||' expression
                        pass 
                        string_literal306=self.match(self.input, 119, self.FOLLOW_119_in_expression2175)
                        if self._state.backtracking == 0:

                            string_literal306_tree = self._adaptor.createWithPayload(string_literal306)
                            self._adaptor.addChild(root_0, string_literal306_tree)

                        self._state.following.append(self.FOLLOW_expression_in_expression2177)
                        expression307 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression307.tree)


                    elif alt70 == 16:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:524: '?' expression ':' expression
                        pass 
                        char_literal308=self.match(self.input, 120, self.FOLLOW_120_in_expression2181)
                        if self._state.backtracking == 0:

                            char_literal308_tree = self._adaptor.createWithPayload(char_literal308)
                            self._adaptor.addChild(root_0, char_literal308_tree)

                        self._state.following.append(self.FOLLOW_expression_in_expression2183)
                        expression309 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression309.tree)
                        char_literal310=self.match(self.input, 121, self.FOLLOW_121_in_expression2185)
                        if self._state.backtracking == 0:

                            char_literal310_tree = self._adaptor.createWithPayload(char_literal310)
                            self._adaptor.addChild(root_0, char_literal310_tree)

                        self._state.following.append(self.FOLLOW_expression_in_expression2187)
                        expression311 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression311.tree)


                    elif alt70 == 17:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:556: ( '=' | '|=' | '^=' | '&=' | '<<=' | '>>=' | '+=' | '-=' | '*=' | '/=' | '%=' ) expression
                        pass 
                        set312 = self.input.LT(1)
                        if self.input.LA(1) == 57 or (122 <= self.input.LA(1) <= 131):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set312))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_expression_in_expression2235)
                        expression313 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression313.tree)


                    else:
                        break #loop70



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 56, expression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "expression"

    class primaryExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.primaryExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "primaryExpression"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:229:1: primaryExpression : ( BooleanLiteral | numberLiteral | HexLiteral | StringLiteral | identifier ( '[' ']' )? | tupleExpression | elementaryTypeNameExpression ( '[' ']' )? );
    def primaryExpression(self, ):

        retval = self.primaryExpression_return()
        retval.start = self.input.LT(1)
        primaryExpression_StartIndex = self.input.index()
        root_0 = None

        BooleanLiteral314 = None
        HexLiteral316 = None
        StringLiteral317 = None
        char_literal319 = None
        char_literal320 = None
        char_literal323 = None
        char_literal324 = None
        numberLiteral315 = None

        identifier318 = None

        tupleExpression321 = None

        elementaryTypeNameExpression322 = None


        BooleanLiteral314_tree = None
        HexLiteral316_tree = None
        StringLiteral317_tree = None
        char_literal319_tree = None
        char_literal320_tree = None
        char_literal323_tree = None
        char_literal324_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:230:3: ( BooleanLiteral | numberLiteral | HexLiteral | StringLiteral | identifier ( '[' ']' )? | tupleExpression | elementaryTypeNameExpression ( '[' ']' )? )
                alt73 = 7
                LA73 = self.input.LA(1)
                if LA73 == BooleanLiteral:
                    alt73 = 1
                elif LA73 == DecimalNumber or LA73 == HexNumber:
                    alt73 = 2
                elif LA73 == HexLiteral:
                    alt73 = 3
                elif LA73 == StringLiteral:
                    alt73 = 4
                elif LA73 == Identifier or LA73 == 61 or LA73 == 88:
                    alt73 = 5
                elif LA73 == 69 or LA73 == 81:
                    alt73 = 6
                elif LA73 == Int or LA73 == Uint or LA73 == Byte or LA73 == Fixed or LA73 == Ufixed or LA73 == 80 or LA73 == 97 or LA73 == 98 or LA73 == 99 or LA73 == 100:
                    alt73 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 73, 0, self.input)

                    raise nvae

                if alt73 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:230:5: BooleanLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    BooleanLiteral314=self.match(self.input, BooleanLiteral, self.FOLLOW_BooleanLiteral_in_primaryExpression2248)
                    if self._state.backtracking == 0:

                        BooleanLiteral314_tree = self._adaptor.createWithPayload(BooleanLiteral314)
                        self._adaptor.addChild(root_0, BooleanLiteral314_tree)



                elif alt73 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:231:5: numberLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_numberLiteral_in_primaryExpression2254)
                    numberLiteral315 = self.numberLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, numberLiteral315.tree)


                elif alt73 == 3:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:232:5: HexLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    HexLiteral316=self.match(self.input, HexLiteral, self.FOLLOW_HexLiteral_in_primaryExpression2260)
                    if self._state.backtracking == 0:

                        HexLiteral316_tree = self._adaptor.createWithPayload(HexLiteral316)
                        self._adaptor.addChild(root_0, HexLiteral316_tree)



                elif alt73 == 4:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:233:5: StringLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    StringLiteral317=self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_primaryExpression2266)
                    if self._state.backtracking == 0:

                        StringLiteral317_tree = self._adaptor.createWithPayload(StringLiteral317)
                        self._adaptor.addChild(root_0, StringLiteral317_tree)



                elif alt73 == 5:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:234:5: identifier ( '[' ']' )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_primaryExpression2272)
                    identifier318 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier318.tree)
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:234:16: ( '[' ']' )?
                    alt71 = 2
                    alt71 = self.dfa71.predict(self.input)
                    if alt71 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:234:17: '[' ']'
                        pass 
                        char_literal319=self.match(self.input, 81, self.FOLLOW_81_in_primaryExpression2275)
                        if self._state.backtracking == 0:

                            char_literal319_tree = self._adaptor.createWithPayload(char_literal319)
                            self._adaptor.addChild(root_0, char_literal319_tree)

                        char_literal320=self.match(self.input, 82, self.FOLLOW_82_in_primaryExpression2277)
                        if self._state.backtracking == 0:

                            char_literal320_tree = self._adaptor.createWithPayload(char_literal320)
                            self._adaptor.addChild(root_0, char_literal320_tree)






                elif alt73 == 6:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:235:5: tupleExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_tupleExpression_in_primaryExpression2285)
                    tupleExpression321 = self.tupleExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tupleExpression321.tree)


                elif alt73 == 7:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:236:5: elementaryTypeNameExpression ( '[' ']' )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementaryTypeNameExpression_in_primaryExpression2291)
                    elementaryTypeNameExpression322 = self.elementaryTypeNameExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementaryTypeNameExpression322.tree)
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:236:34: ( '[' ']' )?
                    alt72 = 2
                    alt72 = self.dfa72.predict(self.input)
                    if alt72 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:236:35: '[' ']'
                        pass 
                        char_literal323=self.match(self.input, 81, self.FOLLOW_81_in_primaryExpression2294)
                        if self._state.backtracking == 0:

                            char_literal323_tree = self._adaptor.createWithPayload(char_literal323)
                            self._adaptor.addChild(root_0, char_literal323_tree)

                        char_literal324=self.match(self.input, 82, self.FOLLOW_82_in_primaryExpression2296)
                        if self._state.backtracking == 0:

                            char_literal324_tree = self._adaptor.createWithPayload(char_literal324)
                            self._adaptor.addChild(root_0, char_literal324_tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 57, primaryExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "primaryExpression"

    class expressionList_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.expressionList_return, self).__init__()

            self.tree = None




    # $ANTLR start "expressionList"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:238:1: expressionList : expression ( ',' expression )* ;
    def expressionList(self, ):

        retval = self.expressionList_return()
        retval.start = self.input.LT(1)
        expressionList_StartIndex = self.input.index()
        root_0 = None

        char_literal326 = None
        expression325 = None

        expression327 = None


        char_literal326_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:239:3: ( expression ( ',' expression )* )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:239:5: expression ( ',' expression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expression_in_expressionList2309)
                expression325 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression325.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:239:16: ( ',' expression )*
                while True: #loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == 63) :
                        alt74 = 1


                    if alt74 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:239:17: ',' expression
                        pass 
                        char_literal326=self.match(self.input, 63, self.FOLLOW_63_in_expressionList2312)
                        if self._state.backtracking == 0:

                            char_literal326_tree = self._adaptor.createWithPayload(char_literal326)
                            self._adaptor.addChild(root_0, char_literal326_tree)

                        self._state.following.append(self.FOLLOW_expression_in_expressionList2314)
                        expression327 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression327.tree)


                    else:
                        break #loop74



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 58, expressionList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "expressionList"

    class nameValueList_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.nameValueList_return, self).__init__()

            self.tree = None




    # $ANTLR start "nameValueList"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:241:1: nameValueList : nameValue ( ',' nameValue )* ( ',' )? ;
    def nameValueList(self, ):

        retval = self.nameValueList_return()
        retval.start = self.input.LT(1)
        nameValueList_StartIndex = self.input.index()
        root_0 = None

        char_literal329 = None
        char_literal331 = None
        nameValue328 = None

        nameValue330 = None


        char_literal329_tree = None
        char_literal331_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:242:3: ( nameValue ( ',' nameValue )* ( ',' )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:242:5: nameValue ( ',' nameValue )* ( ',' )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_nameValue_in_nameValueList2327)
                nameValue328 = self.nameValue()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, nameValue328.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:242:15: ( ',' nameValue )*
                while True: #loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == 63) :
                        LA75_1 = self.input.LA(2)

                        if (LA75_1 == Identifier or LA75_1 == 61 or LA75_1 == 88) :
                            alt75 = 1




                    if alt75 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:242:16: ',' nameValue
                        pass 
                        char_literal329=self.match(self.input, 63, self.FOLLOW_63_in_nameValueList2330)
                        if self._state.backtracking == 0:

                            char_literal329_tree = self._adaptor.createWithPayload(char_literal329)
                            self._adaptor.addChild(root_0, char_literal329_tree)

                        self._state.following.append(self.FOLLOW_nameValue_in_nameValueList2332)
                        nameValue330 = self.nameValue()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, nameValue330.tree)


                    else:
                        break #loop75
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:242:32: ( ',' )?
                alt76 = 2
                LA76_0 = self.input.LA(1)

                if (LA76_0 == 63) :
                    alt76 = 1
                if alt76 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: ','
                    pass 
                    char_literal331=self.match(self.input, 63, self.FOLLOW_63_in_nameValueList2336)
                    if self._state.backtracking == 0:

                        char_literal331_tree = self._adaptor.createWithPayload(char_literal331)
                        self._adaptor.addChild(root_0, char_literal331_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 59, nameValueList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "nameValueList"

    class nameValue_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.nameValue_return, self).__init__()

            self.tree = None




    # $ANTLR start "nameValue"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:244:1: nameValue : identifier ':' expression ;
    def nameValue(self, ):

        retval = self.nameValue_return()
        retval.start = self.input.LT(1)
        nameValue_StartIndex = self.input.index()
        root_0 = None

        char_literal333 = None
        identifier332 = None

        expression334 = None


        char_literal333_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:245:3: ( identifier ':' expression )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:245:5: identifier ':' expression
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_nameValue2348)
                identifier332 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier332.tree)
                char_literal333=self.match(self.input, 121, self.FOLLOW_121_in_nameValue2350)
                if self._state.backtracking == 0:

                    char_literal333_tree = self._adaptor.createWithPayload(char_literal333)
                    self._adaptor.addChild(root_0, char_literal333_tree)

                self._state.following.append(self.FOLLOW_expression_in_nameValue2352)
                expression334 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression334.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 60, nameValue_StartIndex, success)

            pass
        return retval

    # $ANTLR end "nameValue"

    class functionCallArguments_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.functionCallArguments_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionCallArguments"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:247:1: functionCallArguments : ( '{' ( nameValueList )? '}' | ( expressionList )? );
    def functionCallArguments(self, ):

        retval = self.functionCallArguments_return()
        retval.start = self.input.LT(1)
        functionCallArguments_StartIndex = self.input.index()
        root_0 = None

        char_literal335 = None
        char_literal337 = None
        nameValueList336 = None

        expressionList338 = None


        char_literal335_tree = None
        char_literal337_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:248:3: ( '{' ( nameValueList )? '}' | ( expressionList )? )
                alt79 = 2
                alt79 = self.dfa79.predict(self.input)
                if alt79 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:248:5: '{' ( nameValueList )? '}'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal335=self.match(self.input, 62, self.FOLLOW_62_in_functionCallArguments2363)
                    if self._state.backtracking == 0:

                        char_literal335_tree = self._adaptor.createWithPayload(char_literal335)
                        self._adaptor.addChild(root_0, char_literal335_tree)

                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:248:9: ( nameValueList )?
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if (LA77_0 == Identifier or LA77_0 == 61 or LA77_0 == 88) :
                        alt77 = 1
                    if alt77 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: nameValueList
                        pass 
                        self._state.following.append(self.FOLLOW_nameValueList_in_functionCallArguments2365)
                        nameValueList336 = self.nameValueList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, nameValueList336.tree)



                    char_literal337=self.match(self.input, 64, self.FOLLOW_64_in_functionCallArguments2368)
                    if self._state.backtracking == 0:

                        char_literal337_tree = self._adaptor.createWithPayload(char_literal337)
                        self._adaptor.addChild(root_0, char_literal337_tree)



                elif alt79 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:249:5: ( expressionList )?
                    pass 
                    root_0 = self._adaptor.nil()

                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:249:5: ( expressionList )?
                    alt78 = 2
                    alt78 = self.dfa78.predict(self.input)
                    if alt78 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: expressionList
                        pass 
                        self._state.following.append(self.FOLLOW_expressionList_in_functionCallArguments2374)
                        expressionList338 = self.expressionList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expressionList338.tree)





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 61, functionCallArguments_StartIndex, success)

            pass
        return retval

    # $ANTLR end "functionCallArguments"

    class functionCall_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.functionCall_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionCall"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:251:1: functionCall : expression '(' functionCallArguments ')' ;
    def functionCall(self, ):

        retval = self.functionCall_return()
        retval.start = self.input.LT(1)
        functionCall_StartIndex = self.input.index()
        root_0 = None

        char_literal340 = None
        char_literal342 = None
        expression339 = None

        functionCallArguments341 = None


        char_literal340_tree = None
        char_literal342_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:252:3: ( expression '(' functionCallArguments ')' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:252:5: expression '(' functionCallArguments ')'
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expression_in_functionCall2386)
                expression339 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression339.tree)
                char_literal340=self.match(self.input, 69, self.FOLLOW_69_in_functionCall2388)
                if self._state.backtracking == 0:

                    char_literal340_tree = self._adaptor.createWithPayload(char_literal340)
                    self._adaptor.addChild(root_0, char_literal340_tree)

                self._state.following.append(self.FOLLOW_functionCallArguments_in_functionCall2390)
                functionCallArguments341 = self.functionCallArguments()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, functionCallArguments341.tree)
                char_literal342=self.match(self.input, 70, self.FOLLOW_70_in_functionCall2392)
                if self._state.backtracking == 0:

                    char_literal342_tree = self._adaptor.createWithPayload(char_literal342)
                    self._adaptor.addChild(root_0, char_literal342_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 62, functionCall_StartIndex, success)

            pass
        return retval

    # $ANTLR end "functionCall"

    class assemblyBlock_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyBlock_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyBlock"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:254:1: assemblyBlock : '{' ( assemblyItem )* '}' ;
    def assemblyBlock(self, ):

        retval = self.assemblyBlock_return()
        retval.start = self.input.LT(1)
        assemblyBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal343 = None
        char_literal345 = None
        assemblyItem344 = None


        char_literal343_tree = None
        char_literal345_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:255:3: ( '{' ( assemblyItem )* '}' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:255:5: '{' ( assemblyItem )* '}'
                pass 
                root_0 = self._adaptor.nil()

                char_literal343=self.match(self.input, 62, self.FOLLOW_62_in_assemblyBlock2403)
                if self._state.backtracking == 0:

                    char_literal343_tree = self._adaptor.createWithPayload(char_literal343)
                    self._adaptor.addChild(root_0, char_literal343_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:255:9: ( assemblyItem )*
                while True: #loop80
                    alt80 = 2
                    alt80 = self.dfa80.predict(self.input)
                    if alt80 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: assemblyItem
                        pass 
                        self._state.following.append(self.FOLLOW_assemblyItem_in_assemblyBlock2405)
                        assemblyItem344 = self.assemblyItem()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, assemblyItem344.tree)


                    else:
                        break #loop80
                char_literal345=self.match(self.input, 64, self.FOLLOW_64_in_assemblyBlock2408)
                if self._state.backtracking == 0:

                    char_literal345_tree = self._adaptor.createWithPayload(char_literal345)
                    self._adaptor.addChild(root_0, char_literal345_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 63, assemblyBlock_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyBlock"

    class assemblyItem_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyItem_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyItem"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:257:1: assemblyItem : ( identifier | assemblyBlock | assemblyExpression | assemblyLocalDefinition | assemblyAssignment | assemblyStackAssignment | labelDefinition | assemblySwitch | assemblyFunctionDefinition | assemblyFor | assemblyIf | BreakKeyword | ContinueKeyword | subAssembly | numberLiteral | StringLiteral | HexLiteral );
    def assemblyItem(self, ):

        retval = self.assemblyItem_return()
        retval.start = self.input.LT(1)
        assemblyItem_StartIndex = self.input.index()
        root_0 = None

        BreakKeyword357 = None
        ContinueKeyword358 = None
        StringLiteral361 = None
        HexLiteral362 = None
        identifier346 = None

        assemblyBlock347 = None

        assemblyExpression348 = None

        assemblyLocalDefinition349 = None

        assemblyAssignment350 = None

        assemblyStackAssignment351 = None

        labelDefinition352 = None

        assemblySwitch353 = None

        assemblyFunctionDefinition354 = None

        assemblyFor355 = None

        assemblyIf356 = None

        subAssembly359 = None

        numberLiteral360 = None


        BreakKeyword357_tree = None
        ContinueKeyword358_tree = None
        StringLiteral361_tree = None
        HexLiteral362_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:258:3: ( identifier | assemblyBlock | assemblyExpression | assemblyLocalDefinition | assemblyAssignment | assemblyStackAssignment | labelDefinition | assemblySwitch | assemblyFunctionDefinition | assemblyFor | assemblyIf | BreakKeyword | ContinueKeyword | subAssembly | numberLiteral | StringLiteral | HexLiteral )
                alt81 = 17
                alt81 = self.dfa81.predict(self.input)
                if alt81 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:258:5: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_assemblyItem2419)
                    identifier346 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier346.tree)


                elif alt81 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:259:5: assemblyBlock
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblyBlock_in_assemblyItem2425)
                    assemblyBlock347 = self.assemblyBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyBlock347.tree)


                elif alt81 == 3:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:260:5: assemblyExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblyExpression_in_assemblyItem2431)
                    assemblyExpression348 = self.assemblyExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyExpression348.tree)


                elif alt81 == 4:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:261:5: assemblyLocalDefinition
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblyLocalDefinition_in_assemblyItem2437)
                    assemblyLocalDefinition349 = self.assemblyLocalDefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyLocalDefinition349.tree)


                elif alt81 == 5:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:262:5: assemblyAssignment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblyAssignment_in_assemblyItem2443)
                    assemblyAssignment350 = self.assemblyAssignment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyAssignment350.tree)


                elif alt81 == 6:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:263:5: assemblyStackAssignment
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblyStackAssignment_in_assemblyItem2449)
                    assemblyStackAssignment351 = self.assemblyStackAssignment()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyStackAssignment351.tree)


                elif alt81 == 7:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:264:5: labelDefinition
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_labelDefinition_in_assemblyItem2455)
                    labelDefinition352 = self.labelDefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, labelDefinition352.tree)


                elif alt81 == 8:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:265:5: assemblySwitch
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblySwitch_in_assemblyItem2461)
                    assemblySwitch353 = self.assemblySwitch()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblySwitch353.tree)


                elif alt81 == 9:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:266:5: assemblyFunctionDefinition
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblyFunctionDefinition_in_assemblyItem2467)
                    assemblyFunctionDefinition354 = self.assemblyFunctionDefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyFunctionDefinition354.tree)


                elif alt81 == 10:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:267:5: assemblyFor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblyFor_in_assemblyItem2473)
                    assemblyFor355 = self.assemblyFor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyFor355.tree)


                elif alt81 == 11:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:268:5: assemblyIf
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblyIf_in_assemblyItem2479)
                    assemblyIf356 = self.assemblyIf()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyIf356.tree)


                elif alt81 == 12:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:269:5: BreakKeyword
                    pass 
                    root_0 = self._adaptor.nil()

                    BreakKeyword357=self.match(self.input, BreakKeyword, self.FOLLOW_BreakKeyword_in_assemblyItem2485)
                    if self._state.backtracking == 0:

                        BreakKeyword357_tree = self._adaptor.createWithPayload(BreakKeyword357)
                        self._adaptor.addChild(root_0, BreakKeyword357_tree)



                elif alt81 == 13:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:270:5: ContinueKeyword
                    pass 
                    root_0 = self._adaptor.nil()

                    ContinueKeyword358=self.match(self.input, ContinueKeyword, self.FOLLOW_ContinueKeyword_in_assemblyItem2491)
                    if self._state.backtracking == 0:

                        ContinueKeyword358_tree = self._adaptor.createWithPayload(ContinueKeyword358)
                        self._adaptor.addChild(root_0, ContinueKeyword358_tree)



                elif alt81 == 14:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:271:5: subAssembly
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_subAssembly_in_assemblyItem2497)
                    subAssembly359 = self.subAssembly()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, subAssembly359.tree)


                elif alt81 == 15:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:272:5: numberLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_numberLiteral_in_assemblyItem2503)
                    numberLiteral360 = self.numberLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, numberLiteral360.tree)


                elif alt81 == 16:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:273:5: StringLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    StringLiteral361=self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_assemblyItem2509)
                    if self._state.backtracking == 0:

                        StringLiteral361_tree = self._adaptor.createWithPayload(StringLiteral361)
                        self._adaptor.addChild(root_0, StringLiteral361_tree)



                elif alt81 == 17:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:274:5: HexLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    HexLiteral362=self.match(self.input, HexLiteral, self.FOLLOW_HexLiteral_in_assemblyItem2515)
                    if self._state.backtracking == 0:

                        HexLiteral362_tree = self._adaptor.createWithPayload(HexLiteral362)
                        self._adaptor.addChild(root_0, HexLiteral362_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 64, assemblyItem_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyItem"

    class assemblyExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyExpression"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:276:1: assemblyExpression : ( assemblyCall | assemblyLiteral );
    def assemblyExpression(self, ):

        retval = self.assemblyExpression_return()
        retval.start = self.input.LT(1)
        assemblyExpression_StartIndex = self.input.index()
        root_0 = None

        assemblyCall363 = None

        assemblyLiteral364 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:277:3: ( assemblyCall | assemblyLiteral )
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if (LA82_0 == Identifier or LA82_0 == 61 or LA82_0 == 80 or LA82_0 == 88 or LA82_0 == 94 or LA82_0 == 100) :
                    alt82 = 1
                elif (LA82_0 == StringLiteral or LA82_0 == HexLiteral or (DecimalNumber <= LA82_0 <= HexNumber)) :
                    alt82 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 82, 0, self.input)

                    raise nvae

                if alt82 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:277:5: assemblyCall
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblyCall_in_assemblyExpression2526)
                    assemblyCall363 = self.assemblyCall()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyCall363.tree)


                elif alt82 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:277:20: assemblyLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assemblyLiteral_in_assemblyExpression2530)
                    assemblyLiteral364 = self.assemblyLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyLiteral364.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 65, assemblyExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyExpression"

    class assemblyCall_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyCall_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyCall"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:279:1: assemblyCall : ( 'return' | 'address' | 'byte' | identifier ) ( '(' ( assemblyExpression )? ( ',' assemblyExpression )* ')' )? ;
    def assemblyCall(self, ):

        retval = self.assemblyCall_return()
        retval.start = self.input.LT(1)
        assemblyCall_StartIndex = self.input.index()
        root_0 = None

        string_literal365 = None
        string_literal366 = None
        string_literal367 = None
        char_literal369 = None
        char_literal371 = None
        char_literal373 = None
        identifier368 = None

        assemblyExpression370 = None

        assemblyExpression372 = None


        string_literal365_tree = None
        string_literal366_tree = None
        string_literal367_tree = None
        char_literal369_tree = None
        char_literal371_tree = None
        char_literal373_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:3: ( ( 'return' | 'address' | 'byte' | identifier ) ( '(' ( assemblyExpression )? ( ',' assemblyExpression )* ')' )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:5: ( 'return' | 'address' | 'byte' | identifier ) ( '(' ( assemblyExpression )? ( ',' assemblyExpression )* ')' )?
                pass 
                root_0 = self._adaptor.nil()

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:5: ( 'return' | 'address' | 'byte' | identifier )
                alt83 = 4
                LA83 = self.input.LA(1)
                if LA83 == 94:
                    alt83 = 1
                elif LA83 == 80:
                    alt83 = 2
                elif LA83 == 100:
                    alt83 = 3
                elif LA83 == Identifier or LA83 == 61 or LA83 == 88:
                    alt83 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 83, 0, self.input)

                    raise nvae

                if alt83 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:7: 'return'
                    pass 
                    string_literal365=self.match(self.input, 94, self.FOLLOW_94_in_assemblyCall2543)
                    if self._state.backtracking == 0:

                        string_literal365_tree = self._adaptor.createWithPayload(string_literal365)
                        self._adaptor.addChild(root_0, string_literal365_tree)



                elif alt83 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:18: 'address'
                    pass 
                    string_literal366=self.match(self.input, 80, self.FOLLOW_80_in_assemblyCall2547)
                    if self._state.backtracking == 0:

                        string_literal366_tree = self._adaptor.createWithPayload(string_literal366)
                        self._adaptor.addChild(root_0, string_literal366_tree)



                elif alt83 == 3:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:30: 'byte'
                    pass 
                    string_literal367=self.match(self.input, 100, self.FOLLOW_100_in_assemblyCall2551)
                    if self._state.backtracking == 0:

                        string_literal367_tree = self._adaptor.createWithPayload(string_literal367)
                        self._adaptor.addChild(root_0, string_literal367_tree)



                elif alt83 == 4:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:39: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_assemblyCall2555)
                    identifier368 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier368.tree)



                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:52: ( '(' ( assemblyExpression )? ( ',' assemblyExpression )* ')' )?
                alt86 = 2
                alt86 = self.dfa86.predict(self.input)
                if alt86 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:54: '(' ( assemblyExpression )? ( ',' assemblyExpression )* ')'
                    pass 
                    char_literal369=self.match(self.input, 69, self.FOLLOW_69_in_assemblyCall2561)
                    if self._state.backtracking == 0:

                        char_literal369_tree = self._adaptor.createWithPayload(char_literal369)
                        self._adaptor.addChild(root_0, char_literal369_tree)

                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:58: ( assemblyExpression )?
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == StringLiteral or LA84_0 == HexLiteral or (DecimalNumber <= LA84_0 <= HexNumber) or LA84_0 == Identifier or LA84_0 == 61 or LA84_0 == 80 or LA84_0 == 88 or LA84_0 == 94 or LA84_0 == 100) :
                        alt84 = 1
                    if alt84 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: assemblyExpression
                        pass 
                        self._state.following.append(self.FOLLOW_assemblyExpression_in_assemblyCall2563)
                        assemblyExpression370 = self.assemblyExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, assemblyExpression370.tree)



                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:78: ( ',' assemblyExpression )*
                    while True: #loop85
                        alt85 = 2
                        LA85_0 = self.input.LA(1)

                        if (LA85_0 == 63) :
                            alt85 = 1


                        if alt85 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:80: ',' assemblyExpression
                            pass 
                            char_literal371=self.match(self.input, 63, self.FOLLOW_63_in_assemblyCall2568)
                            if self._state.backtracking == 0:

                                char_literal371_tree = self._adaptor.createWithPayload(char_literal371)
                                self._adaptor.addChild(root_0, char_literal371_tree)

                            self._state.following.append(self.FOLLOW_assemblyExpression_in_assemblyCall2570)
                            assemblyExpression372 = self.assemblyExpression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, assemblyExpression372.tree)


                        else:
                            break #loop85
                    char_literal373=self.match(self.input, 70, self.FOLLOW_70_in_assemblyCall2575)
                    if self._state.backtracking == 0:

                        char_literal373_tree = self._adaptor.createWithPayload(char_literal373)
                        self._adaptor.addChild(root_0, char_literal373_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 66, assemblyCall_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyCall"

    class assemblyLocalDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyLocalDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyLocalDefinition"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:282:1: assemblyLocalDefinition : 'let' assemblyIdentifierOrList ( ':=' assemblyExpression )? ;
    def assemblyLocalDefinition(self, ):

        retval = self.assemblyLocalDefinition_return()
        retval.start = self.input.LT(1)
        assemblyLocalDefinition_StartIndex = self.input.index()
        root_0 = None

        string_literal374 = None
        string_literal376 = None
        assemblyIdentifierOrList375 = None

        assemblyExpression377 = None


        string_literal374_tree = None
        string_literal376_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:283:3: ( 'let' assemblyIdentifierOrList ( ':=' assemblyExpression )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:283:5: 'let' assemblyIdentifierOrList ( ':=' assemblyExpression )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal374=self.match(self.input, 132, self.FOLLOW_132_in_assemblyLocalDefinition2589)
                if self._state.backtracking == 0:

                    string_literal374_tree = self._adaptor.createWithPayload(string_literal374)
                    self._adaptor.addChild(root_0, string_literal374_tree)

                self._state.following.append(self.FOLLOW_assemblyIdentifierOrList_in_assemblyLocalDefinition2591)
                assemblyIdentifierOrList375 = self.assemblyIdentifierOrList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyIdentifierOrList375.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:283:36: ( ':=' assemblyExpression )?
                alt87 = 2
                alt87 = self.dfa87.predict(self.input)
                if alt87 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:283:38: ':=' assemblyExpression
                    pass 
                    string_literal376=self.match(self.input, 133, self.FOLLOW_133_in_assemblyLocalDefinition2595)
                    if self._state.backtracking == 0:

                        string_literal376_tree = self._adaptor.createWithPayload(string_literal376)
                        self._adaptor.addChild(root_0, string_literal376_tree)

                    self._state.following.append(self.FOLLOW_assemblyExpression_in_assemblyLocalDefinition2597)
                    assemblyExpression377 = self.assemblyExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyExpression377.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 67, assemblyLocalDefinition_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyLocalDefinition"

    class assemblyAssignment_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyAssignment_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyAssignment"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:285:1: assemblyAssignment : assemblyIdentifierOrList ':=' assemblyExpression ;
    def assemblyAssignment(self, ):

        retval = self.assemblyAssignment_return()
        retval.start = self.input.LT(1)
        assemblyAssignment_StartIndex = self.input.index()
        root_0 = None

        string_literal379 = None
        assemblyIdentifierOrList378 = None

        assemblyExpression380 = None


        string_literal379_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:286:3: ( assemblyIdentifierOrList ':=' assemblyExpression )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:286:5: assemblyIdentifierOrList ':=' assemblyExpression
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_assemblyIdentifierOrList_in_assemblyAssignment2611)
                assemblyIdentifierOrList378 = self.assemblyIdentifierOrList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyIdentifierOrList378.tree)
                string_literal379=self.match(self.input, 133, self.FOLLOW_133_in_assemblyAssignment2613)
                if self._state.backtracking == 0:

                    string_literal379_tree = self._adaptor.createWithPayload(string_literal379)
                    self._adaptor.addChild(root_0, string_literal379_tree)

                self._state.following.append(self.FOLLOW_assemblyExpression_in_assemblyAssignment2615)
                assemblyExpression380 = self.assemblyExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyExpression380.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 68, assemblyAssignment_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyAssignment"

    class assemblyIdentifierOrList_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyIdentifierOrList_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyIdentifierOrList"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:288:1: assemblyIdentifierOrList : ( identifier | '(' assemblyIdentifierList ')' );
    def assemblyIdentifierOrList(self, ):

        retval = self.assemblyIdentifierOrList_return()
        retval.start = self.input.LT(1)
        assemblyIdentifierOrList_StartIndex = self.input.index()
        root_0 = None

        char_literal382 = None
        char_literal384 = None
        identifier381 = None

        assemblyIdentifierList383 = None


        char_literal382_tree = None
        char_literal384_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 69):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:289:3: ( identifier | '(' assemblyIdentifierList ')' )
                alt88 = 2
                LA88_0 = self.input.LA(1)

                if (LA88_0 == Identifier or LA88_0 == 61 or LA88_0 == 88) :
                    alt88 = 1
                elif (LA88_0 == 69) :
                    alt88 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 88, 0, self.input)

                    raise nvae

                if alt88 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:289:5: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_assemblyIdentifierOrList2626)
                    identifier381 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier381.tree)


                elif alt88 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:289:18: '(' assemblyIdentifierList ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal382=self.match(self.input, 69, self.FOLLOW_69_in_assemblyIdentifierOrList2630)
                    if self._state.backtracking == 0:

                        char_literal382_tree = self._adaptor.createWithPayload(char_literal382)
                        self._adaptor.addChild(root_0, char_literal382_tree)

                    self._state.following.append(self.FOLLOW_assemblyIdentifierList_in_assemblyIdentifierOrList2632)
                    assemblyIdentifierList383 = self.assemblyIdentifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyIdentifierList383.tree)
                    char_literal384=self.match(self.input, 70, self.FOLLOW_70_in_assemblyIdentifierOrList2634)
                    if self._state.backtracking == 0:

                        char_literal384_tree = self._adaptor.createWithPayload(char_literal384)
                        self._adaptor.addChild(root_0, char_literal384_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 69, assemblyIdentifierOrList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyIdentifierOrList"

    class assemblyIdentifierList_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyIdentifierList_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyIdentifierList"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:291:1: assemblyIdentifierList : identifier ( ',' identifier )* ;
    def assemblyIdentifierList(self, ):

        retval = self.assemblyIdentifierList_return()
        retval.start = self.input.LT(1)
        assemblyIdentifierList_StartIndex = self.input.index()
        root_0 = None

        char_literal386 = None
        identifier385 = None

        identifier387 = None


        char_literal386_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 70):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:292:3: ( identifier ( ',' identifier )* )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:292:5: identifier ( ',' identifier )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_assemblyIdentifierList2645)
                identifier385 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier385.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:292:16: ( ',' identifier )*
                while True: #loop89
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == 63) :
                        alt89 = 1


                    if alt89 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:292:18: ',' identifier
                        pass 
                        char_literal386=self.match(self.input, 63, self.FOLLOW_63_in_assemblyIdentifierList2649)
                        if self._state.backtracking == 0:

                            char_literal386_tree = self._adaptor.createWithPayload(char_literal386)
                            self._adaptor.addChild(root_0, char_literal386_tree)

                        self._state.following.append(self.FOLLOW_identifier_in_assemblyIdentifierList2651)
                        identifier387 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier387.tree)


                    else:
                        break #loop89



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 70, assemblyIdentifierList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyIdentifierList"

    class assemblyStackAssignment_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyStackAssignment_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyStackAssignment"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:294:1: assemblyStackAssignment : '=:' identifier ;
    def assemblyStackAssignment(self, ):

        retval = self.assemblyStackAssignment_return()
        retval.start = self.input.LT(1)
        assemblyStackAssignment_StartIndex = self.input.index()
        root_0 = None

        string_literal388 = None
        identifier389 = None


        string_literal388_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 71):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:295:3: ( '=:' identifier )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:295:5: '=:' identifier
                pass 
                root_0 = self._adaptor.nil()

                string_literal388=self.match(self.input, 134, self.FOLLOW_134_in_assemblyStackAssignment2665)
                if self._state.backtracking == 0:

                    string_literal388_tree = self._adaptor.createWithPayload(string_literal388)
                    self._adaptor.addChild(root_0, string_literal388_tree)

                self._state.following.append(self.FOLLOW_identifier_in_assemblyStackAssignment2667)
                identifier389 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier389.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 71, assemblyStackAssignment_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyStackAssignment"

    class labelDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.labelDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "labelDefinition"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:297:1: labelDefinition : identifier ':' ;
    def labelDefinition(self, ):

        retval = self.labelDefinition_return()
        retval.start = self.input.LT(1)
        labelDefinition_StartIndex = self.input.index()
        root_0 = None

        char_literal391 = None
        identifier390 = None


        char_literal391_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 72):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:298:3: ( identifier ':' )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:298:5: identifier ':'
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_labelDefinition2678)
                identifier390 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier390.tree)
                char_literal391=self.match(self.input, 121, self.FOLLOW_121_in_labelDefinition2680)
                if self._state.backtracking == 0:

                    char_literal391_tree = self._adaptor.createWithPayload(char_literal391)
                    self._adaptor.addChild(root_0, char_literal391_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 72, labelDefinition_StartIndex, success)

            pass
        return retval

    # $ANTLR end "labelDefinition"

    class assemblySwitch_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblySwitch_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblySwitch"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:300:1: assemblySwitch : 'switch' assemblyExpression ( assemblyCase )* ;
    def assemblySwitch(self, ):

        retval = self.assemblySwitch_return()
        retval.start = self.input.LT(1)
        assemblySwitch_StartIndex = self.input.index()
        root_0 = None

        string_literal392 = None
        assemblyExpression393 = None

        assemblyCase394 = None


        string_literal392_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 73):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:301:3: ( 'switch' assemblyExpression ( assemblyCase )* )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:301:5: 'switch' assemblyExpression ( assemblyCase )*
                pass 
                root_0 = self._adaptor.nil()

                string_literal392=self.match(self.input, 135, self.FOLLOW_135_in_assemblySwitch2691)
                if self._state.backtracking == 0:

                    string_literal392_tree = self._adaptor.createWithPayload(string_literal392)
                    self._adaptor.addChild(root_0, string_literal392_tree)

                self._state.following.append(self.FOLLOW_assemblyExpression_in_assemblySwitch2693)
                assemblyExpression393 = self.assemblyExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyExpression393.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:301:33: ( assemblyCase )*
                while True: #loop90
                    alt90 = 2
                    alt90 = self.dfa90.predict(self.input)
                    if alt90 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: assemblyCase
                        pass 
                        self._state.following.append(self.FOLLOW_assemblyCase_in_assemblySwitch2695)
                        assemblyCase394 = self.assemblyCase()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, assemblyCase394.tree)


                    else:
                        break #loop90



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 73, assemblySwitch_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblySwitch"

    class assemblyCase_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyCase_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyCase"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:303:1: assemblyCase : ( 'case' assemblyLiteral assemblyBlock | 'default' assemblyBlock );
    def assemblyCase(self, ):

        retval = self.assemblyCase_return()
        retval.start = self.input.LT(1)
        assemblyCase_StartIndex = self.input.index()
        root_0 = None

        string_literal395 = None
        string_literal398 = None
        assemblyLiteral396 = None

        assemblyBlock397 = None

        assemblyBlock399 = None


        string_literal395_tree = None
        string_literal398_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 74):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:304:3: ( 'case' assemblyLiteral assemblyBlock | 'default' assemblyBlock )
                alt91 = 2
                LA91_0 = self.input.LA(1)

                if (LA91_0 == 136) :
                    alt91 = 1
                elif (LA91_0 == 137) :
                    alt91 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 91, 0, self.input)

                    raise nvae

                if alt91 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:304:5: 'case' assemblyLiteral assemblyBlock
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal395=self.match(self.input, 136, self.FOLLOW_136_in_assemblyCase2707)
                    if self._state.backtracking == 0:

                        string_literal395_tree = self._adaptor.createWithPayload(string_literal395)
                        self._adaptor.addChild(root_0, string_literal395_tree)

                    self._state.following.append(self.FOLLOW_assemblyLiteral_in_assemblyCase2709)
                    assemblyLiteral396 = self.assemblyLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyLiteral396.tree)
                    self._state.following.append(self.FOLLOW_assemblyBlock_in_assemblyCase2711)
                    assemblyBlock397 = self.assemblyBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyBlock397.tree)


                elif alt91 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:305:5: 'default' assemblyBlock
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal398=self.match(self.input, 137, self.FOLLOW_137_in_assemblyCase2717)
                    if self._state.backtracking == 0:

                        string_literal398_tree = self._adaptor.createWithPayload(string_literal398)
                        self._adaptor.addChild(root_0, string_literal398_tree)

                    self._state.following.append(self.FOLLOW_assemblyBlock_in_assemblyCase2719)
                    assemblyBlock399 = self.assemblyBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyBlock399.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 74, assemblyCase_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyCase"

    class assemblyFunctionDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyFunctionDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyFunctionDefinition"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:307:1: assemblyFunctionDefinition : 'function' identifier '(' ( assemblyIdentifierList )? ')' ( assemblyFunctionReturns )? assemblyBlock ;
    def assemblyFunctionDefinition(self, ):

        retval = self.assemblyFunctionDefinition_return()
        retval.start = self.input.LT(1)
        assemblyFunctionDefinition_StartIndex = self.input.index()
        root_0 = None

        string_literal400 = None
        char_literal402 = None
        char_literal404 = None
        identifier401 = None

        assemblyIdentifierList403 = None

        assemblyFunctionReturns405 = None

        assemblyBlock406 = None


        string_literal400_tree = None
        char_literal402_tree = None
        char_literal404_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 75):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:308:3: ( 'function' identifier '(' ( assemblyIdentifierList )? ')' ( assemblyFunctionReturns )? assemblyBlock )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:308:5: 'function' identifier '(' ( assemblyIdentifierList )? ')' ( assemblyFunctionReturns )? assemblyBlock
                pass 
                root_0 = self._adaptor.nil()

                string_literal400=self.match(self.input, 76, self.FOLLOW_76_in_assemblyFunctionDefinition2730)
                if self._state.backtracking == 0:

                    string_literal400_tree = self._adaptor.createWithPayload(string_literal400)
                    self._adaptor.addChild(root_0, string_literal400_tree)

                self._state.following.append(self.FOLLOW_identifier_in_assemblyFunctionDefinition2732)
                identifier401 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier401.tree)
                char_literal402=self.match(self.input, 69, self.FOLLOW_69_in_assemblyFunctionDefinition2734)
                if self._state.backtracking == 0:

                    char_literal402_tree = self._adaptor.createWithPayload(char_literal402)
                    self._adaptor.addChild(root_0, char_literal402_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:308:31: ( assemblyIdentifierList )?
                alt92 = 2
                LA92_0 = self.input.LA(1)

                if (LA92_0 == Identifier or LA92_0 == 61 or LA92_0 == 88) :
                    alt92 = 1
                if alt92 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: assemblyIdentifierList
                    pass 
                    self._state.following.append(self.FOLLOW_assemblyIdentifierList_in_assemblyFunctionDefinition2736)
                    assemblyIdentifierList403 = self.assemblyIdentifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyIdentifierList403.tree)



                char_literal404=self.match(self.input, 70, self.FOLLOW_70_in_assemblyFunctionDefinition2739)
                if self._state.backtracking == 0:

                    char_literal404_tree = self._adaptor.createWithPayload(char_literal404)
                    self._adaptor.addChild(root_0, char_literal404_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:309:5: ( assemblyFunctionReturns )?
                alt93 = 2
                LA93_0 = self.input.LA(1)

                if (LA93_0 == 138) :
                    alt93 = 1
                if alt93 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: assemblyFunctionReturns
                    pass 
                    self._state.following.append(self.FOLLOW_assemblyFunctionReturns_in_assemblyFunctionDefinition2745)
                    assemblyFunctionReturns405 = self.assemblyFunctionReturns()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyFunctionReturns405.tree)



                self._state.following.append(self.FOLLOW_assemblyBlock_in_assemblyFunctionDefinition2748)
                assemblyBlock406 = self.assemblyBlock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyBlock406.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 75, assemblyFunctionDefinition_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyFunctionDefinition"

    class assemblyFunctionReturns_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyFunctionReturns_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyFunctionReturns"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:311:1: assemblyFunctionReturns : ( '->' assemblyIdentifierList ) ;
    def assemblyFunctionReturns(self, ):

        retval = self.assemblyFunctionReturns_return()
        retval.start = self.input.LT(1)
        assemblyFunctionReturns_StartIndex = self.input.index()
        root_0 = None

        string_literal407 = None
        assemblyIdentifierList408 = None


        string_literal407_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 76):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:312:3: ( ( '->' assemblyIdentifierList ) )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:312:5: ( '->' assemblyIdentifierList )
                pass 
                root_0 = self._adaptor.nil()

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:312:5: ( '->' assemblyIdentifierList )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:312:7: '->' assemblyIdentifierList
                pass 
                string_literal407=self.match(self.input, 138, self.FOLLOW_138_in_assemblyFunctionReturns2761)
                if self._state.backtracking == 0:

                    string_literal407_tree = self._adaptor.createWithPayload(string_literal407)
                    self._adaptor.addChild(root_0, string_literal407_tree)

                self._state.following.append(self.FOLLOW_assemblyIdentifierList_in_assemblyFunctionReturns2763)
                assemblyIdentifierList408 = self.assemblyIdentifierList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyIdentifierList408.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 76, assemblyFunctionReturns_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyFunctionReturns"

    class assemblyFor_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyFor_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyFor"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:314:1: assemblyFor : 'for' ( assemblyBlock | assemblyExpression ) assemblyExpression ( assemblyBlock | assemblyExpression ) assemblyBlock ;
    def assemblyFor(self, ):

        retval = self.assemblyFor_return()
        retval.start = self.input.LT(1)
        assemblyFor_StartIndex = self.input.index()
        root_0 = None

        string_literal409 = None
        assemblyBlock410 = None

        assemblyExpression411 = None

        assemblyExpression412 = None

        assemblyBlock413 = None

        assemblyExpression414 = None

        assemblyBlock415 = None


        string_literal409_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 77):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:315:3: ( 'for' ( assemblyBlock | assemblyExpression ) assemblyExpression ( assemblyBlock | assemblyExpression ) assemblyBlock )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:315:5: 'for' ( assemblyBlock | assemblyExpression ) assemblyExpression ( assemblyBlock | assemblyExpression ) assemblyBlock
                pass 
                root_0 = self._adaptor.nil()

                string_literal409=self.match(self.input, 72, self.FOLLOW_72_in_assemblyFor2776)
                if self._state.backtracking == 0:

                    string_literal409_tree = self._adaptor.createWithPayload(string_literal409)
                    self._adaptor.addChild(root_0, string_literal409_tree)

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:315:11: ( assemblyBlock | assemblyExpression )
                alt94 = 2
                LA94_0 = self.input.LA(1)

                if (LA94_0 == 62) :
                    alt94 = 1
                elif (LA94_0 == StringLiteral or LA94_0 == HexLiteral or (DecimalNumber <= LA94_0 <= HexNumber) or LA94_0 == Identifier or LA94_0 == 61 or LA94_0 == 80 or LA94_0 == 88 or LA94_0 == 94 or LA94_0 == 100) :
                    alt94 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 94, 0, self.input)

                    raise nvae

                if alt94 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:315:13: assemblyBlock
                    pass 
                    self._state.following.append(self.FOLLOW_assemblyBlock_in_assemblyFor2780)
                    assemblyBlock410 = self.assemblyBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyBlock410.tree)


                elif alt94 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:315:29: assemblyExpression
                    pass 
                    self._state.following.append(self.FOLLOW_assemblyExpression_in_assemblyFor2784)
                    assemblyExpression411 = self.assemblyExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyExpression411.tree)



                self._state.following.append(self.FOLLOW_assemblyExpression_in_assemblyFor2792)
                assemblyExpression412 = self.assemblyExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyExpression412.tree)
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:316:24: ( assemblyBlock | assemblyExpression )
                alt95 = 2
                LA95_0 = self.input.LA(1)

                if (LA95_0 == 62) :
                    alt95 = 1
                elif (LA95_0 == StringLiteral or LA95_0 == HexLiteral or (DecimalNumber <= LA95_0 <= HexNumber) or LA95_0 == Identifier or LA95_0 == 61 or LA95_0 == 80 or LA95_0 == 88 or LA95_0 == 94 or LA95_0 == 100) :
                    alt95 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 95, 0, self.input)

                    raise nvae

                if alt95 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:316:26: assemblyBlock
                    pass 
                    self._state.following.append(self.FOLLOW_assemblyBlock_in_assemblyFor2796)
                    assemblyBlock413 = self.assemblyBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyBlock413.tree)


                elif alt95 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:316:42: assemblyExpression
                    pass 
                    self._state.following.append(self.FOLLOW_assemblyExpression_in_assemblyFor2800)
                    assemblyExpression414 = self.assemblyExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assemblyExpression414.tree)



                self._state.following.append(self.FOLLOW_assemblyBlock_in_assemblyFor2804)
                assemblyBlock415 = self.assemblyBlock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyBlock415.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 77, assemblyFor_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyFor"

    class assemblyIf_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyIf_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyIf"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:318:1: assemblyIf : 'if' assemblyExpression assemblyBlock ;
    def assemblyIf(self, ):

        retval = self.assemblyIf_return()
        retval.start = self.input.LT(1)
        assemblyIf_StartIndex = self.input.index()
        root_0 = None

        string_literal416 = None
        assemblyExpression417 = None

        assemblyBlock418 = None


        string_literal416_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 78):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:319:3: ( 'if' assemblyExpression assemblyBlock )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:319:5: 'if' assemblyExpression assemblyBlock
                pass 
                root_0 = self._adaptor.nil()

                string_literal416=self.match(self.input, 89, self.FOLLOW_89_in_assemblyIf2815)
                if self._state.backtracking == 0:

                    string_literal416_tree = self._adaptor.createWithPayload(string_literal416)
                    self._adaptor.addChild(root_0, string_literal416_tree)

                self._state.following.append(self.FOLLOW_assemblyExpression_in_assemblyIf2817)
                assemblyExpression417 = self.assemblyExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyExpression417.tree)
                self._state.following.append(self.FOLLOW_assemblyBlock_in_assemblyIf2819)
                assemblyBlock418 = self.assemblyBlock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyBlock418.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 78, assemblyIf_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyIf"

    class assemblyLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.assemblyLiteral_return, self).__init__()

            self.tree = None




    # $ANTLR start "assemblyLiteral"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:321:1: assemblyLiteral : ( StringLiteral | DecimalNumber | HexNumber | HexLiteral );
    def assemblyLiteral(self, ):

        retval = self.assemblyLiteral_return()
        retval.start = self.input.LT(1)
        assemblyLiteral_StartIndex = self.input.index()
        root_0 = None

        set419 = None

        set419_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 79):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:322:3: ( StringLiteral | DecimalNumber | HexNumber | HexLiteral )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:
                pass 
                root_0 = self._adaptor.nil()

                set419 = self.input.LT(1)
                if self.input.LA(1) == StringLiteral or self.input.LA(1) == HexLiteral or (DecimalNumber <= self.input.LA(1) <= HexNumber):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set419))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 79, assemblyLiteral_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assemblyLiteral"

    class subAssembly_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.subAssembly_return, self).__init__()

            self.tree = None




    # $ANTLR start "subAssembly"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:324:1: subAssembly : 'assembly' identifier assemblyBlock ;
    def subAssembly(self, ):

        retval = self.subAssembly_return()
        retval.start = self.input.LT(1)
        subAssembly_StartIndex = self.input.index()
        root_0 = None

        string_literal420 = None
        identifier421 = None

        assemblyBlock422 = None


        string_literal420_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 80):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:325:3: ( 'assembly' identifier assemblyBlock )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:325:5: 'assembly' identifier assemblyBlock
                pass 
                root_0 = self._adaptor.nil()

                string_literal420=self.match(self.input, 92, self.FOLLOW_92_in_subAssembly2853)
                if self._state.backtracking == 0:

                    string_literal420_tree = self._adaptor.createWithPayload(string_literal420)
                    self._adaptor.addChild(root_0, string_literal420_tree)

                self._state.following.append(self.FOLLOW_identifier_in_subAssembly2855)
                identifier421 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier421.tree)
                self._state.following.append(self.FOLLOW_assemblyBlock_in_subAssembly2857)
                assemblyBlock422 = self.assemblyBlock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assemblyBlock422.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 80, subAssembly_StartIndex, success)

            pass
        return retval

    # $ANTLR end "subAssembly"

    class tupleExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.tupleExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "tupleExpression"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:327:1: tupleExpression : ( '(' ( ( expression )? ( ',' ( expression )? )* ) ')' | '[' ( expression ( ',' expression )* )? ']' );
    def tupleExpression(self, ):

        retval = self.tupleExpression_return()
        retval.start = self.input.LT(1)
        tupleExpression_StartIndex = self.input.index()
        root_0 = None

        char_literal423 = None
        char_literal425 = None
        char_literal427 = None
        char_literal428 = None
        char_literal430 = None
        char_literal432 = None
        expression424 = None

        expression426 = None

        expression429 = None

        expression431 = None


        char_literal423_tree = None
        char_literal425_tree = None
        char_literal427_tree = None
        char_literal428_tree = None
        char_literal430_tree = None
        char_literal432_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 81):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:328:3: ( '(' ( ( expression )? ( ',' ( expression )? )* ) ')' | '[' ( expression ( ',' expression )* )? ']' )
                alt101 = 2
                LA101_0 = self.input.LA(1)

                if (LA101_0 == 69) :
                    alt101 = 1
                elif (LA101_0 == 81) :
                    alt101 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 101, 0, self.input)

                    raise nvae

                if alt101 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:328:5: '(' ( ( expression )? ( ',' ( expression )? )* ) ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal423=self.match(self.input, 69, self.FOLLOW_69_in_tupleExpression2868)
                    if self._state.backtracking == 0:

                        char_literal423_tree = self._adaptor.createWithPayload(char_literal423)
                        self._adaptor.addChild(root_0, char_literal423_tree)

                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:328:9: ( ( expression )? ( ',' ( expression )? )* )
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:328:11: ( expression )? ( ',' ( expression )? )*
                    pass 
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:328:11: ( expression )?
                    alt96 = 2
                    alt96 = self.dfa96.predict(self.input)
                    if alt96 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_tupleExpression2872)
                        expression424 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression424.tree)



                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:328:23: ( ',' ( expression )? )*
                    while True: #loop98
                        alt98 = 2
                        LA98_0 = self.input.LA(1)

                        if (LA98_0 == 63) :
                            alt98 = 1


                        if alt98 == 1:
                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:328:25: ',' ( expression )?
                            pass 
                            char_literal425=self.match(self.input, 63, self.FOLLOW_63_in_tupleExpression2877)
                            if self._state.backtracking == 0:

                                char_literal425_tree = self._adaptor.createWithPayload(char_literal425)
                                self._adaptor.addChild(root_0, char_literal425_tree)

                            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:328:29: ( expression )?
                            alt97 = 2
                            alt97 = self.dfa97.predict(self.input)
                            if alt97 == 1:
                                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: expression
                                pass 
                                self._state.following.append(self.FOLLOW_expression_in_tupleExpression2879)
                                expression426 = self.expression()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, expression426.tree)





                        else:
                            break #loop98



                    char_literal427=self.match(self.input, 70, self.FOLLOW_70_in_tupleExpression2887)
                    if self._state.backtracking == 0:

                        char_literal427_tree = self._adaptor.createWithPayload(char_literal427)
                        self._adaptor.addChild(root_0, char_literal427_tree)



                elif alt101 == 2:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:329:5: '[' ( expression ( ',' expression )* )? ']'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal428=self.match(self.input, 81, self.FOLLOW_81_in_tupleExpression2893)
                    if self._state.backtracking == 0:

                        char_literal428_tree = self._adaptor.createWithPayload(char_literal428)
                        self._adaptor.addChild(root_0, char_literal428_tree)

                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:329:9: ( expression ( ',' expression )* )?
                    alt100 = 2
                    alt100 = self.dfa100.predict(self.input)
                    if alt100 == 1:
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:329:11: expression ( ',' expression )*
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_tupleExpression2897)
                        expression429 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression429.tree)
                        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:329:22: ( ',' expression )*
                        while True: #loop99
                            alt99 = 2
                            LA99_0 = self.input.LA(1)

                            if (LA99_0 == 63) :
                                alt99 = 1


                            if alt99 == 1:
                                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:329:24: ',' expression
                                pass 
                                char_literal430=self.match(self.input, 63, self.FOLLOW_63_in_tupleExpression2901)
                                if self._state.backtracking == 0:

                                    char_literal430_tree = self._adaptor.createWithPayload(char_literal430)
                                    self._adaptor.addChild(root_0, char_literal430_tree)

                                self._state.following.append(self.FOLLOW_expression_in_tupleExpression2903)
                                expression431 = self.expression()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, expression431.tree)


                            else:
                                break #loop99



                    char_literal432=self.match(self.input, 82, self.FOLLOW_82_in_tupleExpression2911)
                    if self._state.backtracking == 0:

                        char_literal432_tree = self._adaptor.createWithPayload(char_literal432)
                        self._adaptor.addChild(root_0, char_literal432_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 81, tupleExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "tupleExpression"

    class elementaryTypeNameExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.elementaryTypeNameExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementaryTypeNameExpression"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:331:1: elementaryTypeNameExpression : elementaryTypeName ;
    def elementaryTypeNameExpression(self, ):

        retval = self.elementaryTypeNameExpression_return()
        retval.start = self.input.LT(1)
        elementaryTypeNameExpression_StartIndex = self.input.index()
        root_0 = None

        elementaryTypeName433 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 82):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:332:3: ( elementaryTypeName )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:332:5: elementaryTypeName
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_elementaryTypeName_in_elementaryTypeNameExpression2922)
                elementaryTypeName433 = self.elementaryTypeName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, elementaryTypeName433.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 82, elementaryTypeNameExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "elementaryTypeNameExpression"

    class numberLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.numberLiteral_return, self).__init__()

            self.tree = None




    # $ANTLR start "numberLiteral"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:334:1: numberLiteral : ( DecimalNumber | HexNumber ) ( NumberUnit )? ;
    def numberLiteral(self, ):

        retval = self.numberLiteral_return()
        retval.start = self.input.LT(1)
        numberLiteral_StartIndex = self.input.index()
        root_0 = None

        set434 = None
        NumberUnit435 = None

        set434_tree = None
        NumberUnit435_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 83):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:335:3: ( ( DecimalNumber | HexNumber ) ( NumberUnit )? )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:335:5: ( DecimalNumber | HexNumber ) ( NumberUnit )?
                pass 
                root_0 = self._adaptor.nil()

                set434 = self.input.LT(1)
                if (DecimalNumber <= self.input.LA(1) <= HexNumber):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set434))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse


                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:335:33: ( NumberUnit )?
                alt102 = 2
                alt102 = self.dfa102.predict(self.input)
                if alt102 == 1:
                    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: NumberUnit
                    pass 
                    NumberUnit435=self.match(self.input, NumberUnit, self.FOLLOW_NumberUnit_in_numberLiteral2941)
                    if self._state.backtracking == 0:

                        NumberUnit435_tree = self._adaptor.createWithPayload(NumberUnit435)
                        self._adaptor.addChild(root_0, NumberUnit435_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 83, numberLiteral_StartIndex, success)

            pass
        return retval

    # $ANTLR end "numberLiteral"

    class identifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(solParser.identifier_return, self).__init__()

            self.tree = None




    # $ANTLR start "identifier"
    # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:337:1: identifier : ( 'from' | 'calldata' | Identifier ) ;
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)
        identifier_StartIndex = self.input.index()
        root_0 = None

        set436 = None

        set436_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 84):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:338:3: ( ( 'from' | 'calldata' | Identifier ) )
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:338:5: ( 'from' | 'calldata' | Identifier )
                pass 
                root_0 = self._adaptor.nil()

                set436 = self.input.LT(1)
                if self.input.LA(1) == Identifier or self.input.LA(1) == 61 or self.input.LA(1) == 88:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set436))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 84, identifier_StartIndex, success)

            pass
        return retval

    # $ANTLR end "identifier"

    # $ANTLR start "synpred61_sol"
    def synpred61_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:108:14: ( storageLocation )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:108:14: storageLocation
        pass 
        self._state.following.append(self.FOLLOW_storageLocation_in_synpred61_sol764)
        self.storageLocation()

        self._state.following.pop()


    # $ANTLR end "synpred61_sol"



    # $ANTLR start "synpred76_sol"
    def synpred76_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:100: ( '[' ( expression )? ']' )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:100: '[' ( expression )? ']'
        pass 
        self.match(self.input, 81, self.FOLLOW_81_in_synpred76_sol903)
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:126:104: ( expression )?
        alt113 = 2
        alt113 = self.dfa113.predict(self.input)
        if alt113 == 1:
            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: expression
            pass 
            self._state.following.append(self.FOLLOW_expression_in_synpred76_sol905)
            self.expression()

            self._state.following.pop()



        self.match(self.input, 82, self.FOLLOW_82_in_synpred76_sol908)


    # $ANTLR end "synpred76_sol"



    # $ANTLR start "synpred77_sol"
    def synpred77_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:129:18: ( '.' identifier )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:129:18: '.' identifier
        pass 
        self.match(self.input, 83, self.FOLLOW_83_in_synpred77_sol925)
        self._state.following.append(self.FOLLOW_identifier_in_synpred77_sol927)
        self.identifier()

        self._state.following.pop()


    # $ANTLR end "synpred77_sol"



    # $ANTLR start "synpred78_sol"
    def synpred78_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:136:7: ( InternalKeyword )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:136:7: InternalKeyword
        pass 
        self.match(self.input, InternalKeyword, self.FOLLOW_InternalKeyword_in_synpred78_sol972)


    # $ANTLR end "synpred78_sol"



    # $ANTLR start "synpred80_sol"
    def synpred80_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:136:43: ( stateMutability )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:136:43: stateMutability
        pass 
        self._state.following.append(self.FOLLOW_stateMutability_in_synpred80_sol980)
        self.stateMutability()

        self._state.following.pop()


    # $ANTLR end "synpred80_sol"



    # $ANTLR start "synpred99_sol"
    def synpred99_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:166:41: ( 'else' statement )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:166:41: 'else' statement
        pass 
        self.match(self.input, 90, self.FOLLOW_90_in_synpred99_sol1166)
        self._state.following.append(self.FOLLOW_statement_in_synpred99_sol1168)
        self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred99_sol"



    # $ANTLR start "synpred100_sol"
    def synpred100_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:172:7: ( variableDeclarationStatement )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:172:7: variableDeclarationStatement
        pass 
        self._state.following.append(self.FOLLOW_variableDeclarationStatement_in_synpred100_sol1203)
        self.variableDeclarationStatement()

        self._state.following.pop()


    # $ANTLR end "synpred100_sol"



    # $ANTLR start "synpred125_sol"
    def synpred125_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:23: ( '(' expression ')' )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:23: '(' expression ')'
        pass 
        self.match(self.input, 69, self.FOLLOW_69_in_synpred125_sol1981)
        self._state.following.append(self.FOLLOW_expression_in_synpred125_sol1983)
        self.expression()

        self._state.following.pop()
        self.match(self.input, 70, self.FOLLOW_70_in_synpred125_sol1985)


    # $ANTLR end "synpred125_sol"



    # $ANTLR start "synpred135_sol"
    def synpred135_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:184: ( ( '++' | '--' ) )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:184: ( '++' | '--' )
        pass 
        if (102 <= self.input.LA(1) <= 103):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse




    # $ANTLR end "synpred135_sol"



    # $ANTLR start "synpred136_sol"
    def synpred136_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:200: ( '[' expression ']' )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:200: '[' expression ']'
        pass 
        self.match(self.input, 81, self.FOLLOW_81_in_synpred136_sol2051)
        self._state.following.append(self.FOLLOW_expression_in_synpred136_sol2053)
        self.expression()

        self._state.following.pop()
        self.match(self.input, 82, self.FOLLOW_82_in_synpred136_sol2055)


    # $ANTLR end "synpred136_sol"



    # $ANTLR start "synpred137_sol"
    def synpred137_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:221: ( '(' functionCallArguments ')' )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:221: '(' functionCallArguments ')'
        pass 
        self.match(self.input, 69, self.FOLLOW_69_in_synpred137_sol2059)
        self._state.following.append(self.FOLLOW_functionCallArguments_in_synpred137_sol2061)
        self.functionCallArguments()

        self._state.following.pop()
        self.match(self.input, 70, self.FOLLOW_70_in_synpred137_sol2063)


    # $ANTLR end "synpred137_sol"



    # $ANTLR start "synpred138_sol"
    def synpred138_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:253: ( '.' identifier )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:253: '.' identifier
        pass 
        self.match(self.input, 83, self.FOLLOW_83_in_synpred138_sol2067)
        self._state.following.append(self.FOLLOW_identifier_in_synpred138_sol2069)
        self.identifier()

        self._state.following.pop()


    # $ANTLR end "synpred138_sol"



    # $ANTLR start "synpred139_sol"
    def synpred139_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:270: ( '**' expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:270: '**' expression
        pass 
        self.match(self.input, 109, self.FOLLOW_109_in_synpred139_sol2073)
        self._state.following.append(self.FOLLOW_expression_in_synpred139_sol2075)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred139_sol"



    # $ANTLR start "synpred142_sol"
    def synpred142_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:288: ( ( '*' | '/' | '%' ) expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:288: ( '*' | '/' | '%' ) expression
        pass 
        if self.input.LA(1) == 60 or (110 <= self.input.LA(1) <= 111):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_expression_in_synpred142_sol2091)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred142_sol"



    # $ANTLR start "synpred144_sol"
    def synpred144_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:319: ( ( '+' | '-' ) expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:319: ( '+' | '-' ) expression
        pass 
        if (104 <= self.input.LA(1) <= 105):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_expression_in_synpred144_sol2103)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred144_sol"



    # $ANTLR start "synpred146_sol"
    def synpred146_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:344: ( ( '<<' | '>>' ) expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:344: ( '<<' | '>>' ) expression
        pass 
        if (112 <= self.input.LA(1) <= 113):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_expression_in_synpred146_sol2115)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred146_sol"



    # $ANTLR start "synpred147_sol"
    def synpred147_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:371: ( '&' expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:371: '&' expression
        pass 
        self.match(self.input, 114, self.FOLLOW_114_in_synpred147_sol2119)
        self._state.following.append(self.FOLLOW_expression_in_synpred147_sol2121)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred147_sol"



    # $ANTLR start "synpred148_sol"
    def synpred148_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:388: ( '^' expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:388: '^' expression
        pass 
        self.match(self.input, 51, self.FOLLOW_51_in_synpred148_sol2125)
        self._state.following.append(self.FOLLOW_expression_in_synpred148_sol2127)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred148_sol"



    # $ANTLR start "synpred149_sol"
    def synpred149_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:405: ( '|' expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:405: '|' expression
        pass 
        self.match(self.input, 115, self.FOLLOW_115_in_synpred149_sol2131)
        self._state.following.append(self.FOLLOW_expression_in_synpred149_sol2133)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred149_sol"



    # $ANTLR start "synpred153_sol"
    def synpred153_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:422: ( ( '<' | '>' | '<=' | '>=' ) expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:422: ( '<' | '>' | '<=' | '>=' ) expression
        pass 
        if (53 <= self.input.LA(1) <= 56):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_expression_in_synpred153_sol2153)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred153_sol"



    # $ANTLR start "synpred155_sol"
    def synpred155_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:461: ( ( '==' | '!=' ) expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:461: ( '==' | '!=' ) expression
        pass 
        if (116 <= self.input.LA(1) <= 117):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_expression_in_synpred155_sol2165)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred155_sol"



    # $ANTLR start "synpred156_sol"
    def synpred156_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:488: ( '&&' expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:488: '&&' expression
        pass 
        self.match(self.input, 118, self.FOLLOW_118_in_synpred156_sol2169)
        self._state.following.append(self.FOLLOW_expression_in_synpred156_sol2171)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred156_sol"



    # $ANTLR start "synpred157_sol"
    def synpred157_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:506: ( '||' expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:506: '||' expression
        pass 
        self.match(self.input, 119, self.FOLLOW_119_in_synpred157_sol2175)
        self._state.following.append(self.FOLLOW_expression_in_synpred157_sol2177)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred157_sol"



    # $ANTLR start "synpred158_sol"
    def synpred158_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:524: ( '?' expression ':' expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:524: '?' expression ':' expression
        pass 
        self.match(self.input, 120, self.FOLLOW_120_in_synpred158_sol2181)
        self._state.following.append(self.FOLLOW_expression_in_synpred158_sol2183)
        self.expression()

        self._state.following.pop()
        self.match(self.input, 121, self.FOLLOW_121_in_synpred158_sol2185)
        self._state.following.append(self.FOLLOW_expression_in_synpred158_sol2187)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred158_sol"



    # $ANTLR start "synpred169_sol"
    def synpred169_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:556: ( ( '=' | '|=' | '^=' | '&=' | '<<=' | '>>=' | '+=' | '-=' | '*=' | '/=' | '%=' ) expression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:227:556: ( '=' | '|=' | '^=' | '&=' | '<<=' | '>>=' | '+=' | '-=' | '*=' | '/=' | '%=' ) expression
        pass 
        if self.input.LA(1) == 57 or (122 <= self.input.LA(1) <= 131):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_expression_in_synpred169_sol2235)
        self.expression()

        self._state.following.pop()


    # $ANTLR end "synpred169_sol"



    # $ANTLR start "synpred185_sol"
    def synpred185_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:258:5: ( identifier )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:258:5: identifier
        pass 
        self._state.following.append(self.FOLLOW_identifier_in_synpred185_sol2419)
        self.identifier()

        self._state.following.pop()


    # $ANTLR end "synpred185_sol"



    # $ANTLR start "synpred187_sol"
    def synpred187_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:260:5: ( assemblyExpression )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:260:5: assemblyExpression
        pass 
        self._state.following.append(self.FOLLOW_assemblyExpression_in_synpred187_sol2431)
        self.assemblyExpression()

        self._state.following.pop()


    # $ANTLR end "synpred187_sol"



    # $ANTLR start "synpred199_sol"
    def synpred199_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:272:5: ( numberLiteral )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:272:5: numberLiteral
        pass 
        self._state.following.append(self.FOLLOW_numberLiteral_in_synpred199_sol2503)
        self.numberLiteral()

        self._state.following.pop()


    # $ANTLR end "synpred199_sol"



    # $ANTLR start "synpred200_sol"
    def synpred200_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:273:5: ( StringLiteral )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:273:5: StringLiteral
        pass 
        self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_synpred200_sol2509)


    # $ANTLR end "synpred200_sol"



    # $ANTLR start "synpred207_sol"
    def synpred207_sol_fragment(self, ):
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:54: ( '(' ( assemblyExpression )? ( ',' assemblyExpression )* ')' )
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:54: '(' ( assemblyExpression )? ( ',' assemblyExpression )* ')'
        pass 
        self.match(self.input, 69, self.FOLLOW_69_in_synpred207_sol2561)
        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:58: ( assemblyExpression )?
        alt118 = 2
        LA118_0 = self.input.LA(1)

        if (LA118_0 == StringLiteral or LA118_0 == HexLiteral or (DecimalNumber <= LA118_0 <= HexNumber) or LA118_0 == Identifier or LA118_0 == 61 or LA118_0 == 80 or LA118_0 == 88 or LA118_0 == 94 or LA118_0 == 100) :
            alt118 = 1
        if alt118 == 1:
            # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:0:0: assemblyExpression
            pass 
            self._state.following.append(self.FOLLOW_assemblyExpression_in_synpred207_sol2563)
            self.assemblyExpression()

            self._state.following.pop()



        # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:78: ( ',' assemblyExpression )*
        while True: #loop119
            alt119 = 2
            LA119_0 = self.input.LA(1)

            if (LA119_0 == 63) :
                alt119 = 1


            if alt119 == 1:
                # D:\\PycharmProjects\\SolidityObfuscator\\src\\solidityobf\\T\\sol.g:280:80: ',' assemblyExpression
                pass 
                self.match(self.input, 63, self.FOLLOW_63_in_synpred207_sol2568)
                self._state.following.append(self.FOLLOW_assemblyExpression_in_synpred207_sol2570)
                self.assemblyExpression()

                self._state.following.pop()


            else:
                break #loop119
        self.match(self.input, 70, self.FOLLOW_70_in_synpred207_sol2575)


    # $ANTLR end "synpred207_sol"




    # Delegated rules

    def synpred149_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred149_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred136_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred136_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred61_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred61_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred157_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred157_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred187_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred187_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred144_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred144_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred153_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred153_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred78_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred78_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred148_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred148_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred99_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred99_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred135_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred135_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred139_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred139_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred199_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred199_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred77_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred77_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred100_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred100_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred156_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred156_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred169_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred169_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred76_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred76_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred142_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred142_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred147_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred147_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred185_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred185_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred125_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred125_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred138_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred138_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred80_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred80_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred155_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred155_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred207_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred207_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred137_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred137_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred146_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred146_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred200_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred200_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred158_sol(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred158_sol_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\40\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\40\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\2\4\36\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\2\154\36\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\34\uffff"
        )

    DFA2_special = DFA.unpack(
        u"\40\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\1\2\1\3\13\uffff\5\3\1\uffff\2\3\2\uffff\2\3\1\uffff"
        u"\1\3\24\uffff\1\2\1\1\5\2\3\uffff\1\3\7\uffff\1\3\12\uffff\2\3"
        u"\6\uffff\1\3\10\uffff\14\3"),
        DFA.unpack(u"\1\2\1\3\13\uffff\5\3\1\uffff\2\3\2\uffff\2\3\1\uffff"
        u"\1\3\25\uffff\1\3\10\uffff\1\3\7\uffff\1\3\12\uffff\2\3\6\uffff"
        u"\1\3\10\uffff\14\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #2

    class DFA2(DFA):
        pass


    # lookup tables for DFA #13

    DFA13_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA13_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA13_min = DFA.unpack(
        u"\1\21\14\uffff"
        )

    DFA13_max = DFA.unpack(
        u"\1\144\14\uffff"
        )

    DFA13_accept = DFA.unpack(
        u"\1\uffff\1\2\1\1\12\uffff"
        )

    DFA13_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA13_transition = [
        DFA.unpack(u"\5\2\10\uffff\1\2\36\uffff\1\2\2\uffff\1\1\6\uffff"
        u"\1\2\1\uffff\4\2\1\uffff\3\2\3\uffff\1\2\3\uffff\1\2\10\uffff\4"
        u"\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #13

    class DFA13(DFA):
        pass


    # lookup tables for DFA #16

    DFA16_eot = DFA.unpack(
        u"\17\uffff"
        )

    DFA16_eof = DFA.unpack(
        u"\17\uffff"
        )

    DFA16_min = DFA.unpack(
        u"\1\21\3\uffff\1\12\12\uffff"
        )

    DFA16_max = DFA.unpack(
        u"\1\144\3\uffff\1\130\12\uffff"
        )

    DFA16_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\4\1\5\1\7\1\10\1\6\2\uffff"
        )

    DFA16_special = DFA.unpack(
        u"\17\uffff"
        )

            
    DFA16_transition = [
        DFA.unpack(u"\5\1\10\uffff\1\1\36\uffff\1\1\11\uffff\1\6\1\uffff"
        u"\1\7\1\10\1\11\1\4\1\uffff\1\12\1\13\1\1\3\uffff\1\1\3\uffff\1"
        u"\1\10\uffff\4\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\14\23\uffff\1\14\36\uffff\1\14\7\uffff\1\1\22\uffff"
        u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #16

    class DFA16(DFA):
        pass


    # lookup tables for DFA #24

    DFA24_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA24_eof = DFA.unpack(
        u"\1\2\11\uffff"
        )

    DFA24_min = DFA.unpack(
        u"\1\6\11\uffff"
        )

    DFA24_max = DFA.unpack(
        u"\1\130\11\uffff"
        )

    DFA24_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\7\uffff"
        )

    DFA24_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA24_transition = [
        DFA.unpack(u"\4\2\1\uffff\1\2\2\uffff\3\2\15\uffff\1\2\36\uffff"
        u"\2\2\6\uffff\1\1\22\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #24

    class DFA24(DFA):
        pass


    # lookup tables for DFA #23

    DFA23_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA23_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA23_min = DFA.unpack(
        u"\1\5\17\uffff"
        )

    DFA23_max = DFA.unpack(
        u"\1\154\17\uffff"
        )

    DFA23_accept = DFA.unpack(
        u"\1\uffff\1\1\15\uffff\1\2"
        )

    DFA23_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA23_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\25\uffff\1\1\10\uffff\1\1\7\uffff\1\1\1\17\11\uffff\2\1\6\uffff"
        u"\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #23

    class DFA23(DFA):
        pass


    # lookup tables for DFA #28

    DFA28_eot = DFA.unpack(
        u"\40\uffff"
        )

    DFA28_eof = DFA.unpack(
        u"\40\uffff"
        )

    DFA28_min = DFA.unpack(
        u"\1\5\37\uffff"
        )

    DFA28_max = DFA.unpack(
        u"\1\154\37\uffff"
        )

    DFA28_accept = DFA.unpack(
        u"\1\uffff\1\2\35\uffff\1\1"
        )

    DFA28_special = DFA.unpack(
        u"\40\uffff"
        )

            
    DFA28_transition = [
        DFA.unpack(u"\1\1\4\uffff\1\37\6\uffff\5\1\1\uffff\6\1\1\uffff\1"
        u"\1\25\uffff\1\1\10\uffff\2\1\1\uffff\1\1\4\uffff\1\1\2\uffff\1"
        u"\1\3\uffff\1\1\3\uffff\2\1\2\uffff\1\1\3\uffff\2\1\1\uffff\22\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #28

    class DFA28(DFA):
        pass


    # lookup tables for DFA #29

    DFA29_eot = DFA.unpack(
        u"\37\uffff"
        )

    DFA29_eof = DFA.unpack(
        u"\37\uffff"
        )

    DFA29_min = DFA.unpack(
        u"\1\5\36\uffff"
        )

    DFA29_max = DFA.unpack(
        u"\1\154\36\uffff"
        )

    DFA29_accept = DFA.unpack(
        u"\1\uffff\1\2\1\1\34\uffff"
        )

    DFA29_special = DFA.unpack(
        u"\37\uffff"
        )

            
    DFA29_transition = [
        DFA.unpack(u"\1\2\13\uffff\5\2\1\uffff\6\2\1\uffff\1\2\25\uffff"
        u"\1\2\10\uffff\2\2\1\uffff\1\1\4\uffff\1\2\2\uffff\1\2\3\uffff\1"
        u"\2\3\uffff\2\2\2\uffff\1\2\3\uffff\2\2\1\uffff\22\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #29

    class DFA29(DFA):
        pass


    # lookup tables for DFA #36

    DFA36_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA36_eof = DFA.unpack(
        u"\1\3\12\uffff"
        )

    DFA36_min = DFA.unpack(
        u"\1\36\1\0\11\uffff"
        )

    DFA36_max = DFA.unpack(
        u"\1\130\1\0\11\uffff"
        )

    DFA36_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\7\uffff"
        )

    DFA36_special = DFA.unpack(
        u"\1\uffff\1\0\11\uffff"
        )

            
    DFA36_transition = [
        DFA.unpack(u"\1\3\36\uffff\1\3\1\uffff\1\3\6\uffff\1\3\17\uffff"
        u"\2\2\1\1"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #36

    class DFA36(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA36_1 = input.LA(1)

                 
                index36_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred61_sol()):
                    s = 2

                elif (True):
                    s = 3

                 
                input.seek(index36_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 36, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #45

    DFA45_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA45_eof = DFA.unpack(
        u"\1\uffff\1\3\10\uffff"
        )

    DFA45_min = DFA.unpack(
        u"\2\36\10\uffff"
        )

    DFA45_max = DFA.unpack(
        u"\2\130\10\uffff"
        )

    DFA45_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\6\uffff"
        )

    DFA45_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA45_transition = [
        DFA.unpack(u"\1\3\36\uffff\1\3\30\uffff\2\2\1\1"),
        DFA.unpack(u"\1\2\23\uffff\1\3\6\uffff\1\3\3\uffff\1\2\1\uffff"
        u"\1\3\6\uffff\1\3\21\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #45

    class DFA45(DFA):
        pass


    # lookup tables for DFA #46

    DFA46_eot = DFA.unpack(
        u"\44\uffff"
        )

    DFA46_eof = DFA.unpack(
        u"\1\uffff\1\5\42\uffff"
        )

    DFA46_min = DFA.unpack(
        u"\1\21\1\6\42\uffff"
        )

    DFA46_max = DFA.unpack(
        u"\1\144\1\u0083\42\uffff"
        )

    DFA46_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\4\1\1\1\5\35\uffff"
        )

    DFA46_special = DFA.unpack(
        u"\44\uffff"
        )

            
    DFA46_transition = [
        DFA.unpack(u"\5\5\10\uffff\1\2\36\uffff\1\2\16\uffff\1\4\3\uffff"
        u"\1\1\3\uffff\1\3\3\uffff\1\2\10\uffff\4\5"),
        DFA.unpack(u"\4\5\3\uffff\1\5\2\uffff\1\6\15\uffff\1\5\23\uffff"
        u"\2\5\1\uffff\5\5\2\uffff\2\5\1\uffff\2\5\4\uffff\2\5\12\uffff\3"
        u"\5\2\uffff\3\5\15\uffff\4\5\3\uffff\27\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #46

    class DFA46(DFA):
        pass


    # lookup tables for DFA #48

    DFA48_eot = DFA.unpack(
        u"\55\uffff"
        )

    DFA48_eof = DFA.unpack(
        u"\1\1\54\uffff"
        )

    DFA48_min = DFA.unpack(
        u"\1\6\12\uffff\1\5\22\uffff\16\0\1\uffff"
        )

    DFA48_max = DFA.unpack(
        u"\1\u0083\12\uffff\1\154\22\uffff\16\0\1\uffff"
        )

    DFA48_accept = DFA.unpack(
        u"\1\uffff\1\2\52\uffff\1\1"
        )

    DFA48_special = DFA.unpack(
        u"\36\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13"
        u"\1\14\1\15\1\uffff"
        )

            
    DFA48_transition = [
        DFA.unpack(u"\4\1\3\uffff\1\1\20\uffff\1\1\23\uffff\2\1\1\uffff"
        u"\5\1\2\uffff\2\1\1\uffff\2\1\4\uffff\2\1\12\uffff\1\13\2\1\2\uffff"
        u"\3\1\15\uffff\4\1\3\uffff\27\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\50\13\uffff\5\53\1\uffff\1\45\1\47\2\uffff\2\46"
        u"\1\uffff\1\51\25\uffff\1\44\10\uffff\1\51\7\uffff\1\37\12\uffff"
        u"\1\53\1\52\1\54\5\uffff\1\51\10\uffff\4\53\1\36\2\40\2\41\2\42"
        u"\1\43"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #48

    class DFA48(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA48_30 = input.LA(1)

                 
                index48_30 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_30)
                if s >= 0:
                    return s
            elif s == 1: 
                LA48_31 = input.LA(1)

                 
                index48_31 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_31)
                if s >= 0:
                    return s
            elif s == 2: 
                LA48_32 = input.LA(1)

                 
                index48_32 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_32)
                if s >= 0:
                    return s
            elif s == 3: 
                LA48_33 = input.LA(1)

                 
                index48_33 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_33)
                if s >= 0:
                    return s
            elif s == 4: 
                LA48_34 = input.LA(1)

                 
                index48_34 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_34)
                if s >= 0:
                    return s
            elif s == 5: 
                LA48_35 = input.LA(1)

                 
                index48_35 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_35)
                if s >= 0:
                    return s
            elif s == 6: 
                LA48_36 = input.LA(1)

                 
                index48_36 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_36)
                if s >= 0:
                    return s
            elif s == 7: 
                LA48_37 = input.LA(1)

                 
                index48_37 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_37)
                if s >= 0:
                    return s
            elif s == 8: 
                LA48_38 = input.LA(1)

                 
                index48_38 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_38)
                if s >= 0:
                    return s
            elif s == 9: 
                LA48_39 = input.LA(1)

                 
                index48_39 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_39)
                if s >= 0:
                    return s
            elif s == 10: 
                LA48_40 = input.LA(1)

                 
                index48_40 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_40)
                if s >= 0:
                    return s
            elif s == 11: 
                LA48_41 = input.LA(1)

                 
                index48_41 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_41)
                if s >= 0:
                    return s
            elif s == 12: 
                LA48_42 = input.LA(1)

                 
                index48_42 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_42)
                if s >= 0:
                    return s
            elif s == 13: 
                LA48_43 = input.LA(1)

                 
                index48_43 = input.index()
                input.rewind()
                s = -1
                if (self.synpred76_sol()):
                    s = 44

                elif (True):
                    s = 1

                 
                input.seek(index48_43)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 48, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #47

    DFA47_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA47_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA47_min = DFA.unpack(
        u"\1\5\17\uffff"
        )

    DFA47_max = DFA.unpack(
        u"\1\154\17\uffff"
        )

    DFA47_accept = DFA.unpack(
        u"\1\uffff\1\1\15\uffff\1\2"
        )

    DFA47_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA47_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\25\uffff\1\1\10\uffff\1\1\7\uffff\1\1\12\uffff\2\1\1\17\5\uffff"
        u"\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #47

    class DFA47(DFA):
        pass


    # lookup tables for DFA #49

    DFA49_eot = DFA.unpack(
        u"\41\uffff"
        )

    DFA49_eof = DFA.unpack(
        u"\1\1\40\uffff"
        )

    DFA49_min = DFA.unpack(
        u"\1\6\15\uffff\1\36\20\uffff\1\0\1\uffff"
        )

    DFA49_max = DFA.unpack(
        u"\1\u0083\15\uffff\1\130\20\uffff\1\0\1\uffff"
        )

    DFA49_accept = DFA.unpack(
        u"\1\uffff\1\2\36\uffff\1\1"
        )

    DFA49_special = DFA.unpack(
        u"\37\uffff\1\0\1\uffff"
        )

            
    DFA49_transition = [
        DFA.unpack(u"\4\1\3\uffff\1\1\20\uffff\1\1\23\uffff\2\1\1\uffff"
        u"\5\1\2\uffff\5\1\4\uffff\2\1\12\uffff\2\1\1\16\2\uffff\3\1\15\uffff"
        u"\4\1\3\uffff\27\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\36\uffff\1\37\32\uffff\1\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #49

    class DFA49(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA49_31 = input.LA(1)

                 
                index49_31 = input.index()
                input.rewind()
                s = -1
                if (self.synpred77_sol()):
                    s = 32

                elif (True):
                    s = 1

                 
                input.seek(index49_31)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 49, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #50

    DFA50_eot = DFA.unpack(
        u"\150\uffff"
        )

    DFA50_eof = DFA.unpack(
        u"\1\1\147\uffff"
        )

    DFA50_min = DFA.unpack(
        u"\1\6\2\uffff\1\0\33\uffff\1\0\110\uffff"
        )

    DFA50_max = DFA.unpack(
        u"\1\u0083\2\uffff\1\0\33\uffff\1\0\110\uffff"
        )

    DFA50_accept = DFA.unpack(
        u"\1\uffff\1\4\36\uffff\1\2\1\uffff\1\3\42\uffff\1\1\42\uffff"
        )

    DFA50_special = DFA.unpack(
        u"\3\uffff\1\0\33\uffff\1\1\110\uffff"
        )

            
    DFA50_transition = [
        DFA.unpack(u"\1\1\1\3\1\1\1\37\1\uffff\1\40\1\uffff\1\1\3\42\15"
        u"\uffff\1\1\23\uffff\2\1\1\uffff\5\1\2\uffff\2\1\1\uffff\2\1\4\uffff"
        u"\2\1\6\uffff\1\1\3\uffff\3\1\2\uffff\3\1\15\uffff\4\1\3\uffff\27"
        u"\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #50

    class DFA50(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA50_3 = input.LA(1)

                 
                index50_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred78_sol()):
                    s = 69

                elif (True):
                    s = 1

                 
                input.seek(index50_3)
                if s >= 0:
                    return s
            elif s == 1: 
                LA50_31 = input.LA(1)

                 
                index50_31 = input.index()
                input.rewind()
                s = -1
                if (self.synpred80_sol()):
                    s = 34

                elif (True):
                    s = 1

                 
                input.seek(index50_31)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 50, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #51

    DFA51_eot = DFA.unpack(
        u"\37\uffff"
        )

    DFA51_eof = DFA.unpack(
        u"\1\2\36\uffff"
        )

    DFA51_min = DFA.unpack(
        u"\1\6\36\uffff"
        )

    DFA51_max = DFA.unpack(
        u"\1\u0083\36\uffff"
        )

    DFA51_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\34\uffff"
        )

    DFA51_special = DFA.unpack(
        u"\37\uffff"
        )

            
    DFA51_transition = [
        DFA.unpack(u"\4\2\3\uffff\1\2\20\uffff\1\2\23\uffff\2\2\1\uffff"
        u"\5\2\2\uffff\2\2\1\uffff\2\2\4\uffff\2\2\6\uffff\1\1\3\uffff\3"
        u"\2\2\uffff\3\2\15\uffff\4\2\3\uffff\27\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #51

    class DFA51(DFA):
        pass


    # lookup tables for DFA #52

    DFA52_eot = DFA.unpack(
        u"\37\uffff"
        )

    DFA52_eof = DFA.unpack(
        u"\37\uffff"
        )

    DFA52_min = DFA.unpack(
        u"\1\5\36\uffff"
        )

    DFA52_max = DFA.unpack(
        u"\1\154\36\uffff"
        )

    DFA52_accept = DFA.unpack(
        u"\1\uffff\1\2\1\1\34\uffff"
        )

    DFA52_special = DFA.unpack(
        u"\37\uffff"
        )

            
    DFA52_transition = [
        DFA.unpack(u"\1\2\13\uffff\5\2\1\uffff\6\2\1\uffff\1\2\25\uffff"
        u"\1\2\10\uffff\2\2\1\uffff\1\1\4\uffff\1\2\2\uffff\1\2\3\uffff\1"
        u"\2\3\uffff\2\2\2\uffff\1\2\3\uffff\2\2\1\uffff\22\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #52

    class DFA52(DFA):
        pass


    # lookup tables for DFA #53

    DFA53_eot = DFA.unpack(
        u"\36\uffff"
        )

    DFA53_eof = DFA.unpack(
        u"\36\uffff"
        )

    DFA53_min = DFA.unpack(
        u"\1\5\35\uffff"
        )

    DFA53_max = DFA.unpack(
        u"\1\154\35\uffff"
        )

    DFA53_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1\14"
        u"\21\uffff"
        )

    DFA53_special = DFA.unpack(
        u"\36\uffff"
        )

            
    DFA53_transition = [
        DFA.unpack(u"\1\14\13\uffff\5\14\1\uffff\2\14\1\10\1\7\2\14\1\uffff"
        u"\1\14\25\uffff\1\14\10\uffff\1\14\1\4\6\uffff\1\14\2\uffff\1\3"
        u"\3\uffff\1\14\3\uffff\2\14\2\uffff\1\14\3\uffff\1\14\1\1\1\uffff"
        u"\1\2\1\5\1\6\1\11\1\12\1\13\14\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #53

    class DFA53(DFA):
        pass


    # lookup tables for DFA #54

    DFA54_eot = DFA.unpack(
        u"\77\uffff"
        )

    DFA54_eof = DFA.unpack(
        u"\1\2\76\uffff"
        )

    DFA54_min = DFA.unpack(
        u"\1\5\1\0\75\uffff"
        )

    DFA54_max = DFA.unpack(
        u"\1\154\1\0\75\uffff"
        )

    DFA54_accept = DFA.unpack(
        u"\2\uffff\1\2\73\uffff\1\1"
        )

    DFA54_special = DFA.unpack(
        u"\1\uffff\1\0\75\uffff"
        )

            
    DFA54_transition = [
        DFA.unpack(u"\1\2\13\uffff\5\2\1\uffff\6\2\1\uffff\1\2\25\uffff"
        u"\1\2\10\uffff\2\2\1\uffff\1\2\4\uffff\1\2\2\uffff\1\2\3\uffff\1"
        u"\2\3\uffff\2\2\2\uffff\1\2\3\uffff\2\2\1\1\22\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #54

    class DFA54(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA54_1 = input.LA(1)

                 
                index54_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred99_sol()):
                    s = 62

                elif (True):
                    s = 2

                 
                input.seek(index54_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 54, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #55

    DFA55_eot = DFA.unpack(
        u"\173\uffff"
        )

    DFA55_eof = DFA.unpack(
        u"\173\uffff"
        )

    DFA55_min = DFA.unpack(
        u"\1\5\1\36\1\20\1\36\2\uffff\1\36\1\5\13\uffff\1\0\1\uffff\1\0"
        u"\23\uffff\1\0\24\uffff\2\0\23\uffff\1\0\37\uffff\1\0\1\uffff\3"
        u"\0\2\uffff\1\0"
        )

    DFA55_max = DFA.unpack(
        u"\1\154\3\u0083\2\uffff\1\u0083\1\154\13\uffff\1\0\1\uffff\1\0"
        u"\23\uffff\1\0\24\uffff\2\0\23\uffff\1\0\37\uffff\1\0\1\uffff\3"
        u"\0\2\uffff\1\0"
        )

    DFA55_accept = DFA.unpack(
        u"\4\uffff\1\1\3\uffff\1\2\162\uffff"
        )

    DFA55_special = DFA.unpack(
        u"\23\uffff\1\0\1\uffff\1\1\23\uffff\1\2\24\uffff\1\3\1\4\23\uffff"
        u"\1\5\37\uffff\1\6\1\uffff\1\7\1\10\1\11\2\uffff\1\12"
        )

            
    DFA55_transition = [
        DFA.unpack(u"\1\10\13\uffff\5\6\1\uffff\2\10\2\uffff\2\10\1\uffff"
        u"\1\3\25\uffff\1\10\10\uffff\1\3\7\uffff\1\7\6\uffff\1\4\3\uffff"
        u"\1\2\1\10\2\uffff\1\4\3\uffff\1\3\10\uffff\1\1\3\6\10\10"),
        DFA.unpack(u"\1\4\23\uffff\2\10\1\uffff\5\10\2\uffff\1\10\1\4\7"
        u"\uffff\1\25\13\uffff\1\23\1\uffff\1\10\2\uffff\3\4\15\uffff\4\10"
        u"\3\uffff\14\10\1\uffff\12\10"),
        DFA.unpack(u"\1\4\15\uffff\1\4\23\uffff\2\10\1\uffff\5\10\2\uffff"
        u"\1\10\1\4\7\uffff\1\10\13\uffff\1\51\1\uffff\1\10\2\uffff\3\4\15"
        u"\uffff\4\10\3\uffff\14\10\1\uffff\12\10"),
        DFA.unpack(u"\1\4\23\uffff\2\10\1\uffff\5\10\2\uffff\1\10\1\4\7"
        u"\uffff\1\10\13\uffff\1\77\1\uffff\1\76\2\uffff\3\4\15\uffff\4\10"
        u"\3\uffff\14\10\1\uffff\12\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\23\uffff\2\10\1\uffff\5\10\2\uffff\1\10\1\4\7"
        u"\uffff\1\10\13\uffff\1\123\1\uffff\1\10\2\uffff\3\4\15\uffff\4"
        u"\10\3\uffff\14\10\1\uffff\12\10"),
        DFA.unpack(u"\1\10\13\uffff\5\172\1\uffff\2\10\2\uffff\2\10\1\uffff"
        u"\1\163\25\uffff\1\10\10\uffff\1\163\1\uffff\1\166\5\uffff\1\10"
        u"\1\167\5\uffff\1\4\3\uffff\1\165\1\10\2\uffff\1\4\3\uffff\1\163"
        u"\10\uffff\4\172\10\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff")
    ]

    # class definition for DFA #55

    class DFA55(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA55_19 = input.LA(1)

                 
                index55_19 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_19)
                if s >= 0:
                    return s
            elif s == 1: 
                LA55_21 = input.LA(1)

                 
                index55_21 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_21)
                if s >= 0:
                    return s
            elif s == 2: 
                LA55_41 = input.LA(1)

                 
                index55_41 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_41)
                if s >= 0:
                    return s
            elif s == 3: 
                LA55_62 = input.LA(1)

                 
                index55_62 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_62)
                if s >= 0:
                    return s
            elif s == 4: 
                LA55_63 = input.LA(1)

                 
                index55_63 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_63)
                if s >= 0:
                    return s
            elif s == 5: 
                LA55_83 = input.LA(1)

                 
                index55_83 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_83)
                if s >= 0:
                    return s
            elif s == 6: 
                LA55_115 = input.LA(1)

                 
                index55_115 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_115)
                if s >= 0:
                    return s
            elif s == 7: 
                LA55_117 = input.LA(1)

                 
                index55_117 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_117)
                if s >= 0:
                    return s
            elif s == 8: 
                LA55_118 = input.LA(1)

                 
                index55_118 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_118)
                if s >= 0:
                    return s
            elif s == 9: 
                LA55_119 = input.LA(1)

                 
                index55_119 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_119)
                if s >= 0:
                    return s
            elif s == 10: 
                LA55_122 = input.LA(1)

                 
                index55_122 = input.index()
                input.rewind()
                s = -1
                if (self.synpred100_sol()):
                    s = 4

                elif (True):
                    s = 8

                 
                input.seek(index55_122)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 55, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #56

    DFA56_eot = DFA.unpack(
        u"\24\uffff"
        )

    DFA56_eof = DFA.unpack(
        u"\24\uffff"
        )

    DFA56_min = DFA.unpack(
        u"\1\5\23\uffff"
        )

    DFA56_max = DFA.unpack(
        u"\1\154\23\uffff"
        )

    DFA56_accept = DFA.unpack(
        u"\1\uffff\1\1\21\uffff\1\2"
        )

    DFA56_special = DFA.unpack(
        u"\24\uffff"
        )

            
    DFA56_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\23\uffff\1\23\1\uffff\1\1\10\uffff\1\1\7\uffff\1\1\6\uffff\1"
        u"\1\3\uffff\2\1\2\uffff\1\1\3\uffff\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #56

    class DFA56(DFA):
        pass


    # lookup tables for DFA #57

    DFA57_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA57_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA57_min = DFA.unpack(
        u"\1\5\17\uffff"
        )

    DFA57_max = DFA.unpack(
        u"\1\154\17\uffff"
        )

    DFA57_accept = DFA.unpack(
        u"\1\uffff\1\1\15\uffff\1\2"
        )

    DFA57_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA57_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\23\uffff\1\17\1\uffff\1\1\10\uffff\1\1\7\uffff\1\1\12\uffff"
        u"\2\1\6\uffff\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #57

    class DFA57(DFA):
        pass


    # lookup tables for DFA #58

    DFA58_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA58_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA58_min = DFA.unpack(
        u"\1\5\17\uffff"
        )

    DFA58_max = DFA.unpack(
        u"\1\154\17\uffff"
        )

    DFA58_accept = DFA.unpack(
        u"\1\uffff\1\1\15\uffff\1\2"
        )

    DFA58_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA58_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\25\uffff\1\1\10\uffff\1\1\7\uffff\1\1\1\17\11\uffff\2\1\6\uffff"
        u"\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #58

    class DFA58(DFA):
        pass


    # lookup tables for DFA #60

    DFA60_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA60_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA60_min = DFA.unpack(
        u"\1\5\17\uffff"
        )

    DFA60_max = DFA.unpack(
        u"\1\154\17\uffff"
        )

    DFA60_accept = DFA.unpack(
        u"\1\uffff\1\1\15\uffff\1\2"
        )

    DFA60_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA60_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\23\uffff\1\17\1\uffff\1\1\10\uffff\1\1\7\uffff\1\1\12\uffff"
        u"\2\1\6\uffff\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #60

    class DFA60(DFA):
        pass


    # lookup tables for DFA #61

    DFA61_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA61_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA61_min = DFA.unpack(
        u"\1\21\1\36\13\uffff"
        )

    DFA61_max = DFA.unpack(
        u"\1\144\1\130\13\uffff"
        )

    DFA61_accept = DFA.unpack(
        u"\2\uffff\1\2\4\uffff\1\3\1\1\4\uffff"
        )

    DFA61_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA61_transition = [
        DFA.unpack(u"\5\2\10\uffff\1\2\36\uffff\1\2\7\uffff\1\7\6\uffff"
        u"\1\2\3\uffff\1\2\3\uffff\1\2\3\uffff\1\2\10\uffff\1\1\3\2"),
        DFA.unpack(u"\1\2\36\uffff\1\2\7\uffff\1\10\13\uffff\1\2\4\uffff"
        u"\3\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #61

    class DFA61(DFA):
        pass


    # lookup tables for DFA #69

    DFA69_eot = DFA.unpack(
        u"\40\uffff"
        )

    DFA69_eof = DFA.unpack(
        u"\40\uffff"
        )

    DFA69_min = DFA.unpack(
        u"\1\5\1\uffff\1\5\14\uffff\16\0\3\uffff"
        )

    DFA69_max = DFA.unpack(
        u"\1\154\1\uffff\1\154\14\uffff\16\0\3\uffff"
        )

    DFA69_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\3\1\4\1\5\1\6\1\7\1\10\26\uffff\1\2"
        )

    DFA69_special = DFA.unpack(
        u"\17\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13"
        u"\1\14\1\15\3\uffff"
        )

            
    DFA69_transition = [
        DFA.unpack(u"\1\10\13\uffff\5\10\1\uffff\2\10\2\uffff\2\10\1\uffff"
        u"\1\10\25\uffff\1\7\10\uffff\1\10\7\uffff\1\2\12\uffff\2\10\6\uffff"
        u"\1\10\10\uffff\4\10\1\1\2\3\2\4\2\5\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\13\uffff\5\34\1\uffff\1\26\1\30\2\uffff\2\27"
        u"\1\uffff\1\32\25\uffff\1\25\10\uffff\1\32\1\uffff\1\10\5\uffff"
        u"\1\20\1\10\11\uffff\1\34\1\33\6\uffff\1\32\10\uffff\4\34\1\17\2"
        u"\21\2\22\2\23\1\24"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #69

    class DFA69(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA69_15 = input.LA(1)

                 
                index69_15 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_15)
                if s >= 0:
                    return s
            elif s == 1: 
                LA69_16 = input.LA(1)

                 
                index69_16 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_16)
                if s >= 0:
                    return s
            elif s == 2: 
                LA69_17 = input.LA(1)

                 
                index69_17 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_17)
                if s >= 0:
                    return s
            elif s == 3: 
                LA69_18 = input.LA(1)

                 
                index69_18 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_18)
                if s >= 0:
                    return s
            elif s == 4: 
                LA69_19 = input.LA(1)

                 
                index69_19 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_19)
                if s >= 0:
                    return s
            elif s == 5: 
                LA69_20 = input.LA(1)

                 
                index69_20 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_20)
                if s >= 0:
                    return s
            elif s == 6: 
                LA69_21 = input.LA(1)

                 
                index69_21 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_21)
                if s >= 0:
                    return s
            elif s == 7: 
                LA69_22 = input.LA(1)

                 
                index69_22 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_22)
                if s >= 0:
                    return s
            elif s == 8: 
                LA69_23 = input.LA(1)

                 
                index69_23 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_23)
                if s >= 0:
                    return s
            elif s == 9: 
                LA69_24 = input.LA(1)

                 
                index69_24 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_24)
                if s >= 0:
                    return s
            elif s == 10: 
                LA69_25 = input.LA(1)

                 
                index69_25 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_25)
                if s >= 0:
                    return s
            elif s == 11: 
                LA69_26 = input.LA(1)

                 
                index69_26 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_26)
                if s >= 0:
                    return s
            elif s == 12: 
                LA69_27 = input.LA(1)

                 
                index69_27 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_27)
                if s >= 0:
                    return s
            elif s == 13: 
                LA69_28 = input.LA(1)

                 
                index69_28 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_sol()):
                    s = 31

                elif (True):
                    s = 8

                 
                input.seek(index69_28)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 69, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #70

    DFA70_eot = DFA.unpack(
        u"\u0117\uffff"
        )

    DFA70_eof = DFA.unpack(
        u"\1\1\u0116\uffff"
        )

    DFA70_min = DFA.unpack(
        u"\1\62\4\uffff\21\0\u0101\uffff"
        )

    DFA70_max = DFA.unpack(
        u"\1\u0083\4\uffff\21\0\u0101\uffff"
        )

    DFA70_accept = DFA.unpack(
        u"\1\uffff\1\22\57\uffff\1\1\16\uffff\1\2\20\uffff\1\3\1\uffff\1"
        u"\4\16\uffff\1\5\16\uffff\1\6\16\uffff\1\7\16\uffff\1\10\16\uffff"
        u"\1\11\16\uffff\1\12\16\uffff\1\13\16\uffff\1\14\16\uffff\1\15\16"
        u"\uffff\1\16\16\uffff\1\17\16\uffff\1\20\16\uffff\1\21"
        )

    DFA70_special = DFA.unpack(
        u"\5\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1"
        u"\14\1\15\1\16\1\17\1\20\u0101\uffff"
        )

            
    DFA70_transition = [
        DFA.unpack(u"\1\1\1\16\1\uffff\4\20\1\25\2\uffff\1\12\2\uffff\2"
        u"\1\4\uffff\1\7\1\1\12\uffff\1\6\1\1\1\10\22\uffff\2\5\2\13\3\uffff"
        u"\1\11\2\12\2\14\1\15\1\17\2\21\1\22\1\23\1\24\1\1\12\25"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #70

    class DFA70(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA70_5 = input.LA(1)

                 
                index70_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred135_sol()):
                    s = 49

                elif (True):
                    s = 1

                 
                input.seek(index70_5)
                if s >= 0:
                    return s
            elif s == 1: 
                LA70_6 = input.LA(1)

                 
                index70_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred136_sol()):
                    s = 64

                elif (True):
                    s = 1

                 
                input.seek(index70_6)
                if s >= 0:
                    return s
            elif s == 2: 
                LA70_7 = input.LA(1)

                 
                index70_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred137_sol()):
                    s = 81

                elif (True):
                    s = 1

                 
                input.seek(index70_7)
                if s >= 0:
                    return s
            elif s == 3: 
                LA70_8 = input.LA(1)

                 
                index70_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred138_sol()):
                    s = 83

                elif (True):
                    s = 1

                 
                input.seek(index70_8)
                if s >= 0:
                    return s
            elif s == 4: 
                LA70_9 = input.LA(1)

                 
                index70_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred139_sol()):
                    s = 98

                elif (True):
                    s = 1

                 
                input.seek(index70_9)
                if s >= 0:
                    return s
            elif s == 5: 
                LA70_10 = input.LA(1)

                 
                index70_10 = input.index()
                input.rewind()
                s = -1
                if (self.synpred142_sol()):
                    s = 113

                elif (True):
                    s = 1

                 
                input.seek(index70_10)
                if s >= 0:
                    return s
            elif s == 6: 
                LA70_11 = input.LA(1)

                 
                index70_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred144_sol()):
                    s = 128

                elif (True):
                    s = 1

                 
                input.seek(index70_11)
                if s >= 0:
                    return s
            elif s == 7: 
                LA70_12 = input.LA(1)

                 
                index70_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred146_sol()):
                    s = 143

                elif (True):
                    s = 1

                 
                input.seek(index70_12)
                if s >= 0:
                    return s
            elif s == 8: 
                LA70_13 = input.LA(1)

                 
                index70_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred147_sol()):
                    s = 158

                elif (True):
                    s = 1

                 
                input.seek(index70_13)
                if s >= 0:
                    return s
            elif s == 9: 
                LA70_14 = input.LA(1)

                 
                index70_14 = input.index()
                input.rewind()
                s = -1
                if (self.synpred148_sol()):
                    s = 173

                elif (True):
                    s = 1

                 
                input.seek(index70_14)
                if s >= 0:
                    return s
            elif s == 10: 
                LA70_15 = input.LA(1)

                 
                index70_15 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_sol()):
                    s = 188

                elif (True):
                    s = 1

                 
                input.seek(index70_15)
                if s >= 0:
                    return s
            elif s == 11: 
                LA70_16 = input.LA(1)

                 
                index70_16 = input.index()
                input.rewind()
                s = -1
                if (self.synpred153_sol()):
                    s = 203

                elif (True):
                    s = 1

                 
                input.seek(index70_16)
                if s >= 0:
                    return s
            elif s == 12: 
                LA70_17 = input.LA(1)

                 
                index70_17 = input.index()
                input.rewind()
                s = -1
                if (self.synpred155_sol()):
                    s = 218

                elif (True):
                    s = 1

                 
                input.seek(index70_17)
                if s >= 0:
                    return s
            elif s == 13: 
                LA70_18 = input.LA(1)

                 
                index70_18 = input.index()
                input.rewind()
                s = -1
                if (self.synpred156_sol()):
                    s = 233

                elif (True):
                    s = 1

                 
                input.seek(index70_18)
                if s >= 0:
                    return s
            elif s == 14: 
                LA70_19 = input.LA(1)

                 
                index70_19 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_sol()):
                    s = 248

                elif (True):
                    s = 1

                 
                input.seek(index70_19)
                if s >= 0:
                    return s
            elif s == 15: 
                LA70_20 = input.LA(1)

                 
                index70_20 = input.index()
                input.rewind()
                s = -1
                if (self.synpred158_sol()):
                    s = 263

                elif (True):
                    s = 1

                 
                input.seek(index70_20)
                if s >= 0:
                    return s
            elif s == 16: 
                LA70_21 = input.LA(1)

                 
                index70_21 = input.index()
                input.rewind()
                s = -1
                if (self.synpred169_sol()):
                    s = 278

                elif (True):
                    s = 1

                 
                input.seek(index70_21)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 70, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #71

    DFA71_eot = DFA.unpack(
        u"\50\uffff"
        )

    DFA71_eof = DFA.unpack(
        u"\1\2\47\uffff"
        )

    DFA71_min = DFA.unpack(
        u"\1\62\1\5\46\uffff"
        )

    DFA71_max = DFA.unpack(
        u"\1\u0083\1\154\46\uffff"
        )

    DFA71_accept = DFA.unpack(
        u"\2\uffff\1\2\26\uffff\1\1\16\uffff"
        )

    DFA71_special = DFA.unpack(
        u"\50\uffff"
        )

            
    DFA71_transition = [
        DFA.unpack(u"\2\2\1\uffff\5\2\2\uffff\1\2\2\uffff\2\2\4\uffff\2"
        u"\2\12\uffff\1\1\2\2\22\uffff\4\2\3\uffff\27\2"),
        DFA.unpack(u"\1\2\13\uffff\5\2\1\uffff\2\2\2\uffff\2\2\1\uffff"
        u"\1\2\25\uffff\1\2\10\uffff\1\2\7\uffff\1\2\12\uffff\2\2\1\31\5"
        u"\uffff\1\2\10\uffff\14\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #71

    class DFA71(DFA):
        pass


    # lookup tables for DFA #72

    DFA72_eot = DFA.unpack(
        u"\50\uffff"
        )

    DFA72_eof = DFA.unpack(
        u"\1\2\47\uffff"
        )

    DFA72_min = DFA.unpack(
        u"\1\62\1\5\46\uffff"
        )

    DFA72_max = DFA.unpack(
        u"\1\u0083\1\154\46\uffff"
        )

    DFA72_accept = DFA.unpack(
        u"\2\uffff\1\2\26\uffff\1\1\16\uffff"
        )

    DFA72_special = DFA.unpack(
        u"\50\uffff"
        )

            
    DFA72_transition = [
        DFA.unpack(u"\2\2\1\uffff\5\2\2\uffff\1\2\2\uffff\2\2\4\uffff\2"
        u"\2\12\uffff\1\1\2\2\22\uffff\4\2\3\uffff\27\2"),
        DFA.unpack(u"\1\2\13\uffff\5\2\1\uffff\2\2\2\uffff\2\2\1\uffff"
        u"\1\2\25\uffff\1\2\10\uffff\1\2\7\uffff\1\2\12\uffff\2\2\1\31\5"
        u"\uffff\1\2\10\uffff\14\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #72

    class DFA72(DFA):
        pass


    # lookup tables for DFA #79

    DFA79_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA79_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA79_min = DFA.unpack(
        u"\1\5\20\uffff"
        )

    DFA79_max = DFA.unpack(
        u"\1\154\20\uffff"
        )

    DFA79_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\16\uffff"
        )

    DFA79_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA79_transition = [
        DFA.unpack(u"\1\2\13\uffff\5\2\1\uffff\2\2\2\uffff\2\2\1\uffff\1"
        u"\2\25\uffff\1\2\10\uffff\1\2\1\1\6\uffff\2\2\11\uffff\2\2\6\uffff"
        u"\1\2\10\uffff\14\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #79

    class DFA79(DFA):
        pass


    # lookup tables for DFA #78

    DFA78_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA78_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA78_min = DFA.unpack(
        u"\1\5\17\uffff"
        )

    DFA78_max = DFA.unpack(
        u"\1\154\17\uffff"
        )

    DFA78_accept = DFA.unpack(
        u"\1\uffff\1\1\15\uffff\1\2"
        )

    DFA78_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA78_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\25\uffff\1\1\10\uffff\1\1\7\uffff\1\1\1\17\11\uffff\2\1\6\uffff"
        u"\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #78

    class DFA78(DFA):
        pass


    # lookup tables for DFA #80

    DFA80_eot = DFA.unpack(
        u"\24\uffff"
        )

    DFA80_eof = DFA.unpack(
        u"\24\uffff"
        )

    DFA80_min = DFA.unpack(
        u"\1\5\23\uffff"
        )

    DFA80_max = DFA.unpack(
        u"\1\u0087\23\uffff"
        )

    DFA80_accept = DFA.unpack(
        u"\1\uffff\1\2\1\1\21\uffff"
        )

    DFA80_special = DFA.unpack(
        u"\24\uffff"
        )

            
    DFA80_transition = [
        DFA.unpack(u"\1\2\22\uffff\5\2\1\uffff\1\2\36\uffff\2\2\1\uffff"
        u"\1\1\4\uffff\1\2\2\uffff\1\2\3\uffff\1\2\3\uffff\1\2\7\uffff\2"
        u"\2\2\uffff\1\2\1\uffff\1\2\5\uffff\1\2\37\uffff\1\2\1\uffff\2\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #80

    class DFA80(DFA):
        pass


    # lookup tables for DFA #81

    DFA81_eot = DFA.unpack(
        u"\152\uffff"
        )

    DFA81_eof = DFA.unpack(
        u"\152\uffff"
        )

    DFA81_min = DFA.unpack(
        u"\1\5\1\171\4\uffff\1\0\12\uffff\2\0\127\uffff"
        )

    DFA81_max = DFA.unpack(
        u"\1\u0087\1\u0085\4\uffff\1\0\12\uffff\2\0\127\uffff"
        )

    DFA81_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\3\uffff\1\4\1\5\1\6\1\10\1\11\1\12\1\13\1\14"
        u"\1\15\1\16\27\uffff\1\7\1\1\25\uffff\1\17\24\uffff\1\20\24\uffff"
        u"\1\21"
        )

    DFA81_special = DFA.unpack(
        u"\1\uffff\1\0\4\uffff\1\1\12\uffff\1\2\1\3\127\uffff"
        )

            
    DFA81_transition = [
        DFA.unpack(u"\1\21\22\uffff\1\22\1\16\1\17\2\6\1\uffff\1\1\36\uffff"
        u"\1\1\1\2\6\uffff\1\10\2\uffff\1\14\3\uffff\1\13\3\uffff\1\3\7\uffff"
        u"\1\1\1\15\2\uffff\1\20\1\uffff\1\3\5\uffff\1\3\37\uffff\1\7\1\uffff"
        u"\1\11\1\12"),
        DFA.unpack(u"\1\50\13\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #81

    class DFA81(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA81_1 = input.LA(1)

                 
                index81_1 = input.index()
                input.rewind()
                s = -1
                if (LA81_1 == 133):
                    s = 8

                elif (LA81_1 == 121):
                    s = 40

                elif (self.synpred185_sol()):
                    s = 41

                elif (self.synpred187_sol()):
                    s = 3

                 
                input.seek(index81_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA81_6 = input.LA(1)

                 
                index81_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred187_sol()):
                    s = 3

                elif (self.synpred199_sol()):
                    s = 63

                 
                input.seek(index81_6)
                if s >= 0:
                    return s
            elif s == 2: 
                LA81_17 = input.LA(1)

                 
                index81_17 = input.index()
                input.rewind()
                s = -1
                if (self.synpred187_sol()):
                    s = 3

                elif (self.synpred200_sol()):
                    s = 84

                 
                input.seek(index81_17)
                if s >= 0:
                    return s
            elif s == 3: 
                LA81_18 = input.LA(1)

                 
                index81_18 = input.index()
                input.rewind()
                s = -1
                if (self.synpred187_sol()):
                    s = 3

                elif (True):
                    s = 105

                 
                input.seek(index81_18)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 81, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #86

    DFA86_eot = DFA.unpack(
        u"\40\uffff"
        )

    DFA86_eof = DFA.unpack(
        u"\1\2\37\uffff"
        )

    DFA86_min = DFA.unpack(
        u"\2\5\32\uffff\1\0\3\uffff"
        )

    DFA86_max = DFA.unpack(
        u"\1\u0089\1\144\32\uffff\1\0\3\uffff"
        )

    DFA86_accept = DFA.unpack(
        u"\2\uffff\1\2\26\uffff\1\1\6\uffff"
        )

    DFA86_special = DFA.unpack(
        u"\34\uffff\1\0\3\uffff"
        )

            
    DFA86_transition = [
        DFA.unpack(u"\1\2\22\uffff\5\2\1\uffff\1\2\36\uffff\4\2\4\uffff"
        u"\1\1\1\2\1\uffff\1\2\3\uffff\1\2\3\uffff\1\2\7\uffff\2\2\2\uffff"
        u"\1\2\1\uffff\1\2\5\uffff\1\2\37\uffff\1\2\1\uffff\4\2"),
        DFA.unpack(u"\1\31\22\uffff\1\31\2\uffff\2\31\1\uffff\1\34\36\uffff"
        u"\1\34\1\uffff\1\31\6\uffff\1\31\11\uffff\1\31\7\uffff\1\34\5\uffff"
        u"\1\31\5\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #86

    class DFA86(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA86_28 = input.LA(1)

                 
                index86_28 = input.index()
                input.rewind()
                s = -1
                if (self.synpred207_sol()):
                    s = 25

                elif (True):
                    s = 2

                 
                input.seek(index86_28)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 86, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #87

    DFA87_eot = DFA.unpack(
        u"\26\uffff"
        )

    DFA87_eof = DFA.unpack(
        u"\1\2\25\uffff"
        )

    DFA87_min = DFA.unpack(
        u"\1\5\25\uffff"
        )

    DFA87_max = DFA.unpack(
        u"\1\u0087\25\uffff"
        )

    DFA87_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\23\uffff"
        )

    DFA87_special = DFA.unpack(
        u"\26\uffff"
        )

            
    DFA87_transition = [
        DFA.unpack(u"\1\2\22\uffff\5\2\1\uffff\1\2\36\uffff\2\2\1\uffff"
        u"\1\2\4\uffff\1\2\2\uffff\1\2\3\uffff\1\2\3\uffff\1\2\7\uffff\2"
        u"\2\2\uffff\1\2\1\uffff\1\2\5\uffff\1\2\37\uffff\1\2\1\1\2\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #87

    class DFA87(DFA):
        pass


    # lookup tables for DFA #90

    DFA90_eot = DFA.unpack(
        u"\27\uffff"
        )

    DFA90_eof = DFA.unpack(
        u"\1\1\26\uffff"
        )

    DFA90_min = DFA.unpack(
        u"\1\5\26\uffff"
        )

    DFA90_max = DFA.unpack(
        u"\1\u0089\26\uffff"
        )

    DFA90_accept = DFA.unpack(
        u"\1\uffff\1\2\23\uffff\1\1\1\uffff"
        )

    DFA90_special = DFA.unpack(
        u"\27\uffff"
        )

            
    DFA90_transition = [
        DFA.unpack(u"\1\1\22\uffff\5\1\1\uffff\1\1\36\uffff\2\1\1\uffff"
        u"\1\1\4\uffff\1\1\2\uffff\1\1\3\uffff\1\1\3\uffff\1\1\7\uffff\2"
        u"\1\2\uffff\1\1\1\uffff\1\1\5\uffff\1\1\37\uffff\1\1\1\uffff\2\1"
        u"\2\25"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #90

    class DFA90(DFA):
        pass


    # lookup tables for DFA #96

    DFA96_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA96_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA96_min = DFA.unpack(
        u"\1\5\20\uffff"
        )

    DFA96_max = DFA.unpack(
        u"\1\154\20\uffff"
        )

    DFA96_accept = DFA.unpack(
        u"\1\uffff\1\1\15\uffff\1\2\1\uffff"
        )

    DFA96_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA96_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\25\uffff\1\1\10\uffff\1\1\1\uffff\1\17\5\uffff\1\1\1\17\11\uffff"
        u"\2\1\6\uffff\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #96

    class DFA96(DFA):
        pass


    # lookup tables for DFA #97

    DFA97_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA97_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA97_min = DFA.unpack(
        u"\1\5\20\uffff"
        )

    DFA97_max = DFA.unpack(
        u"\1\154\20\uffff"
        )

    DFA97_accept = DFA.unpack(
        u"\1\uffff\1\1\15\uffff\1\2\1\uffff"
        )

    DFA97_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA97_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\25\uffff\1\1\10\uffff\1\1\1\uffff\1\17\5\uffff\1\1\1\17\11\uffff"
        u"\2\1\6\uffff\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #97

    class DFA97(DFA):
        pass


    # lookup tables for DFA #100

    DFA100_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA100_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA100_min = DFA.unpack(
        u"\1\5\17\uffff"
        )

    DFA100_max = DFA.unpack(
        u"\1\154\17\uffff"
        )

    DFA100_accept = DFA.unpack(
        u"\1\uffff\1\1\15\uffff\1\2"
        )

    DFA100_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA100_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\25\uffff\1\1\10\uffff\1\1\7\uffff\1\1\12\uffff\2\1\1\17\5\uffff"
        u"\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #100

    class DFA100(DFA):
        pass


    # lookup tables for DFA #102

    DFA102_eot = DFA.unpack(
        u"\53\uffff"
        )

    DFA102_eof = DFA.unpack(
        u"\1\2\52\uffff"
        )

    DFA102_min = DFA.unpack(
        u"\1\5\52\uffff"
        )

    DFA102_max = DFA.unpack(
        u"\1\u0087\52\uffff"
        )

    DFA102_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\50\uffff"
        )

    DFA102_special = DFA.unpack(
        u"\53\uffff"
        )

            
    DFA102_transition = [
        DFA.unpack(u"\1\2\22\uffff\5\2\1\1\1\2\23\uffff\2\2\1\uffff\5\2"
        u"\2\uffff\5\2\4\uffff\2\2\1\uffff\1\2\3\uffff\1\2\3\uffff\4\2\4"
        u"\uffff\2\2\2\uffff\1\2\1\uffff\1\2\5\uffff\1\2\1\uffff\4\2\3\uffff"
        u"\30\2\1\uffff\2\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #102

    class DFA102(DFA):
        pass


    # lookup tables for DFA #113

    DFA113_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA113_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA113_min = DFA.unpack(
        u"\1\5\17\uffff"
        )

    DFA113_max = DFA.unpack(
        u"\1\154\17\uffff"
        )

    DFA113_accept = DFA.unpack(
        u"\1\uffff\1\1\15\uffff\1\2"
        )

    DFA113_special = DFA.unpack(
        u"\20\uffff"
        )

            
    DFA113_transition = [
        DFA.unpack(u"\1\1\13\uffff\5\1\1\uffff\2\1\2\uffff\2\1\1\uffff\1"
        u"\1\25\uffff\1\1\10\uffff\1\1\7\uffff\1\1\12\uffff\2\1\1\17\5\uffff"
        u"\1\1\10\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #113

    class DFA113(DFA):
        pass


 

    FOLLOW_pragmaDirective_in_sourceUnit52 = frozenset([49, 59, 65, 66, 67])
    FOLLOW_importDirective_in_sourceUnit56 = frozenset([49, 59, 65, 66, 67])
    FOLLOW_contractDefinition_in_sourceUnit60 = frozenset([49, 59, 65, 66, 67])
    FOLLOW_EOF_in_sourceUnit64 = frozenset([1])
    FOLLOW_49_in_pragmaDirective75 = frozenset([30, 61, 88])
    FOLLOW_pragmaName_in_pragmaDirective77 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_pragmaValue_in_pragmaDirective79 = frozenset([50])
    FOLLOW_50_in_pragmaDirective81 = frozenset([1])
    FOLLOW_identifier_in_pragmaName92 = frozenset([1])
    FOLLOW_version_in_pragmaValue103 = frozenset([1])
    FOLLOW_expression_in_pragmaValue107 = frozenset([1])
    FOLLOW_versionConstraint_in_version118 = frozenset([1, 4, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_versionConstraint_in_version120 = frozenset([1])
    FOLLOW_set_in_versionOperator0 = frozenset([1])
    FOLLOW_versionOperator_in_versionConstraint167 = frozenset([4])
    FOLLOW_VersionLiteral_in_versionConstraint170 = frozenset([1])
    FOLLOW_identifier_in_importDeclaration181 = frozenset([1, 58])
    FOLLOW_58_in_importDeclaration184 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_importDeclaration186 = frozenset([1])
    FOLLOW_59_in_importDirective199 = frozenset([5])
    FOLLOW_StringLiteral_in_importDirective201 = frozenset([50, 58])
    FOLLOW_58_in_importDirective204 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_importDirective206 = frozenset([50])
    FOLLOW_50_in_importDirective210 = frozenset([1])
    FOLLOW_59_in_importDirective216 = frozenset([30, 60, 61, 88])
    FOLLOW_60_in_importDirective219 = frozenset([58, 61])
    FOLLOW_identifier_in_importDirective223 = frozenset([58, 61])
    FOLLOW_58_in_importDirective227 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_importDirective229 = frozenset([61])
    FOLLOW_61_in_importDirective233 = frozenset([5])
    FOLLOW_StringLiteral_in_importDirective235 = frozenset([50])
    FOLLOW_50_in_importDirective237 = frozenset([1])
    FOLLOW_59_in_importDirective243 = frozenset([62])
    FOLLOW_62_in_importDirective245 = frozenset([30, 61, 88])
    FOLLOW_importDeclaration_in_importDirective247 = frozenset([63, 64])
    FOLLOW_63_in_importDirective251 = frozenset([30, 61, 88])
    FOLLOW_importDeclaration_in_importDirective253 = frozenset([63, 64])
    FOLLOW_64_in_importDirective258 = frozenset([61])
    FOLLOW_61_in_importDirective260 = frozenset([5])
    FOLLOW_StringLiteral_in_importDirective262 = frozenset([50])
    FOLLOW_50_in_importDirective264 = frozenset([1])
    FOLLOW_set_in_contractDefinition275 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_contractDefinition289 = frozenset([62, 68])
    FOLLOW_68_in_contractDefinition297 = frozenset([30, 61, 88])
    FOLLOW_inheritanceSpecifier_in_contractDefinition299 = frozenset([62, 63])
    FOLLOW_63_in_contractDefinition302 = frozenset([30, 61, 88])
    FOLLOW_inheritanceSpecifier_in_contractDefinition304 = frozenset([62, 63])
    FOLLOW_62_in_contractDefinition316 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 64, 69, 71, 73, 74, 75, 76, 78, 79, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_contractPart_in_contractDefinition318 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 64, 69, 71, 73, 74, 75, 76, 78, 79, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_64_in_contractDefinition321 = frozenset([1])
    FOLLOW_userDefinedTypeName_in_inheritanceSpecifier332 = frozenset([1, 69])
    FOLLOW_69_in_inheritanceSpecifier336 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_inheritanceSpecifier338 = frozenset([63, 70])
    FOLLOW_63_in_inheritanceSpecifier342 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_inheritanceSpecifier344 = frozenset([63, 70])
    FOLLOW_70_in_inheritanceSpecifier349 = frozenset([1])
    FOLLOW_stateVariableDeclaration_in_contractPart363 = frozenset([1])
    FOLLOW_usingForDeclaration_in_contractPart369 = frozenset([1])
    FOLLOW_structDefinition_in_contractPart375 = frozenset([1])
    FOLLOW_constructorDefinition_in_contractPart381 = frozenset([1])
    FOLLOW_modifierDefinition_in_contractPart387 = frozenset([1])
    FOLLOW_functionDefinition_in_contractPart393 = frozenset([1])
    FOLLOW_eventDefinition_in_contractPart399 = frozenset([1])
    FOLLOW_enumDefinition_in_contractPart405 = frozenset([1])
    FOLLOW_typeName_in_stateVariableDeclaration416 = frozenset([6, 7, 8, 9, 30, 61, 88])
    FOLLOW_set_in_stateVariableDeclaration422 = frozenset([6, 7, 8, 9, 30, 61, 88])
    FOLLOW_identifier_in_stateVariableDeclaration445 = frozenset([50, 57])
    FOLLOW_57_in_stateVariableDeclaration448 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_stateVariableDeclaration450 = frozenset([50])
    FOLLOW_50_in_stateVariableDeclaration454 = frozenset([1])
    FOLLOW_71_in_usingForDeclaration465 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_usingForDeclaration467 = frozenset([72])
    FOLLOW_72_in_usingForDeclaration469 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 60, 61, 69, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_60_in_usingForDeclaration472 = frozenset([50])
    FOLLOW_typeName_in_usingForDeclaration476 = frozenset([50])
    FOLLOW_50_in_usingForDeclaration479 = frozenset([1])
    FOLLOW_73_in_structDefinition490 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_structDefinition492 = frozenset([62])
    FOLLOW_62_in_structDefinition498 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 64, 69, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_variableDeclaration_in_structDefinition502 = frozenset([50])
    FOLLOW_50_in_structDefinition504 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 64, 69, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_variableDeclaration_in_structDefinition507 = frozenset([50])
    FOLLOW_50_in_structDefinition509 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 64, 69, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_64_in_structDefinition516 = frozenset([1])
    FOLLOW_74_in_constructorDefinition527 = frozenset([69])
    FOLLOW_parameterList_in_constructorDefinition529 = frozenset([6, 7, 8, 9, 11, 14, 15, 16, 30, 61, 62, 88])
    FOLLOW_modifierList_in_constructorDefinition531 = frozenset([6, 7, 8, 9, 11, 14, 15, 16, 30, 61, 62, 88])
    FOLLOW_block_in_constructorDefinition533 = frozenset([1])
    FOLLOW_75_in_modifierDefinition544 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_modifierDefinition546 = frozenset([6, 7, 8, 9, 11, 14, 15, 16, 30, 61, 62, 69, 88])
    FOLLOW_parameterList_in_modifierDefinition548 = frozenset([6, 7, 8, 9, 11, 14, 15, 16, 30, 61, 62, 88])
    FOLLOW_block_in_modifierDefinition551 = frozenset([1])
    FOLLOW_identifier_in_modifierInvocation562 = frozenset([1, 69])
    FOLLOW_69_in_modifierInvocation566 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 70, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expressionList_in_modifierInvocation568 = frozenset([70])
    FOLLOW_70_in_modifierInvocation571 = frozenset([1])
    FOLLOW_76_in_functionDefinition588 = frozenset([10, 30, 61, 88])
    FOLLOW_LT_in_functionDefinition590 = frozenset([10, 30, 61, 88])
    FOLLOW_identifier_in_functionDefinition593 = frozenset([10, 69])
    FOLLOW_LT_in_functionDefinition595 = frozenset([10, 69])
    FOLLOW_parameterList_in_functionDefinition598 = frozenset([10, 62])
    FOLLOW_LT_in_functionDefinition600 = frozenset([10, 62])
    FOLLOW_62_in_functionDefinition604 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 64, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_LT_in_functionDefinition606 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 64, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_statement_in_functionDefinition609 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 64, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_64_in_functionDefinition612 = frozenset([1])
    FOLLOW_77_in_returnParameters624 = frozenset([69])
    FOLLOW_parameterList_in_returnParameters626 = frozenset([1])
    FOLLOW_modifierInvocation_in_modifierList639 = frozenset([1, 6, 7, 8, 9, 11, 14, 15, 16, 30, 61, 88])
    FOLLOW_stateMutability_in_modifierList643 = frozenset([1, 6, 7, 8, 9, 11, 14, 15, 16, 30, 61, 88])
    FOLLOW_ExternalKeyword_in_modifierList647 = frozenset([1, 6, 7, 8, 9, 11, 14, 15, 16, 30, 61, 88])
    FOLLOW_PublicKeyword_in_modifierList655 = frozenset([1, 6, 7, 8, 9, 11, 14, 15, 16, 30, 61, 88])
    FOLLOW_InternalKeyword_in_modifierList659 = frozenset([1, 6, 7, 8, 9, 11, 14, 15, 16, 30, 61, 88])
    FOLLOW_PrivateKeyword_in_modifierList663 = frozenset([1, 6, 7, 8, 9, 11, 14, 15, 16, 30, 61, 88])
    FOLLOW_78_in_eventDefinition677 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_eventDefinition679 = frozenset([69])
    FOLLOW_eventParameterList_in_eventDefinition681 = frozenset([12, 50])
    FOLLOW_AnonymousKeyword_in_eventDefinition683 = frozenset([50])
    FOLLOW_50_in_eventDefinition686 = frozenset([1])
    FOLLOW_identifier_in_enumValue697 = frozenset([1])
    FOLLOW_79_in_enumDefinition708 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_enumDefinition710 = frozenset([62])
    FOLLOW_62_in_enumDefinition712 = frozenset([30, 61, 63, 64, 88])
    FOLLOW_enumValue_in_enumDefinition714 = frozenset([63, 64])
    FOLLOW_63_in_enumDefinition718 = frozenset([30, 61, 88])
    FOLLOW_enumValue_in_enumDefinition720 = frozenset([63, 64])
    FOLLOW_64_in_enumDefinition724 = frozenset([1])
    FOLLOW_69_in_parameterList735 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 70, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_parameter_in_parameterList739 = frozenset([63, 70])
    FOLLOW_63_in_parameterList742 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_parameter_in_parameterList744 = frozenset([63, 70])
    FOLLOW_70_in_parameterList751 = frozenset([1])
    FOLLOW_typeName_in_parameter762 = frozenset([1, 30, 61, 86, 87, 88])
    FOLLOW_storageLocation_in_parameter764 = frozenset([1, 30, 61, 88])
    FOLLOW_identifier_in_parameter767 = frozenset([1])
    FOLLOW_69_in_eventParameterList779 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 70, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_eventParameter_in_eventParameterList783 = frozenset([63, 70])
    FOLLOW_63_in_eventParameterList786 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_eventParameter_in_eventParameterList788 = frozenset([63, 70])
    FOLLOW_70_in_eventParameterList795 = frozenset([1])
    FOLLOW_typeName_in_eventParameter806 = frozenset([1, 13, 30, 61, 88])
    FOLLOW_IndexedKeyword_in_eventParameter808 = frozenset([1, 30, 61, 88])
    FOLLOW_identifier_in_eventParameter811 = frozenset([1])
    FOLLOW_69_in_functionTypeParameterList823 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 70, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_functionTypeParameter_in_functionTypeParameterList827 = frozenset([63, 70])
    FOLLOW_63_in_functionTypeParameterList830 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_functionTypeParameter_in_functionTypeParameterList832 = frozenset([63, 70])
    FOLLOW_70_in_functionTypeParameterList839 = frozenset([1])
    FOLLOW_typeName_in_functionTypeParameter850 = frozenset([1, 86, 87, 88])
    FOLLOW_storageLocation_in_functionTypeParameter852 = frozenset([1])
    FOLLOW_typeName_in_variableDeclaration864 = frozenset([30, 61, 86, 87, 88])
    FOLLOW_storageLocation_in_variableDeclaration866 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_variableDeclaration869 = frozenset([1])
    FOLLOW_elementaryTypeName_in_typeName881 = frozenset([1, 81])
    FOLLOW_userDefinedTypeName_in_typeName885 = frozenset([1, 81])
    FOLLOW_mapping_in_typeName889 = frozenset([1, 81])
    FOLLOW_functionTypeName_in_typeName893 = frozenset([1, 81])
    FOLLOW_80_in_typeName897 = frozenset([16])
    FOLLOW_PayableKeyword_in_typeName899 = frozenset([1, 81])
    FOLLOW_81_in_typeName903 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 82, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_typeName905 = frozenset([82])
    FOLLOW_82_in_typeName908 = frozenset([1, 81])
    FOLLOW_identifier_in_userDefinedTypeName921 = frozenset([1, 83])
    FOLLOW_83_in_userDefinedTypeName925 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_userDefinedTypeName927 = frozenset([1, 83])
    FOLLOW_84_in_mapping941 = frozenset([69])
    FOLLOW_69_in_mapping943 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_elementaryTypeName_in_mapping945 = frozenset([85])
    FOLLOW_85_in_mapping947 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_typeName_in_mapping949 = frozenset([70])
    FOLLOW_70_in_mapping951 = frozenset([1])
    FOLLOW_76_in_functionTypeName962 = frozenset([69])
    FOLLOW_functionTypeParameterList_in_functionTypeName964 = frozenset([1, 7, 9, 11, 14, 15, 16, 77])
    FOLLOW_InternalKeyword_in_functionTypeName972 = frozenset([1, 7, 9, 11, 14, 15, 16, 77])
    FOLLOW_ExternalKeyword_in_functionTypeName976 = frozenset([1, 7, 9, 11, 14, 15, 16, 77])
    FOLLOW_stateMutability_in_functionTypeName980 = frozenset([1, 7, 9, 11, 14, 15, 16, 77])
    FOLLOW_77_in_functionTypeName991 = frozenset([69])
    FOLLOW_functionTypeParameterList_in_functionTypeName993 = frozenset([1])
    FOLLOW_set_in_storageLocation0 = frozenset([1])
    FOLLOW_set_in_stateMutability0 = frozenset([1])
    FOLLOW_62_in_block1048 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 64, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_statement_in_block1050 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 64, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_64_in_block1053 = frozenset([1])
    FOLLOW_ifStatement_in_statement1064 = frozenset([1])
    FOLLOW_whileStatement_in_statement1070 = frozenset([1])
    FOLLOW_forStatement_in_statement1076 = frozenset([1])
    FOLLOW_block_in_statement1082 = frozenset([1])
    FOLLOW_inlineAssemblyStatement_in_statement1088 = frozenset([1])
    FOLLOW_doWhileStatement_in_statement1094 = frozenset([1])
    FOLLOW_continueStatement_in_statement1100 = frozenset([1])
    FOLLOW_breakStatement_in_statement1106 = frozenset([1])
    FOLLOW_returnStatement_in_statement1112 = frozenset([1])
    FOLLOW_throwStatement_in_statement1118 = frozenset([1])
    FOLLOW_emitStatement_in_statement1124 = frozenset([1])
    FOLLOW_simpleStatement_in_statement1130 = frozenset([1])
    FOLLOW_expression_in_expressionStatement1141 = frozenset([50])
    FOLLOW_50_in_expressionStatement1143 = frozenset([1])
    FOLLOW_89_in_ifStatement1154 = frozenset([69])
    FOLLOW_69_in_ifStatement1156 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_ifStatement1158 = frozenset([70])
    FOLLOW_70_in_ifStatement1160 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_statement_in_ifStatement1162 = frozenset([1, 90])
    FOLLOW_90_in_ifStatement1166 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_statement_in_ifStatement1168 = frozenset([1])
    FOLLOW_91_in_whileStatement1182 = frozenset([69])
    FOLLOW_69_in_whileStatement1184 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_whileStatement1186 = frozenset([70])
    FOLLOW_70_in_whileStatement1188 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_statement_in_whileStatement1190 = frozenset([1])
    FOLLOW_variableDeclarationStatement_in_simpleStatement1203 = frozenset([1])
    FOLLOW_expressionStatement_in_simpleStatement1207 = frozenset([1])
    FOLLOW_72_in_forStatement1220 = frozenset([69])
    FOLLOW_69_in_forStatement1222 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 50, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_simpleStatement_in_forStatement1226 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 50, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_50_in_forStatement1230 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 50, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expressionStatement_in_forStatement1236 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 70, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_50_in_forStatement1240 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 70, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_forStatement1244 = frozenset([70])
    FOLLOW_70_in_forStatement1247 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_statement_in_forStatement1249 = frozenset([1])
    FOLLOW_92_in_inlineAssemblyStatement1260 = frozenset([5, 62])
    FOLLOW_StringLiteral_in_inlineAssemblyStatement1262 = frozenset([5, 62])
    FOLLOW_assemblyBlock_in_inlineAssemblyStatement1265 = frozenset([1])
    FOLLOW_93_in_doWhileStatement1276 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_statement_in_doWhileStatement1278 = frozenset([91])
    FOLLOW_91_in_doWhileStatement1280 = frozenset([69])
    FOLLOW_69_in_doWhileStatement1282 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_doWhileStatement1284 = frozenset([70])
    FOLLOW_70_in_doWhileStatement1286 = frozenset([50])
    FOLLOW_50_in_doWhileStatement1288 = frozenset([1])
    FOLLOW_ContinueKeyword_in_continueStatement1299 = frozenset([50])
    FOLLOW_50_in_continueStatement1301 = frozenset([1])
    FOLLOW_BreakKeyword_in_breakStatement1312 = frozenset([50])
    FOLLOW_50_in_breakStatement1314 = frozenset([1])
    FOLLOW_94_in_returnStatement1325 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 50, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_returnStatement1327 = frozenset([50])
    FOLLOW_50_in_returnStatement1330 = frozenset([1])
    FOLLOW_95_in_throwStatement1341 = frozenset([50])
    FOLLOW_50_in_throwStatement1343 = frozenset([1])
    FOLLOW_96_in_emitStatement1354 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_functionCall_in_emitStatement1356 = frozenset([50])
    FOLLOW_50_in_emitStatement1358 = frozenset([1])
    FOLLOW_97_in_variableDeclarationStatement1371 = frozenset([69])
    FOLLOW_identifierList_in_variableDeclarationStatement1373 = frozenset([50, 57])
    FOLLOW_variableDeclaration_in_variableDeclarationStatement1377 = frozenset([50, 57])
    FOLLOW_69_in_variableDeclarationStatement1381 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 63, 69, 70, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_variableDeclarationList_in_variableDeclarationStatement1383 = frozenset([70])
    FOLLOW_70_in_variableDeclarationStatement1385 = frozenset([50, 57])
    FOLLOW_57_in_variableDeclarationStatement1391 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_variableDeclarationStatement1393 = frozenset([50])
    FOLLOW_50_in_variableDeclarationStatement1398 = frozenset([1])
    FOLLOW_variableDeclaration_in_variableDeclarationList1408 = frozenset([1, 63])
    FOLLOW_63_in_variableDeclarationList1412 = frozenset([1, 4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 63, 69, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_variableDeclaration_in_variableDeclarationList1414 = frozenset([1, 63])
    FOLLOW_69_in_identifierList1429 = frozenset([30, 61, 63, 70, 88])
    FOLLOW_identifier_in_identifierList1433 = frozenset([63])
    FOLLOW_63_in_identifierList1436 = frozenset([30, 61, 63, 70, 88])
    FOLLOW_identifier_in_identifierList1441 = frozenset([70])
    FOLLOW_70_in_identifierList1444 = frozenset([1])
    FOLLOW_set_in_elementaryTypeName0 = frozenset([1])
    FOLLOW_101_in_expression1975 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 76, 80, 81, 84, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_typeName_in_expression1977 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_69_in_expression1981 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression1983 = frozenset([70])
    FOLLOW_70_in_expression1985 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_set_in_expression1989 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression1997 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_set_in_expression2001 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2009 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_set_in_expression2013 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2021 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_108_in_expression2025 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2027 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_52_in_expression2031 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2033 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_primaryExpression_in_expression2037 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_set_in_expression2041 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_81_in_expression2051 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2053 = frozenset([82])
    FOLLOW_82_in_expression2055 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_69_in_expression2059 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 70, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_functionCallArguments_in_expression2061 = frozenset([70])
    FOLLOW_70_in_expression2063 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_83_in_expression2067 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_expression2069 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_109_in_expression2073 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2075 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_set_in_expression2079 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2091 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_set_in_expression2095 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2103 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_set_in_expression2107 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2115 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_114_in_expression2119 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2121 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_51_in_expression2125 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2127 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_115_in_expression2131 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2133 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_set_in_expression2137 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2153 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_set_in_expression2157 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2165 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_118_in_expression2169 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2171 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_119_in_expression2175 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2177 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_120_in_expression2181 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2183 = frozenset([121])
    FOLLOW_121_in_expression2185 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2187 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_set_in_expression2191 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expression2235 = frozenset([1, 51, 53, 54, 55, 56, 57, 60, 69, 81, 83, 102, 103, 104, 105, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    FOLLOW_BooleanLiteral_in_primaryExpression2248 = frozenset([1])
    FOLLOW_numberLiteral_in_primaryExpression2254 = frozenset([1])
    FOLLOW_HexLiteral_in_primaryExpression2260 = frozenset([1])
    FOLLOW_StringLiteral_in_primaryExpression2266 = frozenset([1])
    FOLLOW_identifier_in_primaryExpression2272 = frozenset([1, 81])
    FOLLOW_81_in_primaryExpression2275 = frozenset([82])
    FOLLOW_82_in_primaryExpression2277 = frozenset([1])
    FOLLOW_tupleExpression_in_primaryExpression2285 = frozenset([1])
    FOLLOW_elementaryTypeNameExpression_in_primaryExpression2291 = frozenset([1, 81])
    FOLLOW_81_in_primaryExpression2294 = frozenset([82])
    FOLLOW_82_in_primaryExpression2296 = frozenset([1])
    FOLLOW_expression_in_expressionList2309 = frozenset([1, 63])
    FOLLOW_63_in_expressionList2312 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_expressionList2314 = frozenset([1, 63])
    FOLLOW_nameValue_in_nameValueList2327 = frozenset([1, 63])
    FOLLOW_63_in_nameValueList2330 = frozenset([30, 61, 88])
    FOLLOW_nameValue_in_nameValueList2332 = frozenset([1, 63])
    FOLLOW_63_in_nameValueList2336 = frozenset([1])
    FOLLOW_identifier_in_nameValue2348 = frozenset([121])
    FOLLOW_121_in_nameValue2350 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_nameValue2352 = frozenset([1])
    FOLLOW_62_in_functionCallArguments2363 = frozenset([30, 61, 64, 88])
    FOLLOW_nameValueList_in_functionCallArguments2365 = frozenset([64])
    FOLLOW_64_in_functionCallArguments2368 = frozenset([1])
    FOLLOW_expressionList_in_functionCallArguments2374 = frozenset([1])
    FOLLOW_expression_in_functionCall2386 = frozenset([69])
    FOLLOW_69_in_functionCall2388 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 70, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_functionCallArguments_in_functionCall2390 = frozenset([70])
    FOLLOW_70_in_functionCall2392 = frozenset([1])
    FOLLOW_62_in_assemblyBlock2403 = frozenset([5, 24, 25, 26, 27, 28, 30, 61, 62, 64, 69, 72, 76, 80, 88, 89, 92, 94, 100, 132, 134, 135])
    FOLLOW_assemblyItem_in_assemblyBlock2405 = frozenset([5, 24, 25, 26, 27, 28, 30, 61, 62, 64, 69, 72, 76, 80, 88, 89, 92, 94, 100, 132, 134, 135])
    FOLLOW_64_in_assemblyBlock2408 = frozenset([1])
    FOLLOW_identifier_in_assemblyItem2419 = frozenset([1])
    FOLLOW_assemblyBlock_in_assemblyItem2425 = frozenset([1])
    FOLLOW_assemblyExpression_in_assemblyItem2431 = frozenset([1])
    FOLLOW_assemblyLocalDefinition_in_assemblyItem2437 = frozenset([1])
    FOLLOW_assemblyAssignment_in_assemblyItem2443 = frozenset([1])
    FOLLOW_assemblyStackAssignment_in_assemblyItem2449 = frozenset([1])
    FOLLOW_labelDefinition_in_assemblyItem2455 = frozenset([1])
    FOLLOW_assemblySwitch_in_assemblyItem2461 = frozenset([1])
    FOLLOW_assemblyFunctionDefinition_in_assemblyItem2467 = frozenset([1])
    FOLLOW_assemblyFor_in_assemblyItem2473 = frozenset([1])
    FOLLOW_assemblyIf_in_assemblyItem2479 = frozenset([1])
    FOLLOW_BreakKeyword_in_assemblyItem2485 = frozenset([1])
    FOLLOW_ContinueKeyword_in_assemblyItem2491 = frozenset([1])
    FOLLOW_subAssembly_in_assemblyItem2497 = frozenset([1])
    FOLLOW_numberLiteral_in_assemblyItem2503 = frozenset([1])
    FOLLOW_StringLiteral_in_assemblyItem2509 = frozenset([1])
    FOLLOW_HexLiteral_in_assemblyItem2515 = frozenset([1])
    FOLLOW_assemblyCall_in_assemblyExpression2526 = frozenset([1])
    FOLLOW_assemblyLiteral_in_assemblyExpression2530 = frozenset([1])
    FOLLOW_94_in_assemblyCall2543 = frozenset([1, 69])
    FOLLOW_80_in_assemblyCall2547 = frozenset([1, 69])
    FOLLOW_100_in_assemblyCall2551 = frozenset([1, 69])
    FOLLOW_identifier_in_assemblyCall2555 = frozenset([1, 69])
    FOLLOW_69_in_assemblyCall2561 = frozenset([5, 24, 27, 28, 30, 61, 63, 70, 80, 88, 94, 100])
    FOLLOW_assemblyExpression_in_assemblyCall2563 = frozenset([63, 70])
    FOLLOW_63_in_assemblyCall2568 = frozenset([5, 24, 27, 28, 30, 61, 80, 88, 94, 100])
    FOLLOW_assemblyExpression_in_assemblyCall2570 = frozenset([63, 70])
    FOLLOW_70_in_assemblyCall2575 = frozenset([1])
    FOLLOW_132_in_assemblyLocalDefinition2589 = frozenset([30, 61, 69, 88])
    FOLLOW_assemblyIdentifierOrList_in_assemblyLocalDefinition2591 = frozenset([1, 133])
    FOLLOW_133_in_assemblyLocalDefinition2595 = frozenset([5, 24, 27, 28, 30, 61, 80, 88, 94, 100])
    FOLLOW_assemblyExpression_in_assemblyLocalDefinition2597 = frozenset([1])
    FOLLOW_assemblyIdentifierOrList_in_assemblyAssignment2611 = frozenset([133])
    FOLLOW_133_in_assemblyAssignment2613 = frozenset([5, 24, 27, 28, 30, 61, 80, 88, 94, 100])
    FOLLOW_assemblyExpression_in_assemblyAssignment2615 = frozenset([1])
    FOLLOW_identifier_in_assemblyIdentifierOrList2626 = frozenset([1])
    FOLLOW_69_in_assemblyIdentifierOrList2630 = frozenset([30, 61, 88])
    FOLLOW_assemblyIdentifierList_in_assemblyIdentifierOrList2632 = frozenset([70])
    FOLLOW_70_in_assemblyIdentifierOrList2634 = frozenset([1])
    FOLLOW_identifier_in_assemblyIdentifierList2645 = frozenset([1, 63])
    FOLLOW_63_in_assemblyIdentifierList2649 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_assemblyIdentifierList2651 = frozenset([1, 63])
    FOLLOW_134_in_assemblyStackAssignment2665 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_assemblyStackAssignment2667 = frozenset([1])
    FOLLOW_identifier_in_labelDefinition2678 = frozenset([121])
    FOLLOW_121_in_labelDefinition2680 = frozenset([1])
    FOLLOW_135_in_assemblySwitch2691 = frozenset([5, 24, 27, 28, 30, 61, 80, 88, 94, 100])
    FOLLOW_assemblyExpression_in_assemblySwitch2693 = frozenset([1, 136, 137])
    FOLLOW_assemblyCase_in_assemblySwitch2695 = frozenset([1, 136, 137])
    FOLLOW_136_in_assemblyCase2707 = frozenset([5, 24, 27, 28, 30, 61, 80, 88, 94, 100])
    FOLLOW_assemblyLiteral_in_assemblyCase2709 = frozenset([5, 62])
    FOLLOW_assemblyBlock_in_assemblyCase2711 = frozenset([1])
    FOLLOW_137_in_assemblyCase2717 = frozenset([5, 62])
    FOLLOW_assemblyBlock_in_assemblyCase2719 = frozenset([1])
    FOLLOW_76_in_assemblyFunctionDefinition2730 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_assemblyFunctionDefinition2732 = frozenset([69])
    FOLLOW_69_in_assemblyFunctionDefinition2734 = frozenset([30, 61, 70, 88])
    FOLLOW_assemblyIdentifierList_in_assemblyFunctionDefinition2736 = frozenset([70])
    FOLLOW_70_in_assemblyFunctionDefinition2739 = frozenset([5, 62, 138])
    FOLLOW_assemblyFunctionReturns_in_assemblyFunctionDefinition2745 = frozenset([5, 62])
    FOLLOW_assemblyBlock_in_assemblyFunctionDefinition2748 = frozenset([1])
    FOLLOW_138_in_assemblyFunctionReturns2761 = frozenset([30, 61, 88])
    FOLLOW_assemblyIdentifierList_in_assemblyFunctionReturns2763 = frozenset([1])
    FOLLOW_72_in_assemblyFor2776 = frozenset([5, 24, 27, 28, 30, 61, 62, 80, 88, 94, 100])
    FOLLOW_assemblyBlock_in_assemblyFor2780 = frozenset([5, 24, 27, 28, 30, 61, 80, 88, 94, 100])
    FOLLOW_assemblyExpression_in_assemblyFor2784 = frozenset([5, 24, 27, 28, 30, 61, 80, 88, 94, 100])
    FOLLOW_assemblyExpression_in_assemblyFor2792 = frozenset([5, 24, 27, 28, 30, 61, 62, 80, 88, 94, 100])
    FOLLOW_assemblyBlock_in_assemblyFor2796 = frozenset([5, 62])
    FOLLOW_assemblyExpression_in_assemblyFor2800 = frozenset([5, 62])
    FOLLOW_assemblyBlock_in_assemblyFor2804 = frozenset([1])
    FOLLOW_89_in_assemblyIf2815 = frozenset([5, 24, 27, 28, 30, 61, 80, 88, 94, 100])
    FOLLOW_assemblyExpression_in_assemblyIf2817 = frozenset([5, 62])
    FOLLOW_assemblyBlock_in_assemblyIf2819 = frozenset([1])
    FOLLOW_set_in_assemblyLiteral0 = frozenset([1])
    FOLLOW_92_in_subAssembly2853 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_subAssembly2855 = frozenset([5, 62])
    FOLLOW_assemblyBlock_in_subAssembly2857 = frozenset([1])
    FOLLOW_69_in_tupleExpression2868 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 63, 69, 70, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_tupleExpression2872 = frozenset([63, 70])
    FOLLOW_63_in_tupleExpression2877 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 63, 69, 70, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_tupleExpression2879 = frozenset([63, 70])
    FOLLOW_70_in_tupleExpression2887 = frozenset([1])
    FOLLOW_81_in_tupleExpression2893 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 82, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_tupleExpression2897 = frozenset([63, 82])
    FOLLOW_63_in_tupleExpression2901 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_tupleExpression2903 = frozenset([63, 82])
    FOLLOW_82_in_tupleExpression2911 = frozenset([1])
    FOLLOW_elementaryTypeName_in_elementaryTypeNameExpression2922 = frozenset([1])
    FOLLOW_set_in_numberLiteral2933 = frozenset([1, 29])
    FOLLOW_NumberUnit_in_numberLiteral2941 = frozenset([1])
    FOLLOW_set_in_identifier2953 = frozenset([1])
    FOLLOW_storageLocation_in_synpred61_sol764 = frozenset([1])
    FOLLOW_81_in_synpred76_sol903 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 82, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred76_sol905 = frozenset([82])
    FOLLOW_82_in_synpred76_sol908 = frozenset([1])
    FOLLOW_83_in_synpred77_sol925 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_synpred77_sol927 = frozenset([1])
    FOLLOW_InternalKeyword_in_synpred78_sol972 = frozenset([1])
    FOLLOW_stateMutability_in_synpred80_sol980 = frozenset([1])
    FOLLOW_90_in_synpred99_sol1166 = frozenset([4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 72, 76, 80, 81, 84, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_statement_in_synpred99_sol1168 = frozenset([1])
    FOLLOW_variableDeclarationStatement_in_synpred100_sol1203 = frozenset([1])
    FOLLOW_69_in_synpred125_sol1981 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred125_sol1983 = frozenset([70])
    FOLLOW_70_in_synpred125_sol1985 = frozenset([1])
    FOLLOW_set_in_synpred135_sol2041 = frozenset([1])
    FOLLOW_81_in_synpred136_sol2051 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred136_sol2053 = frozenset([82])
    FOLLOW_82_in_synpred136_sol2055 = frozenset([1])
    FOLLOW_69_in_synpred137_sol2059 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 62, 69, 70, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_functionCallArguments_in_synpred137_sol2061 = frozenset([70])
    FOLLOW_70_in_synpred137_sol2063 = frozenset([1])
    FOLLOW_83_in_synpred138_sol2067 = frozenset([30, 61, 88])
    FOLLOW_identifier_in_synpred138_sol2069 = frozenset([1])
    FOLLOW_109_in_synpred139_sol2073 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred139_sol2075 = frozenset([1])
    FOLLOW_set_in_synpred142_sol2079 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred142_sol2091 = frozenset([1])
    FOLLOW_set_in_synpred144_sol2095 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred144_sol2103 = frozenset([1])
    FOLLOW_set_in_synpred146_sol2107 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred146_sol2115 = frozenset([1])
    FOLLOW_114_in_synpred147_sol2119 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred147_sol2121 = frozenset([1])
    FOLLOW_51_in_synpred148_sol2125 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred148_sol2127 = frozenset([1])
    FOLLOW_115_in_synpred149_sol2131 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred149_sol2133 = frozenset([1])
    FOLLOW_set_in_synpred153_sol2137 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred153_sol2153 = frozenset([1])
    FOLLOW_set_in_synpred155_sol2157 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred155_sol2165 = frozenset([1])
    FOLLOW_118_in_synpred156_sol2169 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred156_sol2171 = frozenset([1])
    FOLLOW_119_in_synpred157_sol2175 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred157_sol2177 = frozenset([1])
    FOLLOW_120_in_synpred158_sol2181 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred158_sol2183 = frozenset([121])
    FOLLOW_121_in_synpred158_sol2185 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred158_sol2187 = frozenset([1])
    FOLLOW_set_in_synpred169_sol2191 = frozenset([4, 5, 17, 18, 19, 20, 21, 23, 24, 27, 28, 30, 51, 52, 53, 54, 55, 56, 57, 61, 69, 80, 81, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    FOLLOW_expression_in_synpred169_sol2235 = frozenset([1])
    FOLLOW_identifier_in_synpred185_sol2419 = frozenset([1])
    FOLLOW_assemblyExpression_in_synpred187_sol2431 = frozenset([1])
    FOLLOW_numberLiteral_in_synpred199_sol2503 = frozenset([1])
    FOLLOW_StringLiteral_in_synpred200_sol2509 = frozenset([1])
    FOLLOW_69_in_synpred207_sol2561 = frozenset([5, 24, 27, 28, 30, 61, 63, 70, 80, 88, 94, 100])
    FOLLOW_assemblyExpression_in_synpred207_sol2563 = frozenset([63, 70])
    FOLLOW_63_in_synpred207_sol2568 = frozenset([5, 24, 27, 28, 30, 61, 80, 88, 94, 100])
    FOLLOW_assemblyExpression_in_synpred207_sol2570 = frozenset([63, 70])
    FOLLOW_70_in_synpred207_sol2575 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("solLexer", solParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
