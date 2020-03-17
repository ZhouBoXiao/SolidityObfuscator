
opt=-Xmx1024m 
jar=../thirdparty/antlr-3.1.3.jar
gramfile=Solidity
ending=.g 
antlropt=-Xconversiontimeout 200000 
outputdir=./parser


$(outputdir)/$(gramfile)Parser.py: $(gramfile)$(ending)
	java $(opt) -jar $(jar) $(gramfile)$(ending) $(antlropt) -o $(outputdir)


force: 
	@touch $(gramfile)$(ending)
	@$(MAKE)


clean:
	find ./ -name "*.pyo" -exec rm  \{\} \;
	find ./ -name "*.pyc" -exec rm  \{\} \;
	find ./ -name "*~" -exec rm  \{\} \;
	rm -f *~ $(outputdir)/$(gramfile)Lexer.py *.pyc $(outputdir)/$(gramfile)Parser.py *.o $(outputdir)/*.tokens 

antlr4:
	java -jar ../thirdparty/antlr-4.7.2-complete.jar -Dlanguage=Python2 Solidity.g4 -o solidityobf\parser


