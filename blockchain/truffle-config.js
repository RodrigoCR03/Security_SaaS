module.exports = {
    networks: {
      development: {
        host: "127.0.0.1",
        port: 8545, // Porta do Ganache ou outro cliente Ethereum
        network_id: "*" // Qualquer network id
      }
    },
    compilers: {
      solc: {
        version: "0.8.0", // Versão do Solidity
        settings: {
          optimizer: {
            enabled: true,
            runs: 200
          }
        }
      }
    }
  };
  