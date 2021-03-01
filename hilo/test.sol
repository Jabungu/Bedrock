pragma solidity ^0.7.4;

contract UserRegistration {

    struct User {
        address addr;
        uint id;
        string FirstName;
        string LastName;
        string Address1;
        string Address2;
        string City;
        string State;
        uint Zip;
        string Country;
    }

    mapping(address => User) users;

    uint public userCount;

    function addUser(address addr, uint _id, string memory _FirstName, string memory _LastName, string memory _Address1, string memory _Address2, string memory _City, string memory _State, uint _Zip, string memory _Country) public {
        
        users[msg.sender] = User(addr, _id, _FirstName, _LastName, _Address1, _Address2, _City, _State, _Zip, _Country);
    }
    function findUser(uint _id) public {

        address[1];
    }
}


// contract Login {

    


    
    



// }
// contract StatusReport {
//     bool WaterOn;
//     bool ElectricityOn;
//     string ElectricityProvider;
//     bool InternetOn;
//     string InternetProvider;

// }