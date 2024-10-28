pragma solidity ^0.8.0;

contract IdentityManagement {
    mapping(address => string) private identities;

    event IdentityRegistered(address indexed user, string data);

    function registerIdentity(string memory data) public {
        identities[msg.sender] = data;
        emit IdentityRegistered(msg.sender, data);
    }

    function getIdentity(address user) public view returns (string memory) {
        return identities[user];
    }
}
