const em = artifacts.require("energymeter");

module.exports = function (deployer) {
  deployer.deploy(em);
};
