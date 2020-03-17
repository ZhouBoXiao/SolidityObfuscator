
//pragma solidity >=0.4.22 <0.6.0;
//import "mortal";
//import a as b from "mor";
//import a as b, c as d from "mortal"
// contract Descriptor {
    
// 	function getDescription() constant returns (uint16[3]){	
// 		uint16[3] somevar;
// 		return somevar;
// 	}
// }

contract ArrayPasser is mortal {

    //using we for *;
    //using er for asd;
    //constructor(int memory a, uint b) pure{
    //    int a = b + 1 + (c++ + 1 );
    //}
    //enum aea{
    //        QWE,
    //        WEQERWQ
    //    }

    //modifier onlyOwner (int a){
    //    if (msg.sender != owner)
    //        throw;
    //    _;
    //}
    address creator;
    
    /***
     * 1. Declare a 3x3 map of Tiles
     ***/
    uint8 mapsize = 3;

    event da(int indexed a, string b) anonymous;
    struct Tile 
    {
        /***
         * 2. A tile is comprised of the owner, elevation and a pointer to a 
         *      contract that explains what the tile looks like
         ****/
        uint8 elevation;
        //Descriptor descriptor;
    }
    Tile[3][3] tiles;
    event  ad(int indexed a) anonymous;
    /***
     * 3. Upon construction, initialize the internal map elevations.
     *      The Descriptors start uninitialized.
     ***/
    function ArrayPasser(uint8[9] incmap, string memory q) pure  returns (uint)
    {


        break;
        //baddress = new ReplicatorB();
        blockCreatedOn = block.number;
        continue;
        emit ArrayPasser(c, d);
        do{
            a = 1;
        }while(a>1);
        while(a>1){
            a = 2;
        }
        creator = msg.sender;
        uint8 counter = 0;
        if (counter==0){
            return 1;
        }else {
            return 11;
        }
        for(uint8 y = 0; y < mapsize; y++)
       	{
           	for(uint8 x = 0; x < mapsize; x++)
           	{
           		//tiles[x][y].elevation = incmap[counter];
           		counter = counter + 1;
           	}	
        }	
    }
   
    /***
     * 4. After contract mined, check the map elevations
     ***/
    function getElevations() constant returns (uint8[3][3])
    {
        uint8[3][3] memory elevations;
        for(uint8 y = 0; y < mapsize; y++)
        {
        	for(uint8 x = 0; x < mapsize; x++)
        	{
        		elevations[x][y] = tiles[x][y].elevation; 
        	}	
        }	
    	return elevations;
    }
}