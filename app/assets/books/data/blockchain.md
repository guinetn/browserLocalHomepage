# BLOCKCHAIN: trust redefined

Decentralized ledger system providing secure and permanent records (transactions).
Blockchain help when dealing with transactional data

Network of nodes working on consensus and trust
All the functionality/applications work using complex algorithms and cryptography.

Blockchain is a system of recording information in a way that makes it difficult or impossible to change, hack, or cheat the system.

“Picture a spreadsheet that is duplicated thousands of times across a network of computers. Then imagine that this network is designed to regularly update this spreadsheet and you have a basic understanding of the blockchain.”

### Blockchain's Promises
* no downtime, no error or lost records. On traditional server architectures, if a single app is compromised or goes offline, many users and other apps are affected.
* no censorship, transparent, safe, auditable, no fraud: multi-source identification
* no third-party interference. By tokenizing the process and eliminating any middlemen

### Blockchain's applications
...

### Smart Contracts

A smart contract is a self-executing contract with the terms of the agreement between buyer and seller being directly written into lines of code. Smart contracts are simply programs stored on a blockchain that run when predetermined conditions are met.


Program complex logic and functionality without any constraints in terms of industry.
Implement functionality 
By releasing assets on single/multiple chains 
Based on the business logic and architecture
WHEN 
Fixed and acknowledged contractual clauses are fulfilled, or fail to fulfill.


### Node
A node is an instance or the most basic element of a node-based P2P network.
Blockchain based networks are P2P network in nature

### Block
Ledger unit
Register transaction records with corresponding transaction hashes with all the data being open and transparent for all the nodes to be accessed and synchronized with. 
Blocks can be referred to using their height in the chain. 
A collection of time synchronized and linked blocks essentially forms the blockchain.
Blockchain generation rates: new block being generated in every x seconds.

### Transaction
Traditional transactions: transmission of financial assets and goods. 
Blockchain transaction: transfer of data/message between two nodes of the blockchain network
Has a transaction hash used to find out details regarding the particular transaction.

# Ethereum Blockchain
https://ethereum.org/en/
Ethereum is a decentralized, open-source blockchain with smart contract functionality. Ether (ETH) is the native cryptocurrency of the platform. Ethereum is the community-run technology powering the cryptocurrency, ether (ETH), and thousands of decentralized applications.

# Alchemy 
https://www.alchemy.com/
A blockchain developer platform and API that allows us to communicate with ethereum chain without running our own nodes. It's an awesome platform and will get you started with Ethereum blockchain development in no time at all.

```js
const SHA256 = require("crypto-js/sha256");

// BLOCK
class Block {
    constructor(index, timestamp, data, previousHash = '') {
        this.index = index;
        this.previousHash = previousHash;
        this.timestamp = timestamp;
        this.data = data;
        this.hash = this.calculateHash(); // link to previous, date, data, salt
        this.nonce = 0;
    }

    calculateHash() {
        return SHA256(this.index + this.previousHash + this.timestamp + JSON.stringify(this.data) + this.nonce).toString();
    }

    mineBlock(difficulty) {
        // Proof of work = energy 
        while (this.hash.substring(0, difficulty) !== Array(difficulty + 1).join("0")) {
            this.nonce++;
            this.hash = this.calculateHash();
        }

        console.log("BLOCK MINED: " + this.hash);
    }
}

// Ledger
class Blockchain{
    constructor() {
        this.chain = [this.createGenesisBlock()];
        this.difficulty = 5;
    }

    createGenesisBlock() {
        const index = 0;
        const timestamp = new Date().toLocaleDateString(); // "01/01/2021" 
        // Better: new Date().toISOString() → "2021-01-01T08:00:00.225Z"
        const data = "Genesis block";
        const previousHash = '0';
        return new Block(index, timestamp, data, previousHash);
    }

    getLatestBlock() {
        return this.chain[this.chain.length - 1];
    }

    addBlock(newBlock) {
        newBlock.previousHash = this.getLatestBlock().hash;
        newBlock.mineBlock(this.difficulty);
        this.chain.push(newBlock);
    }

    isChainValid() {
        for (let i = 1; i < this.chain.length; i++){
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i - 1];

            if (currentBlock.hash !== currentBlock.calculateHash()) {
                return false;
            }

            if (currentBlock.previousHash !== previousBlock.hash) {
                return false;
            }
        }

        return true;
    }
}

let saveCoin = new Blockchain();
console.log('Mining block 1...');
saveCoin.addBlock(new Block(1, "01/01/2021", { amount: 4 }));

console.log('Mining block 2...');
saveCoin.addBlock(new Block(2, "01/01/2021", { amount: 8 }));
```



## More

- https://www.youtube.com/watch?v=_160oMzblY8  ★★★
- https://python.plainenglish.io/create-your-own-cryptocurrency-blockchain-in-python-3-9-4-806f8825608e
- https://gist.github.com/bryandijkhuizen/c681fe0f554e707ad846188d86a23366#file-fullcodeblock-chain-py
- https://www.youtube.com/watch?v=coQ5dg8wM2o