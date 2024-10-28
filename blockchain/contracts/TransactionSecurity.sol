pragma solidity ^0.8.0;

contract TransactionSecurity {
    event TransactionRecorded(address indexed from, address indexed to, uint256 amount, uint256 timestamp);

    function recordTransaction(address to, uint256 amount) public {
        emit TransactionRecorded(msg.sender, to, amount, block.timestamp);
    }
}
