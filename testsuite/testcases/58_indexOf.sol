
contract IndexOf1 {

    address creator;

    function LIndexOf()
    {
        creator = msg.sender;
    }
    
    int whatwastheval = -10; // -2 = not yet tested, as separate from -1, tested but error
    
    function indexOf(string _a, string _b) returns (int) // _a = string to search, _b = string we want to find
    {
    	bytes memory a = bytes(_a);  
        bytes memory b = bytes(_b);
       
    	if(a.length < 1)
    	{
    		whatwastheval = -1;
    		return -1;
    	}
    	else
    	{
    		whatwastheval = -1;
    		return -1;									
    	}

    }
    
    function whatWasTheVal() constant returns (int)
    {
    	return whatwastheval;
    }
    
    /**********
     Standard kill() function to recover funds 
     **********/
    
    function kill()
    { 
        if (msg.sender == creator)
        {
            suicide(creator);  // kills this contract and sends remaining funds back to creator
        }
    }
}