const IdentityManagement = artifacts.require("IdentityManagement");
const TransactionSecurity = artifacts.require("TransactionSecurity");

module.exports = function(deployer) {
  deployer.deploy(IdentityManagement);
  deployer.deploy(TransactionSecurity);
};
