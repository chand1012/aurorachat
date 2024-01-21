---
cover: .gitbook/assets/Gitbook - Cover Image (8).png
coverY: 0
---

# 🖖 Welcome

<figure><img src=".gitbook/assets/gogopool_cover.jpeg" alt=""><figcaption></figcaption></figure>

## What is GoGoPool?

GoGoPool is the first permissionless staking protocol built for [Avalanche Subnets](https://docs.avax.network/subnets), allowing node operators to launch validators cheaper and faster using the GGP token. Currently, we cater to node operators and liquid stakers.

### With GoGoPool, a node operator can:

* Launch their node for 1000 AVAX + 100 AVAX in GGP tokens, nearly half the price of the traditional avenue!
* Earn rewards on their staked AVAX, their staked GGP, and an operating fee for running a node.
* Become a validator with just a few clicks.

Start your minipool today: [app.gogopool.com/create-minipool](https://app.gogopool.com/create-minipool)

### For liquid stakers, we offer:

* Affordable staking for as little as .01 AVAX.

* A token, ggAVAX, to provide instant liquidity that accrues value overtime.

---
description: Overview on how GoGoPool works
---

# GoGoPool Mechanics Overview

GoGoPool's core mechanics revolve around the concept of a Minipool. This term was originally coined by RocketPool, which GoGoPool is based on.  A GoGoPool Minipool represents a validator that was funded via AVAX contributed from liquid stakers using the deposit pool and AVAX contributed from node operators during their registration with GoGoPool.

To become a validator on Avalanche, the current requirement is 2000 AVAX. With GoGoPool's Minipool design, the upfront cost for node operators drops to 1100 AVAX. Learn more about how Minipools work [here](../how-minipools-work/).

The 2000 AVAX requirement is met through sourcing 1000 AVAX from GoGoPool's liquid stakers. Learn more about liquid staking works [here](../how-liquid-staking-works/).

To ensure good behavior and collateralize the AVAX the node operators are borrowing from the liquid staker's deposit pool, node operators stake at least 100 AVAX worth of GGP.

Because they are staking GGP, they also have an opportunity to earn monthly GGP rewards. Learn more about the GGP rewards cycle [here](../how-minipools-work/ggp-rewards.md).\
\
If a validator fails to get rewarded by Avalanche, then the node operator's staked GGP gets slashed to make up for the liquid staker's loss of rewards.\
\
The protocol operates with two DAOs. The ProtocolDAO, which is tasked with the longterm sustainability of the protocol and is goverened with the GGP token. And the OracleDAO which is tasked with handling offchian interactions. Learn more about the two DAOs here (coming soon).

# How Liquid Staking Works

<figure><img src="../../.gitbook/assets/liquid_staking_illu.png" alt=""><figcaption></figcaption></figure>

## Overview

When a user liquid stakes with GoGoPool, their $AVAX goes directly towards growing the Avalanche network and getting more subnets and validators launched.\
\
Their AVAX is staked into a deposit pool. These deposit pool funds are used to match with node operators who want to become a validator for Avalanche's primary network. To learn more about how Avalanche utilizes proof-of-stake validation, check out [Avalanche's official documentation](https://www.avax.network/proof-of-stake-pos).\
\
Every Subnet requires validators to operate, and every Subnet validator must also validate the Avalanche Primary network. Currently, there is no cohesive way for Subnets in need of validators and validators who want to validate Subnets to get in contact.

GoGoPool aims to solve this by incentivizing node operators to run through the protocol, in order to create a set of validators that are oriented towards helping Subnets. Our community of Liquid Stakers is essential for this mission to succeed.

## What is ggAVAX and what can users do with it?

[ggAVAX is an ERC4626](../../gogopooldesign/ggpavax-via-erc-4626.md). When users stake AVAX, ggAVAX is minted and given to them in exchange.&#x20;

This token is considered liquid and can be used like AVAX whereby users can hold it to accrue staking rewards, sell it, or use it to earn additional yield.&#x20;

## What happens to the user's staked AVAX?

When a user deposits AVAX as a liquid staker on GoGoPool, their AVAX gets staked to the TokenggAVAX contract, this is also known as the deposit pool. Each time a new Minipool is launched, 1000 AVAX is withdrawn from this contract (code reference).

Together with the Minipool owner's staked 1000 AVAX, Avalanche's minimum 2000 AVAX requirement is met for the Minipool to become a validator. GoGoPool's advanced multisig technology transfers those funds from the C-chain to the P-chain and registers the minipool as a validator with Avalanche.

Every 15 days a Minipool finishes its validation period. At this time, the Minipool funds and the rewards it earned from validating are transferred back to the C-chain. Because the 1000 AVAX  from the deposit pool did work by validating, it gets part of the rewards the Minipool earned from Avalanche. Those rewards and the original 1000 AVAX are put back into the deposit pool. Over time as the deposit pool grows due to the rewards it has earned and ggAVAX accrues value.

## What happens when ggAVAX is redeemed for AVAX?

When funds are available in the pool, ggAVAX holders can swap their ggAVAX for AVAX.

However, if all funds in the pool are validating on-chain in a Minipool, users must wait until a Minipool has completed before swapping. Once a user successfully redeems their ggAVAX for AVAX, the ggAVAX is burned.

# The Life of a Minipool

1. The minipool gets created by the node operator.&#x20;
2. The minipool is put in a queue to be matched with liquid staking funds
3. The OracleDAO transfers 2000 AVAX (1000 AVAX from the deposit pool and 1000 AVAX from the node operator) from the C-chain to the P-chain to be staked.
4. The OracleDAO registers the minipool with Avalanche as a validator for 15 days and stakes the joint 2000 AVAX.
5. At the end of 15 days, the OracleDAO transfers the funds back to the C-chain.
6. The liquid staking funds (1000 AVAX) and their accompanying rewards are then deposited back into the deposit pool.
7. If the minipool has more time on its duration, then the protocol will recreate the minipool for another 15-day cycle. The recreated minipool will utilize the rewards that the first cycle earned, to compound long-term gains.
8. The original funds from the deposit pool from #6 are withdrawn again and pooled together with the mirrored amount from the node operator's funds and their rewards.
9.

The OracleDAO once again transfers the joint funds (more than 2000 AVAX this time) from the C-chain to the P-chain to stake and registers the minipool as a validator for 15 days. This process will repeat for the full duration of the minipool.
10. Once the full duration of the minipool has been fulfilled, the node operator will be able to withdraw their funds and rewards.

Additionally, a GGP rewards cycle is underway throughout this process, enabling node operators to earn rewards on their staked GGP. More information can be found [here](ggp-rewards.md).

# How Minipools Work

<figure><img src="../../.gitbook/assets/minipool_launch.jpeg" alt=""><figcaption></figcaption></figure>

A GoGoPool minipool represents a validator that was funded via AVAX contributed from liquid stakers using the deposit pool and AVAX contributed from node operators during their registration with GoGoPool.

## How are minipools created?

A node operator brings their NodeId to GoGoPool and registers with it. This indicates that they have their own hardware set up and are ready to become an Avalanche validator. For detailed instructions on setting up a node, refer to [Avalanche's official documentation](https://docs.avax.network/nodes).

To become a validator with Avalanche, a node needs 2000 AVAX. Through GoGoPool, the node operator contributes half of this amount, while the remaining half is sourced from the liquid staking deposit pool. To secure the half obtained from the deposit pool, the node operator pledges at least 100 AVAX worth of collateral in the form of GGP tokens.

This collateral serves as a commitment to good behavior and allows the protocol to recover losses in case of misconduct.

After registering their NodeId, staking 1000 AVAX, and collateralizing with GGP tokens, the node operator's[ minipool is created](https://github.com/multisig-labs/gogopool/blob/main/contracts/contract/MinipoolManager.sol#L192).

The minipool is then [matched with liquid staking funds](https://github.com/multisig-labs/gogopool/blob/main/contracts/contract/MinipoolManager.sol#L324) from the deposit pool. The OracleDAO transfers these funds from the C-chain to the P-chain for staking purposes and registers the minipool as a validator in the Avalanche network.

To ensure consistent returns for liquid stakers and compound returns for node operators, the protocol implements minipool cycling.

## What is minipool cycling?

Minipools validate in 15-day cycles. At the end of each cycle, the OracleDAO transfers the original 2000 AVAX and earned rewards back to the C-chain.

The liquid staking funds and their corresponding rewards are returned to the deposit pool for accurate growth tracking. If the protocol determines that the minipool should [undergo another cycle](https://github.com/multisig-labs/gogopool/blob/main/contracts/contract/MinipoolManager.sol#L459), the funds are once again withdrawn. These funds are [paired](https://github.com/multisig-labs/gogopool/blob/main/contracts/contract/MinipoolManager.sol#L488) with the mirrored amount from the node operator's original funds and rewards. As a result, **more than** 2000 AVAX is staked for the upcoming 15-day validation period, leading to compounded rewards for both parties involved.

# One-Click Launcher

### Minipool Streamliner Contract Documentation

The Minipool Streamliner is designed to streamline the process of participating in our staking protocol. It automates various processes, integrating with Trader Joe, ooNodz, and our native contracts for a seamless one-click solution.

**Key Functions and Workflow**

1. **Token Swaps using Trader Joe's LBRouter**:
   * The contract starts by swapping AVAX for GGP (our native token) using the LBRouter from Trader Joe.
   * It also swaps AVAX for USDC, necessary for interacting with ooNodz, which only accepts USDC for payment.
2. **Staking GGP on Behalf of the User**:
   * Once GGP is obtained through the swap, the contract stakes these tokens on behalf of the user in our staking system. This step is crucial for participating in our protocol.
3. **Node Setup with ooNodz**:
   * With USDC in hand, the contract communicates with ooNodz to set up an Avalanche node. This process includes sending USDC to ooNodz and receiving a NodeID in return.

The NodeID is essential for creating a minipool.
4. **Minipool Creation**:
   * With the GGP staked and a NodeID acquired, the contract then proceeds to the final and critical step of creating a minipool in our protocol. This is the entry point for users to begin earning rewards.

**Contract's Additional Features and Safeguards**

* **Mismatched Funds Handling**:
  * The contract includes a check to ensure that the amount of AVAX sent matches the sum required for minipool creation, GGP purchase, and node rental. If the amounts don't match, the contract reverts the transaction.
* **Swap Failure Handling**:
  * If the token swap (AVAX to GGP or AVAX to USDC) fails or doesn't meet the minimum output requirement, the contract reverts the transaction, safeguarding users from unfavorable swaps.
* **Refunding Unused USDC**:
  * In cases where there are leftover USDC funds after node setup, the contract ensures these are refunded back to the user.

* **Event Emission**:
  * The contract emits events for key actions like the creation of a new streamlined minipool and refunds of USDC, aiding in transparency and tracking.

**Conclusion**

The Minipool Streamliner contract represents a significant leap in user convenience and efficiency.

---
description: Every 30 days GGP stakers are eligible for rewards
---

# GGP Rewards

<figure><img src="../../.gitbook/assets/Rewards.png" alt=""><figcaption></figcaption></figure>

## Overview

GGP is GoGoPool's protocol token. Its utility is collateral for the 1k AVAX that node operators borrow from the protocol to launch their validator. For providing this collateral, the protocol rewards the node operator with GGP rewards generated by the inflation built into the protocol. The more GGP staked as insurance, up to a maximum of 150% of the staked AVAX's value, the more GGP rewards the node operator receives.

## How does monthly inflation work?

GGP has a fixed supply of 22.5 million. On genesis 18 million GGP were minted. Learn more about the distribution of that supply [here](../../readme-1/tokens-and-utility.md#supply-breakdown-and-vesting). This means that there are still 4.5 million tokens left to be minted. These tokens will be released to the ecosystem in the form of a monthly rewards cycle.

To start, this inflation will be 5% annually.

## What are the requirements to be eligible?

* Any one of a user's minipools has to have started validating for at least 15 days before the end of the rewards cycle.
* A user must have GGP staked at the time of the rewards calculation.

## How much is distributed each month?

It changes over time, this [spreadsheet](https://docs.google.com/spreadsheets/d/1Gjdp1rP2MrsGO9QQuia\_rjyo\_8nQm-5jNDt2vIUZMhI/edit#gid=0) can be used to get a rough estimate. Feel free to make a copy for your own use.

## How is the monthly inflation distributed?

To start, the distribution of the monthly inflation is as follows:

* 70% to Node Operators
* 10% to Oracle DAO&#x20;
* 20% to Protocol DAO Treasury

## How are individual Node Operator's rewards calculated?

Generally speaking, it is a node operator's effective GGP stake over the total effective GGP stake of all the eligible node operators for that cycle.

Where effective GGP stake is staked GGP up to the 150% collateralization ratio.

That being said, GoGoPool does have some seed investors that are running minipools, to bootstrap the protocol. Those individuals will be weighted at a lower amount than a typical node operator. This weight will grow over time, as the investor's GGP vests.\
\
GGP rewards calculator coming soon.

# Contracts

`Storage.sol` <dd>The GoGoPool smart contract architecture is based around techniques from [RocketPool](https://github.com/rocket-pool/rocketpool). The `Storage.sol` contract is non-upgradeable, and contains generic getters/setters to access it's storage. Other contracts are "registered" with the storage contract as a "Network Contract", and can then use it to read and write typed key/value pairs. In this way, other contracts can be upgraded at will, as they contain no local storage of their own. </dd>

`Vault.sol` <dd> Non-upgradeable contract used to store AVAX/ERC20 tokens on behalf of other network contracts.

Not storing value in network contracts allows them to be upgradeable.</dd>

`MultisigManager.sol` <dd>Registry of Rialto TSS (Threshold Signatures) wallets that are allowed to extract protocol funds and deploy them into yield-bearing staking transactions on the Avalanche P-chain.</dd>

`Ocyticus.sol` <dd> Protocol emergency pause feature, such that any one of a specified group of "Defenders" can pause the entire protocol should that be necessary. The Defenders will be a different set of users from Guardians, and their only permission will be the ability to call the Pause function. Only the Guardian can add and remove Defenders.</dd>

`TokenGGP.sol` <dd> Fixed-supply, non-upgradeable GGP utility token. GGP is our protocol token used to collateralize minipools and rewards Node Operators in addition to the AVAX Validation rewards.</dd>

`TokenggAVAX.sol` <dd>Upgradeable (via OpenZeppelin proxy) [ERC4626](https://eips.ethereum.org/EIPS/eip-4626) yield-bearing liquid staking token.

Additionally, the [xERC4626](https://github.com/fei-protocol/ERC4626/blob/main/src/xERC4626.sol) technique is used to stream rewards to users over a set cycle period. AVAX funds from TokenggAVAX are used by Node Operators to create a full validator from their minipool.</dd>

`Base.sol`, `BaseAbstract.sol`, `BaseUpgradeable.sol` <dd> modifiers, helper methods and storage wrapper methods. `BaseAbstract` is where the implementation lives, and it’s inherited by both `Base` and `BaseUpgradeable` to be used in standard network contracts and the proxy upgradeable `TokenggAVAX` , respectively.</dd>

`ClaimNodeOp.sol`, `ClaimProtocolDAO.sol` <dd> Two contracts for claiming inflated GGP Tokens. Multisig isn’t included here as a separate contract, we instead distribute those rewards right from `RewardsPool.sol`. </dd>

`Oracle.sol` <dd> GGP price submission from Rialto oracle.</dd>

`ProtocolDAO.sol` <dd> Maintains protocol settings used across all network contracts.

Currently all settings are controlled by the Guardian. In a future iteration will include a DAO mechanism for modifying settings.</dd>

`RewardsPool.sol` <dd> Handles GGP rewards cycles which includes inflation of new tokens and distribution of the tokens to the claiming contracts.</dd>

`Staking.sol` <dd> Access point for staking GGP. Also maintains information on Node Operators.

<dl>

**_<dt>Owner</dt>_** <dd>C-chain address creating minipools with Node IDs</dd>

**_<dt>LiquidStaker</dt>_** <dd>User who deposits AVAX in exchange for ggAVAX. The ggAVAX <-> AVAX exchange rate will increase as Staking rewards are deposited.</dd>

**_<dt>Minipool</dt>_**<dd>A pool of AVAX created by a Node Operator. After being matched with Liquid Staker funds, Rialto will withdraw all funds to stake and become a validator under the Node Operator's Node ID on Avalanche's P-chian.</dd>

**_<dt>Node Operator</dt>_** <dd>An owner of a Minipool controlling hardware. They deposit half of the AVAX required to validate.</dd>

**_<dt>Protocol DAO</dt>_** <dd>Place where Protocol settings are stored. Not a DAO yet. Probably more aptly named Protocol Settings.</dd>

**_<dt>Multisig</dt>_** <dd>A threshold multisig bridge between the C-Chain and the P-Chain. Internally referred to as Rialto.</dd>

**_<dt>Rialto</dt>_** <dd>Threshold multisig bridge for moving funds between C-Chain and P-Chain.

Calls to contracts to stake & process Minipools, start Rewards cycles, distribute GGP Rewards, etc.</dd>

**_<dt>Token GGAVAX</dt>_** <dd>Liquid Staking token. Represents staked AVAX in the protocol.</dd>

**_<dt>Token GGP</dt>_** <dd>Inflationary Protocol Token. Inflated tokens are used as rewards for Node Operators, the Protocol DAO and Rialto multisigs.

# Minipool Statuses

Each minipool is equivalent to an Avalanche validator with a NodeId

## Minipool Status Descriptions

Each Minipool has a status field

### **Prelaunch (0)**

* Minipool is created in [Storage.sol](https://github.com/multisig-labs/gogopool/blob/master/contracts/contract/Storage.sol) Key-Value data structure
* Node Operator has deposited 1K AVAX and specified duration and Avalanche NodeID. Their minipool is collateralized by atleast 10% with staked GGP.
* Can be moved to status `Canceled` by the Owner of the node after a 5 day waiting period and all AVAX returned.
* The minipool is now in a queue, and awaits getting matched with liquid staking funds.

### **Launched (1)**

* Minipool is now **locked** and cannot be canceled by the owner.
* Rialto withdraws 2K AVAX from vault to stake it on Avalanche P-chain and register the node as a validator

### **Staking (2)**

* Minipool is now validating and **locked** for the duration of the validation period.

* Nothing will happen until the duration is over and validation has ended.
* Rialto will Export/Import 2K AVAX plus any rewards back to [MinipoolManager.sol](https://github.com/multisig-labs/gogopool/blob/master/contracts/contract/MinipoolManager.sol).
* MinipoolManager.sol will handle all funds distribution to liq staking users, GGP slashing, etc, then set status to `Withdrawable`.

### **Withdrawable (3)**

* Minipool is now available for node operator funds to be withdrawn. Node operator **cannot** create a new minipol with this NodeId until they have withdrawn all AVAX funds (user's principal and staking rewards) for this minipool.
* Once withdrawal happens, the status is changed to `Finished`.

### **Finished (4)**

* Minipool is finished, all AVAX funds have been withdrawn (user's principal and staking rewards for this node).
* Node operator can now submit another validation request with us for this NodeId. We will replace all the data from the last validation with new data for this validation.

A minipool doesnt have its own `id` we always use nodeID as a primary key.

### **Canceled (5)**

* If a minipool is canceled it is set to this status. Can be resubmitted.
* A minipool can only be canceled by the owner after a 5 day waiting period. This is to prevent griefing.

### Error (6)

* Minipool failed.
* The node likely failed to be registered as a validator with Avalanche.
* Will move to the status `Finished` once the node operator withdraws their funds.

# Technical Overview

The protocol can be split into 4 components.

- [Data Separation Upgrade mechanism](#data-separation-upgrade-mechanism)
- [Liquid Staking](#liquid-staking)
- [Minipool Creation & Validation](#minipool-creating--validation)
- [Rewards](#rewards)

## Data Separation Upgrade mechanism

The protocol is designed with the ability to have upgradable contracts without fear of losing settings or funds. The storage has two, non-upgradable parts. This part of the protocol was heavily inspired by our Ethereum counterpart’s design, [Rocketpool](https://docs.rocketpool.net/developers/usage/contracts/contracts.html#introduction).

- [Storage](https://github.com/multisig-labs/gogopool-contracts/blob/master/contracts/contract/Storage.sol) (`Storage.sol`)
- [The Vault](https://github.com/multisig-labs/gogopool-contracts/blob/master/contracts/contract/Vault.sol) (`Vault.sol`)

### Storage

Storage is responsible for all persistent storage across all contracts regardless of their version.

This allows us to use it as a database of sorts, storing values based on hashed keys, and even using it to store more complex data structures (see `MinipoolManager.sol`for an example). Only contracts within the GoGoPool network can write to Storage, but anyone can read from it. The Storage contract also holds the addresses to the newest versions of our network contracts, allowing the current contracts to call one another while preventing older contracts from updating data.

### The Vault

The Vault is where funds are stored for all contracts. Storing the funds in a non-upgradable vault ensures that subsequent upgrades of the protocol do not cause a loss of funds.

## Liquid Staking

Our Liquid Staking system allows for users who lack the funds to create regular AVAX Validator nodes or GoGoPool Minipool Validators (see below) to reap rewards on their tokens. The following contracts are a part of the operation of Liquid Staking.

- [ggAVAX](https://github.com/multisig-labs/gogopool-contracts/blob/master/contracts/contract/tokens/TokenggAVAX.sol) (`TokenggAVAX.sol`)
- [Oracle](https://github.com/multisig-labs/gogopool-contracts/blob/master/contracts/contract/Oracle.sol) (`Oracle.sol`)
- [Minipool Manager](https://github.com/multisig-labs/gogopool-contracts/blob/master/contracts/contract/MinipoolManager.sol) (`MinipoolManager.sol`)

### Flow

1. Liquid stakers deposit AVAX in exchange for ggAVAX
2. When there are sufficient funds deposited and a minipool to match, AVAX is withdrawn by the minipool for staking.
3. After the staking period, AVAX used for staking and Avalanche rewards are deposited back to the ggAVAX contract.
4. Rewards are reflected in the exchange rate of ggAVAX → AVAX and are streamed over a 14 day period.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1ec3c2c8-f07f-4597-a5d7-9e35680404e6/Untitled.png)

### Liquid Stakers

Users depositing AVAX in exchange for ggAVAX.

### ggAVAX

ggAVAX is our Liquid Staking token. This token is how we will keep track of our user’s staked AVAX. The token contract also contains the proper methods allowing a user to deposit and withdraw their tokens.

### MinipoolManager

In the context of Liquid Staking, the Minipool Manager is responsible for matching our Minipool with the funds the Liquid Stakers have deposited to the network. When a Liquid Staker deposits AVAX, the AVAX sits and waits for a Minipool to come online. Once a Minipool with the proper collateral has come online, and has put forth the first half of the AVAX required to start it, funds are placed into a wallet controlled by the protocol to be staked using the new minipool hardware that has come online.

## Minipool Creating & Validation

These are the contracts for creating and managing minipools staking funds. A Minipool is what we (as well as our peers at RocketPool) use to describe a validator on our network.

The following contracts are a part of the Minipool Creation and Validation processes.

- [GGP](https://github.com/multisig-labs/gogopool-contracts/blob/master/contracts/contract/tokens/TokenGGP.sol) (`TokenGGP.sol`)
- [Staking](https://github.com/multisig-labs/gogopool-contracts/blob/master/contracts/contract/Staking.sol) (`Staking.sol`)
- [Minipool Manager](https://github.com/multisig-labs/gogopool-contracts/blob/master/contracts/contract/MinipoolManager.sol) (`MinipoolManager.sol`)

### Flow

1. Node Operator stakes GGP to collateralize the AVAX they want assigned from liquid stakers.
2. Node Operator creates a minipool by submitting their desired duration, delegation fee and AVAX assignment, along with their nodeID and 1000 AVAX.
3. Rialto records that a minipool is in queue and waits until sufficient liquid staker funds before launching the minipool as a validator with avalanche
4. After the validation period is over, Rialto returns funds to the Vault and can be withdrawn by the Node Operator.

Minipool Manager determines if GGP needs to be slashed for a failed validation period.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a63f7064-47c4-4f1c-a372-0c30bdf802d7/Untitled.png)

### GGP

GGP is our Utility Token. It is used as a collateral for our Minipool Validators. When someone creates a new Minipool on our network, they have to put up 10% of their requested AVAX as a collateral in GGP. For example, if they are borrowing 1000 AVAX from liquid stakers, they will have to put up 1000 AVAX \* 0.1 GGP in order to stake on our network. If the validator is failing at their duties, their GGP will be slashed and used to compensate the loss to our Liquid Stakers.

### Staking

This contract contains all the code required to update the AVAX staked and assigned, GGP staked and rewarded, and determine a GGP → AVAX collateralization ratio.

### Minipool Manager

For the context of Minipools, the Minipool manager handles creating minipools, as well as containing the functions called by our Oracle to start and end validation and reward payout.

On creation, a minipool is expected to have the required GGP Collateral as well as the proper amount of AVAX deposited to the contract. After depositing the GGP to the staking contract, the `createMinipool` function should be called along with the proper amount of AVAX for staking and a time frame for staking. After that is complete, Rialto (the Oracle) handles creating a threshold signature wallet and staking the AVAX on the network.

## Rewards

The rewards part of the protocol is responsible for calculating and distributing rewards across our minipool operators. The following contracts are a part of the rewards system.

- [Rewards Pool](https://github.com/multisig-labs/gogopool-contracts/blob/master/contracts/contract/RewardsPool.sol) (`RewardsPool.sol`)
- [Claim Node Operator](https://github.com/multisig-labs/gogopool-contracts/blob/master/contracts/contract/ClaimNodeOp.sol) (`ClaimNodeOp.sol`)

Reward are also distributed to Multisig operators and the ProtocolDAO.

### Flow

1. When a node operator creates a minipool they become eligible for GGP rewards.
2. Every rewards period tokens are inflated and distributed amongst NodeOperators, Multisigs and the ProtocolDAO
3. For Node Operators, the Rialto multisig will loop over all GGP stakers, determining eligibility based on their minipool creation time.
4. If eligible the amount of rewards earmarked for that node operator is increased in the Staking contract.
5. Finally Node Operators can claim and or restake any amount of their GGP Rewards.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f8a18d2-470c-4796-86d9-5d1e04a01de0/Untitled.png)

### Rewards Pool

The rewards are initiated periodically by the Oracle. This calculates the amount of inflation of GGP, then calculates the amount of rewards to be distributed to node operators, multisigs and the ProtocolDAO.

### Claim Node Op

This contract contains the function that gets executed when a Node Operator wants to withdraw their funds. They also have the option to only withdraw the rewards they earned, keeping their required collateral in the network to allow for a new staking cycle.

---
description: >-
  ERC4626 is a new type of token that allows for distributed shares of a token
  vault.
---

# ggAVAX via ERC4626

## What is it?

* New Token type based on ERC-20
* Allows users to pool native tokens into the vault and own "shares".
* Those shares can be redeemed for the tokens.
* Protocols then implement a strategy to maximize yield on these tokens (staking) so that its users earn interest.

## How does this work for GoGoPool?

* Users deposit their AVAX into our ERC-4626 contract, known as TokenggAVAX.
* The contract mints them equivalent ggAVAX.
* Users can redeem ggAVAX for equivalent AVAX plus their interest.
* The deposited AVAX is then sent to our minipools to be staked for an amount of time.
* Users can then redeem their ggAVAX whenever they like, if there is floating AVAX available.

---
description: Reported Vulnerabilities and Fixes
---

# ⚠ Vulnerability Reports

## November 23, 2023 - URL Rewrite

### Severity - Medium

Reported via the [GoGoPool Discord](https://discord.gg/CkXS83M85V), this vulnerability was discovered by [0xTeam](https://github.com/0xteam). **No user funds were directly at risk.** This vulnerability stemmed from an unsanitized input in the Next.js SDK tunnel endpoint, a part of the 'tunnel' feature in Sentry. It would allow attackers to send HTTP requests to arbitrary URLs and reflect the response back to the user. The primary concern was the insufficient restrictions on the 'o' query parameter, which could enable attackers to redirect requests and potentially execute malicious scripts. The vulnerability had the potential to significantly impact users. Malicious actors could exploit it to load pages with scripts in the backend, enabling them to connect to users' Web3 wallets.

This could result in unauthorized transactions, registration of fake tokens, or even the rewriting of false airdrop or giveaway pages to siphon user funds.

### Mitigation

The problem was mitigated by simply updating the Sentry NextJS Plugin. To mitigate further risk in the future, Sentry is being removed from our frontend site, effectively immediately. We thank 0xTeam for their responsible disclosure and an appropriate bounty will be paid.

# 🔐 Code4rena Audit

## Overview

### About C4

[Code4rena (C4)](https://code4rena.com/) is an open organization consisting of security researchers, auditors, developers, and individuals with domain expertise in smart contracts.

A C4 audit contest is an event in which community participants, referred to as Wardens, review, audit, or analyze smart contract logic in exchange for a bounty provided by sponsoring projects.

During the audit contest outlined in this document, C4 conducted an analysis of the GoGoPool smart contract system written in Solidity. The audit contest took place between December 15—January 3 2023.

Following the C4 audit contest, 3 wardens ([hansfriese](https://twitter.com/hansfriese), RaymondFam, and [ladboy233](https://twitter.com/Xc1008Cu)) reviewed the mitigations for all identified issues; the mitigation review report is appended below the audit contest report.

### Wardens

114 Wardens contributed reports to the GoGoPool contest:

1. [0Kage](https://twitter.com/0kage\_eth)
2.

[0x73696d616f](https://twitter.com/3xJanx2009)
3. 0xLad
4. [0xNazgul](https://twitter.com/0xNazgul)
5. [0xSmartContract](https://twitter.com/0xSmartContract)
6. 0xbepresent
7. 0xc0ffEE
8. [0xdeadbeef0x](https://twitter.com/0xdeadbeef\_\_\_\_)
9. 0xhunter
10. 0xmint
11. [AkshaySrivastav](https://twitter.com/akshaysrivastv)
12. [Allarious](https://twitter.com/\_Allarious)
13. Arbor-Finance (namaskar and bookland)
14. Atarpara
15. [Aymen0909](https://github.com/Aymen1001)
16. Bnke0x0
17. Breeje
18. [Ch\_301](https://twitter.com/0xch301)
19. [Czar102](https://twitter.com/\_Czar102)
20. [Deivitto](https://twitter.com/Deivitto)
21. [Faith](https://twitter.com/farazsth98)
22. [Franfran](https://franfran.dev/)
23. HE1M
24. HollaDieWaldfee
25. IllIllI
26. [Jeiwan](https://jeiwan.net)
27. Josiah
28. KmanOfficial
29. Lirios
30. [Manboy](https://twitter.com/manboy\_eth)
31. Matin
32. NoamYakov
33. [Nyx](https://twitter.com/Nyksx\_\_)
34. PaludoX0
35. [Qeew](https://twitter.com/adigunq\_adigun)
36. RaymondFam
37.

Rolezn
38. SEVEN
39. Saintcode\_
40. [SamGMK](../../about-gogopool/@sam\_gmk/)
41. SmartSek (0xDjango and hake)
42. [TomJ](https://mobile.twitter.com/tomj\_bb)
43. V\_B (Barichek and vlad\_bochok)
44. WatchDogs
45. \_\_141345\_\_
46. [adriro](https://github.com/romeroadrian)
47. ak1
48. ast3ros
49. [aviggiano](https://twitter.com/agfviggiano)
50. [betweenETHlines](https://twitter.com/eth\_lines)
51. [bin2chen](https://twitter.com/bin2chen)
52. brgltd
53. btk
54. [c3phas](https://twitter.com/c3ph\_)
55. [camdengrieh](https://twitter.com/camdenincrypto)
56. caventa
57. cccz
58. chaduke
59. ck
60. clems4ever
61. [codeislight](https://twitter.com/codeIslight)
62. cozzetti
63. cryptonue
64. cryptostellar5
65. [csanuragjain](https://twitter.com/csanuragjain)
66. [danyams](https://twitter.com/daniel\_yamagata)
67. datapunk
68. dic0de
69. eierina
70. enckrish
71. [fatherOfBlocks](https://twitter.com/father0fBl0cks)
72. fs0c
73. gz627
74. [hansfriese](https://twitter.com/hansfriese)
75. hihen
76. imare
77. immeas
78.

jadezti
79. [joestakey](https://twitter.com/JoeStakey)
80. kaliberpoziomka8552
81. kartkhira
82. [kiki\_dev](https://twitter.com/Kiki\_developer)
83. koxuan
84. [ladboy233](https://twitter.com/Xc1008Cu)
85. latt1ce
86. lukris02
87. mert\_eren
88. minhtrng
89. mookimgo
90. [nadin](https://twitter.com/nadin20678790)
91. nameruse
92. neumo
93. [nogo](https://twitter.com/0xnogo)
94. [pauliax](https://twitter.com/SolidityDev)
95. [peakbolt](https://twitter.com/peak\_bolt)
96. peanuts
97. peritoflores
98. rvierdiiev
99. sces60107
100. shark
101. simon135
102. sk8erboy
103. slowmoses
104. [stealthyz](https://twitter.com/Stealthyzzzz)
105. [supernova](https://twitter.com/harshit16024263)
106. tonisives
107. unforgiven
108. wagmi
109. wallstreetvilkas
110. yixxas
111. yongskiws

This contest was judged by [Alex the Entreprenerd](https://twitter.com/judge).

Final report assembled by [liveactionllama](https://twitter.com/liveactionllama).

## Summary

The C4 analysis yielded an aggregated total of 28 unique vulnerabilities. Of these vulnerabilities, 6 received a risk rating in the category of HIGH severity and 22 received a risk rating in the category of MEDIUM severity.

Additionally, C4 analysis included 15 reports detailing issues with a risk rating of LOW severity or non-critical. There were also 12 reports recommending gas optimizations.

All of the issues presented here are linked back to their original finding.

[Findings Repo](https://github.com/code-423n4/2022-12-gogopool-findings/issues)

## Scope

The code under review can be found within the [C4 GoGoPool contest repository](https://github.com/code-423n4/2022-12-gogopool), and is composed of 18 smart contracts written in the Solidity programming language and includes 2,040 lines of Solidity code.

## Severity Criteria

C4 assesses the severity of disclosed vulnerabilities based on three primary risk categories: high, medium, and low/non-critical.

High-level considerations for vulnerabilities span the following key areas when conducting assessments:

* Malicious Input Handling
* Escalation of privileges
* Arithmetic
* Gas use

For more information regarding the severity criteria referenced throughout the submission review process, please refer to the documentation provided on [the C4 website](https://code4rena.com), specifically our section on [Severity Categorization](https://docs.code4rena.com/awarding/judging-criteria/severity-categorization).

1\] AVAX Assigned High Water is updated incorrectly](https://github.com/code-423n4/2022-12-gogopool-findings/issues/566)

_Submitted by_ [_hansfriese_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/566)_, also found by_ [_unforgiven_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/827)_,_ [_wagmi_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/641)_,_ [_betweenETHlines_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/452)_,_ [_Allarious_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/401)_,_ [_HollaDieWaldfee_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/266)_, and_ [_chaduke_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/193)

[contracts/contract/MinipoolManager.sol#L374](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L374)

Node operators can manipulate the assigned high water to be higher than the actual.

#### Proof of Concept

The protocol rewards node operators according to the `AVAXAssignedHighWater` that is the maximum amount assigned to the specific staker during the reward cycle.

In the function `MinipoolManager.recordStakingStart()`, the `AVAXAssignedHighWater` is updated as below.

set the initialStartTime
365: 		uint256 initialStartTime = getUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".initialStartTime")));
366: 		if (initialStartTime == 0) {
367: 			setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".initialStartTime")), startTime);
368: 		}
369:
370: 		address owner = getAddress(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".owner")));
371: 		uint256 avaxLiquidStakerAmt = getUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".avaxLiquidStakerAmt")));
372: 		Staking staking = Staking(getContractAddress("Staking"));
373: 		if (staking.getAVAXAssignedHighWater(owner) < staking.getAVAXAssigned(owner)) {
374: 			staking.increaseAVAXAssignedHighWater(owner, avaxLiquidStakerAmt);//@audit wrong
375: 		}
376:
377: 		emit MinipoolStatusChanged(nodeID, MinipoolStatus.Staking);
378: 	}
```

In the line #373, if the current assigned AVAX is greater than the owner's `AVAXAssignedHighWater`, it is increased by `avaxLiquidStakerAmt`.

But this is supposed to be updated to `staking.getAVAXAssigned(owner)` rather than being increased by the amount.

Example: The node operator creates a minipool with 1000AVAX via `createMinipool(nodeID, 2 weeks, delegationFee, 1000*1e18)`.\
On creation, the assigned AVAX for the operator will be 1000AVAX.\
If the Rialtor calls `recordStakingStart()`, `AVAXAssignedHighWater` will be updated to 1000AVAX. After the validation finishes, the operator creates another minipool with 1500AVAX this time. Then on `recordStakingStart()`, `AVAXAssignedHighWater` will be updated to 2500AVAX by increasing 1500AVAX because the current assigned AVAX is 1500AVAX which is higher than the current `AVAXAssignedHighWater=1000AVAX`.\
This is wrong because the actual highest assigned amount is 1500AVAX.\
Note that `AVAXAssignedHighWater` is reset only through the function `calculateAndDistributeRewards` which can be called after `RewardsCycleSeconds=28 days`.

#### Recommended Mitigation Steps

Call `staking.resetAVAXAssignedHighWater(owner)` instead of calling `increaseAVAXAssignedHighWater()`.

```solidity
MinipoolManager.sol
373: 		if (staking.getAVAXAssignedHighWater(owner) < staking.getAVAXAssigned(owner)) {
374: 			staking.resetAVAXAssignedHighWater(owner); //@audit update to the current AVAX assigned
375: 		}
```

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/566)

[**Franfran (warden) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/566#issuecomment-1407447319)**:**

> Can we take some extra considerations here please?\
> Discussed with @0xju1ie (GoGoPool) about this specific issue, and this was the answer:
>
> (_it_ is AVAXAssignedHighWater)
>
> ```
> It increases on a per minipool basis right now, increasing based on only what that single minipool is getting.

> If it was to just update the AVAXAssignedHighWater to getAVAXAssigned, then it could be assigning the highwater mark too early.
>
> EX for how it is now:
> 1. create minipool1, assignedAvax = 1k, high water= 0
> 2. create minipool2, assignedAvax =1k, high water = 0
> 3. record start for minipool1, highwater -> 1k
> 4.  record start for minipool2, highwater -> 2k
>
> EX for how your suggestion could be exploited:
> 1. create minipool1, assignedAvax = 1k, high water= 0
> 2. create minipool2, assignedAvax =1k, high water = 0
> 3. record start for minipool1, highwater -> 2k
> 4.  cancel minipool2, highwater -> 2k
>
> if we used only avax assigned for that case then it would mess up the collateralization ratio for the second minipool and they would only get paid for the minipool that they are currently operating, not the one that ended previously.

> ```

[**0xju1ie (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/566#issuecomment-1411791734)**:**

> Their example in the proof of concept section is correct, and we have decided that this is not the ideal behavior and thus this is a bug. However, their recommended mitigation steps would create other issues, as highlighted by what @Franfran said. We intend to solve this issue differently than what they suggested.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/566#issuecomment-1414347752)**:**

> The Warden has shown a flaw in the way `increaseAVAXAssignedHighWater` is used, which can be used to:
>
> * Inflate the amount of AVAX
> * With the goal of extracting more rewards than intended
>
> I believe that the finding highlights both a way to extract further rewards as well as broken accounting.
>
> For this reason I agree with High Severity.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> New variable to track validating avax: [multisig-labs/gogopool#25](https://github.com/multisig-labs/gogopool/pull/25)

**Status:** Mitigation confirmed with comments. Full details in [report from RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/2).

d by_ [_AkshaySrivastav_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/845)_,_ [_hansfriese_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/571)_,_ [_hansfriese_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/567)_,_ [_caventa_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/544)_,_ [_shark_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/507)_,_ [_RaymondFam_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/354)_,_ [_csanuragjain_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/306)_,_ [_rvierdiiev_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/238)_, and_ [_cozzetti_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/178)

[contracts/contract/Staking.sol#L379-L383](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/Staking.sol#L379-L383)

ProtocolDAO implementation does not have a method to take out GGP.

So it can't handle ggp unless it updates ProtocolDAO.

#### Proof of Concept

recordStakingEnd() will pass the rewards of this reward.\
"If the validator is failing at their duties, their GGP will be slashed and used to compensate the loss to our Liquid Stakers"

At this point slashGGP() will be executed and the GGP will be transferred to "ProtocolDAO"

staking.slashGGP():

```solidity
    function slashGGP(address stakerAddr, uint256 ggpAmt) public onlySpecificRegisteredContract("MinipoolManager", msg.sender) {
        Vault vault = Vault(getContractAddress("Vault"));
        decreaseGGPStake(stakerAddr, ggpAmt);
        vault.transferToken("ProtocolDAO", ggp, ggpAmt);
    }
```

But the current ProtocolDAO implementation does not have a method to take out GGP. So it can't handle ggp unless it updates ProtocolDAO

#### Recommended Mitigation Steps

1.transfer GGP to ClaimProtocolDAO\
or\
2.Similar to ClaimProtocolDAO, add spend method to retrieve GGP

```solidity
contract ProtocolDAO is Base {
...

+    function spend(
+        address recipientAddress,
+        uint256 amount
+    ) external onlyGuardian {
+        Vault vault = Vault(getContractAddress("Vault"));
+        TokenGGP ggpToken = TokenGGP(getContractAddress("TokenGGP"));
+
+        if (amount == 0 || amount > vault.balanceOfToken("ProtocolDAO", ggpToken)) {
+            revert InvalidAmount();
+        }
+
+        vault.withdrawToken(recipientAddress, ggpToken, amount);
+
+        emit GGPTokensSentByDAOProtocol(address(this), recipientAddress, amount);
+   }
```

[**Alex the Entreprenerd (judge) increased severity to High and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/532#issuecomment-1414367063)**:**

> The Warden has shown how, due to a lack of `sweep` the default contract for fee handling will be unable to retrieve tokens sent to it.

>
> While the issue definitely would have been discovered fairly early in Prod, the in-scope system makes it clear that the funds would have been sent to ProtocolDAO.sol and would have been lost indefinitely.
>
> For this reason, I believe the finding to be of High Severity.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/532#issuecomment-1421419694)**:**

> Acknowledged.
>
> Thanks for the report. This is something we're aware of and are not going to fix at the moment.
>
> The funds are transferred to the Vault and the ProtocolDAO contract is upgradeable. Therefore in the future we can upgrade the contract to spend the Vault GGP tokens to return funds to Liquid Stakers.
>
> We expect slashing to be a rare event and might have some manual steps involved in the early days of the protocol to do this process if it occurs.

mmeas_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/493)_, also found by_ [_Allarious_](../../about-gogopool/undefined/)_,_ [_ast3ros_](../../about-gogopool/undefined/)_,_ [_unforgiven_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/881)_,_ [_Josiah_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/794)_,_ [_SmartSek_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/592)_,_ [_Franfran_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/490)_,_ [_HollaDieWaldfee_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/344)_,_ [_RaymondFam_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/322)_, and_ [_0xdeadbeef0x_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/216)

[contracts/contract/MinipoolManager.sol#L673-L675](https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/MinipoolManager.sol#L673-L675)

A node operator sends in the amount of duration they want to stake for.

Behind the scenes Rialto will stake in 14 day cycles and then distribute rewards.

If a node operator doesn't have high enough availability and doesn't get any rewards, the protocol will slash their staked `GGP`. For calculating the expected rewards that are missed however, the full duration is used:

```javascript
File: MinipoolManager.sol

557:	function getExpectedAVAXRewardsAmt(uint256 duration, uint256 avaxAmt) public view returns (uint256) {
558:		ProtocolDAO dao = ProtocolDAO(getContractAddress("ProtocolDAO"));
559:		uint256 rate = dao.getExpectedAVAXRewardsRate();
560:		return (avaxAmt.mulWadDown(rate) * duration) / 365 days; // full duration used when calculating expected reward
561:	}

...

670:	function slash(int256 index) private {

...

673:		uint256 duration = getUint(keccak256(abi.encodePacked("minipool.item", index, ".duration")));
674:		uint256 avaxLiquidStakerAmt = getUint(keccak256(abi.encodePacked("minipool.item", index, ".avaxLiquidStakerAmt")));
675:		uint256 expectedAVAXRewardsAmt = getExpectedAVAXRewardsAmt(duration, avaxLiquidStakerAmt); // full duration
676:		uint256 slashGGPAmt = calculateGGPSlashAmt(expectedAVAXRewardsAmt);
```

This is unfair to the node operator because the expected rewards is from a 14 day cycle.

Also, If they were to be unavailable again, in a later cycle, they would get slashed for the full duration once again.

#### Impact

A node operator staking for a long time is getting slashed for an unfairly large amount if they aren't available during a 14 day period.

The protocol also wants node operators to stake in longer periods: [https://multisiglabs.notion.site/Known-Issues-42e2f733daf24893a93ad31100f4cd98](https://multisiglabs.notion.site/Known-Issues-42e2f733daf24893a93ad31100f4cd98)

> Team Comment:\
>
>
> * This can only be taken advantage of when signing up for 2-4 week validation periods. **Our protocol is incentivizing nodes to sign up for 3-12 month validation periods.** If the team notices this mechanic being abused, Rialto may update its GGP reward calculation to disincentive this behavior.

This slashing amount calculation incentives the node operator to sign up for the shortest period possible and restake themselves to minimize possible losses.

lto));
		minipoolMgr.recordStakingStart(mp1.nodeID, txID, block.timestamp);

		skip(2 weeks); // a two week cycle

		vm.prank(address(rialto));
		minipoolMgr.recordStakingEnd{value: validationAmt}(mp1.nodeID, block.timestamp, 0 ether);

		assertEq(vault.balanceOf("MinipoolManager"), depositAmt);

		int256 minipoolIndex = minipoolMgr.getIndexOf(mp1.nodeID);
		MinipoolManager.Minipool memory mp1Updated = minipoolMgr.getMinipool(minipoolIndex);
		assertEq(mp1Updated.status, uint256(MinipoolStatus.Withdrawable));
		assertEq(mp1Updated.avaxTotalRewardAmt, 0);
		assertTrue(mp1Updated.endTime != 0);

		assertEq(mp1Updated.avaxNodeOpRewardAmt, 0);
		assertEq(mp1Updated.avaxLiquidStakerRewardAmt, 0);

		assertEq(minipoolMgr.getTotalAVAXLiquidStakerAmt(), 0);

		assertEq(staking.getAVAXAssigned(mp1Updated.owner), 0);
		assertEq(staking.getMinipoolCount(mp1Updated.owner), 0);

		// log slash amount
		console.log("slashedAmount",mp1Updated.ggpSlashAmt);
	}
```

Slashed amount for a `365 days` duration is `100 eth` (10%).

However, where they to stake for the minimum time, `14 days` the slashed amount would be only \~`3.8 eth`.

#### Tools Used

vs code, forge

#### Recommended Mitigation Steps

Either hard code the duration to 14 days for calculating expected rewards or calculate the actual duration using `startTime` and `endTime`.

[**0xju1ie (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/493#event-8306021419)

[**Alex the Entreprenerd (judge) increased severity to High and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/493#issuecomment-1413687136)**:**

> The Warden has shown an incorrect formula that uses the `duration` of the pool for slashing.
>
> The resulting loss can be up to 26 times the yield that should be made up for.
>
> Because the:
>
> * Math is incorrect
> * Based on intended usage
> * Impact is more than an order of magnitude off
> * Principal is impacted (not just loss of yield)
>
> I believe the most appropriate severity to be High.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Base slash on validation period not full duration: [multisig-labs/gogopool#41](https://github.com/multisig-labs/gogopool/pull/41)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/3) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/22).

23n4/2022-12-gogopool-findings/issues/263)_,_ [_kaliberpoziomka8552_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/257)_,_ [_HollaDieWaldfee_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/255)_,_ [_wallstreetvilkas_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/199)_,_ [_stealthyz_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/196)_,_ [_cozzetti_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/181)_,_ [_rvierdiiev_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/173)_,_ [_ladboy233_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/123)_,_ [_chaduke_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/83)_,_ [_chaduke_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/81)_, and_ [_Manboy_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/76)

A malicious actor can hijack a minipool of any node operator that finished the validation period or had an error.

The impacts:

1. Node operators staked funds will be lost (Loss of funds)
2. Hacker can hijack the minipool and retrieve rewards without hosting a node. (Theft of yield)

2.1 See scenario #2 comment for dependencies

#### Proof of Concept

**Background description**

The protocol created a state machine that validates transitions between minipool states. For this exploit it is important to understand three states:

1. `Prelaunch` - This state is the initial state when a minipool is created. The created minipool will have a status of `Prelaunch` until liquid stakers funds are matched and `rialto` stakes 2000 AVAX into Avalanche.
2. `Withdrawable` - This state is set when the 14 days validation period is over. In this state:\
   2.1. `rialto` returned 1000 AVAX to the liquid stakers and handled reward distribution.\
   2.2. Node operators can withdraw their staked funds and rewards.\
   2.3.

If the node operator signed up for a duration longer than 14 days `rialto` will recreate the minipool and stake it for another 14 days.\

3.

e the funds in Avalanche

The state machine allows transitions according the `requireValidStateTransition` function: [https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L164](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L164)

```
    function requireValidStateTransition(int256 minipoolIndex, MinipoolStatus to) private view {
------
        } else if (currentStatus == MinipoolStatus.Withdrawable || currentStatus == MinipoolStatus.Error) {
		isValid = (to == MinipoolStatus.Finished || to == MinipoolStatus.Prelaunch);
	} else if (currentStatus == MinipoolStatus.Finished || currentStatus == MinipoolStatus.Canceled) {
		// Once a node is finished/canceled, if they re-validate they go back to beginning state
		isValid = (to == MinipoolStatus.Prelaunch);
------
```

In the above restrictions, we can see that the following transitions are allowed:

1.

From `Withdrawable` state to `Prelaunch` state. This transition enables `rialto` to call `recreateMinipool`
2. From `Finished` state to `Prelaunch` state. This transition allows a node operator to re-use their nodeID to stake again in the protocol.
3. From `Error` state to `Prelaunch` state. This transition allows a node operator to re-use their nodeID to stake again in the protocol after an error.

gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L242)

```
	function createMinipool(
		address nodeID,
		uint256 duration,
		uint256 delegationFee,
		uint256 avaxAssignmentRequest
	) external payable whenNotPaused {
---------
		// Create or update a minipool record for nodeID
		// If nodeID exists, only allow overwriting if node is finished or canceled
		// 		(completed its validation period and all rewards paid and processing is complete)
		int256 minipoolIndex = getIndexOf(nodeID);
		if (minipoolIndex != -1) {
			requireValidStateTransition(minipoolIndex, MinipoolStatus.Prelaunch);
			resetMinipoolData(minipoolIndex);
----------
		setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".status")), uint256(MinipoolStatus.Prelaunch));
----------
		setAddress(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".owner")), msg.sender);
----------
	}

```

THE BUG: `createMinipool` can be called by **Anyone** with the `nodeID` of any node operator.

If `createMinipool` is called at the `Withdrawable` state or `Error` state:

* The transaction will be allowed
* The owner of the minipool will be switched to the caller.

Therefore, the minipool is hijacked and the node operator will not be able to withdraw their funds.

**Exploit scenarios**

As shown above, an attacker can **always** hijack the minipool and lock the node operators funds.

1. Cancel the minipool
2. Earn rewards on behalf of original NodeOp

_**Scenario #1 - Cancel the minipool**_

A hacker can hijack the minipool and immediately cancel the pool after a 14 day period is finished or an error state. Results:

1. Node operator will lose all his staked AVAX\
   1.1. This can be done by a malicious actor to **ALL** GoGoPool stakers to lose their funds in a period of 14 days.\

2. Hacker will not lose anything and not gain anything.

Consider the following steps:

1. Hacker creates a node and creates a minipool `node-1337`.
2.

NodeOp registers a nodeID `node-123` and finished the 14 days stake period. State is `Withdrawable`.
3. Hacker calls `createMinipool` with `node-123` and deposits 1000 AVAX. Hacker is now owner of the minipool
4. Hacker calls `cancelMinipool` of `node-123` and receives his staked 1000 AVAX.
5. NodeOp cannot withdraw his staked AVAX as NodeOp is no longer the owner.
6.

│                           │   │  NodeOp loses  │   │◄─────────────────────────┤ │Withdraw  │
             │                           │   │  his 1000 AVAX │   │      1000 AVAX + REWARDS │ │stake and │
             │                           │   │  Stake, cannot │   ├─────────────────────────►│ │rewards   │
             │                           │   │  withdraw      │   │                          │ └──────────┘
             │                           │   └────────────────┘   │     ┌───────────────┐    │
             │                           │                        │     │Hacker loses no│    │
             │                           │                        │     │funds, can     │    │
             │                           │                        │     │withdraw GPP   │    │
             │                           │                        │     └───────────────┘    │
```

_**Scenario #2 - Use node of node operator**_

In this scenario the NodeOp registers for a duration longer then 14 days.

The hacker will hijack the minipool after 14 days and earn rewards on behalf of the node operators node for the rest of the duration.\
As the NodeOp registers for a longer period of time, it is likely he will not notice he is not the owner of the minipool and continue to use his node to validate Avalanche.

Results:

1. Node operator will lose all his staked AVAX
2. Hacker will gain rewards for staking without hosting a node

Important to note:

* This scenario is only possible if `recordStakingEnd` and `recreateMinipool` are **not** called in the same transaction by `rialto`.
* During the research the sponsor has elaborated that they plan to perform the calls in the same transaction.
* The sponsor requested to submit issues related to `recordStakingEnd` and `recreateMinipool` single/multi transactions for information and clarity anyway.

Consider the following steps:

1. Hacker creates a node and creates a minipool `node-1337`.
2.

NodeOp registers a nodeID `node-123` for 28 days duration and finished the 14 days stake period. State is `Withdrawable`.
3. Hacker calls `createMinipool` with `node-1234` and deposits 1000 AVAX. Hacker is now owner of minipool
4. Rialto calls `recreateMinipool` to restake the minipool in Avalanche. (This time: the owner is the hacker, the hardware is NodeOp)
5. 14 days have passed, hacker can withdraw the rewards and 1000 staked AVAX
6. NodeOps cannot withdraw staked AVAX.

**Foundry POC**

The POC will demonstrate scenario #1.

.nodeID);
		assertEq(hacker.balance, depositAmt);
		// Hacker withdraws his own minipool and receives 1000 AVAX + rewards
		minipoolMgr.withdrawMinipoolFunds(hackerMp.nodeID);
		assertEq(hacker.balance, depositAmt + depositAmt + expectedRewards);

		// Hacker withdraws his staked ggp
		staking.withdrawGGP(ggpStakeAmt);
		assertEq(ggp.balanceOf(hacker), ggpStakeAmt);
		vm.stopPrank();

		vm.startPrank(nodeOp);
		// NodeOp tries to withdraw his funds from the minipool
		// Transaction reverts because NodeOp is not the owner anymore
		vm.expectRevert(MinipoolManager.OnlyOwner.selector);
		minipoolMgr.withdrawMinipoolFunds(nodeOpMp.nodeID);

		// NodeOp can still release his staked gpp
		staking.withdrawGGP(ggpStakeAmt);
		assertEq(ggp.balanceOf(nodeOp), ggpStakeAmt);
		vm.stopPrank();
	}
```

To run the POC, execute:

```
forge test -m testHijackMinipool -v
```

Expected output:

```
Running 1 test for test/unit/MinipoolManager.t.sol:MinipoolManagerTest
[PASS] testHijackMinipool() (gas: 2346280)
Test result: ok.

1 passed; 0 failed; finished in 9.63s
```

#### Tools Used

VS Code, Foundry

#### Recommended Mitigation Steps

Fortunately, the fix is very simple.\
The reason `createMinipool` is called with an existing `nodeID` is to re-use the `nodeID` again with the protocol. GoGoPool can validate that the owner is the same address as the calling address. GoGoPool have already implemented a function that does this: `onlyOwner(index)`.

om/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L243](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L243)

```
	function createMinipool(
		address nodeID,
		uint256 duration,
		uint256 delegationFee,
		uint256 avaxAssignmentRequest
	) external payable whenNotPaused {
----------
		int256 minipoolIndex = getIndexOf(nodeID);
		if (minipoolIndex != -1) {
                        onlyOwner(minipoolIndex); // AUDIT: ADDED HERE
----------
		} else {
----------
	}
```

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/213#issuecomment-1410348485)**:**

> The Warden has shown how, due to a lax check for State Transition, a Pool ID can be hijacked, causing the loss of the original deposit
>
> Because the attack is contingent on a logic flaw and can cause a complete loss of Principal, I agree with High Severity.

>
> Separate note: I created [issue 904](https://github.com/code-423n4/2022-12-gogopool-findings/issues/904). For the Finding 2 of this report, please refrain from grouping findings especially when they use different functions and relate to different issues.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Atomically recreate minipool to not allow hijack: [multisig-labs/gogopool#23](https://github.com/multisig-labs/gogopool/pull/23)

**Status:** Mitigation confirmed, but a new medium severity issue was found. Full details in [report from hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/23), and also included in Mitigation Review section below.

ol-findings/issues/319)_,_ [_yongskiws_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/285)_,_ [_0xLad_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/204)_,_ [_btk_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/187)_,_ [_rvierdiiev_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/179)_,_ [_koxuan_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/155)_,_ [_ladboy233_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/147)_,_ [_Rolezn_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/96)_,_ [_HE1M_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/68)_,_ [_yongskiws_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/39)_,_ [_SEVEN_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/37)_, and_ [_dic0de_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/14)

Inflation of `ggAVAX` share price can be done by depositing as soon as the vault is created.

Impact:

1. Early depositor will be able steal other depositors funds
2. Exchange rate is inflated. As a result depositors are not able to deposit small funds.

#### Proof of Concept

If `ggAVAX` is not seeded as soon as it is created, a malicious depositor can deposit 1 WEI of AVAX to receive 1 share.\
The depositor can donate WAVAX to the vault and call `syncRewards`. This will start inflating the price.

When the attacker front-runs the creation of the vault, the attacker:

1. Calls `depositAVAX` to receive 1 share
2. Transfers `WAVAX` to `ggAVAX`
3. Calls `syncRewards` to inflate exchange rate

The issue exists because the exchange rate is calculated as the ratio between the `totalSupply` of shares and the `totalAssets()`.\
When the attacker transfers `WAVAX` and calls `syncRewards()`, the `totalAssets()` increases gradually and therefore the exchange rate also increases.

`convertToShares` : [https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L123](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L123)

```
	function convertToShares(uint256 assets) public view virtual returns (uint256) {
		uint256 supply = totalSupply; // Saves an extra SLOAD if totalSupply is non-zero.

		return supply == 0 ? assets : assets.mulDivDown(supply, totalAssets());
	}
```

Its important to note that while it is true that cycle length is 14 days, in practice time between cycles can very between 0-14 days. This is because syncRewards validates that the next reward cycle is evenly divided by the length (14 days).

`syncRewards`: [https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L102](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L102)

```
	function syncRewards() public {
----------
		// Ensure nextRewardsCycleEnd will be evenly divisible by `rewardsCycleLength`.
		uint32 nextRewardsCycleEnd = ((timestamp + rewardsCycleLength) / rewardsCycleLength) * rewardsCycleLength;
---------
	}
```

Therefore:

* The closer the call to `syncRewards` is to the next evenly divisible value of `rewardsCycleLength`, the closer the next `rewardsCycleEnd` will be.
* The closer the delta between `syncRewards` calls is, the higher revenue the attacker will get.

Edge case example:\
`syncRewards` is called with the timestamp 1672876799, `syncRewards` will be able to be called again 1 second later.

`(1672876799 + 14 days) / 14 days) * 14 days) = 1672876800`

Additionally, the price inflation causes a revert for users who want to deposit less then the donation (WAVAX transfer) amount, due to precision rounding when depositing.

```
	function depositAVAX() public payable returns (uint256 shares) {
------
		if ((shares = previewDeposit(assets)) == 0) {
			revert ZeroShares();
		}
------
	}
```

`previewDeposit` and `convertToShares` :\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L133](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L133)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L123](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L123)

```
	function convertToShares(uint256 assets) public view virtual returns (uint256) {
		uint256 supply = totalSupply; // Saves an extra SLOAD if totalSupply is non-zero.

return supply == 0 ? assets : assets.mulDivDown(supply, totalAssets());
	}
	function previewDeposit(uint256 assets) public view virtual returns (uint256) {
		return convertToShares(assets);
	}
```

**Foundry POC**

The POC will demonstrate the below scenario:

1. Bob front-runs the vault creation.
2. Bob deposits 1 WEI of AVAX to the vault.
3. Bob transfers 1000 WAVAX to the vault.
4. Bob calls `syncRewards` when block.timestamp = `1672876799`.
5. Bob waits 1 second.
6. Bob calls `syncRewards` again. Share price fully inflated.
7. Alice deposits 2000 AVAX to vault.
8. Bob withdraws 1500 AVAX (steals 500 AVAX from Alice).
9. Alice share earns her 1500 AVAX (although she deposited 2000).

Additionally, the POC will show that depositors trying to deposit less then the donation amount will revert.

lob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/test/unit/TokenggAVAX.t.sol#L108](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/test/unit/TokenggAVAX.t.sol#L108)

```
	function testShareInflation() public {
		uint256 depositAmount = 1;
		uint256 aliceDeposit = 2000 ether;
		uint256 donationAmount = 1000 ether;
		vm.deal(bob, donationAmount  + depositAmount);
		vm.deal(alice, aliceDeposit);
		vm.warp(1672876799);

		// create new ggAVAX
		ggAVAXImpl = new TokenggAVAX();
		ggAVAX = TokenggAVAX(deployProxy(address(ggAVAXImpl), address(guardian)));
		ggAVAX.initialize(store, ERC20(address(wavax)));

		// Bob deposits 1 WEI of AVAX
		vm.prank(bob);
		ggAVAX.depositAVAX{value: depositAmount}();
		// Bob transfers 1000 AVAX to vault
		vm.startPrank(bob);
		wavax.deposit{value: donationAmount}();
		wavax.transfer(address(ggAVAX), donationAmount);
		vm.stopPrank();
		// Bob Syncs rewards
		ggAVAX.syncRewards();

		// 1 second has passed
		// This can range between 0-14 days.

2000 AVAX
		vm.prank(alice);
		ggAVAX.depositAVAX{value: aliceDeposit}();

		//Expectet revert when any depositor deposits less then 1000 AVAX
		vm.expectRevert(bytes4(keccak256("ZeroShares()")));
		ggAVAX.depositAVAX{value: 10 ether}();

		// Bob withdraws maximum assests for his share
		uint256 maxWithdrawAssets = ggAVAX.maxWithdraw(bob);
		vm.prank(bob);
		ggAVAX.withdrawAVAX(maxWithdrawAssets);

		//Validate bob has withdrawn 1500 AVAX
		assertEq(bob.balance, 1500 ether);

		// Alice withdraws maximum assests for her share
		maxWithdrawAssets = ggAVAX.maxWithdraw(alice);
		ggAVAX.syncRewards(); // to update accounting
		vm.prank(alice);
		ggAVAX.withdrawAVAX(maxWithdrawAssets);

		// Validate that Alice withdraw 1500 AVAX + 1 (~500 AVAX loss)
		assertEq(alice.balance, 1500 ether + 1);
	}
```

To run the POC, execute:

```
forge test -m testShareInflation -v
```

Expected output:

```
Running 1 test for test/unit/TokenggAVAX.t.sol:TokenggAVAXTest
[PASS] testShareInflation() (gas: 3874399)
Test result: ok.

1 passed; 0 failed; finished in 8.71s
```

#### Tools Used

VS Code, Foundry

#### Recommended Mitigation Steps

When creating the vault add initial funds in order to make it harder to inflate the price. Best practice would add initial funds as part of the initialization of the contract (to prevent front-running).

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/209#issuecomment-1379257413)

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/209#issuecomment-1407738455)**:**

> The Warden has shown how, by performing a small deposit, followed by a transfer, shares can be rebased, causing a grief in the best case, and complete fund loss in the worst case for every subsequent depositor.
>
> While the finding is fairly known, it's impact should not be understated, and because of this I agree with High Severity.

>
> I recommend watching this presentation by Riley Holterhus which shows possible mitigations for the attack: https://youtu.be/\_pO2jDgL0XE?t=601

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Initialize ggAVAX with a deposit: [multisig-labs/gogopool#49](https://github.com/multisig-labs/gogopool/pull/49)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/5) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/24).

e-423n4/2022-12-gogopool-findings/issues/136)_, also found by_ [_enckrish_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/743)_,_ [_imare_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/709)_,_ [_bin2chen_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/525)_,_ [_danyams_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/321)_,_ [_0xdeadbeef0x_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/221)_,_ [_cozzetti_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/186)_, and_ [_ladboy233_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/128)

When staking is done, a Rialto multisig calls `MinipoolManager.recordStakingEnd` ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L385-L440](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L385-L440)).

If the `avaxTotalRewardAmt` has the value zero, the `MinipoolManager` will slash the node operator's GGP.

The issue is that the amount to slash can be greater than the GGP balance the node operator has staked.

This will cause the call to `MinipoolManager.recordStakingEnd` to revert because an underflow is detected.

This means a node operator can create a minipool that cannot be slashed.

A node operator must provide at least 10% of `avaxAssigned` as collateral by staking GGP.

It is assumed that a node operator earns AVAX at a rate of 10% per year.

So if a Minipool is created with a duration of `> 365 days`, the 10% collateral is not sufficient to pay the expected rewards.

This causes the function call to revert.

Another cause of the revert can be that the GGP price in AVAX changes. Specifically if the GGP price falls, there needs to be slashed more GGP.

Therefore if the GGP price drops enough it can cause the call to slash to revert.

I think it is important to say that with any collateralization ratio this can happen. The price of GGP must just drop enough or one must use a long enough duration.

The exact impact of this also depends on how the Rialto multisig handles failed calls to `MinipoolManager.recordStakingEnd`.

It looks like if this happens, `MinipoolManager.recordStakingError` ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L484-L515](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L484-L515)) is called.

This allows the node operator to withdraw his GGP stake.

**So in summary a node operator can create a Minipool that cannot be slashed and probably remove his GGP stake when it should have been slashed.**

#### Proof of Concept

When calling `MinipoolManager.recordStakingEnd` ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L385-L440](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L385-L440)) and the `avaxTotalRewardAmt` parameter is zero, the node operator is slashed:

```solidity
// No rewards means validation period failed, must slash node ops GGP.

tAmt = 1000 ether;
    uint256 avaxAssignmentRequest = 1000 ether;
    uint256 validationAmt = depositAmt + avaxAssignmentRequest;
    uint128 ggpStakeAmt = 100 ether;

    vm.startPrank(nodeOp);
    ggp.approve(address(staking), MAX_AMT);
    staking.stakeGGP(ggpStakeAmt);
    MinipoolManager.Minipool memory mp1 = createMinipool(depositAmt, avaxAssignmentRequest, duration);
    vm.stopPrank();

    address liqStaker1 = getActorWithTokens("liqStaker1", MAX_AMT, MAX_AMT);
    vm.prank(liqStaker1);
    ggAVAX.depositAVAX{value: MAX_AMT}();

    vm.prank(address(rialto));
    minipoolMgr.claimAndInitiateStaking(mp1.nodeID);

    bytes32 txID = keccak256("txid");
    vm.prank(address(rialto));
    minipoolMgr.recordStakingStart(mp1.nodeID, txID, block.timestamp);

    vm.startPrank(address(rialto));

    skip(duration);

    minipoolMgr.recordStakingEnd{value: validationAmt}(mp1.nodeID, block.timestamp, 0 ether);
}
```

See that it runs successfully with `duration = 365 days` and fails with `duration = 366 days`.

The similar issue occurs when the GGP price drops. I chose to implement the test with `duration` as the cause for the underflow because your tests use a fixed AVAX/GGP price.

#### Tools Used

VSCode, Foundry

#### Recommended Mitigation Steps

You should check if the amount to be slashed is greater than the node operator's GGP balance. If this is the case, the amount to be slashed should be set to the node operator's GGP balance.

I believe this check can be implemented within the `MinipoolManager.slash` function without breaking any of the existing accounting logic.

56(abi.encodePacked("minipool.item", index, ".owner")));
    uint256 duration = getUint(keccak256(abi.encodePacked("minipool.item", index, ".duration")));
    uint256 avaxLiquidStakerAmt = getUint(keccak256(abi.encodePacked("minipool.item", index, ".avaxLiquidStakerAmt")));
    uint256 expectedAVAXRewardsAmt = getExpectedAVAXRewardsAmt(duration, avaxLiquidStakerAmt);
    uint256 slashGGPAmt = calculateGGPSlashAmt(expectedAVAXRewardsAmt);
    setUint(keccak256(abi.encodePacked("minipool.item", index, ".ggpSlashAmt")), slashGGPAmt);

    emit GGPSlashed(nodeID, slashGGPAmt);

    Staking staking = Staking(getContractAddress("Staking"));

    if (slashGGPAmt > staking.getGGPStake(owner)) {
        slashGGPAmt = staking.getGGPStake(owner);
    }

    staking.slashGGP(owner, slashGGPAmt);
}
```

[**emersoncloud (GoGoPool) confirmed, but commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/136#issuecomment-1380932948)**:**

> This is a combination of two other issues from other wardens
>
> 1.

Slash amount shouldn't depend on duration: https://github.com/code-423n4/2022-12-gogopool-findings/issues/694
> 2. GGP Slash shouldn't revert: https://github.com/code-423n4/2022-12-gogopool-findings/issues/743

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/136#issuecomment-1415768955)**:**

> This finding combines 2 issues:
>
> * If price drops Slash can revert -> Medium
> * Attacker can set Duration to too high to cause a revert -> High
>
> Am going to dedupe this and the rest, but ultimately I think these are different findings, that should have been filed separately.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/136#issuecomment-1415772950)**:**

> The Warden has shown how a malicious staker could bypass slashing, by inputting a duration that is beyond the intended amount.

>
> Other reports have shown how to sidestep the slash or reduce it, however, this report shows how the bypass can be enacted maliciously to break the protocol functionality, to the attacker's potential gain.
>
> Because slashing is sidestepped in it's entirety, I believe this finding to be of High Severity.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> If staked GGP doesn't cover slash amount, slash it all: [multisig-labs/gogopool#41](https://github.com/multisig-labs/gogopool/pull/41)

**Status:** Original finding mitigated, but a medium severity economical risk is still present. Full details in reports from [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/6), [ladboy233](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/61) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/25).

Also included in Mitigation Review section below.

***

## Medium Risk Findings (22)

### [\[M-01\] `RewardsPool.sol` : It is safe to have the `startRewardsCycle` with `WhenNotPaused` modifier](https://github.com/code-423n4/2022-12-gogopool-findings/issues/823)

_Submitted by_ [_ak1_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/823)_, also found by_ [_sces60107_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/745)

When the contract is paused , allowing startRewardsCycle would inflate the token value which might not be safe.

Rewards should not be claimed by anyone when all other operations are paused.

I saw that the `witdrawGGP` has this `WhenNotPaused` modifier.

Inflate should not consider the paused duration.

Let's say, when the contract is paused for the duration of 2 months, then the dao, protocol, and node validator would enjoy the rewards. This is not good for a healthy protocol.

#### Proof of Concept

startRewardsCycle does not have the WhenNotPaused modifier.

tAllotment + nopClaimContractAllotment + multisigClaimContractAllotment > getRewardsCycleTotalAmt()) {
		revert IncorrectRewardsDistribution();
	}


	TokenGGP ggp = TokenGGP(getContractAddress("TokenGGP"));
	Vault vault = Vault(getContractAddress("Vault"));


	if (daoClaimContractAllotment > 0) {
		emit ProtocolDAORewardsTransfered(daoClaimContractAllotment);
		vault.transferToken("ClaimProtocolDAO", ggp, daoClaimContractAllotment);
	}


	if (multisigClaimContractAllotment > 0) {
		emit MultisigRewardsTransfered(multisigClaimContractAllotment);
		distributeMultisigAllotment(multisigClaimContractAllotment, vault, ggp);
	}


	if (nopClaimContractAllotment > 0) {
		emit ClaimNodeOpRewardsTransfered(nopClaimContractAllotment);
		ClaimNodeOp nopClaim = ClaimNodeOp(getContractAddress("ClaimNodeOp"));
		nopClaim.setRewardsCycleTotal(nopClaimContractAllotment);
		vault.transferToken("ClaimNodeOp", ggp, nopClaimContractAllotment);
	}
}
```

#### Recommended Mitigation Steps

We suggest to use `WhenNotPaused` modifier.

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/823)

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/823#issuecomment-1415693372)**:**

> The Warden has shown an inconsistency as to how Pausing is used.
>
> While other aspects of the code are pausable and under the control of the `guardian`, a call to `startRewardsCycle` can be performed by anyone, and in the case of a system-wide pause may create unfair gains or lost rewards.
>
> For this reason I agree with Medium Severity.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Pause startRewardsCycle when protocol is paused: [multisig-labs/gogopool#22](https://github.com/multisig-labs/gogopool/pull/22)

**Status:** Mitigation confirmed with comments.

Full details in [report from RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/12).

2-gogopool-findings/issues/335)_,_ [_chaduke_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/315)_, and_ [_HollaDieWaldfee_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/275)

[Link to original code](https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/ProtocolDAO.sol#L209-L216)

```solidity
File: https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/ProtocolDAO.sol

205	/// @notice Upgrade a contract by unregistering the existing address, and registring a new address and name
	/// @param newAddr Address of the new contract
	/// @param newName Name of the new contract
	/// @param existingAddr Address of the existing contract to be deleted
209	function upgradeExistingContract(
			address newAddr,
			string memory newName,
			address existingAddr
		) external onlyGuardian {
			registerContract(newAddr, newName);
			unregisterContract(existingAddr);
216	}
```

Function `ProtocolDAO.upgradeExistingContract` handles contract upgrading.

However, there are multiple implicaitons of the coding logic in the function, which render the contract upgrading impractical.

**Implication 1**:

The above function `upgradeExistingContract` registers the upgraded contract first, then unregisters the existing contract. This leads to the requirement that the upgraded contract name **must be different from** the existing contract name. Otherwise the updated contract address returned by `Storage.getAddress(keccak256(abi.encodePacked("contract.address", contractName)))` will be `address(0)` (please refer to the below POC Testcase 1). This is because if the upgraded contract uses the original name (i.e. the contract name is not changed), function call `unregisterContract(existingAddr)` in the `upgradeExistingContract` will override the registered contract address in `Storage` to address(0) due to the use of the same contract name.

Since using the same name after upgrading will run into trouble with current coding logic, a safeguard should be in place to make sure two names are really different. For example, put this statement in the `upgradeExistingContract` function:\
`require(newName != existingName, "Name not changed");`, where `existingName` can be obtained using:\
`string memory existingName = store.getString(keccak256(abi.encodePacked("contract.name", existingAddr)));`.

**Implication 2**:

If we really want a different name for an upgraded contract, we then get into more serious troubles: We have to upgrade other contracts that reference the upgraded contract since contract names are referenced mostly hardcoded (for security considerations). This may lead to a very complicated issue because contracts are cross-referenced.

For example, contract `ClaimNodeOp` references contracts `RewardsPool`, `ProtocolDAO` and `Staking`. At the same time, contract `ClaimNodeOp` is referenced by contracts `RewardsPool` and `Staking`.

This means that:

1. If contract `ClaimNodeOp` was upgraded, which means the contract name `ClaimNodeOp` was changed;
2. This requires contracts `RewardsPool` and `Staking` to be upgraded (with new names) in order to correctly reference to newly named `ClaimNodeOp` contract;
3. This further requires those contracts that reference `RewardsPool` or `Staking` to be upgraded in order to correctly reference them;
4. and this further requires those contracts that reference the above upgraded contracts to be upgraded ...
5. This may lead to complicated code management issue and expose new vulnerabilites due to possible incomplete code adaptation.
6. This may render the contracts upgrading impractical.

I rate this issue as high severity due to the fact that:\
Contract upgradability is one of the main features of the whole system design (all other contracts are designed upgradable except for `TokenGGP`, `Storage` and `Vault` ).

However, the current `upgradeExistingContract` function's coding logic requires the upgraded contract must change its name (refer to the below Testcase 1). This inturn requires to upgrade all relevant cross-referenced contracts (refer to the below Testcase 2). Thus leading to a quite serous code management issue while upgrading contracts, and renders upgrading contracts impractical.

#### Proof of Concept

**Testcase 1**:

This testcase demonstrates that current coding logic of upgrading contracts requires: **the upgraded contract must change its name**. Otherwise contract upgrading will run into issue. Put the below test case in file `ProtocolDAO.t.sol`. The test case demonstrates that `ProtocolDAO.upgradeExistingContract` does not function properly if the upgraded contract does not change the name. That is: the upgraded contract address returned by `Storage.getAddress(keccak256(abi.encodePacked("contract.address", contractName)))` will be `address(0)` if its name unchanged.

ExistingContract(addr, name, existingAddr);
		assertEq(store.getBool(keccak256(abi.encodePacked("contract.exists", addr))), true);
		//@audit the registered address was deleted by function call `PtotocolDAO.unregisterContract(existingAddr)`
		assertEq(store.getAddress(keccak256(abi.encodePacked("contract.address", name))), address(0));
		assertEq(store.getString(keccak256(abi.encodePacked("contract.name", addr))), name);

               //@audit verify that the old contract has been de-registered
		assertEq(store.getBool(keccak256(abi.encodePacked("contract.exists", existingAddr))), false);
		assertEq(store.getAddress(keccak256(abi.encodePacked("contract.address", existingName))), address(0));
		assertEq(store.getString(keccak256(abi.encodePacked("contract.name", existingAddr))), "");
	}
```

**Testcase 2**:

This testcase demonstrates that current coding logic of upgrading contracts requires: **in order to upgrade a single contract, all cross-referenced contracts have to be upgraded and change their names**.

Otherwise, other contracts will run into issues.\
If the upgraded contract does change its name, contract upgrading will succeed. However, other contracts' functions that reference the upgraded contract will fail due to referencing hardcoded contract name.\
The below testcase upgrades contract `ClaimNodeOp` to `ClaimNodeOpV2`. Then, contract `Staking` calls `increaseGGPRewards` which references hardcoded contract name `ClaimNodeOp` in its modifier. The call is failed.

Test steps:

1. Copy contract file `ClaimNodeOp.sol` to `ClaimNodeOpV2.sol`, and rename the contract name from `ClaimNodeOp` to `ClaimNodeOpV2` in file `ClaimNodeOpV2.sol`;
2. Put the below test file `UpgradeContractIssue.t.sol` under folder `test/unit/`;
3. Run the test.

**Note**: In order to test actual function call after upgrading contract, this testcase upgrades a real contract `ClaimNodeOp`. This is different from the above Testcase 1 which uses a random address to simulate a contract.

vault), rewardsPoolAmt);
		vault.depositToken("RewardsPool", ggp, rewardsPoolAmt);
		vm.stopPrank();
	}

	function testUpgradeExistingContractWithNameChanged() public {

		vm.prank(nodeOp1);
		staking.stakeGGP(10 ether);

                //@audit increase GGPRewards before upgrading contract - succeed
		vm.prank(address(nopClaim));
		staking.increaseGGPRewards(address(nodeOp1), 10 ether);
		assert(staking.getGGPRewards(address(nodeOp1)) == 10 ether);

		//@audit Start to upgrade contract ClaimNodeOp to ClaimNodeOpV2

		vm.startPrank(guardian);
		//@audit upgrad contract
		ClaimNodeOpV2 nopClaimV2 = new ClaimNodeOpV2(store, ggp);
		address addr = address(nopClaimV2);
		//@audit contract name must be changed due to the limitation of `upgradeExistingContract` coding logic
		string memory name = "ClaimNodeOpV2";

		//@audit get existing contract ClaimNodeOp info
		address existingAddr = address(nopClaim);
		string memory existingName = "ClaimNodeOp";

		//@audit the existing contract should be already registered.

Verify its info.

keccak256(abi.encodePacked("contract.address", name))), addr);
		assertEq(store.getString(keccak256(abi.encodePacked("contract.name", addr))), name);

		//@audit verify that the old contract has been de-registered
		assertEq(store.getBool(keccak256(abi.encodePacked("contract.exists", existingAddr))), false);
		assertEq(store.getAddress(keccak256(abi.encodePacked("contract.address", existingName))), address(0));
		assertEq(store.getString(keccak256(abi.encodePacked("contract.name", existingAddr))), "");
		vm.stopPrank();

		vm.prank(nodeOp1);
		staking.stakeGGP(10 ether);

                //@audit increase GGPRewards after upgrading contract ClaimNodeOp to ClaimNodeOpV2
		vm.prank(address(nopClaimV2)); //@audit using the upgraded contract
		vm.expectRevert(BaseAbstract.InvalidOrOutdatedContract.selector);
		//@audit revert due to contract Staking using hardcoded contract name "ClaimNodeOp" in the modifier
		staking.increaseGGPRewards(address(nodeOp1), 10 ether);
	}
}

```

#### Recommended Mitigation Steps

1.

Upgrading contract does not have to change contranct names especially in such a complicated system wherein contracts are cross-referenced in a hardcoded way. I would suggest not to change contract names when upgrading contracts.
2. In function `upgradeExistingContract` definition, swap fucnction call sequence between `registerContract()` and `unregisterContract()` so that contract names can keep unchanged after upgrading.

:

```solidity
File: https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/ProtocolDAO.sol

205	/// @notice Upgrade a contract by unregistering the existing address, and registring a new address and name
	/// @param newAddr Address of the new contract
	/// @param newName Name of the new contract
	/// @param existingAddr Address of the existing contract to be deleted
209	function upgradeExistingContract(
			address newAddr,
			string memory newName,  //@audit this `newName` parameter can be removed if upgrading don't change contract name
			address existingAddr
		) external onlyGuardian {
  		unregisterContract(existingAddr);  //@audit unregister the existing contract first
		registerContract(newAddr, newName);  //@audit then register the upgraded contract
216	}
```

**POC of Mitigation**:

After the above recommended mitigation, the below Testcase verifies that after upgrading contracts, other contract's functions, which reference the hardcoded contract name, can still opetate correctly.

1. Make the above recommended mitigation in function `ProtocolDAO.upgradeExistingContract`;
2. Put the below test file `UpgradeContractImproved.t.sol` under folder `test/unit/`;
3. Run the test.

**Note**: Since we don't change the upgraded contract name, for testing purpose, we just need to create a new contract instance (so that the contract instance address is changed) to simulate the contract upgrading.

rdsPool", ggp, rewardsPoolAmt);
			vm.stopPrank();
		}

		function testUpgradeContractCorrectlyWithNameUnChanged() public {
			//@audit increase GGPRewards before upgrading contract - no problem
			vm.prank(nodeOp1);
			staking.stakeGGP(10 ether);

			vm.prank(address(nopClaim));
			staking.increaseGGPRewards(address(nodeOp1), 10 ether);
			assert(staking.getGGPRewards(address(nodeOp1)) == 10 ether);

			//@audit Start to upgrade contract ClaimNodeOp
			vm.startPrank(guardian);
			//@audit upgraded contract by creating a new contract instance
			ClaimNodeOp nopClaimV2 = new ClaimNodeOp(store, ggp);
			address addr = address(nopClaimV2);
			//@audit contract name is not changed!
			string memory name = "ClaimNodeOp";

			//@audit get existing contract info
			address existingAddr = address(nopClaim);
			string memory existingName = "ClaimNodeOp";

			//@audit new contract address is different from the old one
			assertFalse(addr == existingAddr);

			//@audit the existing contract should be already registered.

Verify its info.

ncodePacked("contract.exists", existingAddr))), true);
			assertEq(store.getAddress(keccak256(abi.encodePacked("contract.address", existingName))), existingAddr);
			assertEq(store.getString(keccak256(abi.encodePacked("contract.name", existingAddr))), existingName);

                        //@audit Upgrade contract
			dao.upgradeExistingContract(addr, name, existingAddr);

			//@audit verify the upgraded contract has correct contract info registered
			assertEq(store.getBool(keccak256(abi.encodePacked("contract.exists", addr))), true);
			assertEq(store.getAddress(keccak256(abi.encodePacked("contract.address", name))), addr);
			assertEq(store.getString(keccak256(abi.encodePacked("contract.name", addr))), name);

			//@audit verify that the old contract has been de-registered
			assertEq(store.getBool(keccak256(abi.encodePacked("contract.exists", existingAddr))), false);
			assertEq(store.getString(keccak256(abi.encodePacked("contract.name", existingAddr))), "");
			//@audit The contract has new address now.

mNodeOp" in the modifier
			staking.increaseGGPRewards(address(nodeOp1), 10 ether);
			//@audit Successfully increased!
			assert(staking.getGGPRewards(address(nodeOp1)) == 20 ether);
		}
	}

```

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/742#issuecomment-1379350503)

[**0xju1ie (GoGoPool) disagreed with severity and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/742#issuecomment-1384535064)**:**

> Not sure if this is considered a high since there isn't a direct loss of funds?
>
> `Medium: Assets not at direct risk, but the function of the protocol or its availability could be impacted, or leak value with a hypothetical attack path with stated assumptions, but external requirements.`

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/742#issuecomment-1409240633)**:**

> In spite of the lack of risk for Principal, a core functionality of the protocol is impaired.

>
> This has to be countered versus the requirement of the names being the same, which intuitively seems to be the intended use case, as changing the name would also break balances / other integrations such as the modifier `onlySpecificRegisteredContract`.
>
> The other side of the argument is that the mistake is still fixable by the same actor within a reasonable time frame.

[**Alex the Entreprenerd (judge) decreased severity to Medium and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/742#issuecomment-1414350784)**:**

> I believe the finding is meaningful and well written, but ultimately the damage can be undone with a follow-up call to `registerContract`.
>
> Because of this am downgrading to Medium Severity.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Fix upgrade to work when a contract has the same name: [multisig-labs/gogopool#32](https://github.com/multisig-labs/gogopool/pull/32)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/11) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/27).

/github.com/code-423n4/2022-12-gogopool-findings/issues/85)

[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L484](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L484)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L528](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L528)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L287](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L287)

The Multisig can call `MinipoolManager.sol::recordStakingError()` if there is an error while registering the node as a validator.

Also the Multisig can call [MinipoolManager.sol::finishFailedMinipoolByMultisig()](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L528) in order to "finish" the NodeOp's minipool proccess.

If the Multisig accidentally/intentionally calls `recordStakingError()` then `finishFailedMinipoolByMultisig()` the NodeOp funds may be trapped in the protocol.

The `finishFailedMinipoolByMultisig()` has the next comment: _Multisig can move a minipool from the error state to the finished state after a human review of the error_ but the NodeOp should be able to withdraw his funds after a finished minipool.

#### Proof of Concept

I created a test for this situation in `MinipoolManager.t.sol`. At the end you can observe that the `withdrawMinipoolFunds()` reverts with `InvalidStateTransition` error:

1. NodeOp creates the minipool
2. Rialto calls claimAndInitiateStaking
3. Something goes wrong and Rialto calls recordStakingError()
4.

Rialto accidentally/intentionally calls finishFailedMinipoolByMultisig() in order to finish the NodeOp's minipool
5. The NodeOp can not withdraw his funds. The withdraw function reverts with InvalidStateTransition() error

```solidity
function testUserFundsStuckErrorFinished() public {
    // NodeOp funds may be trapped by a invalid state transition
    // 1. NodeOp creates the minipool
    // 2. Rialto calls claimAndInitiateStaking
    // 3. Something goes wrong and Rialto calls recordStakingError()
    // 4. Rialto accidentally/intentionally calls finishFailedMinipoolByMultisig() in order
    // to finish the NodeOp's minipool
    // 5. The NodeOp can not withdraw his funds. The withdraw function reverts with
    // InvalidStateTransition() error
    //
    // 1.

Create the minipool by the NodeOp
    //
    address liqStaker1 = getActorWithTokens("liqStaker1", MAX_AMT, MAX_AMT);
    vm.prank(liqStaker1);
    ggAVAX.depositAVAX{value: MAX_AMT}();
    assertEq(liqStaker1.balance, 0);
    uint256 duration = 2 weeks;
    uint256 depositAmt = 1000 ether;
    uint256 avaxAssignmentRequest = 1000 ether;
    uint256 validationAmt = depositAmt + avaxAssignmentRequest;
    uint128 ggpStakeAmt = 200 ether;
    vm.startPrank(nodeOp);
    ggp.approve(address(staking), ggpStakeAmt);
    staking.stakeGGP(ggpStakeAmt);
    MinipoolManager.Minipool memory mp = createMinipool(depositAmt, avaxAssignmentRequest, duration);
    vm.stopPrank();
    assertEq(vault.balanceOf("MinipoolManager"), depositAmt);
    //
    // 2. Rialto calls claimAndInitiateStaking
    //
    vm.startPrank(address(rialto));
    minipoolMgr.claimAndInitiateStaking(mp.nodeID);
    assertEq(vault.balanceOf("MinipoolManager"), 0);
    //
    // 3.

Something goes wrong and Rialto calls recordStakingError()
    //
    bytes32 errorCode = "INVALID_NODEID";
    minipoolMgr.recordStakingError{value: validationAmt}(mp.nodeID, errorCode);
    // NodeOps funds should be back in vault
    assertEq(vault.balanceOf("MinipoolManager"), depositAmt);
    // 4. Rialto accidentally/intentionally calls finishFailedMinipoolByMultisig() in order
    // to finish the NodeOp's minipool
    minipoolMgr.finishFailedMinipoolByMultisig(mp.nodeID);
    vm.stopPrank();
    // 5. The NodeOp can not withdraw his funds.

The withdraw function reverts with
    // InvalidStateTransition() error
    vm.startPrank(nodeOp);
    vm.expectRevert(MinipoolManager.InvalidStateTransition.selector);
    minipoolMgr.withdrawMinipoolFunds(mp.nodeID);
    vm.stopPrank();
}
```

#### Tools used

Foundry/Vscode

#### Recommended Mitigation Steps

The `withdrawMinipoolFunds` could add another [requireValidStateTransition](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#LL290C3-L290C30) in order to allow the withdraw after the finished minipoool.

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/723)

[**0xju1ie (GoGoPool) disagreed with severity and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/723#issuecomment-1385123551)**:**

> I think this should be the primary for the `finishFailedMinipoolByMultisig()` problem.
>
> Medium feels like a more appropriate severity.

This issue depends on rialto multisig improperly functioning but we do intend to fix the finishFailedMinipoolByMultisig method to not lock users out of their funds.

[**Alex the Entreprenerd (judge) decreased severity to Medium and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/723#issuecomment-1415686783)**:**

> The Warden has shown a potential issues with the FSM of the system, per the Audit Scope, the transition should not happen on the deployed system, however, the Warden has shown an issue with the state transition check and has detailed the consequences of it.
>
> For this reason, I agree with Medium Severity.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Remove method that trapped Node Operator's funds: [multisig-labs/gogopool#20](https://github.com/multisig-labs/gogopool/pull/20)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/13) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/28).

h_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/560)_,_ [_AkshaySrivastav_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/538)_,_ [_betweenETHlines_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/481)_,_ [_simon135_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/395)_,_ [_0xbepresent_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/343)_,_ [_0Kage_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/316)_,_ [_kaliberpoziomka8552_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/276)_,_ [_0Kage_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/271)_,_ [_Saintcode\__](https://github.com/code-423n4/2022-12-gogopool-findings/issues/190)_,_ [_Faith_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/141)_, and_ [_dic0de_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/12)

For every created minipool a multisig address is set to continue validator interactions.

Every minipool multisig address get assigned by calling `requireNextActiveMultisig`.

This function always return the first enabled multisig address.

In case the specific address is disabled all created minipools will be stuck with this address which increase the probability of also funds being stuck.

#### Impact

Probability of funds being stuck increases if `requireNextActiveMultisig` always return the same address.

#### Proof of Concept

[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MultisigManager.sol#L80-L91](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MultisigManager.sol#L80-L91)

#### Recommended Mitigation Steps

Use a strategy like [round robin](https://en.wikipedia.org/wiki/Round-robin\_item\_allocation) to assign next active multisig to minipool.

Something like this :

```solidity
private uint nextMultisigAddressIdx;

function requireNextActiveMultisig() external view returns (address) {
    uint256 total = getUint(keccak256("multisig.count"));
    address addr;
    bool enabled;

    uint256 i = nextMultisigAddressIdx; // cache last used
    if (nextMultisigAddressIdx==total) {
        i = 0;
    }

    for (; i < total; i++) {
        (addr, enabled) = getMultisig(i);
        if (enabled) {
            nextMultisigAddressIdx = i+1;
            return addr;
        }
    }

    revert NoEnabledMultisigFound();
}
```

[**emersoncloud (GoGoPool) disagreed with severity and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/702#issuecomment-1384310351)**:**

> Without a mechanism for funds to become stuck, I don't think this warrants a medium severity.
>
> I do agree with the principle that if we have multiple multisigs, some system to distribute minipools between them seems reasonable.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/702#issuecomment-1410942197)**:**

> While the finding will not be awarded as Admin Privilege, I believe that ultimately the Warden has shown an incorrect implementation of the function `requireNextActiveMultisig` which would ideally either offer:
>
> * Round Robin
> * Provable Random Selection
>
> For those reasons I think the finding is still notable, in that the function doesn't work as intended, and believe it should be judged Medium Severity.
>
> I will be consulting with an additional Judge to ensure that the logic above is acceptable given the custom scope for this contest.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/702#issuecomment-1421415846)**:**

> Acknowledged.
>
> We're not going to fix this in the first iteration of our protocol, we're expecting to only have one active multisig.

We will definitely implement some system to distribute minipools between multisigs when we have more.

/236)_, and_ [_RaymondFam_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/79)

[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/Staking.sol#L328-L332](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/Staking.sol#L328-L332)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L89-L114](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L89-L114)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimProtocolDAO.sol#L20-L35](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimProtocolDAO.sol#L20-L35)

The `whenNotPaused` modifier is used to pause minipool creation and staking/withdrawing GGP.

However, there are several cases this modifier could be bypassed, which breaks the intended admin control function and special mode.

#### Proof of Concept

**`stake()`**

In paused mode, no more `stakeGGP()` is allowed,

```solidity
File: contract/Staking.sol
319: 	function stakeGGP(uint256 amount) external whenNotPaused {
320: 		// Transfer GGP tokens from staker to this contract
321: 		ggp.safeTransferFrom(msg.sender, address(this), amount);
322: 		_stakeGGP(msg.sender, amount);
323: 	}
```

However, `restakeGGP()` is still available, which potentially violate the purpose of pause mode.

```solidity
File: contract/Staking.sol
328: 	function restakeGGP(address stakerAddr, uint256 amount) public onlySpecificRegisteredContract("ClaimNodeOp", msg.sender) {
329: 		// Transfer GGP tokens from the ClaimNodeOp contract to this contract
330: 		ggp.safeTransferFrom(msg.sender, address(this), amount);
331: 		_stakeGGP(stakerAddr, amount);
332: 	}
```

**`withdraw()`**

In paused mode, no more `withdrawGGP()` is allowed,

```solidity
File: contract/Staking.sol
358: 	function withdrawGGP(uint256 amount) external whenNotPaused {

373: 		vault.withdrawToken(msg.sender, ggp, amount);
```

However, `claimAndRestake()` is still available, which can withdraw from the vault.

```solidity
File: contract/ClaimNodeOp.sol
089: 	function claimAndRestake(uint256 claimAmt) external {

103: 		if (restakeAmt > 0) {
104: 			vault.withdrawToken(address(this), ggp, restakeAmt);
105: 			ggp.approve(address(staking), restakeAmt);
106: 			staking.restakeGGP(msg.sender, restakeAmt);
107: 		}
108:
109: 		if (claimAmt > 0) {
110: 			vault.withdrawToken(msg.sender, ggp, claimAmt);
111: 		}
```

The function `spend()` can also ignore the pause mode to withdraw from the vault. But this is a guardian function. It could be intended behavior.

```solidity
File: contract/ClaimProtocolDAO.sol
20: 	function spend(
21: 		string memory invoiceID,
22: 		address recipientAddress,
23: 		uint256 amount
24: 	) external onlyGuardian {

32: 		vault.withdrawToken(recipientAddress, ggpToken, amount);
```

#### Recommended Mitigation Steps

* add the `whenNotPaused` modifier to `restakeGGP()` and `claimAndRestake()`
* maybe also for guardian function `spend()`.

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/673)

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/673#issuecomment-1407733362)**:**

> The warden has shown an inconsistency within similar functions regarding how they behave during a pause.\
> Because the finding pertains to an inconsistent functionality, without a loss of principal, I agree with Medium Severity.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Pause claimAndRestake as well: [multisig-labs/gogopool#22](https://github.com/multisig-labs/gogopool/pull/22)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/14) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/30).

ubmitted by_ [_wagmi_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/648)_, also found by_ [_peritoflores_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/811)_,_ [_sces60107_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/674)_,_ [_\_\_141345\_\__](https://github.com/code-423n4/2022-12-gogopool-findings/issues/646)_,_ [_hansfriese_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/575)_,_ [_slowmoses_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/464)_,_ [_supernova_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/374)_,_ [_rvierdiiev_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/239)_,_ [_HollaDieWaldfee_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/157)_, and_ [_chaduke_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/92)

When doing inflation, function `getInflationAmt()` calculated number of intervals elapsed by dividing the duration with interval length.

```solidity
function getInflationIntervalsElapsed() public view returns (uint256) {
    ProtocolDAO dao = ProtocolDAO(getContractAddress("ProtocolDAO"));
    uint256 startTime = getInflationIntervalStartTime();
    if (startTime == 0) {
        revert ContractHasNotBeenInitialized();
    }
    return (block.timestamp - startTime) / dao.getInflationIntervalSeconds();
}
```

As we can noticed that, this calculation is rounding down, it means if `block.timestamp - startTime = 1.99 intervals`, it only account for `1 interval`.

However, when updating start time after inflating, it still update to current timestamp while it should only increased by `intervalLength * intervalsElapsed` instead.

```solidity
addUint(keccak256("RewardsPool.InflationIntervalStartTime"), inflationIntervalElapsedSeconds);
// @audit should only update to oldStartTime + inverval * numInterval
setUint(keccak256("RewardsPool.RewardsCycleTotalAmt"), newTokens);
```

Since default value of inflation interval = 1 days and reward cycle length = 14 days, so the impact is reduced. However, these configs can be changed in the future.

#### Proof of Concept

Consider the scenario:

1. Assume last inflation time is `InflationIntervalStartTime = 100`. `InflationIntervalSeconds = 50`.
2. At `timestamp = 199`, function `getInflationAmt()` will calculate

```solidity
inflationIntervalsElapsed = (199 - 100) / 50 = 1
// Compute inflation for total inflation intervals elapsed
for (uint256 i = 0; i < inflationIntervalsElapsed; i++) {
    newTotalSupply = newTotalSupply.mulWadDown(inflationRate);
} // @audit only loop once.
```

3.

And then in `inflate()` function, `InflationIntervalStartTime` is still updated to current timestamp, so `InflationIntervalStartTime = 199`.
4. If this sequence of actions are repeatedly used, we can easily see

```solidity
InflationIntervalStartTime = 199, inflated count = 1
InflationIntervalStartTime = 298, inflated count = 2
InflationIntervalStartTime = 397, inflated count = 3
InflationIntervalStartTime = 496, inflated count = 4
InflationIntervalStartTime = 595, inflated count = 5
```

While at `timestamp = 595`, inflated times should be `(595 - 100) / 50 = 9` instead.

#### Recommended Mitigation Steps

Consider only increasing `InflationIntervalStartTime` by the amount of intervals time interval length.

[**emersoncloud (GoGoPool) disagreed with severity and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/648#issuecomment-1379452071)**:**

> I agree with this issue, but assets can't be stolen, lost or compromised directly.

Medium severity is more appropriate ([https://docs.code4rena.com/awarding/judging-criteria#estimating-risk](https://docs.code4rena.com/awarding/judging-criteria#estimating-risk))

[**Alex the Entreprenerd (judge) decreased severity to Medium and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/648#issuecomment-1407742757)**:**

> I have considered a Higher Severity, due to logical flaws.
>
> However, I believe that the finding
>
> * Relies on the Condition of being called less than intended
> * Causes an incorrect amount of emissions (logically close to loss of Yield)
>
> For those reasons, I believe Medium Severity to be the most appropriate

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/648#issuecomment-1421426366)**:**

> Acknowledged, not fixing in this first version of the protocol.
>
> We can and will have rialto call startRewardsCycle if needed, and think it's unlikely to become delayed.

***

### [\[M-07\] Rialto may not be able to cancel minipools created by contracts that cannot receive AVAX](https://github.com/code-423n4/2022-12-gogopool-findings/issues/623)

_Submitted by_ [_Jeiwan_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/623)_, also found by_ [_AkshaySrivastav_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/809)_,_ [_peritoflores_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/686)_, and_ [_ladboy233_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/146)

A malicious node operator may create a minipool that cannot be cancelled.

#### Proof of Concept

Rialto may cancel a minipool by calling [cancelMinipoolByMultisig](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L520), however the function sends AVAX to the minipool owner, and the owner may block receiving of AVAX, causing the call to `cancelMinipoolByMultisig` to fail ([MinipoolManager.sol#L664](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L664)):

```solidity
function _cancelMinipoolAndReturnFunds(address nodeID, int256 index) private {
  ...
  address owner = getAddress(keccak256(abi.encodePacked("minipool.item", index, ".owner")));
  ...

{
  uint256 duration = 2 weeks;
  uint256 depositAmt = 1000 ether;
  uint256 avaxAssignmentRequest = 1000 ether;
  uint128 ggpStakeAmt = 200 ether;

  // Node operator is a contract than cannot receive AVAX:
  // contract NodeOpContract {}
  NodeOpContract nodeOpContract = new NodeOpContract();
  dealGGP(address(nodeOpContract), ggpStakeAmt);
  vm.deal(address(nodeOpContract), depositAmt);

  vm.startPrank(address(nodeOpContract));
  ggp.approve(address(staking), MAX_AMT);
  staking.stakeGGP(ggpStakeAmt);
  MinipoolManager.Minipool memory mp1 = createMinipool(depositAmt, avaxAssignmentRequest, duration);
  vm.stopPrank();

  bytes32 errorCode = "INVALID_NODEID";
  int256 minipoolIndex = minipoolMgr.getIndexOf(mp1.nodeID);
  store.setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".status")), uint256(MinipoolStatus.Prelaunch));

  // Rialto trices to cancel the minipool created by the node operator contract but the transaction reverts since
  // the node operator contract cannot receive AVAX.

vm.prank(address(rialto));
  // FAIL: reverted with ETH_TRANSFER_FAILED
  minipoolMgr.cancelMinipoolByMultisig(mp1.nodeID, errorCode);
}
```

#### Recommended Mitigation Steps

Consider using the [Pull over Push pattern](https://fravoll.github.io/solidity-patterns/pull\_over\_push.html) to return AVAX to owners of minipools that are canceled by Rialto.

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/623)

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/623#issuecomment-1407735453)**:**

> The warden has shown how the checked return value from call can be used as a grief to prevent canceling of a minipool.
>
> The finding can have different severities based on the context, in this case, the cancelling can be denied, however, other state transitions are still possible.
>
> For this reason (functionality is denied), I agree with Medium Severity.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/623#issuecomment-1421428356)**:**

> Acknowledged.
>
> We'll make a note of this in our documentation, but not fixing immediately.

***

### [\[M-08\] Recreated pools receive a wrong AVAX amount due to miscalculated compounded liquid staker amount](https://github.com/code-423n4/2022-12-gogopool-findings/issues/620)

_Submitted by_ [_Jeiwan_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/620)_, also found by_ [_yixxas_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/501)_,_ [_Franfran_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/489)_, and_ [_0xbepresent_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/347)

After recreation, minipools will receive more AVAX than the sum of their owners' current stake and the rewards that they generated.

#### Proof of Concept

Multipools that successfully finished validation may be recreated by multisigs, before staked GGP and deposited AVAX have been withdrawn by minipool owners ([MinipoolManager.sol#L444](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L444)).

on compounds deposited AVAX by adding the rewards earned during previous validation periods to the AVAX amounts deposited and requested from stakers ([MinipoolManager.sol#L450-L452](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L450-L452)):

```solidity
Minipool memory mp = getMinipool(minipoolIndex);
// Compound the avax plus rewards
// NOTE Assumes a 1:1 nodeOp:liqStaker funds ratio
uint256 compoundedAvaxNodeOpAmt = mp.avaxNodeOpAmt + mp.avaxNodeOpRewardAmt;
setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".avaxNodeOpAmt")), compoundedAvaxNodeOpAmt);
setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".avaxLiquidStakerAmt")), compoundedAvaxNodeOpAmt);
```

The function assumes that a node operator and liquid stakers earned an equal reward amount: `compoundedAvaxNodeOpAmt` is calculated as the sum of the current AVAX deposit of the minipool owner and the node operator reward earned so far.

However, liquid stakers get a smaller reward than node operators: the minipool node commission fee is applied to their share ([MinipoolManager.sol#L417](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L417)):

```solidity
  uint256 avaxHalfRewards = avaxTotalRewardAmt / 2;

  // Node operators recv an additional commission fee
  ProtocolDAO dao = ProtocolDAO(getContractAddress("ProtocolDAO"));
  uint256 avaxLiquidStakerRewardAmt = avaxHalfRewards - avaxHalfRewards.mulWadDown(dao.getMinipoolNodeCommissionFeePct());
  uint256 avaxNodeOpRewardAmt = avaxTotalRewardAmt - avaxLiquidStakerRewardAmt;
```

As a result, the `avaxLiquidStakerAmt` set in the `recreateMinipool` function will always be bigger than the actual amount since it equals to the compounded node operator amount, which includes node operator rewards.

Next, in the `recreateMinipool` function, the assigned AVAX amount is increased by the amount borrowed from liquid stakers + the node operator amount, which is again wrong because the assigned AVAX amount can only be increased by the liquid stakers' reward share ([MinipoolManager.sol#L457-L459](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L457-L459)):

```solidity
staking.increaseAVAXStake(mp.owner, mp.avaxNodeOpRewardAmt);
staking.increaseAVAXAssigned(mp.owner, compoundedAvaxNodeOpAmt);
staking.increaseMinipoolCount(mp.owner);
```

As a result, the amount of AVAX borrowed from liquid stakers by the minipool will be increased by the minipool node commission fee, the increased amount will be sent to the validator, and it will be required to end the validation period.

liqStaker1 = getActorWithTokens("liqStaker1", MAX_AMT, MAX_AMT);
  vm.prank(liqStaker1);
  ggAVAX.depositAVAX{value: MAX_AMT}();

  vm.prank(address(rialto));
  minipoolMgr.claimAndInitiateStaking(mp.nodeID);

  bytes32 txID = keccak256("txid");
  vm.prank(address(rialto));
  minipoolMgr.recordStakingStart(mp.nodeID, txID, block.timestamp);

  skip(duration / 2);

  // Give rialto the rewards it needs
  uint256 rewards = 10 ether;
  deal(address(rialto), address(rialto).balance + rewards);

  // Pay out the rewards
  vm.prank(address(rialto));
  minipoolMgr.recordStakingEnd{value: validationAmt + rewards}(mp.nodeID, block.timestamp, rewards);
  MinipoolManager.Minipool memory mpAfterEnd = minipoolMgr.getMinipoolByNodeID(mp.nodeID);
  assertEq(mpAfterEnd.avaxNodeOpAmt, depositAmt);
  assertEq(mpAfterEnd.avaxLiquidStakerAmt, avaxAssignmentRequest);

  // After the validation periods has ended, the node operator and liquid stakers got different rewards,
  // since a fee was taken from the liquid stakers' share.

uint256 nodeOpReward = 5.75 ether;
  uint256 liquidStakerReward = 4.25 ether;
  assertEq(mpAfterEnd.avaxNodeOpRewardAmt, nodeOpReward);
  assertEq(mpAfterEnd.avaxLiquidStakerRewardAmt, liquidStakerReward);

  // Add a bit more collateral to cover the compounding rewards
  vm.prank(nodeOp);
  staking.stakeGGP(1 ether);

  vm.prank(address(rialto));
  minipoolMgr.recreateMinipool(mp.nodeID);

  MinipoolManager.Minipool memory mpCompounded = minipoolMgr.getMinipoolByNodeID(mp.nodeID);
  // After pool was recreated, node operator's amounts were increased correctly.
  assertEq(mpCompounded.avaxNodeOpAmt, mp.avaxNodeOpAmt + nodeOpReward);
  assertEq(mpCompounded.avaxNodeOpAmt, mp.avaxNodeOpInitialAmt + nodeOpReward);
  assertEq(staking.getAVAXStake(mp.owner), mp.avaxNodeOpAmt + nodeOpReward);

  // However, liquid stakers' amount were increased incorrectly: nodeOpReward was added instead of liquidStakerReward.

ewardAmt + liquidStakerRewardAmt) / 2;
+
+               uint256 compoundedAvaxNodeOpAmt = mp.avaxNodeOpAmt + avgRewardAmt;
                setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".avaxNodeOpAmt")), compoundedAvaxNodeOpAmt);
                setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".avaxLiquidStakerAmt")), compoundedAvaxNodeOpAmt);

                Staking staking = Staking(getContractAddress("Staking"));
                // Only increase AVAX stake by rewards amount we are compounding
                // since AVAX stake is only decreased by withdrawMinipool()
-               staking.increaseAVAXStake(mp.owner, mp.avaxNodeOpRewardAmt);
+               staking.increaseAVAXStake(mp.owner, avgRewardAmt);
                staking.increaseAVAXAssigned(mp.owner, compoundedAvaxNodeOpAmt);
                staking.increaseMinipoolCount(mp.owner);
```

Also, consider sending equal amounts of rewards to the vault and the ggAVAX token in the `recordStakingEnd` function.

[**emersoncloud (GoGoPool) disagreed with severity and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/620#issuecomment-1379479577)**:**

> I need to do a bit more digging on my end, but this might be working as designed. Will come back to it.

[**0xju1ie (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/620#issuecomment-1385310905)**:**

> I think this is valid - don't think it is high though as there isn't really a loss of funds.

[**0xju1ie (GoGoPool) disputed and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/620#issuecomment-1387167944)**:**

> Talked to the rest of the team and this is not valid - it is working as designed. We are matching 1:1 with what the node operators are earning/staking.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/620#issuecomment-1415662963)**:**

> Will flag to triage but I agree with the sponsor.

his:
>
> * This function may return false while there is the correct amount of AVAX as `avaxLiquidStakerAmt` (in extreme cases)
> * This is going to pull too much funds from the `Manager`: https://github.com/code-423n4/2022-12-gogopool/blob/1c30b320b7105e57c92232408bc795b6d2dfa208/contracts/contract/MinipoolManager.sol#L329
> * This will fake the "high water" value: https://github.com/code-423n4/2022-12-gogopool/blob/1c30b320b7105e57c92232408bc795b6d2dfa208/contracts/contract/MinipoolManager.sol#L371
> * As there is a strict equality and that not all rewards may be sent by Rialto (only those really yielded by the validation), the staking end may never be triggered: https://github.com/code-423n4/2022-12-gogopool/blob/1c30b320b7105e57c92232408bc795b6d2dfa208/contracts/contract/MinipoolManager.sol#L399-L403, same for the `recordStakingError`

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/620#issuecomment-1416059877)**:**

> @Franfran - I can chime in here.

>
> When recreating a minipool, we intend to allow Node Operators to compound their staking rewards for the next cycle.
>
> Say that a minipool with 2000 AVAX was running. After one cycle the minipool was rewarded 20 AVAX. 15 AVAX goes to Node Operators and 5 AVAX to Liquid Stakers (in this example).
>
> When we recreate the minipool we want to allow the Node Operator to run a minipool with 1015 AVAX. Right now we require a 1:1 match of Node Operator to Liquid Staker funds, so that means we'll withdraw 1015 AVAX from the Liquid Staking pool. That's 10 AVAX more than we deposited from this one minipool. We are relying on there being 10 free floating AVAX in the Liquid Staking fund to recreate this minipool.
>
> The Warden says "The function assumes that a node operator and liquid stakers earned an equal reward amount". We're were not assuming that, but we are assuming that there will be some free AVAX in the Liquid Staker pool to withdraw more than we've just deposited from rewards.

>
> All that being said, we do not like this assumption and will change to use `avaxLiquidStakerAmt` instead of `avaxNodeOpAmt` for both. Ensuring that we will always have enough Liquid Staker AVAX to recreate the minipool and we will maintain the one-to-one match.

[**Alex the Entreprenerd (judge) set severity to Medium and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/620#issuecomment-1423878926)**:**

> The warden has shown a potential risk when it comes to accounting, fees and the requirement on liquid funds, more specifically the accounting in storage will use the values earned by the validator, however when recreating new funds will need to be pulled.
>
> The discrepancy may cause issues.
>
> I believe this report has shown a potential risk, but I also think the Warden should have spent more time explaining it in depth vs stopping at the potential invariant being broken.

>
> I'm flagging this out of caution after considering scrapping it / inviting the Wardens to follow up in mitigation review.

[**Jeiwan (warden) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/620#issuecomment-1424187308)**:**

> @emersoncloud -
>
> > The Warden says "The function assumes that a node operator and liquid stakers earned an equal reward amount". We're were not assuming that
>
> As can be seen from the linked code snippet (the comments, specifically):
>
> ```solidity
> // Compound the avax plus rewards
> // NOTE Assumes a 1:1 nodeOp:liqStaker funds ratio
> uint256 compoundedAvaxNodeOpAmt = mp.avaxNodeOpAmt + mp.avaxNodeOpRewardAmt;
> ```
>
> The assumption is that the 1:1 funds ratio is preserved after rewards have been accounted. This can only be true when the reward amounts are equal, which is violated due to the fees applied to `avaxLiquidStakerRewardAmt`.

>
> @Alex the Entreprenerd - I'm sorry for not providing more details on how this can affect the entire system. Yes, my assumption was that extra staker funds would be required to recreate a pool, and there might be not enough funds staked (and deeper accounting may be affected, as pointed out by @Franfran), while the earned rewards + the previous staked amounts would be enough to recreate a pool.
>
> Thus, the mitigation that uses `avaxLiquidStakerAmt` for both amounts looks good to me, since, out of the two amounts, the smaller one will always be picked, which won't require pulling extra funds from stakers. The difference between this mitigation and the mitigation suggested in the report, is that the latter uses the full reward amount in a recreated pool, while using `avaxLiquidStakerAmt` for both amounts leaves a portion of the reward idle.
>
> I also agree with the medium severity, the High Risk label was probably a misclick.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Use liquid staker avax amount instead of node op amount: [multisig-labs/gogopool#43](https://github.com/multisig-labs/gogopool/pull/43)

**Status:** Mitigation not confirmed. Full details in [report from RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/52), and also included in Mitigation Review section below.

-gogopool-findings/issues/498)_,_ [_immeas_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/491)_,_ [_Franfran_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/484)_,_ [_Nyx_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/439)_,_ [_Ch\_301_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/423)_,_ [_0xdeadbeef0x_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/398)_,_ [_HollaDieWaldfee_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/362)_,_ [_RaymondFam_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/353)_,_ [_cccz_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/332)_,_ [_0Kage_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/324)_, and_ [_kaliberpoziomka8552_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/269)

This issue is related to state transition of Minipools.\
According to the implementation, the possible states and transitions are as below.

pool is in states of `Withdrawable, Finished, Error, Canceled`.\
The problem is that these four states are not the same in the sense of holding the node operator's AVAX.\
If the state flow has followed `Prelaunch->Launched->Staking->Error`, all the AVAX are still in the vault.\
If the state flow has followed `Prelaunch->Launched->Staking->Error->Finished` (last transition by `withdrawMinipoolFunds`), all the AVAX are sent back to the node operator.\
So if the Rialto calls `recreateMinipool` for the second case, there are no AVAX deposited from the node operator at that point but there can be AVAX from other mini pools in the state of Prelaunch.\
Because there are AVAX in the vault (and these are not managed per staker base), `recreatePool` results in a new mini pool in `Prelaunch` state and it is further possible to go through the normal flow `Prelaunch->Launched->Staking->Withdrawable->Finished`.\
And the other minipool that was waiting for launch will not be able to launch because the vault is lack of AVAX.

Below is a test case written to show an example.

itAmt);

  // Node Op 1: Prelaunch -> Launched
  vm.prank(address(rialto));
  minipoolMgr.claimAndInitiateStaking(mp1.nodeID);

  // Node Op 1: Launched -> Staking
  vm.prank(address(rialto));
  minipoolMgr.recordStakingStart(mp1.nodeID, txID, block.timestamp);

  assertEq(staking.getAVAXStake(nodeOp), 0);
  assertEq(staking.getAVAXAssigned(nodeOp), depositAmt);
  assertEq(staking.getAVAXAssignedHighWater(nodeOp), depositAmt);

  // now try to launch the second operator's pool, it will fail with InsufficientContractBalance
  vm.prank(address(rialto));
  vm.expectRevert(Vault.InsufficientContractBalance.selector);
  minipoolMgr.claimAndInitiateStaking(mp2.nodeID);
}

```

#### Tools Used

Manual Review, Foundry

#### Recommended Mitigation Steps

Make sure to keep the node operator's deposit status the same for all states that can lead to the same state.\
For example, for all states that can transition to Prelaunch, make sure to send the AVAX back to the user and get them back on the call `recreateMiniPool()`.

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/569)

[**0xju1ie (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/569#issuecomment-1408511782)**:**

> I think [#213](https://github.com/code-423n4/2022-12-gogopool-findings/issues/213) might be a better primary. This one primarily depends on minipools going to staking->error which wouldn't actually happen unless Rialto made a mistake.

[**Alex the Entreprenerd (judge) decreased severity to Medium and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/569#issuecomment-1415814227)**:**

> The Warden has shown an issue with the FSM, Pools are allowed to perform the following transition\
> \> `Prelaunch->Launched->Staking->Error->Finished->Prelaunch` which allows to spin up the pool without funds.
>
> This could only happen if Rialto performs a mistake, so the finding is limited to highlighting the issue with the State Transition.

>
> For this reason, I believe Medium to be the most appropriate severity.

[**Franfran (warden) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/569#issuecomment-1415883621)**:**

> @Alex the Entreprenerd - Please note that the issue is not limited to Rialto doing a mistake, but it's actually possible to trick it by frontrunning the Rialto transaction as outlined in my finding: [#484 (comment)](https://github.com/code-423n4/2022-12-gogopool-findings/issues/484#issuecomment-1382584856)\
> That's why the high severity was chosen initially.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Atomically recreate minipool so a node operator can't withdraw inbetween: [multisig-labs/gogopool#23](https://github.com/multisig-labs/gogopool/pull/23)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/15) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/34).

-12-gogopool-findings/issues/555)

_Submitted by_ [_unforgiven_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/555)_, also found by_ [_caventa_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/522) _and_ [_rvierdiiev_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/251)

[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L271-L283](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L271-L283)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L642-L665](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L642-L665)

The value of `RewardsStartTime` shows when node runner started the minipool and validation rewards are generated by node runner.

it is used to see if node runners are eligible for ggp rewards or not and node runners should run their node for minimum amount of time during the rewarding cycle to be eligible for rewards. but right now node runner can create a mimipool and cancel it (after waiting time) and even so the minipool generated no rewards and cancelled the value of `RewardsStartTime` won't get reset for node runner and in the end of the cycle node runner would be eligible for rewards (node runner can create another minipool near the end of cycle). so this issue would cause wrong reward distribution between node runners and code doesn't correctly track `RewardsStartTime` for node runners and malicious node runners can use this issue and receive rewards without running validation nodes for the minimum amount of required time.

)));
		uint256 avaxLiquidStakerAmt = getUint(keccak256(abi.encodePacked("minipool.item", index, ".avaxLiquidStakerAmt")));

		Staking staking = Staking(getContractAddress("Staking"));
		staking.decreaseAVAXStake(owner, avaxNodeOpAmt);
		staking.decreaseAVAXAssigned(owner, avaxLiquidStakerAmt);

		staking.decreaseMinipoolCount(owner);

		emit MinipoolStatusChanged(nodeID, MinipoolStatus.Canceled);

		Vault vault = Vault(getContractAddress("Vault"));
		vault.withdrawAVAX(avaxNodeOpAmt);
		owner.safeTransferETH(avaxNodeOpAmt);
	}
```

As you can see there is no check that user's minipool count is zero and if it is to reset the value of `RewardsStartTime` for user so if a user creates a minipool in the start of the cycle and then cancel it after 5 days and wait for end of the cycle and start another minipool and increase his staking AVAX he would be eligible for ggp rewards (`ClaimNodeOp.isEligible()` would return `true` for that user even so the user didn't run node for the required amount of time in the cycle).

these are the steps to exploit this:

1. node runner would create a minipool near start time of the ggp rewarding cycle and the value of `RewardsStartTime` would set for node runner.
2. after 5 days that node runner's minipool has not been launched by multisig (for any reason) node runner would call `cancelMinipool()` and code would cancel his minipool but won't reset `RewardsStartTime` for node runner.
3. after 20 days and near end of the gpp reward cycle node runner would create another minipool and start running node.
4. in the end even so node runner only start running node and earning reward near end of the reward cycle but code would count node runner as eligible for rewards because `RewardsStartTime` for node runner shows wrong value.

This bug would cause rewards to be distributed wrongly between node runners and malicious node runners can bypass required time for running nodes during reward cycle to be eligible for rewards.

#### Tools Used

VIM

#### Recommended Mitigation Steps

Set the value of `RewardsStartTime` based on successfully finished minipools or when minipool is launched and user can't cancel minipool.

[**Alex the Entreprenerd (judge) decreased severity to Medium and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/555#issuecomment-1412633697)**:**

> The Warden has shown how, due to `cancelMinipool` not resetting `rewardsStartTime` a pool owner could receive rewards for time in which they did not have any activePool.
>
> Because this is contingent on the Multisig not cancelling the pool and because it would limit the attack to rewards, I believe Medium Severity to be the most appropriate.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Reset rewards start time in cancel minipool: [multisig-labs/gogopool#51](https://github.com/multisig-labs/gogopool/pull/51)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/16) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/35).

***

### [\[M-11\] MultisigManager may not be able to add a valid Multisig](https://github.com/code-423n4/2022-12-gogopool-findings/issues/521)

_Submitted by_ [_bin2chen_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/521)_, also found by_ [_immeas_](../../about-gogopool/undefined/)_,_ [_RaymondFam_](../../about-gogopool/undefined/)_,_ [_ast3ros_](../../about-gogopool/undefined/)_,_ [_cryptonue_](../../about-gogopool/undefined/)_,_ [_0xhunter_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/828)_,_ [_adriro_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/765)_,_ [_0xbepresent_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/349)_, and_ [_Saintcode\__](https://github.com/code-423n4/2022-12-gogopool-findings/issues/189)

When more than 10 mulitsig, it is impossible to modify or delete the old ones, making it impossible to create new valid ones.

#### Proof of Concept

MultisigManager limits the number of Multisig to 10, which cannot be deleted or replaced after they have been disabled.\
This will have a problem, if the subsequent use of 10, all 10 for some reason, be disabled.\
Then it is impossible to add new ones and replace the old ones, so you have to continue using the old Multisig at risk.

red();
        }
        uint256 index = getUint(keccak256("multisig.count"));
        if (index >= MULTISIG_LIMIT) {
            revert MultisigLimitReached(); //***@audit limt 10, and no other way to delete or replace the old Multisig ***//
        }
```

#### Recommended Mitigation Steps

Add replace old mulitsig method

```solidity
    function replaceMultisig(address addr,address oldAddr) external onlyGuardian {
        int256 multisigIndex = getIndexOf(oldAddr);
        if (multisigIndex == -1) {
            revert MultisigNotFound();
        }

        setAddress(keccak256(abi.encodePacked("multisig.item", multisigIndex, ".address")), addr);
        emit RegisteredMultisig(addr, msg.sender);
    }
```

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/521)

[**0xju1ie (GoGoPool) disagreed with severity and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/521#issuecomment-1396847761)**:**

> I'd argue Low since its unlikely.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/521#issuecomment-1396857560)**:**

> I disagree @0xju1ie. I think it's an oversight not to have a way to delete old multisigs with the limit in place rather than a quality assurance issue.

[**0xju1ie (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/521#issuecomment-1397034274)**:**

> [#349](https://github.com/code-423n4/2022-12-gogopool-findings/issues/349) has an interesting fix for this issue

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/521#issuecomment-1401952336)**:**

> Which was: "Count only the validated/enabled multisigs in order to control the limit."

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/521#issuecomment-1413624527)**:**

> The Warden has shown how, due to a logic flaw, the system can only ever add up to 10 multi sigs, even after disabling all, no more multi sigs could be added.
>
> Because this shows how an external condition can break the functionality of the MultisigManager, I agree with Medium Severity.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/521#issuecomment-1421429303)**:**

> Acknowledged.
>
> Not fixing right now, we don't foresee having many multisigs at launch, and will upgrade as necessary to support more.

eenETHlines_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/483)_,_ [_Allarious_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/458)_,_ [_stealthyz_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/281)_,_ [_mert\_eren_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/259)_, and_ [_0xdeadbeef0x_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/211)

[https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/MinipoolManager.sol#L225-L227](https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/MinipoolManager.sol#L225-L227)\
[https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/MinipoolManager.sol#L279-L281](https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/MinipoolManager.sol#L279-L281)

When canceling a minipool that was canceled before, it may skip `MinipoolCancelMoratoriumSeconds` checking and allow the user to cancel the minipool immediately.

#### Proof of Concept

A user may create a minipool.

```
/// @notice Accept AVAX deposit from node operator to create a Minipool. Node Operator must be staking GGP. Open to public.

ationRatio()) {
			revert InsufficientGGPCollateralization();
		}

		// Get a Rialto multisig to assign for this minipool
		MultisigManager multisigManager = MultisigManager(getContractAddress("MultisigManager"));
		address multisig = multisigManager.requireNextActiveMultisig();

		// Create or update a minipool record for nodeID
		// If nodeID exists, only allow overwriting if node is finished or canceled
		// 		(completed its validation period and all rewards paid and processing is complete)
		int256 minipoolIndex = getIndexOf(nodeID);
		if (minipoolIndex != -1) {
			onlyOwner(minipoolIndex);
			requireValidStateTransition(minipoolIndex, MinipoolStatus.Prelaunch);
			resetMinipoolData(minipoolIndex);
			// Also reset initialStartTime as we are starting a whole new validation
			setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".initialStartTime")), 0);

		} else {
			minipoolIndex = int256(getUint(keccak256("minipool.count")));
			// The minipoolIndex is stored 1 greater than actual value.

olIndex, ".avaxLiquidStakerAmt")), avaxAssignmentRequest);

		emit MinipoolStatusChanged(nodeID, MinipoolStatus.Prelaunch);

		Vault vault = Vault(getContractAddress("Vault"));
		vault.depositAVAX{value: msg.value}();
	}
```

and after 5 days, the user cancels the minipool

```
	/// @notice Owner of a minipool can cancel the (prelaunch) minipool
	/// @param nodeID 20-byte Avalanche node ID the Owner registered with
	function cancelMinipool(address nodeID) external nonReentrant {
		Staking staking = Staking(getContractAddress("Staking"));
		ProtocolDAO dao = ProtocolDAO(getContractAddress("ProtocolDAO"));
		int256 index = requireValidMinipool(nodeID);
		onlyOwner(index);
		// make sure they meet the wait period requirement
		if (block.timestamp - staking.getRewardsStartTime(msg.sender) < dao.getMinipoolCancelMoratoriumSeconds()) {
			revert CancellationTooEarly();
		}
		_cancelMinipoolAndReturnFunds(nodeID, index);
	}
```

Then, the user recreates the minipool again by calling the same createMinipool function.

Then, the user cancels the minipool immediately. The user should not be allowed to cancel the minpool immediately and he should wait for 5 more days.

Added a test unit to MinipoolManager.t.sol

```
	function testMinipoolManager() public {
		address nodeID1 = randAddress();

		vm.startPrank(nodeOp);
		ggp.approve(address(staking), MAX_AMT);
		staking.stakeGGP(100 ether);

		{
			MinipoolManager.Minipool memory mp = createMyMinipool(nodeID1, 1000 ether, 1000 ether, 2 weeks);

			skip(5 days);
			minipoolMgr.cancelMinipool(mp.nodeID); // Must skip 5 days to be executed
		}

		{
			MinipoolManager.Minipool memory mp = createMyMinipool(nodeID1, 1000 ether, 1000 ether, 2 weeks);
			minipoolMgr.cancelMinipool(mp.nodeID); // Do not need 5 days more to be executed which is wrong
		}

		vm.stopPrank();
	}
```

#### Tools Used

Manual and added a test unit

#### Recommended Mitigation Steps

Change the createMinipool function. Always setRewardsStartTime everytime the minipool is recreated.

```
/// @notice Accept AVAX deposit from node operator to create a Minipool. Node Operator must be staking GGP. Open to public.

ratio < dao.getMinCollateralizationRatio()) {
			revert InsufficientGGPCollateralization();
		}

		// Get a Rialto multisig to assign for this minipool
		MultisigManager multisigManager = MultisigManager(getContractAddress("MultisigManager"));
		address multisig = multisigManager.requireNextActiveMultisig();

		// Create or update a minipool record for nodeID
		// If nodeID exists, only allow overwriting if node is finished or canceled
		// 		(completed its validation period and all rewards paid and processing is complete)
		int256 minipoolIndex = getIndexOf(nodeID);
		if (minipoolIndex != -1) {
			requireValidStateTransition(minipoolIndex, MinipoolStatus.Prelaunch);
			resetMinipoolData(minipoolIndex);
			// Also reset initialStartTime as we are starting a whole new validation
			setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".initialStartTime")), 0);
		} else {
			minipoolIndex = int256(getUint(keccak256("minipool.count")));
			// The minipoolIndex is stored 1 greater than actual value.

tionFee")), delegationFee);
		setAddress(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".owner")), msg.sender);
		setAddress(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".multisigAddr")), multisig);
		setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".avaxNodeOpInitialAmt")), msg.value);
		setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".avaxNodeOpAmt")), msg.value);
		setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".avaxLiquidStakerAmt")), avaxAssignmentRequest);

		emit MinipoolStatusChanged(nodeID, MinipoolStatus.Prelaunch);

		Vault vault = Vault(getContractAddress("Vault"));
		vault.depositAVAX{value: msg.value}();
	}
```

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/519)

[**0xju1ie (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/519#issuecomment-1398302235)**:**

> This solution would mess up other aspects of the protocol.

In cancel minipool, we should really just check the minipoolStartTime against the cancelMoratoriumSeconds.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/519#issuecomment-1407750433)**:**

> The warden has shown a logic flaw in the Finite State Machine, as shown in the POC, cancelling a second miniPool can be done before `MinipoolCancelMoratoriumSeconds`.
>
> Because the exploit doesn't demonstrate a reliable way to extra value or funds from the protocol, I agree with Medium Severity.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Base cancelMinipool delay on minipool creation time not rewards start time: [multisig-labs/gogopool#40](https://github.com/multisig-labs/gogopool/pull/40)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/17) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/37).

s://github.com/code-423n4/2022-12-gogopool-findings/issues/494)_, also found by_ [_HollaDieWaldfee_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/886)_,_ [_datapunk_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/826)_,_ [_wagmi_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/645)_,_ [_yixxas_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/561)_,_ [_ck_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/437)_,_ [_cccz_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/333)_,_ [_nameruse_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/278)_,_ [_cozzetti_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/183)_,_ [_0x73696d616f_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/142)_, and_ [_koxuan_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/131)

When creating a minipool the node operator is required to put up a collateral in `GGP`, the protocol token.

The amount of `GGP` collateral needed is currently calculated to be 10% of the `AVAX` staked. This is calculated using the price of `GGP - AVAX`.

If the node operator doesn't have high enough availability and doesn't get any rewards the protocol will slash their `GGP` collateral to reward liquid stakers. This is also calculated using the price of `GGP - AVAX`:

```javascript
File: MinipoolManager.sol

547:	function calculateGGPSlashAmt(uint256 avaxRewardAmt) public view returns (uint256) {
548:		Oracle oracle = Oracle(getContractAddress("Oracle"));
549:		(uint256 ggpPriceInAvax, ) = oracle.getGGPPriceInAVAX(); // price might change or be manipulated
550:		return avaxRewardAmt.divWadDown(ggpPriceInAvax);
551:	}

...

670:	function slash(int256 index) private {

...

673:		uint256 duration = getUint(keccak256(abi.encodePacked("minipool.item", index, ".duration")));
674:		uint256 avaxLiquidStakerAmt = getUint(keccak256(abi.encodePacked("minipool.item", index, ".avaxLiquidStakerAmt")));
675:		uint256 expectedAVAXRewardsAmt = getExpectedAVAXRewardsAmt(duration, avaxLiquidStakerAmt);
676:		uint256 slashGGPAmt = calculateGGPSlashAmt(expectedAVAXRewardsAmt);

...

681:		Staking staking = Staking(getContractAddress("Staking"));
682:		staking.slashGGP(owner, slashGGPAmt);
683:	}
```

This is then subtracted from their staked amount:

```javascript
File: Staking.sol

94: 	function decreaseGGPStake(address stakerAddr, uint256 amount) internal {
95: 		int256 stakerIndex = requireValidStaker(stakerAddr);
96: 		subUint(keccak256(abi.encodePacked("staker.item", stakerIndex, ".ggpStaked")), amount); // can fail due to underflow
97: 	}

...

379:	function slashGGP(address stakerAddr, uint256 ggpAmt) public onlySpecificRegisteredContract("MinipoolManager", msg.sender) {
380:		Vault vault = Vault(getContractAddress("Vault"));
381:		decreaseGGPStake(stakerAddr, ggpAmt);
382:		vault.transferToken("ProtocolDAO", ggp, ggpAmt);
383:	}
```

The issue is that the current staked amount is never checked so the `subUint` can fail due to underflow if the price has changed since the minipool was created/recreated.

#### Impact

If a node operator doesn't have enough collateral, possibly caused by price changes in `GGP` during slashing they evade slashing all together.

It's even possible for the node operator to foresee this and manipulate the price of `GGP` just prior to the period ending if they know that they are going to be slashed.

tPrank(nodeOp);
		ggp.approve(address(staking), MAX_AMT);
		staking.stakeGGP(ggpStakeAmt);
		MinipoolManager.Minipool memory mp1 = createMinipool(depositAmt, avaxAssignmentRequest, duration);
		vm.stopPrank();

		address liqStaker1 = getActorWithTokens("liqStaker1", MAX_AMT, MAX_AMT);
		vm.prank(liqStaker1);
		ggAVAX.depositAVAX{value: MAX_AMT}();

		vm.prank(address(rialto));
		minipoolMgr.claimAndInitiateStaking(mp1.nodeID);

		bytes32 txID = keccak256("txid");
		vm.prank(address(rialto));
		minipoolMgr.recordStakingStart(mp1.nodeID, txID, block.timestamp);

		skip(2 weeks);

		vm.prank(address(rialto)); // price changes just a bit
		oracle.setGGPPriceInAVAX(0.999 ether, block.timestamp);

		vm.prank(address(rialto));
		vm.expectRevert(); // staking cannot end because of underflow
		minipoolMgr.recordStakingEnd{value: validationAmt}(mp1.nodeID, block.timestamp, 0 ether);
	}
```

The only thing the protocol can do now is to call `recordStakingError` for the minipool, since no other state changes are allowed.

This will return the staked funds but it will not slash the `GGP` amount for the node operator. Hence the node operator has evaded the slashing.

#### Tools Used

vs code, forge

#### Recommended Mitigation Steps

If the amount to be slashed is greater than what the node operator has staked, slash all their stake.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/494#issuecomment-1416338579)**:**

> The Warden has shown a risk to the protocol, in cases in which the price of GPP drops too low, slashing could not be performed.
>
> In contrast to other reports, this is a finding that shows an issue with the system and it's consequences, more so than an economic attack.
>
> For this reason I believe Medium to be the most appropriate severity.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> If staked GGP doesn't cover slash amount, slash it all: [multisig-labs/gogopool#41](https://github.com/multisig-labs/gogopool/pull/41)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/56) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/38).

tps://github.com/code-423n4/2022-12-gogopool-findings/issues/492)_, also found by_ [_unforgiven_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/880)_,_ [_V\_B_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/841)_,_ [_0xbepresent_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/345)_,_ [_0xdeadbeef0x_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/215)_, and_ [_0x73696d616f_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/138)

[https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/MinipoolManager.sol#L196-L269](https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/MinipoolManager.sol#L196-L269)\
[https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/MinipoolManager.sol#L560](https://github.com/code-423n4/2022-12-gogopool/blob/main/contracts/contract/MinipoolManager.sol#L560)

When a node operator creates a minipool they pass which duration they want to stake for.

There is no validation for this field so they can pass any field:

```javascript
File: MinipoolManager.sol

196:	function createMinipool(
197:		address nodeID,
198:		uint256 duration,
199:		uint256 delegationFee,
200:		uint256 avaxAssignmentRequest
201:	) external payable whenNotPaused {

...     // no validation for duration

256:		setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".status")), uint256(MinipoolStatus.Prelaunch));
257:		setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".duration")), duration); // duration stored
258:		setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".delegationFee")), delegationFee);
```

Later when staking is done.

if the node op was slashed, `duration` is used to calculate the slashing amount:

```javascript
File: MinipoolManager.sol

557:	function getExpectedAVAXRewardsAmt(uint256 duration, uint256 avaxAmt) public view returns (uint256) {
558:		ProtocolDAO dao = ProtocolDAO(getContractAddress("ProtocolDAO"));
559:		uint256 rate = dao.getExpectedAVAXRewardsRate();
560:		return (avaxAmt.mulWadDown(rate) * duration) / 365 days;
561:	}

...

670:	function slash(int256 index) private {

...

673:		uint256 duration = getUint(keccak256(abi.encodePacked("minipool.item", index, ".duration")));
674:		uint256 avaxLiquidStakerAmt = getUint(keccak256(abi.encodePacked("minipool.item", index, ".avaxLiquidStakerAmt")));
675:		uint256 expectedAVAXRewardsAmt = getExpectedAVAXRewardsAmt(duration, avaxLiquidStakerAmt);
676:		uint256 slashGGPAmt = calculateGGPSlashAmt(expectedAVAXRewardsAmt);
```

The node operator cannot pass in `0` because that reverts due to zero transfer check in Vault.

However the node operator can pass in `1` to guarantee the lowest slash amount possible.

Rialto might fail this, but there is little information about how Rialto uses the `duration` passed. According to this comment they might default to `14 days` in which this finding is valid:

> JohnnyGault — 12/30/2022 3:22 PM

> To clarify duration for everyone -- a nodeOp can choose a duration they want, from 14 days to 365 days. But behind the scenes, Rialto will only create a validator for 14 days. ...

#### Impact

The node operator can send in a very low `duration` to get minimize slashing amounts. It depends on the implementation in Rialto, which we cannot see. Hence submitting this.

ether);

		assertEq(vault.balanceOf("MinipoolManager"), depositAmt);

		int256 minipoolIndex = minipoolMgr.getIndexOf(mp1.nodeID);
		MinipoolManager.Minipool memory mp1Updated = minipoolMgr.getMinipool(minipoolIndex);
		assertEq(mp1Updated.status, uint256(MinipoolStatus.Withdrawable));
		assertEq(mp1Updated.avaxTotalRewardAmt, 0);
		assertTrue(mp1Updated.endTime != 0);

		assertEq(mp1Updated.avaxNodeOpRewardAmt, 0);
		assertEq(mp1Updated.avaxLiquidStakerRewardAmt, 0);

		assertEq(minipoolMgr.getTotalAVAXLiquidStakerAmt(), 0);

		assertEq(staking.getAVAXAssigned(mp1Updated.owner), 0);
		assertEq(staking.getMinipoolCount(mp1Updated.owner), 0);

		// very small slash amount
		assertLt(mp1Updated.ggpSlashAmt, 0.000_01 ether);
		assertGt(staking.getGGPStake(mp1Updated.owner), ggpStakeAmt - 0.000_01 ether);
	}
```

#### Tools Used

vs code, forge

#### Recommended Mitigation Steps

Regardless if Rialto will fail this or not, I recommend that the `duration` passed is validated to be within `14 days` and `365 days`.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/492#issuecomment-1413678353)**:**

> The Warden has shown how, due to a lack of check, a duration below 14 days can be set, this could also be used to reduce the slash penalty.
>
> I believe that in reality, such a pool will be closed via `recordStakingError`, however, this enables a grief that could impact the Protocol in a non-trivial manner.
>
> For this reason, I believe the most appropriate severity to be Medium.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Added bounds for duration passed by Node Operator: [multisig-labs/gogopool#38](https://github.com/multisig-labs/gogopool/pull/38)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/57) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/39).

09](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L88-L109)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L166-L178](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L166-L178)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L180-L189](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L180-L189)

Function `syncRewards()` distributes rewards to TokenggAVAX holders, it linearly distribute cycle's rewards from `block.timestamp` to the cycle end time which is next multiple of the `rewardsCycleLength` (the end time of the cycle is defined and the real duration of the cycle changes).

when a cycle ends `syncRewards()` should be called so the next cycle starts but if `syncRewards()` doesn't get called fast, then users depositing or withdrawing funds before call to `syncRewards()` would lose their rewards and those rewards would go to users who deposited funds after `syncRewards()` call. contract should try to start the next cycle whenever deposit or withdraw happens to make sure rewards are distributed fairly between users.

#### Proof of Concept

This is `syncRewards()` code:

```
	function syncRewards() public {
		uint32 timestamp = block.timestamp.safeCastTo32();

		if (timestamp < rewardsCycleEnd) {
			revert SyncError();
		}

		uint192 lastRewardsAmt_ = lastRewardsAmt;
		uint256 totalReleasedAssets_ = totalReleasedAssets;
		uint256 stakingTotalAssets_ = stakingTotalAssets;

		uint256 nextRewardsAmt = (asset.balanceOf(address(this)) + stakingTotalAssets_) - totalReleasedAssets_ - lastRewardsAmt_;

		// Ensure nextRewardsCycleEnd will be evenly divisible by `rewardsCycleLength`.

uint32 nextRewardsCycleEnd = ((timestamp + rewardsCycleLength) / rewardsCycleLength) * rewardsCycleLength;

		lastRewardsAmt = nextRewardsAmt.safeCastTo192();
		lastSync = timestamp;
		rewardsCycleEnd = nextRewardsCycleEnd;
		totalReleasedAssets = totalReleasedAssets_ + lastRewardsAmt_;
		emit NewRewardsCycle(nextRewardsCycleEnd, nextRewardsAmt);
	}
```

As you can see whenever this function is called it starts the new cycle and sets the end of the cycle to the next multiple of the `rewardsCycleLength` and it release the rewards linearly between current timestamp and cycle end time. So if `syncRewards()` get called near to multiple of the `rewardsCycleLength` then rewards would be distributed with higher speed in less time.

The problem is that users depositing funds before call `syncRewards()` won't receive new cycles rewards and early depositing won't get considered in reward distribution if deposits happen before `syncRewards()` call and if a user withdraws his funds before the `syncRewards()` call then he receives no rewards.

Imagine this scenario:

1. `rewardsCycleLength` is 10 days and the rewards for the next cycle is `100` AVAX.
2. the last cycle has been ended and user1 has `10000` AVAX deposited and has 50% of the pool shares.
3. `syncRewards()` don't get called for 8 days.
4. users1 withdraws his funds receive `10000` AVAX even so he deposits for 8 days in the current cycle.
5. users2 deposit `1000` AVAX and get 10% of pool shares and the user2 would call `syncRewards()` and contract would start distributing `100` avax as reward.
6.

after 2 days cycle would finish and user2 would receive `100 * 10% = 10` AVAX as rewards for his `1000` AVAX deposit for 2 days but user1 had `10000` AVAX for 8 days and would receive 0 rewards.

So rewards won't distribute fairly between depositors across the time and any user interacting with contract before the `syncRewards()` call can lose his rewards. Contract won't consider deposit amounts and duration before `syncRewards()` call and it won't make sure that `syncRewards()` logic would be executed as early as possible with deposit or withdraw calls when a cycle ends.

#### Tools Used

VIM

#### Recommended Mitigation Steps

One way to solve this is to call `syncRewards()` logic in each deposit or withdraw and make sure that cycles start as early as possible (the revert "SyncError()" in the `syncRewards()` should be removed for this).

[**emersoncloud (GoGoPool) disagreed with severity and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/478#issuecomment-1382098984)**:**

> I think that medium severity is more appropriate. User funds aren't drained or lost, but liquid staking rewards may be unfairly calculated.
>
> Good find. I think there is something we could do to either incentivize the `syncRewards` call or call it on deposit and withdraw.
>
> But I disagree with the concept that the user who staked for 8 days is entitled to rewards for staking. Rewards depend on properly running minipools. Reward amounts can fluctuate depending on the utilization of liquid staking funds by minipools.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/478#issuecomment-1401657682)**:**

> After some more discussion, this is working as designed.

And Rialto will call `syncRewards` at the start of each reward cycle, so the possible loss to the user who withdraws before `syncRewards` was supposed to be called is mitigated.

[**Alex the Entreprenerd (judge) decreased severity to Medium and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/478#issuecomment-1415624850)**:**

> The Warden has shown a potential risk for end-users that withdraw before `syncRewards` is called.
>
> Because the finding pertains to a loss of yield, I believe the finding to be of Medium Severity.
>
> While Rialto may call this as a perfect actor, we cannot guarantee that a end user could forfeit some amount of yield, due to external conditions.
>
> I believe this finding to potentially be a nofix, as long as all participants are aware of the mechanic.

>
> Per discussions had on [#99](https://github.com/code-423n4/2022-12-gogopool-findings/issues/99), I don't believe that any specific MEV attack has been identified, however this finding does highlight a potential risk that a mistimed withdrawal could cause.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/478#issuecomment-1421430629)**:**

> Acknowledged.
>
> Not fixing but will add a note in our docs.

om/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L205-L213](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L205-L213)

Functions `maxWithdraw()` and `maxRedeem()` returns max amount of assets or shares owner would be able to withdraw taking into account liquidity in the TokenggAVAX contract, but logics don't consider that when user withdraws the withdrawal amounts subtracted from `totalReleasedAssets` (in `beforeWithdraw()` function) so the maximum amounts that can user withdraws should always be lower than `totalReleasedAssets` (which shows all the deposits and withdraws) but because functions `maxWithdraw()` and `maxRedeem()` uses `totalAssets()` to calculate available AVAX which includes deposits and current cycle rewards so those functions would return wrong value (whenever the return value is bigger than `totalReleaseAssets` then it would be wrong).

#### Proof of Concept

This is `beforeWithdraw()` code:

```
	function beforeWithdraw(
		uint256 amount,
		uint256 /* shares */
	) internal override {
		totalReleasedAssets -= amount;
	}
```

This is `beforeWithdraw()` code which is called whenever users withdraws their funds and as you can see the amount of withdrawal assets subtracted from `totalReleaseAssets` so withdrawal amounts can never be bigger than `totalReleaseAssets`.

This is `maxWithdraw()` code:

```
	function maxWithdraw(address _owner) public view override returns (uint256) {
		if (getBool(keccak256(abi.encodePacked("contract.paused", "TokenggAVAX")))) {
			return 0;
		}
		uint256 assets = convertToAssets(balanceOf[_owner]);
		uint256 avail = totalAssets() - stakingTotalAssets;
		return assets > avail ? avail : assets;
	}
```

As you can see to calculate available AVAX in the contract address code uses `totalAssets() - stakingTotalAssets` and `totalAssets()` shows deposits + current cycle rewards so `totalAssets()` is bigger than `totalReleaseAssets` and the value of the `totalAssets() - stakingTotalAssets` can be bigger than `totalReleaseAssets` and if code returns `avail` as answer then the return value would be wrong.

Imagine this scenario:

1. `totalReleaseAssets` is `10000` AVAX.
2. `stakingTotalAssets` is `1000` AVAX.
3. current cycle rewards is `4000` AVAX and `block.timestamp` is currently in the middle of the cycle so current rewards is `2000` AVAX.
4.

`totalAssets()` is `totalReleaseAssets + current rewards = 10000 + 2000 = 12000`.
5. contract balance is `10000 + 4000 - 1000 = 13000` AVAX.
6. user1 has 90% contract shares and calls `maxWithdraw()` and code would calculate user assets as `10800` AVAX and available AVAX in contract as `totalAssets() - stakingTotalAssets = 12000 - 1000 = 11000` and code would return `10800` as answer.
7. now if user1 withdraws `10800` AVAX code would revert in the function `beforeWithdraw()` because code would try to execute `totalReleaseAssets = totalReleaseAssets - amount = 10000 - 10800` and it would revert because of the underflow. so in reality user1 couldn't withdraw `10800` AVAX which was the return value of the `maxWithdraw()` for user1.

The root cause of the bug is that the withdrawal amount is subtracted from `totalReleaseAssets` and so max withdrawal can never be `totalReleaseAssets` and function `maxWithdraw()` should never return value bigger than `totalReleaseAssets`.

(the bug in function `maxRedeem()` is similar)

This bug would cause other contract or front end calls to fail, for example if the logic is something like this:

```
   amount = maxWithdraw(user);
   TokenggAVAX.withdrawAVAX(amount);
```

According the function definitions this code should work bug because of the the issue there are situations that this would revert and other contracts and UI can't work properly with the protocol.

#### Tools Used

VIM

#### Recommended Mitigation Steps

Consider `totalReleaseAssets` in max withdrawal amount too.

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/476)

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/476#issuecomment-1412684720)**:**

> The Warden has shown an inconsistency between the view functions and the actual behaviour of `TokenggAVAX`.\
> This breaks ERC4626, as well as offering subpar experience for end-users.

>
> For this reason I agree with Medium Severity.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/476#issuecomment-1421431600)**:**

> Acknowledged.
>
> I've added some tests to explore this more, but it's a known issue with how we've implemented the streaming of rewards in our 4626. Some more context here https://github.com/fei-protocol/ERC4626/issues/24.
>
> It's most prevalent with low liquidity in ggAVAX.
>
> We're not going to fix in the first iteration of protocol.

192)

[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L484](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L484)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L56](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L56)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L89](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L89)

The [documentation](https://multisiglabs.notion.site/Architecture-Protocol-Overview-4b79e351133f4d959a65a15478ec0121) says that the NodeOps could be elegible for GGP rewards if they have a valid minipool.

The problem is that if the MiniPool [has an error](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L484) while registering the node as a validator, the NodeOp can get rewards even if the minipool had an error.

When the Rialto calls `recordStakingError()` function the `AssignedHighWater` is not reseted. So the malicious NodeOp (staker) can create pools which will have an error in the registration and get rewards from the protocol.

#### Proof of Concept

I created a test in `ClaimNodeOp.t.sol`:

1. NodeOp1 creates minipool
2. Rialto calls claimAndInitiateStaking, recordStakingStart and recordStakingError()
3. NodeOp1 withdraw his funds from minipool
4. NodeOp1 can get rewards even if there was an error with the node registration as validator.

```solidity
function testRecordStakingErrorCanGetRewards() public {
    // NodeOp can get rewards even if there was an error in registering the node as a validator
    // 1.

NodeOp1 creates minipool
    // 2. Rialot/multisig claimAndInitiateStaking, recordStakingStart and recordStakingError
    // 3. NodeOp1 withdraw his funds from minipool
    // 4. NodeOp1 can get rewards even if there was an error with the node registration as validator.
    address nodeOp1 = getActorWithTokens("nodeOp1", MAX_AMT, MAX_AMT);
    uint256 duration = 2 weeks;
    uint256 depositAmt = 1000 ether;
    uint256 avaxAssignmentRequest = 1000 ether;
    skip(dao.getRewardsCycleSeconds());
    rewardsPool.startRewardsCycle();
    //
    // 1. NodeOp1 creates minipool
    //
    vm.startPrank(nodeOp1);
    ggp.approve(address(staking), MAX_AMT);
    staking.stakeGGP(200 ether);
    MinipoolManager.Minipool memory mp1 = createMinipool(depositAmt, avaxAssignmentRequest, duration);
    vm.stopPrank();
    address liqStaker1 = getActorWithTokens("liqStaker1", MAX_AMT, MAX_AMT);
    vm.prank(liqStaker1);
    ggAVAX.depositAVAX{value: MAX_AMT}();
    //
    // 2.

p1.nodeID);
    bytes32 txID = keccak256("txid");
    vm.prank(address(rialto));
    minipoolMgr.recordStakingStart(mp1.nodeID, txID, block.timestamp);
    bytes32 errorCode = "INVALID_NODEID";
    int256 minipoolIndex = minipoolMgr.getIndexOf(mp1.nodeID);
    skip(2 weeks);
    vm.prank(address(rialto));
    minipoolMgr.recordStakingError{value: depositAmt + avaxAssignmentRequest}(mp1.nodeID, errorCode);
    assertEq(vault.balanceOf("MinipoolManager"), depositAmt);
    MinipoolManager.Minipool memory mp1Updated = minipoolMgr.getMinipool(minipoolIndex);
    assertEq(mp1Updated.avaxTotalRewardAmt, 0);
    assertEq(mp1Updated.errorCode, errorCode);
    assertEq(mp1Updated.avaxNodeOpRewardAmt, 0);
    assertEq(mp1Updated.avaxLiquidStakerRewardAmt, 0);
    assertEq(minipoolMgr.getTotalAVAXLiquidStakerAmt(), 0);
    assertEq(staking.getAVAXAssigned(mp1Updated.owner), 0);
    // The highwater doesnt get reset in this case
    assertEq(staking.getAVAXAssignedHighWater(mp1Updated.owner), depositAmt);
    //
    // 3.

NodeOp1 withdraw his funds from the minipool
    //
    vm.startPrank(nodeOp1);
    uint256 priorBalance_nodeOp = nodeOp1.balance;
    minipoolMgr.withdrawMinipoolFunds(mp1.nodeID);
    assertEq((nodeOp1.balance - priorBalance_nodeOp), depositAmt);
    vm.stopPrank();
    //
    // 4. NodeOp1 can get rewards even if there was an error with the node registration as validator.

//
    skip(2629756);
    vm.startPrank(address(rialto));
    assertTrue(nopClaim.isEligible(nodeOp1)); //<- The NodeOp1 is eligible for rewards
    nopClaim.calculateAndDistributeRewards(nodeOp1, 200 ether);
    vm.stopPrank();
    assertGt(staking.getGGPRewards(nodeOp1), 0);
    vm.startPrank(address(nodeOp1));
    nopClaim.claimAndRestake(staking.getGGPRewards(nodeOp1)); //<- Claim nodeOp1 rewards
    vm.stopPrank();
}
```

#### Tools used

Foundry/VsCode

#### Recommended Mitigation Steps

The `MinipoolManager.sol::recordStakingError()` function should reset the Assigned high water `staking.resetAVAXAssignedHighWater(stakerAddr);` so the user can not claim rewards for a minipool with errors.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/471#issuecomment-1382233034)**:**

> Good find.

This is unique in terms of calling out `avaxAssignedHighWater` but I'm going to link other issues dealing with `recordStakingError`
>
> https://github.com/code-423n4/2022-12-gogopool-findings/issues/819

[**emersoncloud (GoGoPool) disagreed with severity and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/471#issuecomment-1382233406)**:**

> Since this is not a leak of funds in the protocol but GGP rewards instead, I think a medium designation is more appropriate

[**0xju1ie (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/471#issuecomment-1397195132)**:**

> So the warden is incorrect about the order of events that should happen, the correct order is the following:
>
> 1. NodeOp1 creates minipool
> 2. Rialto calls `claimAndInitiateStaking()`
> 3. Rialto calls `recordStakingStart()` if the staking with avalanche was successful. If it was not, Rialto will call `recordStakingError()`.

So Rialto will never be calling both of these functions, it is one or the other.
>
> `avaxAssignedHighWater` is only changed in `recordStakingStart()`, so not sure we would want to reset it in `recordStakingError()`.
>
> Questioning the validity of the issue.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/471#issuecomment-1398365148)**:**

> The key issue is that a minipool won't ever go from `Staking` to `Error` state. It's currently allowed in our state machine but it's not a situation that can happen on the Avalanche network and something we'll fix. In that way it depends on Rialto making a mistake to transition the minipool from staking to error.
>
> I think pointing out the issue in our state machine is valid and QA level.

[**Alex the Entreprenerd (judge) decreased severity to Medium and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/471#issuecomment-1415584261)**:**

> The Warden has highlighted an issue with the FSM of the system.
>
> While Rialto is assumed as a perfect actor, the code allows calling `recordStakingStart` and then `recordStakingError`.
>
> This state transition is legal, however will cause issues, such as setting `avaxAssignedHighWater` to a higher value than intended, which could allow the staker to be entitled to rewards.
>
> Because the State Transition will not happen in reality (per the Scope Requirements), am downgrading the finding to Medium Severity and believe the State Transition Check should be added to offer operators and end users a higher degree of on-chain guarantees.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Remove the state transition from Staking to Error: [multisig-labs/gogopool#28](https://github.com/multisig-labs/gogopool/pull/28)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/58) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/42).

28d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L191](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L191)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L88](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L88)

The `totalReleasedAssets` variable is updated on the [syncRewards()](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L88) function if someone calls the function before `rewardsCycleEnd` the [redeemAVAX()](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L191) will be reverted because the `totalReleasedAssets` may not include all the rewards.

The ggAvax holder can not redeem his funds until the `rewardsCycleEnd`.

#### Proof of Concept

I did the next test:

1. Create minipool (2000 avax)
2. Deposit rewards to the minipool (200 AVAX rewards)
3. Sync the rewards before the cycle ends
4. Redeem function will revert
5. Redeem will be available after the cycle end

```solidity
function testRedeemUnderOverFlow() public {
    // Redeem function reverts arithmetic error
    // 1.- Create minipool
    // 2.- Deposit rewards to the minipool
    // 3.- Sync the Rewards before the cycle end
    // 4.- Redeem function will revert
    // 5.- Redeem will be available after the cycle end.

ewards amount:", rewardsAmt / 1 ether);
    vm.deal(address(rialto), address(rialto).balance + rewardsAmt);
    vm.prank(address(rialto));
    minipoolMgr.recordStakingEnd{value: nodeAmt + rewardsAmt}(mp.nodeID, block.timestamp, rewardsAmt);
    //
    // 3.- Sync the Rewards before the cycle end
    //
    ggAVAX.syncRewards();
    uint256 maxRedeemSharesBob = ggAVAX.maxRedeem(bob);
    console.log("TotalReleasedAssets after syncRewards:", ggAVAX.totalReleasedAssets() / 1 ether);
    console.log("LastRewards after syncRewards:", ggAVAX.lastRewardsAmt() / 1 ether);
    console.log("Bob maxRedeem():", maxRedeemSharesBob / 1 ether);
    //
    // 4.- Redeem function will revert
    //
    skip(1 days);
    console.log("Bob PreviewRedeem() after skip one day:", ggAVAX.previewRedeem(maxRedeemSharesBob) / 1 ether);
    vm.prank(bob);
    vm.expectRevert(stdError.arithmeticError); // Revert by arithmetic error
    ggAVAX.redeemAVAX(maxRedeemSharesBob);
    //
    // 5.- Redeem will be available after the cycle end.

b);
    console.log("");
    console.log("TotalReleasedAssets after syncRewards:", ggAVAX.totalReleasedAssets() / 1 ether);
    console.log("LastRewards after syncRewards:", ggAVAX.lastRewardsAmt() / 1 ether);
    console.log("Bob maxRedeem():", maxRedeemSharesBob / 1 ether);
    console.log("Bob PreviewRedeem() after skip to the cycle end:", ggAVAX.previewRedeem(maxRedeemSharesBob) / 1 ether);
    vm.prank(bob);
    ggAVAX.redeemAVAX(maxRedeemSharesBob);
}
```

Output:

```
[PASS] testRedeemUnderOverFlow() (gas: 1244356)
Logs:
  Rewards amount: 200
  TotalReleasedAssets after syncRewards: 1200
  LastRewards after syncRewards: 85
  Bob maxRedeem(): 1200
  Bob PreviewRedeem() after skip one day: 1206

  TotalReleasedAssets after syncRewards: 1285
  LastRewards after syncRewards: 0
  Bob maxRedeem(): 1200
  Bob PreviewRedeem() after skip to the cycle end: 1285
```

#### Tools used

Foundry/VsCode

#### Recommended Mitigation Steps

Consider redeem the max available amount for the shares owner instead of revert.

The `maxRedeem()` function amount is not the same as the `previewRedeem()` amount.

[**emersoncloud (GoGoPool) acknowledged and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/317#issuecomment-1385070739)**:**

> This is a known issue that we don't intend to fix. The issue is most likely to present itself at the very start of the ggAVAX and not during typical operation. There's a bit more explanation here: https://github.com/fei-protocol/ERC4626/issues/24
>
> I don't believe redeeming max available is an appropriate solution because the spec for redeem reads
>
> > MUST revert if all of shares cannot be redeemed (due to withdrawal limit being reached, slippage, the owner not having enough shares, etc).

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/317#issuecomment-1409217179)**:**

> The Warden has shown a scenario in which `maxRedeem` can revert.

>
> While this can be attributed to rounding errors, it ultimately is possible for certain depositors to lose marginal amounts of their rewards or principal.
>
> Because of the reduced impact, I agree with Medium Severity.
>
> This is a hedge case that has been argued to have happened very rarely, and for this reason, I maintain that the severity is Medium, but can agree with a nofix, as the worst case will require the Sponsor to offer a small amount of additional token, to allow the last withdrawer to maxRedeem.

opool-findings/issues/603)_,_ [_SmartSek_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/590)_,_ [_bin2chen_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/511)_,_ [_Allarious_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/504)_,_ [_cccz_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/326)_,_ [_kaliberpoziomka8552_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/274)_,_ [_rvierdiiev_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/253)_, and_ [_Saintcode\__](https://github.com/code-423n4/2022-12-gogopool-findings/issues/188)

The `MinipoolManager.recordStakingError` function ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L484-L515](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L484-L515)) does not decrease the `minipoolCount` of the staker.

This means that if a staker has a minipool that encounters an error, his `minipoolCount` can never go to zero again.

This is bad because the `minipoolCount` is used in `ClaimNodeOp.calculateAndDistributeRewards` to determine if the `rewardsStartTime` of the staker should be reset ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L81-L84](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L81-L84)).

Since the `minipoolCount` cannot go to zero, the `rewardsStartTime` will never be reset.

This means that the staker is immediately eligible for rewards when he creates a minipool again whereas he should have to wait `rewardsEligibilityMinSeconds` before he is eligible (which is 14 days at the moment) ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L51](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L51)).

To conclude, failing to decrease the `minipoolCount` allows the staker to earn higher rewards because he is eligible for staking right after he creates a new minipool and does not have to wait again.

#### Proof of Concept

I have created the following test that you can add to the `MinipoolManager.t.sol` file that logs the `minipoolCount` in the `Staking`, `Error` and `Finished` state.

The `minipoolCount` is always `1` although it should decrease to `0` when `recordStakingError` is called.

);
    // minipool count when in "Staking" state: 1
    console.log(staking.getMinipoolCount(nodeOp));
    vm.prank(address(rialto));
    minipoolMgr.recordStakingError{value: validationAmt}(mp1.nodeID, errorCode);
    vm.prank(nodeOp);
    // minipool count when in "Error" state: 1
    console.log(staking.getMinipoolCount(nodeOp));

    vm.prank(address(rialto));

    assertEq(vault.balanceOf("MinipoolManager"), depositAmt);

    MinipoolManager.Minipool memory mp1Updated = minipoolMgr.getMinipool(minipoolIndex);

    vm.prank(address(rialto));
    minipoolMgr.finishFailedMinipoolByMultisig(mp1Updated.nodeID);
    MinipoolManager.Minipool memory mp1finished = minipoolMgr.getMinipool(minipoolIndex);
    vm.prank(nodeOp);
    // minipool count when in "Finished" state: 1
    console.log(staking.getMinipoolCount(nodeOp));
}
```

#### Tools Used

VSCode

#### Recommended Mitigation Steps

You need to simply add the line `staking.decreaseMinipoolCount(owner);` to the `MinipoolManager.recordStakingError` function.

[**0xju1ie (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/235)

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/235#issuecomment-1410538395)**:**

> The Warden has shown how, calling `recordStakingError` will not decrease the `minipoolCount`.
>
> This will not only impact view functions but also impact Yield calculations.
>
> For this reason, I agree with Medium Severity.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> We removed minipool count entirely: [multisig-labs/gogopool#42](https://github.com/multisig-labs/gogopool/pull/42)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/59) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/44).

***

### [\[M-20\] TokenggAVAX: maxDeposit and maxMint return wrong value when contract is paused](https://github.com/code-423n4/2022-12-gogopool-findings/issues/144)

_Submitted by_ [_HollaDieWaldfee_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/144)_, also found by_ [_aviggiano_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/247)

The `TokenggAVAX` contract ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L24](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L24)) can be paused.

The `whenTokenNotPaused` modifier is applied to the following functions ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L225-L239](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L225-L239)):\
`previewDeposit`, `previewMint`, `previewWithdraw` and `previewRedeem`

Thereby any calls to functions that deposit or withdraw funds revert.

There are two functions (`maxWithdraw` and `maxRedeem`) that calculate the max amount that can be withdrawn or redeemed respectively.

Both functions return `0` if the `TokenggAVAX` contract is paused.

The issue is that `TokenggAVAX` does not override the `maxDeposit` and `maxMint` functions ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L156-L162](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L156-L162)) in the `ERC4626Upgradable` contract like it does for `maxWithdraw` and `maxRedeem`.

Thereby these two functions return a value that cannot actually be deposited or minted.

This can cause any components that rely on any of these functions to return a correct value to malfunction.

So `maxDeposit` and `maxMint` should return the value `0` when `TokenggAVAX` is paused.

#### Proof of Concept

1.

The `TokenggAVAX` contract is paused by calling `Ocyticus.pauseEverything` ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/Ocyticus.sol#L37-L43](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/Ocyticus.sol#L37-L43))
2. `TokenggAVAX.maxDeposit` returns `type(uint256).max` ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L157](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L157))
3.

However `deposit` cannot be called with this value because it is paused (`previewDeposit` reverts because of the `whenTokenNotPaused` modifier) ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L44](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L44))

#### Tools Used

VSCode

#### Recommended Mitigation Steps

The `maxDeposit` and `maxMint` functions should be overridden by `TokenggAVAX` just like `maxWithdraw` and `maxRedeem` are overridden and return `0` when the contract is paused ([https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L206-L223](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L206-L223)).

So add these two functions to the `TokenggAVAX` contract:

```solidity
function maxDeposit(address) public view override returns (uint256) {
    if (getBool(keccak256(abi.encodePacked("contract.paused", "TokenggAVAX")))) {
        return 0;
    }
    return return type(uint256).max;
}

function maxMint(address) public view override returns (uint256) {
    if (getBool(keccak256(abi.encodePacked("contract.paused", "TokenggAVAX")))) {
        return 0;
    }
    return return type(uint256).max;
}
```

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/144#issuecomment-1372623332)**:**

> Looks off, the modifiers will revert on pause, not return 0.

[**0xju1ie (GoGoPool) disagreed with severity and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/144#issuecomment-1396711908)**:**

> I'd say Low: `(e.g. assets are not at risk: state handling, function incorrect as to spec, issues with comments).

Excludes Gas optimizations, which are submitted and judged separately.`

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/144#issuecomment-1396712353)**:**

> Good catch, I think we should override those for consistency at least but there's no way to exploit to lose assets. Agreed that QA makes sense.

[**Alex the Entreprenerd (judge) decreased severity to Low and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/144#issuecomment-1410419042)**:**

> By definition, the finding is Informational in Nature.
>
> Because of the relevancy, I'm awarding it QA - Low

[**Alex the Entreprenerd (judge) increased severity to Medium and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/144#issuecomment-1411061391)**:**

> I had a change of heart on this issue, because this pertains to a standard that is being implemented.

>
> For that reason am going to award Medium Severity, because the function breaks the standard, and historically we have awarded similar findings (e..g broken ERC20, broken ERC721 standard), with Medium.
>
> The Warden has shown an inconsistency between the ERC-4626 Spec and the implementation done by the sponsor, while technically this is an informational finding, the fact that a standard was broken warrants a higher severity, leading me to believe that Medium is a more appropriate Severity.
>
> Am making this decision because the Sponsor is following the standard, and the implementation of these functions is not consistent with it.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Return correct value from maxMint and maxDeposit when the contract is paused: [multisig-labs/gogopool#33](https://github.com/multisig-labs/gogopool/pull/33)

**Status:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/60) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/45).

tisigs
/// @param vault Vault contract
/// @param ggp TokenGGP contract
function distributeMultisigAllotment(
uint256 allotment,
Vault vault,
TokenGGP ggp
) internal {
MultisigManager mm = MultisigManager(getContractAddress("MultisigManager"));

uint256 enabledCount;
uint256 count = mm.getCount();
address[] memory enabledMultisigs = new address[](count);

// there should never be more than a few multisigs, so a loop should be fine here
for (uint256 i = 0; i < count; i++) {
	(address addr, bool enabled) = mm.getMultisig(i);
	if (enabled) {
		enabledMultisigs[enabledCount] = addr;
		enabledCount++;
	}
}

// Dirty hack to cut unused elements off end of return value (from RP)
// solhint-disable-next-line no-inline-assembly
assembly {
	mstore(enabledMultisigs, enabledCount)
}

uint256 tokensPerMultisig = allotment / enabledCount;
for (uint256 i = 0; i < enabledMultisigs.length; i++) {
	vault.withdrawToken(enabledMultisigs[i], ggp, tokensPerMultisig);
}
}
```

The code distributes the reward to all multisig evenly.

```solidity
uint256 tokensPerMultisig = allotment / enabledCount;
```

However, if the enabledCount is 0, meaning no multisig wallet is enabled, the transactions revert in division by zero error and revert the startRewardsCycle transaction.

As shown in POC.

In RewardsPool.t.sol,

we change the name from testStartRewardsCycle to testStartRewardsCycle\_POC

[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/test/unit/RewardsPool.t.sol#L123](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/test/unit/RewardsPool.t.sol#L123)

we add the code to disable all multisig wallet.

2561353689)
    │   ├─ [537] Storage::getAddress(0xcda836d09bcf3adcec2f52ddddeceac31738a574d5063511c887064e499593df) [staticcall]
    │   │   └─ ← MultisigManager: [0xA12E9172eB5A8B9054F897cC231Cd7a2751D6D93]
    │   ├─ [1313] MultisigManager::getCount() [staticcall]
    │   │   ├─ [549] Storage::getUint(0x778484468bc504108f077f6bf471293e4138c2d117c6f33607855518cf4bda79) [staticcall]
    │   │   │   └─ ← 1
    │   │   └─ ← 1
    │   ├─ [3050] MultisigManager::getMultisig(0) [staticcall]
    │   │   ├─ [537] Storage::getAddress(0xfebe6f39b65f18e050b53df1d0c8d45b8c5cce333324eb048b67b8ee5f26b7a3) [staticcall]
    │   │   │   └─ ← RialtoSimulator: [0x98D1613BC08756f51f46E841409E61C32f576F2f]
    │   │   ├─ [539] Storage::getBool(0x7ef800e7ca09c0c1063313b56290c06f6bc4bae0e9b7af3899bb7d5ade0403c8) [staticcall]
    │   │   │   └─ ← false
    │   │   └─ ← RialtoSimulator: [0x98D1613BC08756f51f46E841409E61C32f576F2f], false
    │   └─ ← "Division or modulo by 0"
    └─ ← "Division or modulo by 0"

Test result: FAILED.

0 passed; 1 failed; finished in 11.64ms

Failing tests:
Encountered 1 failing test in test/unit/RewardsPool.t.sol:RewardsPoolTest
[FAIL. Reason: Division or modulo by 0] testStartRewardsCycle_POC() (gas: 332890)
```

#### Recommended Mitigation Steps

We recommend the project handle the case when the number of enabled multisig is 0 gracefully to not block the startRewardCycle transaction.

[**emersoncloud (GoGoPool) confirmed**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/143)

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/143#issuecomment-1412623590)**:**

> The Warden has shown a scenario that could cause the call to `startRewardsCycle` to revert.
>
> When all multisigs are disabled (or no multisig is added), the division by zero will cause reverts.
>
> While Admin Privilege is out of scope for this contest, the Warden has identified how a lack of zero-check can cause an open function to revert.

>
> For this reason, I agree with Medium Severity.

[**emersoncloud (GoGoPool) mitigated**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest#mitigations-to-be-reviewed)**:**

> Prevents division by zero error blocking startRewardCycle(): [multisig-labs/gogopool#37](https://github.com/multisig-labs/gogopool/pull/37)

**Status:** Mitigation confirmed, but a new medium severity issue was found. Full details in reports from [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/46) and [ladboy233](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/8). Also included in Mitigation Review section below.

of validation rewards from function `ExpectedRewardAVA` in `MiniPoolManager.sol`](https://github.com/code-423n4/2022-12-gogopool-findings/issues/122)

_Submitted by_ [_ladboy233_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/122)_, also found by_ [_hansfriese_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/572)

[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L560](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L560)\
[https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L676](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L676)

The validation rewards can be inaccurately displayed to user and the slahsed amount can be wrong when slashing happens.

#### Proof of Concept

Note the function below:

```solidity
	/// @notice Given a duration and an AVAX amt, calculate how much AVAX should be earned via validation rewards
	/// @param duration The length of validation in seconds
	/// @param avaxAmt The amount of AVAX the node staked for their validation period
	/// @return The approximate rewards the node should recieve from Avalanche for beign a validator
	function getExpectedAVAXRewardsAmt(uint256 duration, uint256 avaxAmt) public view returns (uint256) {
		ProtocolDAO dao = ProtocolDAO(getContractAddress("ProtocolDAO"));
		uint256 rate = dao.getExpectedAVAXRewardsRate();
		return (avaxAmt.mulWadDown(rate) * duration) / 365 days;
	}
```

As outlined in the comment section, the function is intended to calculate how much AVAX should be earned via validation rewards.

Besides displaying the reward, this function is also used in the function slash.

```solidity
/// @notice Slashes the GPP of the minipool with the given index
/// @dev Extracted this because of "stack too deep" errors.

keccak256(abi.encodePacked("minipool.item", index, ".nodeID")));
	address owner = getAddress(keccak256(abi.encodePacked("minipool.item", index, ".owner")));
	uint256 duration = getUint(keccak256(abi.encodePacked("minipool.item", index, ".duration")));
	uint256 avaxLiquidStakerAmt = getUint(keccak256(abi.encodePacked("minipool.item", index, ".avaxLiquidStakerAmt")));
	uint256 expectedAVAXRewardsAmt = getExpectedAVAXRewardsAmt(duration, avaxLiquidStakerAmt);
	uint256 slashGGPAmt = calculateGGPSlashAmt(expectedAVAXRewardsAmt);
	setUint(keccak256(abi.encodePacked("minipool.item", index, ".ggpSlashAmt")), slashGGPAmt);

	emit GGPSlashed(nodeID, slashGGPAmt);

	Staking staking = Staking(getContractAddress("Staking"));
	staking.slashGGP(owner, slashGGPAmt);
}
```

Note the code:

```solidity
uint256 expectedAVAXRewardsAmt = getExpectedAVAXRewardsAmt(duration, avaxLiquidStakerAmt);
uint256 slashGGPAmt = calculateGGPSlashAmt(expectedAVAXRewardsAmt);
```

The slashedGGPAmt is calculated based on the AVAX reward amount.

However, the estimation of the validation rewards is not accurate.

According to the doc:

[https://docs.avax.network/nodes/build/set-up-an-avalanche-node-with-microsoft-azure](https://docs.avax.network/nodes/build/set-up-an-avalanche-node-with-microsoft-azure)

> Running a validator and staking with Avalanche provides extremely competitive rewards of between 9.69% and 11.54% depending on the length you stake for.

This implies that the staking length affect staking rewards, but this is kind of vague. What is the exact implementation of the reward calculation?

The implementation is linked below:

[https://github.com/ava-labs/avalanchego/blob/master/vms/platformvm/reward/calculator.go#L40](https://github.com/ava-labs/avalanchego/blob/master/vms/platformvm/reward/calculator.go#L40)

```Golang
// Reward returns the amount of tokens to reward the staker with.

ew(big.Int).Mul(c.maxSubMinConsumptionRate, bigStakedDuration)
	adjustedMinConsumptionRateNumerator := new(big.Int).Mul(c.minConsumptionRate, c.mintingPeriod)
	adjustedConsumptionRateNumerator.Add(adjustedConsumptionRateNumerator, adjustedMinConsumptionRateNumerator)
	adjustedConsumptionRateDenominator := new(big.Int).Mul(c.mintingPeriod, consumptionRateDenominator)

	remainingSupply := c.supplyCap - currentSupply
	reward := new(big.Int).SetUint64(remainingSupply)
	reward.Mul(reward, adjustedConsumptionRateNumerator)
	reward.Mul(reward, bigStakedAmount)
	reward.Mul(reward, bigStakedDuration)
	reward.Div(reward, adjustedConsumptionRateDenominator)
	reward.Div(reward, bigCurrentSupply)
	reward.Div(reward, c.mintingPeriod)

	if !reward.IsUint64() {
		return remainingSupply
	}

	finalReward := reward.Uint64()
	if finalReward > remainingSupply {
		return remainingSupply
	}

	return finalReward
}
```

Note the reward calculation formula:

```solidity
// Reward returns the amount of tokens to reward the staker with.

//
// RemainingSupply = SupplyCap - ExistingSupply
// PortionOfExistingSupply = StakedAmount / ExistingSupply
// PortionOfStakingDuration = StakingDuration / MaximumStakingDuration
// MintingRate = MinMintingRate + MaxSubMinMintingRate * PortionOfStakingDuration
// Reward = RemainingSupply * PortionOfExistingSupply * MintingRate * PortionOfStakingDuration
```

However, in the current ExpectedRewardAVA, the implementation is just:

AVAX reward rate \* avax amount \* duration / 365 days.

```solidity
ProtocolDAO dao = ProtocolDAO(getContractAddress("ProtocolDAO"));
		uint256 rate = dao.getExpectedAVAXRewardsRate();
		return (avaxAmt.mulWadDown(rate) * duration) / 365 days;
```

Clearly, the implementation of the avalanche side is more sophisticated and accurate than the implemented ExpectedRewardAVA.

#### Recommended Mitigation Steps

We recommend the project make the ExpectedRewardAVA implementation match the implement.

[https://github.com/ava-labs/avalanchego/blob/master/vms/platformvm/reward/calculator.go#L40](https://github.com/ava-labs/avalanchego/blob/master/vms/platformvm/reward/calculator.go#L40)

[**0xju1ie (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/122#issuecomment-1398876613)**:**

> Rialto is going to report the correct rewards rate to the DAO from Avalanche. Not sure if it's a medium.

[**emersoncloud (GoGoPool) acknowledged and commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/122#issuecomment-1398893666)**:**

> We felt comfortable with a static setting number because we are (initally) staking minipools for 2 week increments with 2000 AVAX, making the variability in rewards rates minimal.
>
> We will develop a more complex calculation as the protocol starts handling a wider range of funds and durations.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/122#issuecomment-1414356992)**:**

> The Warden has shown an incorrect implementation of the formula to estimate rewards.
>
> The math would cause the slash value to be incorrect, causing improper yield to be distributed, for this reason I agree with Medium Severity.

[**emersoncloud (GoGoPool) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/122#issuecomment-1421434941)**:**

> Acknowledged. See comments above!

***

## Low Risk and Non-Critical Issues

For this contest, 15 reports were submitted by wardens detailing low risk and non-critical issues. The [report highlighted below](https://github.com/code-423n4/2022-12-gogopool-findings/issues/728) by **IllIllI** received the top score from the judge.

|
| \[N‑25] | Contracts should have full test coverage                                                                                        |     1     |
| \[N‑26] | Large or complicated code bases should implement fuzzing tests                                                                  |     1     |
| \[N‑27] | Function ordering does not follow the Solidity style guide                                                                      |     15    |
| \[N‑28] | Contract does not follow the Solidity style guide's suggested layout ordering                                                   |     9     |
| \[N‑29] | Open TODOs                                                                                                                      |     1     |

Total: 99 instances over 29 issues

### \[L‑01] Inflation not locked for four years

The [litepaper](https://docs.gogopool.com/about-gogopool/gogopool-litepaper) says that there will be no inflation for four years, but there is no code enforcing this.

_There is 1 instance of this issue:_

```solidity
File: /contracts/contract/ProtocolDAO.sol

39   		// GGP Inflation
40   		setUint(keccak256("ProtocolDAO.InflationIntervalSeconds"), 1 days);
41:  		setUint(keccak256("ProtocolDAO.InflationIntervalRate"), 1000133680617113500); // 5% annual calculated on a daily interval - Calculate in js example: let dailyInflation = web3.utils.toBN((1 + 0.05) ** (1 / (365)) * 1e18);

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ProtocolDAO.sol#L39-L41

### \[L‑02] Contract will stop functioning in the year 2106

Limiting the timestamp to fit in a `uint32` will cause the call below to start reverting in 2106.

_There is 1 instance of this issue:_

```solidity
File: /contracts/contract/tokens/TokenggAVAX.sol

89:  		uint32 timestamp = block.timestamp.safeCastTo32();

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L89

### \[L‑03] Lower-level initializations should come first

There may not be an issue now, but if `ERC4626` changes to rely on some of the functions `BaseUpgradeable` provides, things will break.

_There is 1 instance of this issue:_

```solidity
File: /contracts/contract/tokens/TokenggAVAX.sol

72   	function initialize(Storage storageAddress, ERC20 asset) public initializer {
73   		__ERC4626Upgradeable_init(asset, "GoGoPool Liquid Staking Token", "ggAVAX");
74:  		__BaseUpgradeable_init(storageAddress);

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L72-L74

### \[L‑04] Incorrect percentage conversion

0.2 ether should be 20%, not 2%. [Other](https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ProtocolDAO.sol#L44) areas use 0.X as X0%.

_There is 1 instance of this issue:_

```solidity
File: /contracts/contract/MinipoolManager.sol

194: 	/// @param delegationFee Percentage delegation fee in units of ether (2% is 0.2 ether)

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L194

### \[L‑05] Loss of precision

Division by large numbers may result in the result being zero, due to solidity not supporting fractions. Consider requiring a minimum amount for the numerator to ensure that it is always larger than the denominator.

_There are 2 instances of this issue:_

```solidity
File: contracts/contract/RewardsPool.sol

60:   		return (block.timestamp - startTime) / dao.getInflationIntervalSeconds();

128:  		return (block.timestamp - startTime) / dao.getRewardsCycleSeconds();

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/RewardsPool.sol#L60

### \[L‑06] Signatures vulnerable to malleability attacks

`ecrecover()` accepts as valid, two versions of signatures, meaning an attacker can use the same signature twice. Consider adding checks for signature malleability, or using OpenZeppelin's `ECDSA` library to perform the extra checks necessary in order to prevent this attack.

s issue:_

```solidity
File: contracts/contract/tokens/upgradeable/ERC20Upgradeable.sol

132   			address recoveredAddress = ecrecover(
133   				keccak256(
134   					abi.encodePacked(
135   						"\x19\x01",
136   						DOMAIN_SEPARATOR(),
137   						keccak256(
138   							abi.encode(
139   								keccak256("Permit(address owner,address spender,uint256 value,uint256 nonce,uint256 deadline)"),
140   								owner,
141   								spender,
142   								value,
143   								nonces[owner]++,
144   								deadline
145   							)
146   						)
147   					)
148   				),
149   				v,
150   				r,
151   				s
152:  			);

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC20Upgradeable.sol#L132-L152

### \[L‑07] `require()` should be used instead of `assert()`

Prior to solidity version 0.8.0, hitting an assert consumes the **remainder of the transaction's available gas** rather than returning it, as `require()`/`revert()` do.

`assert()` should be avoided even past solidity version 0.8.0 as its [documentation](https://docs.soliditylang.org/en/v0.8.14/control-structures.html#panic-via-assert-and-error-via-require) states that "The assert function creates an error of type Panic(uint256). ... Properly functioning code should never create a Panic, not even on invalid external input. If this happens, then there is a bug in your contract which you should fix".

#L71-L74) performs similar operations, so the common code should be refactored to a function

_There is 1 instance of this issue:_

```solidity
File: /contracts/contract/MultisigManager.sol

110: 		addr = getAddress(keccak256(abi.encodePacked("multisig.item", index, ".address")));

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MultisigManager.sol#L110

### \[N‑02] String constants used in multiple places should be defined as constants

_There is 1 instance of this issue:_

```solidity
File: /contracts/contract/MultisigManager.sol

110: 		addr = getAddress(keccak256(abi.encodePacked("multisig.item", index, ".address")));

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MultisigManager.sol#L110

### \[N‑03] Constants in comparisons should appear on the left side

Doing so will prevent [typo bugs](https://www.moserware.com/2008/01/constants-on-left-are-better-but-this.html).

_There is 1 instance of this issue:_

```solidity
File: /contracts/contract/ClaimNodeOp.sol

92:  		if (ggpRewards == 0) {

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ClaimNodeOp.sol#L92

### \[N‑04] Inconsistent address separator in storage names

Most addresses in storage names don't separate the prefix from the address with a period, but this one has one.

_There is 1 instance of this issue:_

```solidity
File: /contracts/contract/ProtocolDAO.sol

102  	function getClaimingContractPct(string memory claimingContract) public view returns (uint256) {
103  		return getUint(keccak256(abi.encodePacked("ProtocolDAO.ClaimingContractPct.", claimingContract)));
104  	}
105
106  	/// @notice Set the percentage a contract is owed for a rewards cycle
107  	function setClaimingContractPct(string memory claimingContract, uint256 decimal) public onlyGuardian valueNotGreaterThanOne(decimal) {
108  		setUint(keccak256(abi.encodePacked("ProtocolDAO.ClaimingContractPct.", claimingContract)), decimal);
109: 	}

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ProtocolDAO.sol#L102-L109

### \[N‑05] Confusing function name

Consider changing the name to `stakeGGPAs` or `stakeGGPFor`.

_There is 1 instance of this issue:_

```solidity
File: /contracts/contract/Staking.sol

328: 	function restakeGGP(address stakerAddr, uint256 amount) public onlySpecificRegisteredContract("ClaimNodeOp", msg.sender) {

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/Staking.sol#L328

### \[N‑06] Misplaced punctuation

There's an extra comma - it looks like a find-and-replace error.

_There is 1 instance of this issue:_

```solidity
File: /contracts/contract/Vault.sol

154  		// Update balances
155  		tokenBalances[contractKey] = tokenBalances[contractKey] - amount;
156  		// Get the toke ERC20 instance
157  		ERC20 tokenContract = ERC20(tokenAddress);
158  		// Withdraw to the withdrawal address, , safeTransfer will revert if it fails
159  		tokenContract.safeTransfer(withdrawalAddress, amount);
160: 	}

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/Vault.sol#L154-L160

### \[N‑07] Upgradeable contract is missing a `__gap[50]` storage variable to allow for new storage variables in later versions

See [this](https://docs.openzeppelin.com/contracts/4.x/upgradeable#storage\_gaps) link for a description of this storage variable. While some contracts may not currently be sub-classed, adding the variable now protects against forgetting to add it in the future.

_There is 1 instance of this issue:_

```solidity
File: contracts/contract/tokens/TokenggAVAX.sol

24:   contract TokenggAVAX is Initializable, ERC4626Upgradeable, UUPSUpgradeable, BaseUpgradeable {

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L24

### \[N‑08] Import declarations should import specific identifiers, rather than the whole file

Using import declarations of the form `import {<identifier_name>} from "some/file.sol"` avoids polluting the symbol namespace making flattened files smaller, and speeds up compilation.

_There are 13 instances of this issue.

(For in-depth details on this and all further issues with multiple instances, please see the warden's_ [_full report_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/728)_.)_

### \[N‑09] Missing `initializer` modifier on constructor

OpenZeppelin [recommends](https://forum.openzeppelin.com/t/uupsupgradeable-vulnerability-post-mortem/15680/5) that the `initializer` modifier be applied to constructors in order to avoid potential griefs, [social engineering](https://forum.openzeppelin.com/t/uupsupgradeable-vulnerability-post-mortem/15680/4), or exploits. Ensure that the modifier is applied to the implementation contract. If the default constructor is currently being used, it should be changed to be an explicit one with the modifier applied.

_There is 1 instance of this issue:_

```solidity
File: contracts/contract/BaseUpgradeable.sol

9:    contract BaseUpgradeable is Initializable, BaseAbstract {

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/BaseUpgradeable.sol#L9

### \[N‑10] The `nonReentrant` `modifier` should occur before all other modifiers

This is a best-practice to protect against reentrancy in other modifiers.

_There are 2 instances of this issue._

### \[N‑11] `override` function arguments that are unused should have the variable name removed or commented out to avoid compiler warnings

_There is 1 instance of this issue:_

```solidity
File: contracts/contract/tokens/TokenggAVAX.sol

255:  	function _authorizeUpgrade(address newImplementation) internal override onlyGuardian {}

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/TokenggAVAX.sol#L255

### \[N‑12] `constant`s should be defined rather than using magic numbers

Even [assembly](https://github.com/code-423n4/2022-05-opensea-seaport/blob/9d7ce4d08bf3c3010304a0476a785c70c0e90ae7/contracts/lib/TokenTransferrer.sol#L35-L39) can benefit from using readable constants instead of hex/numeric literals.

_There are 2 instances of this issue._

### \[N‑13] Missing event and or timelock for critical parameter change

Events help non-contract tools to track changes, and events prevent users from being surprised by changes.

_There is 1 instance of this issue:_

```solidity
File: contracts/contract/Storage.sol

41    	function setGuardian(address newAddress) external {
42    		// Check tx comes from current guardian
43    		if (msg.sender != guardian) {
44    			revert MustBeGuardian();
45    		}
46    		// Store new address awaiting confirmation
47    		newGuardian = newAddress;
48:   	}

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/Storage.sol#L41-L48

### \[N‑14] Events that mark critical parameter changes should contain both the old and the new value

This should especially be done if the new value is not required to be different from the old value.

_There are 2 instances of this issue._

### \[N‑15] Use a more recent version of solidity

Use a solidity version of at least 0.8.13 to get the ability to use `using for` with a list of free functions.

_There is 1 instance of this issue:_

```solidity
File: contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol

2:    pragma solidity >=0.8.0;

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC4626Upgradeable.sol#L2

### \[N‑16] Use a more recent version of solidity

* Use a solidity version of at least 0.8.4 to get `bytes.concat()` instead of `abi.encodePacked(<bytes>,<bytes>)`.
* Use a solidity version of at least 0.8.12 to get `string.concat()` instead of `abi.encodePacked(<str>,<str>)`.

_There is 1 instance of this issue:_

```solidity
File: contracts/contract/tokens/upgradeable/ERC20Upgradeable.sol

2:    pragma solidity >=0.8.0;

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/tokens/upgradeable/ERC20Upgradeable.sol#L2

### \[N‑17] Constant redefined elsewhere

Consider defining in only one contract so that values cannot become out of sync when only one location is updated. A [cheap way](https://medium.com/coinmonks/gas-cost-of-solidity-library-functions-dbe0cedd4678) to store constants in a single location is to create an `internal constant` in a `library`. If the variable is a local cache of another contract's value, consider making the cache variable internal or private, which will require external users to query the contract with the source of truth, so that callers don't get out of sync.

_There are 2 instances of this issue._

### \[N‑18] Lines are too long

Usually lines in source code are limited to [80](https://softwareengineering.stackexchange.com/questions/148677/why-is-80-characters-the-standard-limit-for-code-width) characters. Today's screens are much larger so it's reasonable to stretch this in some cases.

Since the files will most likely reside in GitHub, and GitHub starts using a scroll bar in all cases when the length is over [164](https://github.com/aizatto/character-length) characters, the lines below should be split when they reach that length

_There is 1 instance of this issue:_

```solidity
File: contracts/contract/ProtocolDAO.sol

41:   		setUint(keccak256("ProtocolDAO.InflationIntervalRate"), 1000133680617113500); // 5% annual calculated on a daily interval - Calculate in js example: let dailyInflation = web3.utils.toBN((1 + 0.05) ** (1 / (365)) * 1e18);

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/ProtocolDAO.sol#L41

### \[N‑19] Variable names that consist of all capital letters should be reserved for `constant`/`immutable` variables

If the variable needs to be different based on which class it comes from, a `view`/`pure` _function_ should be used instead (e.g.

like [this](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/76eee35971c2541585e05cbf258510dda7b2fbc6/contracts/token/ERC20/extensions/draft-IERC20Permit.sol#L59)).

_There are 2 instances of this issue._

### \[N‑20] Using `>`/`>=` without specifying an upper bound is unsafe

There _will_ be breaking changes in future versions of solidity, and at that point your code will no longer be compatable. While you may have the specific version to use in a configuration file, others that include your source files may not.

_There are 2 instances of this issue._

### \[N‑21] Typos

_There are 3 instances of this issue._

### \[N‑22] File is missing NatSpec

_There are 3 instances of this issue._

### \[N‑23] NatSpec is incomplete

_There are 27 instances of this issue._

### \[N‑24] Not using the named return variables anywhere in the function is confusing

Consider changing the variable to be an unnamed one.

_There is 1 instance of this issue:_

```solidity
File: contracts/contract/MinipoolManager.sol

/// @audit mp
572:  	function getMinipoolByNodeID(address nodeID) public view returns (Minipool memory mp) {

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L572

### \[N‑25] Contracts should have full test coverage

While 100% code coverage does not guarantee that there are no bugs, it often will catch easy-to-find bugs, and will ensure that there are fewer regressions when the code invariably has to be modified. Furthermore, in order to get full coverage, code authors will often have to re-organize their code so that it is more modular, so that each component can be tested separately, which reduces interdependencies between modules and layers, and makes for code that is easier to reason about and audit.

_There is 1 instance of this issue:_

```solidity
File: Various Files

```

### \[N‑26] Large or complicated code bases should implement fuzzing tests

Large code bases, or code with lots of inline-assembly, complicated math, or complicated interactions between multiple contracts, should implement [fuzzing tests](https://medium.com/coinmonks/smart-contract-fuzzing-d9b88e0b0a05). Fuzzers such as Echidna require the test writer to come up with invariants which should not be violated under any circumstances, and the fuzzer tests various inputs and function calls to ensure that the invariants always hold. Even code with 100% code coverage can still have bugs due to the order of the operations a user performs, and fuzzers, with properly and extensively-written invariants, can close this testing gap significantly.

_There is 1 instance of this issue:_

```solidity
File: Various Files

```

### \[N‑27] Function ordering does not follow the Solidity style guide

According to the [Solidity style guide](https://docs.soliditylang.org/en/v0.8.17/style-guide.html#order-of-functions), functions should be laid out in the following order :`constructor()`, `receive()`, `fallback()`, `external`, `public`, `internal`, `private`, but the cases below do not follow this pattern.

_There are 15 instances of this issue._

### \[N‑28] Contract does not follow the Solidity style guide's suggested layout ordering

The [style guide](https://docs.soliditylang.org/en/v0.8.16/style-guide.html#order-of-layout) says that, within a contract, the ordering should be 1) Type declarations, 2) State variables, 3) Events, 4) Modifiers, and 5) Functions, but the contract(s) below do not follow this ordering.

_There are 9 instances of this issue._

### \[N‑29] Open TODOs

Code architecture, incentives, and error handling/reporting questions/issues should be resolved before deployment.

_There is 1 instance of this issue:_

```solidity
File: contracts/contract/MinipoolManager.sol

412:  		// TODO Revisit this logic if we ever allow unequal matched funds

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/MinipoolManager.sol#L412

### Excluded findings

These findings are excluded from awards calculations because there are publicly-available automated tools that find them. The valid ones appear here for completeness.

|     2     |
| \[N‑31] | `public` functions not called by the contract should be declared `external` instead |     54    |
| \[N‑32] | Event is missing `indexed` fields                                                   |     26    |

Total: 82 instances over 3 issues

#### \[L‑08] Missing checks for `address(0x0)` when assigning values to `address` state variables

_There is 1 instance of this issue:_

```solidity
File: contracts/contract/Storage.sol

/// @audit (valid but excluded finding)
47:   		newGuardian = newAddress;

```

https://github.com/code-423n4/2022-12-gogopool/blob/aec9928d8bdce8a5a4efe45f54c39d4fc7313731/contracts/contract/Storage.sol#L47

#### \[L‑09] `abi.encodePacked()` should not be used with dynamic types when passing the result to a hash function such as `keccak256()`

Use `abi.encode()` instead which will pad items to 32 bytes, which will [prevent hash collisions](https://docs.soliditylang.org/en/v0.8.13/abi-spec.html#non-standard-packed-mode) (e.g.

`abi.encodePacked(0x123,0x456)` => `0x123456` => `abi.encodePacked(0x1,0x23456)`, but `abi.encode(0x123,0x456)` => `0x0...1230...456`). "Unless there is a compelling reason, `abi.encode` should be preferred". If there is only one argument to `abi.encodePacked()` it can often be cast to `bytes()` or `bytes32()` [instead](https://ethereum.stackexchange.com/questions/30912/how-to-compare-strings-in-solidity#answer-82739).

If all arguments are strings and or bytes, `bytes.concat()` should be used instead.

_There are 155 instances of this issue._

#### \[N‑30] Return values of `approve()` not checked

Not all `IERC20` implementations `revert()` when there's a failure in `approve()`. The function signature has a `boolean` return value and they indicate errors that way instead. By not checking the return value, operations that should have marked as failed, may potentially go through without actually approving anything.

_There are 2 instances of this issue._

#### \[N‑31] `public` functions not called by the contract should be declared `external` instead

Contracts [are allowed](https://docs.soliditylang.org/en/latest/contracts.html#function-overriding) to override their parents' functions and change the visibility from `external` to `public`.

_There are 54 instances of this issue._

#### \[N‑32] Event is missing `indexed` fields

Index event fields make the field more quickly accessible [to off-chain tools](https://ethereum.stackexchange.com/questions/40396/can-somebody-please-explain-the-concept-of-event-indexing) that parse events. However, note that each index field costs extra gas during emission, so it's not necessarily best to index the maximum allowed per event (three fields). Each `event` should use three `indexed` fields if there are three or more fields, and gas usage is not particularly of concern for the events in question. If there are fewer than three fields, all of the fields should be indexed.

_There are 26 instances of this issue._

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/728#issuecomment-1404109188)**:**

> **\[L‑01] Inflation not locked for four years**\
> Refactor. Code as is will revert after 4 years, so it's enforced via config.

>
> **\[N‑21] Typos**\
> Non-Critical
>
> **\[N‑22] File is missing NatSpec**\
> Non-Critical
>
> **\[N‑23] NatSpec is incomplete**\
> Non-Critical
>
> **\[N‑24] Not using the named return variables anywhere in the function is confusing**\
> Refactor
>
> **\[N‑25] Contracts should have full test coverage**\
> Refactor
>
> **\[N‑26] Large or complicated code bases should implement fuzzing tests**\
> Refactor
>
> **\[N‑27] Function ordering does not follow the Solidity style guide**\
> Non-Critical
>
> **\[N‑28] Contract does not follow the Solidity style guide's suggested layout ordering**\
> Non-Critical
>
> **\[N-29] Open TODOs**\
> Non-Critical

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/728#issuecomment-1416111377)**:**

> 6 Low, 15 Refactor, 15 Non-Critical, including downgraded findings ([#733](https://github.com/code-423n4/2022-12-gogopool-findings/issues/733) & [#734](https://github.com/code-423n4/2022-12-gogopool-findings/issues/734)).

>
> Best report by far, so far I thought the second best was the best (this one scores above 100%).
>
> Well played.

***

## Gas Optimizations

For this contest, 12 reports were submitted by wardens detailing gas optimizations. The [report highlighted below](https://github.com/code-423n4/2022-12-gogopool-findings/issues/125) by **NoamYakov** received the top score from the judge.

d use bit shifting                                                                                                                    |     1     |        20       |
| \[G‑14] | The result of function calls should be cached rather than re-calling the function                                                                          |     2     |       200       |
| \[G‑15] | Don't compare boolean expressions to boolean literals                                                                                                      |     3     |        27       |
| \[G‑16] | Splitting `require()` statements that use `&&` saves gas                                                                                                   |     1     |        3        |
| \[G‑17] | Stack variable used as a cheaper cache for a state variable is only used once                                                                              |     3     |        9        |

Total: 256 instances over 17 issues with **17165 gas** saved.

Gas totals use lower bounds of ranges and count two iterations of each `for`-loop. All values above are runtime, not deployment, values; deployment values are listed in the individual issue descriptions.

### \[G‑01] State variables can be packed into fewer storage slots

If variables occupying the same slot are both written by the same function or by the constructor, avoids a separate Gsset (**20000 gas**). Reads of the variables can also be cheaper.

_There is 1 instance of this issue:_

```solidity
File: contracts\contract\tokens\TokenggAVAX.sol

/// @audit currently, `lastSync`, `rewardsCycleLength` and `rewardsCycleEnd` are
/// 	stored in a single storage slot and `lastRewardsAmt` is in another one.
/// 	Since all of these state variables except for `rewardsCycleLength` are
/// 	being set together (in `syncRewards()`), I suggest to reorder them so
/// 	that they will use the same storage slot and `rewardsCycleLength` will
/// 	use a different one.

40  	/// @notice the effective start of the current cycle
41  	uint32 public lastSync;
42
43  	/// @notice the maximum length of a rewards cycle
44  	uint32 public rewardsCycleLength;
45
46  	/// @notice the end of the current cycle. Will always be evenly divisible by `rewardsCycleLength`.
47  	uint32 public rewardsCycleEnd;
48
49  	/// @notice the amount of rewards distributed in a the most recent cycle.
50  	uint192 public lastRewardsAmt;
```

### \[G‑02] Use a more recent version of solidity

* Use a solidity version of at least 0.8.2 to get simple compiler automatic inlining.
* Use a solidity version of at least 0.8.3 to get better struct packing and cheaper multiple storage reads.
* Use a solidity version of at least 0.8.4 to get custom errors, which are cheaper at deployment than `revert()/require()` strings.
* Use a solidity version of at least 0.8.10 to have external calls skip contract existence checks if the external call has a return value.

_There are 2 instances of this issue.

(For in-depth details on this and all further gas optimizations with multiple instances, please see the warden's_ [_full report_](https://github.com/code-423n4/2022-12-gogopool-findings/issues/125)_.)_

### \[G‑03] `++i`/`i++` should be `unchecked{++i}`/`unchecked{i++}` when it is not possible for them to overflow, as is the case when used in `for`- and `while`-loops

The `unchecked` keyword is new in solidity version 0.8.0, so this only applies to that version or higher, which these instances are. This saves **30-40 gas** [**per loop**](https://gist.github.com/hrkrshnn/ee8fabd532058307229d65dcd5836ddc#the-increment-in-for-loop-post-condition-can-be-made-unchecked).

_There are 10 instances of this issue._

### \[G‑04] `internal` functions only called once can be inlined to save gas

Not inlining costs **20 to 40 gas** because of two extra `JUMP` instructions and additional stack operations needed for function calls.

_There are 4 instances of this issue._

### \[G‑05] Functions guaranteed to revert when called by normal users can be marked `payable`

If a function modifier such as `onlyOwner` is used, the function will revert if a normal user tries to pay the function. Marking the function as `payable` will lower the gas cost for legitimate callers because the compiler will not include checks for whether a payment was provided. The extra opcodes avoided are `CALLVALUE`(2), `DUP1`(3), `ISZERO`(3), `PUSH2`(3), `JUMPI`(10), `PUSH1`(3), `DUP1`(3), `REVERT`(0), `JUMPDEST`(1), `POP`(2), which costs an average of about **21 gas per call** to the function, in addition to the extra deployment cost.

_There are 62 instances of this issue._

### \[G‑06] Optimize names to save gas

`public`/`external` function names and `public` member variable names can be optimized to save gas. See [this](https://gist.github.com/IllIllI000/a5d8b486a8259f9f77891a919febd1a9) link for an example of how it works.

Below are the interfaces/abstract contracts that can be optimized so that the most frequently-called functions use the least amount of gas possible during method lookup. Method IDs that have two leading zero bytes can save **128 gas** each during deployment, and renaming functions to have lower method IDs will save **22 gas** per call, [per sorted position shifted](https://medium.com/joyso/solidity-how-does-function-name-affect-gas-consumption-in-smart-contract-47d270d8ac92).

_There are 13 instances of this issue._

### \[G‑07] Use custom errors rather than `revert()`/`require()` strings to save gas

Custom errors are available from solidity version 0.8.4. Custom errors save [**\~50 gas**](https://gist.github.com/IllIllI000/ad1bd0d29a0101b25e57c293b4b0c746) each time they're hit by [avoiding having to allocate and store the revert string](https://blog.soliditylang.org/2021/04/21/custom-errors/#errors-in-depth). Not defining the strings also save deployment gas.

_There are 4 instances of this issue._

### \[G‑08] Add `unchecked {}` for subtractions where the operands cannot underflow because of a previous `require()` or `if`-statement

`require(a <= b); x = b - a` => `require(a <= b); unchecked { x = b - a }`.

_There are 7 instances of this issue._

### \[G‑09] Multiple accesses of a mapping/array should use a local variable cache

The instances below point to the second+ access of a value inside a mapping/array, within a function. Caching a mapping's value in a local `storage` or `calldata` variable when the value is accessed [multiple times](https://gist.github.com/IllIllI000/ec23a57daa30a8f8ca8b9681c8ccefb0), saves **\~42 gas per access** due to not having to recalculate the key's keccak256 hash (Gkeccak256 - **30 gas**) and that calculation's associated stack operations. Caching an array's struct avoids recalculating the array offsets into memory/calldata.

_There are 4 instances of this issue._

### \[G‑10] State variables should be cached in stack variables rather than re-reading them from storage

The instances below point to the second+ access of a state variable within a function. Caching of a state variable replaces each Gwarmaccess (**100 gas**) with a much cheaper stack read. Other less obvious fixes/optimizations include having local memory caches of state variable structs, or having local caches of state variable contracts/addresses.

_There are 11 instances of this issue._

### \[G‑11] Modification of `getX()`, `setX()`, `deleteX()`, `addX()` and `subX()` in `BaseAbstract.sol` increases gas savings in \[G‑10]

Modify the `getX()`, `setX()`, `deleteX()`, `addX()` and `subX()` functions in `BaseAbstract.sol` to receive the address of the `Storage` contract as an argument. This modification will create dozens more fixable instances of \[G‑10].

_There are 116 instances of this issue._

### \[G‑12] `<x> += <y>` costs more gas than `<x> = <x> + <y>` for state variables (`-=` too)

Using the addition operator instead of plus-equals saves [**113 gas**](https://gist.github.com/IllIllI000/cbbfb267425b898e5be734d4008d4fe8). Subtructions act the same way.

_There are 12 instances of this issue._

### \[G‑13] Division by two should use bit shifting

`<x> / 2` is the same as `<x> >> 1`. While the compiler uses the `SHR` opcode to accomplish both, the version that uses division incurs an overhead of [**20 gas**](https://gist.github.com/IllIllI000/ec0e4e6c4f52a6bca158f137a3afd4ff) due to `JUMP`s to and from a compiler utility function that introduces checks which can be avoided by using `unchecked {}` around the division by two.

_There is 1 instance of this issue:_

```solidity
File: contracts\contract\MinipoolManager.sol

413 		uint256 avaxHalfRewards = avaxTotalRewardAmt / 2;
```

### \[G‑14] The result of function calls should be cached rather than re-calling the function

The instances below point to the second+ call of the function within a single function. _Every_ external call made to a contract incurs at least **100 gas** of overhead.

_There are 2 instances of this issue._

### \[G‑15] Don't compare boolean expressions to boolean literals

`if (<x> == true)` => `if (<x>)`, `if (<x> == false)` => `if (!<x>)`.

_There are 3 instances of this issue._

### \[G‑16] Splitting `require()` statements that use `&&` saves gas

See [this issue](https://github.com/code-423n4/2022-01-xdefi-findings/issues/128) which describes the fact that there is a larger deployment gas cost, but with enough runtime calls, the change ends up being cheaper by **3 gas**.

_There is 1 instance of this issue:_

```solidity
File: contracts\contract\tokens\upgradeable\ERC20Upgradeable.sol

154 			require(recoveredAddress != address(0) && recoveredAddress == owner, "INVALID_SIGNER");
```

### \[G‑17] Stack variable used as a cheaper cache for a state variable is only used once

If the variable is only accessed once, it's cheaper to use the state variable directly that one time, and save the **3 gas** the extra stack assignment would spend.

\* 116
>
> 1856
>
> **\[G‑12] `<x> += <y>` costs more gas than `<x> = <x> + <y>` for state variables (-= too)**\
> Out of scope
>
> **\[G‑13] Division by two should use bit shifting**\
> Equivalent to using unchecked
>
> 20
>
> **\[G‑14] The result of function calls should be cached rather than re-calling the function**\
> 340 \* 2
>
> 680
>
> **\[G‑15] Don't compare boolean expressions to boolean literals**\
> 27
>
> **\[G‑16] Splitting require() statements that use && saves gas**\
> Marginal
>
> **\[G‑17] Stack variable used as a cheaper cache for a state variable is only used once**\
> Marginal
>
> Total: 4262

[**NoamYakov (warden) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/125#issuecomment-1416791198)**:**

> > **\[G‑11] Modification of `getX()`, `setX()`, `deleteX()`, `addX()` and `subX()` in BaseAbstract.sol increases gas savings in \[G‑10]**\
> > Am understanding this as the idea of inlining the call rather than using a function 16 \* 116
>
> This wasn't what I meant.

I meant that each of these functions accesses the `gogoStorage` state variable (SLOAD). Therefore, when there's more than one call to this group of functions (for example, `setUint()` followed by another `setUint()`, or `setUint()` followed by `getAddress()`), it would me much cheaper to cache that state variable (`gogoStorage`) and pass it to the these functions. This way, there will be only one SLOAD.
>
> In my gas report, I flagged the second+ calls to this group of functions as instances, since this optimization can spare an SLOAD in each of these calls. There are 116 instances, each saves 100 gas (like in G-10) - meaning a total saving of 11600 gas.
>
> > **\[G‑12] `<x> += <y>` costs more gas than `<x> = <x> + <y>` for state variables (-= too)**\
> > Out of scope
>
> Why is that out-of-scope? The `TokenggAVAX.sol` and `ERC20Upgradeable.sol` contracts are in scope, and this optimization wasn't included in the C4audit output.
>
> Overall, My gas report saves an additional amount of 12956 gas.

So the total gas savings are **17218 gas**. Therefore, I believe my gas report should be the one selected for the report.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/125#issuecomment-1416805415)**:**

> @NoamYakov - Thank you for the comment, to clarify regarding G-11, are you saying to cache the address of Storage or to make it Immutable as to avoid the extra SLOAD?
>
> The += is a knee jerk reaction I have in judging and have judged it as OOS for all reports.\
> My own benchmarks show that's it's a very marginal saving, especially because it will not save gas when used in combination with `unchecked`, either way it would raise / lower the majority of reports so it will not matter as much.
>
> Lmk about G-11 please.

[**NoamYakov (warden) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/125#issuecomment-1416807927)**:**

> I'm saying to cache the address of Storage in order to avoid the extra SLOAD.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2022-12-gogopool-findings/issues/125#issuecomment-1422190992)**:**

> I agree with the suggested refactoring, I believe there's fair ground to cap the value of the refactoring to a certain value (e.g 5k gas saved). That said, after factoring that in, the refactoring would save the most gas.
>
> Technically a better solution would be to just use `immutable` which would avoid all SLOADs.

***

## Mitigation Review

### Introduction

Following the C4 audit contest, 3 wardens ([hansfriese](https://twitter.com/hansfriese), RaymondFam, and [ladboy233](https://twitter.com/Xc1008Cu)) reviewed the mitigations for all identified issues. Additional details can be found within the [C4 GoGoPool Versus Mitigation Review contest repository](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest).

### Overview of Changes

**Summary from the Sponsor:**

> Here's our biggest changes to look out for:
>
> 1.

Minipool State Machine - We've tightened up the allowed state transitions including a new recreate minipool method that's atomic and doesn't allow node ops to withdraw funds or hijack a minipool.
> 2. Tracking AVAX High Water - Our previous system forced some tradeoffs to which AVAX is calculated in HighWater. We added a new variable `AVAXValidating` which tracks amount of AVAX actually validating on the P-Chain, and High Water is simply the highest validating amount during the period.
> 3. TokenGGP - Changed how tokens are inflated to actually mint rather than track tokens in the ProtocolDAO
> 4. Contract Upgrades - We're now able to upgrade as expected, to a contract with the same name as the existing contract
> 5.

m/multisig-labs/gogopool/pull/51 | M-10          | Reset rewards start time in cancel minipool                                   |
| Not fixing                                        | M-11          | N/A                                                                           |
| https://github.com/multisig-labs/gogopool/pull/40 | M-12          | Base cancelMinipool delay on minipool creation time not rewards start time    |
| https://github.com/multisig-labs/gogopool/pull/41 | M-13          | If staked GGP doesn't cover slash amount, slash it all                        |
| https://github.com/multisig-labs/gogopool/pull/38 | M-14          | Added bounds for duration passed by Node Operator                             |
| Not fixing in this version of the protocol        | M-15          | N/A                                                                           |
| https://github.com/multisig-labs/gogopool/pull/50 | M-16          | ggAVAX max redeem incorrect, **not fixing**, but made test to illustrate.

|
| https://github.com/multisig-labs/gogopool/pull/28 | M-17          | Remove the state transition from Staking to Error.                            |
| Not fixing in this version of the protocol        | M-18          | N/A                                                                           |
| https://github.com/multisig-labs/gogopool/pull/42 | M-19          | We removed minipool count entirely.                                           |
| https://github.com/multisig-labs/gogopool/pull/33 | M-20          | Return correct value from maxMint and maxDeposit when the contract is paused. |
| https://github.com/multisig-labs/gogopool/pull/37 | M-21          | Prevents division by zero error blocking startRewardCycle().

ation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/57) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/39)
* **M-17:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/58) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/42)
* **M-19:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/59) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/44)
* **M-20:** Mitigation confirmed by [RaymondFam](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/60) and [hansfriese](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/45)

The 4 remaining mitigations have either not been confirmed and/or introduced new issues.

See full details below.\
_(Note: mitigation reviews below are referenced as `MR:S-N`, `MitigationReview:NewIssueSeverity-NewIssueNumber`)_

### [\[MR:M-01\] The node operators are likely to be slashed in an unfair way](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/23)

_Submitted by hansfriese_

#### Original Issue

H-04: [Hijacking of node operators minipool causes loss of staked funds](https://github.com/code-423n4/2022-12-gogopool-findings/issues/213)

#### Comments

In the original implementation, the protocol had some unnecessary state transitions and it was possible for node operators to interfere the recreation process.\
The main problem was the `recordStakingEnd()` and `recreateMiniPool()` were separate external functions and the operator could frontrun the `recreateMiniPool()` and call `withdrawMinipoolFunds()`.

#### Mitigation

[PR #23](https://github.com/multisig-labs/gogopool/pull/23)\
The mitigation added a new function `recordStakingEndThenMaybeCycle()` and handled `recordStakingEnd()` and `recreateMiniPool()` in an atomic way.\
With this mitigation, the state flow is now as below and it is impossible for a node operator to interfere the recreation process.\
![Imgur](https://imgur.com/JCoiCvl.jpg) But this mitigation created another minor issue that the node operators have risks to be slashed in an unfair way.

#### New issue

The node operators are likely to be slashed in an unfair way

#### Code snippet

https://github.com/multisig-labs/gogopool/blob/4bcef8b1d4e595c9ba41a091b2ebf1b45858f022/contracts/contract/MinipoolManager.sol#L464

#### Proof of concept

In the previous implementation, I assumed rialtos are smart enough to recreate minipools only when it's necessary.\
But now, the recreation process is included as an optional way in the `recordStakingEndThenMaybeCycle()`, so as long as the check `initialStartTime + duration > block.timestamp` at L#464 passes, recreation will be processed.

Now let us consider the timeline. One validation cycle in the whole sense contains several steps as below. ![Imgur](https://imgur.com/p6xWqgC.jpg)

1. Let us assume it is somehow possible that `startTime[1] > endTime[0]`, i.e., the multisig failed to start the next cycle at the exact the same timestamp to the previous end time. This is quite possible due to various reasons because there are external processes included.

In this case the timeline will look as below.\
   ![Imgur](https://imgur.com/e292GIO.jpg) As an extreme example, let us say the node operator created a minipool with duration of 42 days (with 3 cycles in mind) and it took 12 days to start the second cycle. When the `recordStakingEndThenMaybeCycle()` (finishing the second cycle) was called, two cases are possible.

* It is possible that the `initialStartTime + duration <= block.timestamp`. In this case, the protocol will not start the next cycle. And the node validation was done for two cycles different to the initial plan.
* If `initialStartTime + duration > block.timestamp`, the protocol will start the third cycle. But on the end of that cycle, it is likely that the node is not eligible for reward by the Avalanche validators voting.

(Imagine the node op lent a server for 42 days, then 42-14\*2-12=2 days from the third cycle start the node might have stopped working and does not meet the 80% uptime condition) Then the node operator will be punished and GGP stake will be slashed. This is unfair.

2. Assume it is 100% guaranteed that `startTime[n+1]=endTime[n]` for all cycles.\
   The timeline will look as below and we can say the second case of the above scenario still exists if the node operator didn't specify the duration to be a complete multiple of 14 days. (365 days is not!)\
   ![Imgur](https://imgur.com/tGHnMTL.jpg) Then the last cycle end will be later than `initialStartTime + duration` and the node op can be slashed in an unfair way again.\
   So even assuming the perfect condition, the protocol works in kind of unfair way for node operators.

The main reason of this problem is that technically there exists two timelines.

And the protocol does not track the actual validation duration that the node was used accurately.\
At least, the protocol should not start a new cycle if `initialStartTime + duration < block.timestamp + 14 days` because it is likely that the node operator get punished at the end of that cycle.

#### Recommended additional mitigation

* If it is 100% guaranteed that `startTime[n+1]=endTime[n]` for all cycles, I recommend starting a new cycle only if `initialStartTime + duration < block.timestamp + 14 days`.
* If not, I suggest adding a new state variable that will track the actual validation period (actual utilized period).

#### Conclusion

Mitigation error - created another issue for the same edge case.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/23#issuecomment-1437349389)**:**

> Per full discussion with sponsor and warden [here](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/23#issuecomment-1433580156), Medium seems like the most appropriate Severity, the finding is valid though in that the FSM can behave in an unintended way due to lack of modulo math.

***

### [\[MR:M-02\] Deficiency of slashed GGP amount should be made up from node operator's AVAX](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/6)

_Submitted by RaymondFam, also found by_ [_hansfriese_](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/25) _and_ [_ladboy233_](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/61)

https://github.com/multisig-labs/gogopool/blob/9ad393c825e6ac32f3f6c017b4926806a9383df1/contracts/contract/MinipoolManager.sol#L731-L733

#### Original Issue

H-06: [MinipoolManager: node operator can avoid being slashed](https://github.com/code-423n4/2022-12-gogopool-findings/issues/136)

#### Impact

If staked GGP doesn't cover slash amount, slashing it all will not be fair to the liquid stakers.

Slashing is rare, and that the current 14 day validation cycle which is typically 1/26 of the minimum amount of GGP staked is unlikely to bump into this situation unless there is a nosedive of GGP price in AVAX. The deficiency should nonetheless be made up from `avaxNodeOpAmt` should this unfortunate situation happen.

#### Proof of Concept

[File: MinipoolManager.sol#L731-L733](https://github.com/multisig-labs/gogopool/blob/9ad393c825e6ac32f3f6c017b4926806a9383df1/contracts/contract/MinipoolManager.sol#L731-L733)

```solidity
		if (staking.getGGPStake(owner) < slashGGPAmt) {
			slashGGPAmt = staking.getGGPStake(owner);
		}
```

As can be seen from the code block above, in extreme and unforeseen cases, the difference between `staking.getGGPStake(owner)` and `slashGGPAmt` can be significant. Liquid stakers would typically and ultimately care about how they are going to be adequately compensated with, in AVAX preferably.

#### Recommended Mitigation Steps

Consider having the affected if block refactored as follows:

```diff
		Staking staking = Staking(getContractAddress("Staking"));
		if (staking.getGGPStake(owner) < slashGGPAmt) {
			slashGGPAmt = staking.getGGPStake(owner);

+			uint256 diff = slashGGPAmt - staking.getGGPStake(owner);
+			Oracle oracle = Oracle(getContractAddress("Oracle"));
+			(uint256 ggpPriceInAvax, ) = oracle.getGGPPriceInAVAX();
+			uint256 diffInAVAX = diff.mulWadUp(ggpPriceInAvax);
+                       staking.decreaseAVAXStake(owner, diffInAVAX);
+			Vault vault = Vault(getContractAddress("Vault"));
+			vault.transferAVAX("ProtocolDAO", diffInAVAX);

		}
```

[**0xju1ie (GoGoPool) commented**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/6#issuecomment-1433528943)**:**

> As the warden pointed out, this event is very unlikely. I think that it is a reasonable risk for the protocol to take.

Slashing does not exist in Avalanche, you simply get rewards or do not, so personally, I don't think slashing their AVAX would be a good solution as it goes against Avalanche practices. Will bring it up to the team to see what they think.

[**0xju1ie (GoGoPool) commented**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/6#issuecomment-1433711442)**:**

> The team seems to be in consensus that this is unlikely and that we will not be changing. The proposed solution goes against how Avalanche protocol operates so we believe it would not be an appropriate fix.

[**RaymondFam (warden) commented**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/6#issuecomment-1433960117)**:**

> The proposed solution refers to slashing of AVAX in C Chain where this measure is solely at the discretion of the protocol. But I understand the complication entailed in making fixes for incidents that will be rare to occur.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/6#issuecomment-1435639671)**:**

> I believe the Sponsors opinion to be valid, and that the scenario may be unlikely.
>
> However, I think the math shows that the system would be taking a loss which may be notable.
>
> I'm thinking Medium Severity would be appropriate, but a Nofix seems acceptable given the odds (a "risk treasury" could be created to account for this scenario without needing to change the contracts).

***

### [\[MR:M-03\] `amountAvailableForStaking()` not fully utilized with `compoundedAvaxNodeOpAmt` easily forfeited](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/52)

_Submitted by RaymondFam_

https://github.com/multisig-labs/gogopool/blob/3b5ab1d6505ef9be6197c4056acd38d6bed4aff6/contracts/contract/tokens/TokenggAVAX.sol#L134-L146\
https://github.com/multisig-labs/gogopool/blob/3b5ab1d6505ef9be6197c4056acd38d6bed4aff6/contracts/contract/MinipoolManager.sol#L497-L505

#### Original Issue

M-08: [Recreated pools receive a wrong AVAX amount due to miscalculated compounded liquid staker amount](https://github.com/code-423n4/2022-12-gogopool-findings/issues/620)

#### Impact

The mitigated step is implemented at the expense of economic loss to both the node operators and the liquid stakers if `compoundedAvaxNodeOpAmt <= ggAVAX.amountAvailableForStaking()`.

#### Proof of Concept

Here is a typical scenario:

1.

The protocol now assumes that a 1:1 nodeOp:liqStaker funds ratio is guaranteed to be met because of the atomic transaction that has also been implemented.
2. This is deemed an edge case that will only be optimally utilized if `compoundedAvaxAmt == ggAVAX.amountAvailableForStaking()`.
3. The atomic transaction is going to fail if `compoundedAvaxAmt > ggAVAX.amountAvailableForStaking()` after all due to situations like liquid stakers have been actively calling [`withdrawAVAX()`](https://github.com/multisig-labs/gogopool/blob/3b5ab1d6505ef9be6197c4056acd38d6bed4aff6/contracts/contract/tokens/TokenggAVAX.sol#L196-L205).

Under normal circumstances, [`ggAVAX.amountAvailableForStaking()`](https://github.com/multisig-labs/gogopool/blob/3b5ab1d6505ef9be6197c4056acd38d6bed4aff6/contracts/contract/tokens/TokenggAVAX.sol#L134-L146) is going to be adequate enough to cater for `compoundedAvaxNodeOpAmt`.

This should not be easily forfeited without first checking whether or not `ggAVAX.amountAvailableForStaking()` is greater than `compoundedAvaxNodeOpAmt`.

// So we re-set it here to their initial start time for this minipool
			staking.setRewardsStartTime(mp.owner, mp.initialStartTime);
		}

		ProtocolDAO dao = ProtocolDAO(getContractAddress("ProtocolDAO"));
		uint256 ratio = staking.getCollateralizationRatio(mp.owner);
		if (ratio < dao.getMinCollateralizationRatio()) {
			revert InsufficientGGPCollateralization();
		}

		resetMinipoolData(minipoolIndex);

		setUint(keccak256(abi.encodePacked("minipool.item", minipoolIndex, ".status")), uint256(MinipoolStatus.Prelaunch));

		emit MinipoolStatusChanged(nodeID, MinipoolStatus.Prelaunch);
	}
```

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/52#issuecomment-1437348706)**:**

> Per full discussion with sponsor and warden [here](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/52#issuecomment-1433722646), I believe we can agree with the validity of the finding but we're unclear in terms of resolution.

>
> I'll give it a second check before awarding, but marking as valid for now.

the funds plus rewards back to MinipoolManager
> 		minipoolMgr.recordStakingEndThenMaybeCycle{value: totalAvax + rewards}(mp.nodeID, block.timestamp, rewards);
> 		mp = minipoolMgr.getMinipoolByNodeID(mp.nodeID);
> 		return mp;
> 	}
>
> 	function processMinipoolEndWithoutRewards(address nodeID) public returns (MinipoolManager.Minipool memory) {
> +	        if (ggAVAX.amountAvailableForStaking() == 0) revert UnableToProcess();
> 		MinipoolManager.Minipool memory mp = minipoolMgr.getMinipoolByNodeID(nodeID);
> 		uint256 totalAvax = mp.avaxNodeOpAmt + mp.avaxLiquidStakerAmt;
> 		uint256 rewards = 0;
> 		// Send the funds plus NO rewards back to MinipoolManager
> 		minipoolMgr.recordStakingEndThenMaybeCycle{value: totalAvax + rewards}(mp.nodeID, block.timestamp, rewards);
> 		mp = minipoolMgr.getMinipoolByNodeID(mp.nodeID);
> 		return mp;
> 	}
> ```
>
> The added check ensures the atomic transaction is going to reliably recreate amidst the right pick for the validating amount I recommended earlier in this issue.

>
> Otherwise, opting for a resolution by using `canClaimAndInitiateStaking()` is going to be tricky due to the restricting `requireValidStateTransition()`.

***

### [\[MR:M-04\] There is no way to retrieve the rewards from the MultisigManager and rewards are locked in the vault](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/46)

_Submitted by hansfriese, also found by_ [_ladboy233_](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/8)

#### Original Issue

M-21: [Division by zero error can block RewardsPool#startRewardCycle if all multisig wallet are disabled](https://github.com/code-423n4/2022-12-gogopool-findings/issues/143)

#### Comments

The protocol provides an external function `startRewardsCycle()` so that anyone can start a new reward cycle if necessary.\
Before mitigation, there was an edge case where this function will revert due to division by zero. Edge case: there are no multisigs enabled.

(possible when `Ocyticus.disableAllMultisigs(), Ocyticus.pauseEverything()` is called)

#### Mitigation

[PR #37](https://github.com/multisig-labs/gogopool/pull/37)\
If no multisig is enabled, the mitigation sends the rewards to the `MultisigManager` and it makes sense.\
But this created another issue. There is no way to retrieve the rewards back from the `MultisigManager`.

#### New issue

There is no way to retrieve the rewards from the `MultisigManager` and rewards are locked in the vault.

#### Code snippet

https://github.com/multisig-labs/gogopool/blob/4bcef8b1d4e595c9ba41a091b2ebf1b45858f022/contracts/contract/RewardsPool.sol#L229

#### Impact

There is no way to retrieve the rewards from the `MultisigManager` and rewards are locked in the vault.

#### Proof of Concept

The rewards that were accrued in this specific edge case are locked in the `MultisigManager`.\
It is understood that the funds are not lost and the protocol can be upgraded with a new `MultisigManager` contract with a proper function.\
I evaluate the severity of the new issue as Medium because funds are locked in some specific edge cases and only withdrawable after contract upgrades.

#### Recommended additional mitigation

Add a new external function in the `MultisigManager` with `guardianOrSpecificRegisteredContract("Ocyticus", msg.sender)` modifier and distribute the pending rewards to the active multisigs.

#### Conclusion

Mitigation error - created another issue for the same edge case.

[**0xju1ie (GoGoPool) confirmed and commented**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/46#issuecomment-1433705450)**:**

> I think this is valid. We do plan on adding a claim or withdrawal method that allows an enabled multisig to receive those funds.

This can also be easily added with an upgrade once the issue occurs if we arent able to add it to this version.

[**Alex the Entreprenerd (judge) commented**](https://github.com/code-423n4/2023-02-gogopool-mitigation-contest-findings/issues/46#issuecomment-1435717627)**:**

> Seems like `MultisigManager` doesn't offer a sweep function, which would cause tokens to be stuck.
>
> Due to the conditionality, I agree with Medium Severity.

***

## Disclosures

C4 is an open organization governed by participants in the community.

C4 Contests incentivize the discovery of exploits, vulnerabilities, and bugs in smart contracts. Security researchers are rewarded at an increasing rate for finding higher-risk issues. Contest submissions are judged by a knowledgeable security researcher and solidity developer and disclosed to sponsoring developers. C4 does not conduct formal verification regarding the provided code but instead provides final verification.

C4 does not provide any guarantee or warranty regarding the security of this project. All smart contract software should be used at the sole risk and responsibility of users.

# 🔐 Zellic Audit

## GoGoPool

#### Smart Contract Security Assessment

**February 22, 2023**

_Prepared for:_ **Multisig Labs**

_Prepared by:_ **Katerina Belotskaia and Vlad Toie**

Zellic Inc.

ellic-audit.md#55-file-basesol)
  * [5.6 File: `BaseAbstract.sol`](zellic-audit.md#56-file-baseabstractsol)
  * [5.7 File: `Storage.sol`](zellic-audit.md#57-file-storagesol)
  * [5.8 File: `TokenGGP.sol`](zellic-audit.md#58-file-tokenggpsol)
  * [5.9 File: `Vault.sol`](zellic-audit.md#59-file-vaultsol)
  * [5.10 File: `MinipoolManager`](zellic-audit.md#510-file-minipoolmanager)
  * [5.11 File: `MultisigManager`](zellic-audit.md#511-file-multisigmanager)
  * [5.12 File: `Ocyticus`](zellic-audit.md#512-file-ocyticus)
  * [5.13 File: `Oracle`](zellic-audit.md#513-file-oracle)
  * [5.14 File: `ProtocolDAO`](zellic-audit.md#514-file-protocoldao)
  * [5.15 File: `RewardsPool`](zellic-audit.md#515-file-rewardspool)
  * [5.16 File: `Staking`](zellic-audit.md#516-file-staking)
* [6 Audit Results](zellic-audit.md#6-audit-results)
  * [6.1 Disclaimers.](zellic-audit.md#61-disclaimers)

## About Zellic

Zellic was founded in 2020 by a team of blockchain specialists with more than a decade of combined industry experience.

We are leading experts in smart contracts and Web3 development, cryptography, web security, and reverse engineering. Before Zellic, we founded perfect blue, the top competitive hacking team in the world. Since then, our team has won countless cybersecurity contests and blockchain security events.

Zellic aims to treat clients on a case-by-case basis and to consider their individual, unique concerns and business needs. Our goal is to see the long-term success of our partners rather than simply provide a list of present security issues. Similarly, we strive to adapt to our partners’ timelines and to be as available as possible. To keep up with our latest endeavors and research, check out our website zellic.io or follow @zellic\_io on Twitter. If you are interested in partnering with Zellic, please email us at hello@zellic.io or contact us on Telegram at https://t.me/zellic\_io.

## 1 Executive Summary

Zellic conducted an audit for Multisig Labs from November 14th to 29th, 2022.

Our general overview of the code is that it was well-organized and structured. The code coverage is high, and tests are included for the majority of the functions. Some areas of the code have limited negative testing, which could be improved. The documentation was adequate, although it could be improved. The code was easy to comprehend, and in most cases, intuitive.

Zellic thoroughly reviewed the GoGoPool codebase to find protocol-breaking bugs as defined by the documentation and to find any technical issues outlined in the Methodology section (2.2) of this document.

Specifically, taking into account GoGoPool’s threat model, we focused heavily on issues that would break core invariants such as the management of the minipools, staking, withdrawing and minting shares, and the states of the Storage contract.

During our assessment on the scoped GoGoPool contracts, we discovered seven findings.

Of the seven findings, four were of high severity, one was of medium severity, one was of low severity and the remaining finding was informational.

Additionally, Zellic recorded its notes and observations from the audit for Multisig Labs’s benefit in the Discussion section [( 4 )](#user-content-fn-1)[^1] at the end of the document.

### Breakdown of Finding Impacts

|  Impact Level | Count |
| :-----------: | :---: |
|    Critical   |   0   |
|      High     |   4   |
|     Medium    |   1   |
|      Low      |   1   |
| Informational |   1   |

## 2 Introduction

### 2.1 About GoGoPool

GoGoPool allows Avalanche users to stake a minimum of 0.01 AVAX and operate a validator node with a minimum of 1000 AVAX, while providing instant liquidity and earning rewards for validating subnets. As an open protocol, any individual, business, or subnet can plug into the protocol without being charged platform fees.

### 2.2 Methodology

During a security assessment, Zellic works through standard phases of security auditing including both automated testing and manual review. These processes can vary significantly per engagement, but the majority of the time is spent on a thorough manual review of the entire scope.

Alongside a variety of open-source tools and analyzers used on an as-needed basis, Zellic focuses primarily on the following classes of security and reliability issues:

**Basic coding mistakes.** Many critical vulnerabilities in the past have been caused by simple, surface-level mistakes that could have easily been caught ahead of time by code review. We analyze the scoped smart contract code using automated tools to quickly sieve out and catch these shallow bugs. Depending on the engagement, we may also employ sophisticated analyzers such as model checkers, theorem provers, fuzzers, and so forth as necessary. We also perform a cursory review of the code to familiarize ourselves with the contracts.

**Business logic errors.** Business logic is the heart of any smart contract application. We manually review the contract logic to ensure that the code implements the expected functionality as specified in the platform’s design documents. We also thoroughly examine the specifications and designs themselves for inconsistencies, flaws, and vulnerabilities. This involves use cases that open the opportunity for abuse, such as flawed tokenomics or share pricing, arbitrage opportunities, and so forth.

**Complex integration risks.** Several high-profile exploits have not been the result of any bug within the contract itself; rather, they are an unintended consequence of the contract’s interaction with the broader DeFi ecosystem. We perform a meticulous review of all of the contract’s possible external interactions and summarize the associated risks: for example, flash loan attacks, oracle price manipulation, MEV/sandwich attacks, and so forth.

**Codematurity.** We review for possible improvements in the codebase in general. We look for violations of industry best practices and guidelines and code quality standards. We also provide suggestions for possible optimizations, such as gas optimization, upgradeability weaknesses, centralization risks, and so forth.

For each finding, Zellic assigns it an impact rating based on its severity and likelihood. There is no hard-and-fast formula for calculating a finding’s impact; we assign it on a case-by-case basis based on our professional judgment and experience. As one would expect, both the severity and likelihood of an issue affect its impact; for instance, a highly severe issue’s impact may be attenuated by a very low likelihood. We assign the following impact ratings (ordered by importance): Critical, High, Medium, Low, and Informational.

Similarly, Zellic organizes its reports such that the most important findings come first in the document rather than being ordered on impact alone.

Thus, we may sometimes emphasize an “Informational” finding higher than a “Low” finding. The key distinction is that although certain findings may have the same impact rating, their importance may differ. This varies based on numerous soft factors, such as our clients’ threat models, their business needs, their project timelines, and so forth. We aim to provide useful and actionable advice to our partners that consider their long-term goals rather than simply provide a list of security issues at present.

### 2.3 Scope

The engagement involved a review of the following targets:

**GoGoPool Contracts**

**Repository**: https://github.com/multisig-labs/gogopool-contracts

**Versions**: 7768287e94bff0f2e12f03427309777e82a6e2fc

**Contracts**:

* BaseAbstract.sol
* RewardsPool.sol
* BaseUpgradeable.sol
* MultisigManager.sol
* Oracle.sol
* MinipoolManager.sol
* Vault.sol
* Storage.sol
* Base.sol
* ProtocolDAO.sol
* Ocyticus.sol
* tokens/TokenggAVAX.sol
* tokens/TokenGGP.sol
* tokens/upgradeable/ERC20Upgradeable.sol
* tokens/upgradeable/ERC4626Upgradeable.sol
* ClaimProtocolDAO.sol
* ClaimNodeOp.sol
* Staking.sol

**Type**: Solidity

**Platform**: EVM-compatible

### 2.4 Project Overview

Zellic was contracted to perform a security assessment with two consultants for a total of four person-weeks. The assessment was conducted over the course of two calendar weeks.

**Contact Information**

The following project managers were associated with the engagement:

```
Jasraj Bedi , Co-founder
jazzy@zellic.io
```

```
Chad McDonald , Engagement Manager
chad@zellic.io
```

The following consultants were engaged to conduct the assessment:

```
Katerina Belotskaia , Engineer
kate@zellic.io
```

```
Vlad Toie , Engineer
vlad@zellic.io
```

### 2.5 Project Timeline

The key dates of the engagement are detailed below.

```
November 14, 2022 Kick-off call
November 14, 2022 Start of primary review period
November 28, 2022 End of primary review period
```

## 3 Detailed Findings

### 3.1 The `transferAVAX` function allows arbitrary transfers

* **Target** : Vault.sol
* **Category** : Business Logic
* **Likelihood** : Medium
* **Severity** : High
* **Impact** : **High**

#### Description

The `transferAVAX` function is used to perform transfers of avax between two registered contracts.

```solidity
function transferAVAX (
    string memory fromContractName,
    string memory toContractName,
    uint256 amount
) external onlyRegisteredNetworkContract{

    // Valid Amount?
    if (amount == 0 ) {
    revertInvalidAmount();
    }

    // Emit transfer event
    emit AVAXTransfer(fromContractName, toContractName, amount);

    // Make sure the contracts are valid, will revert if not
    getContractAddress(fromContractName);
    getContractAddress(toContractName);

    // Verify there are enough funds
    if (avaxBalances[fromContractName] < amount) {
        revert InsufficientContractBalance();
    }

    // Update balances
    avaxBalances[fromContractName] = avaxBalances[fromContractName] - amount;
    avaxBalances[toContractName] = avaxBalances[toContractName] + amount;
}
```

The current checks ensure that the `msg.sender` is a `registeredNetworkContract`; however, the function lacks a check on whether the `msg.sender` actually calls the function or not.

#### Impact

Due to the fact that `fromContractName` can be an arbitrary address, a presumably malicious `registeredNetworkCContract` can drain the avax balances of all the other registered contracts.

#### Recommendations

We recommend removing the `fromContractName` parameter altogether and ensuring that the funds can only be transferred by the caller of the function, `msg.sender`.

```solidity
// @audit-info doesn't exist in rocketvault
function transferAVAX (
    string memory fromContractName,
    string memory toContractName,
    uint256 amount
) external onlyRegisteredNetworkContract {

    // Valid Amount?
    if(amount=) 0 ) {
        revert InvalidAmount();
    }
    // Emit transfer event
    emit AVAXTransfer(msg.sender, toContractName, amount);

    // Make sure the contracts are valid, will revert if not
    getContractAddress(msg.sender);
    getContractAddress(toContractName);

    // Verify there are enough funds
    if (avaxBalances[msg.sender] < amount) {
        revert InsufficientContractBalance();
    }
    // Update balances
    avaxBalances[msg.sender] = avaxBalances[msg.sender] - amount;
    avaxBalances[toContractName] = avaxBalances[toContractName] + amount;
}
```

#### Remediation

The issue has been fixed by Multisig Labs in commit 84211f.

### 3.2 Ocyticus does not include the Staking pause

* **Target** : Ocyticus, Staking
* **Category** : Business Logic
* **Likelihood** : Medium
* **Severity** : High
* **Impact** : **High**

#### Description

The `pauseEverything` and `resumeEverything` functions are used to restrict access to important functions.

```solidity
function pauseEverything() external onlyDefender {
    ProtocolDAO dao = ProtocolDAO(getContractAddress(“ProtocolDAO”));
    dao.pauseContract(“TokenggAVAX”);
    dao.pauseContract(“MinipoolManager”);
    disableAllMultisigs();
}

/// @notice Reestablish all contract's abilities
/// @dev Multisigs will need to be enabled seperately, we dont know which  ones to enable
function resumeEverything() external onlyDefender {
    ProtocolDAO dao = ProtocolDAO(getContractAddress(“ProtocolDAO”));
    dao.resumeContract(“TokenggAVAX”);
    dao.resumeContract(“MinipoolManager”);
}
```

Apart from the `TokenGGAvax` and `MinipoolManager`, the `Staking` contract also makes use of the `whenNotPaused` modifier for its important functions. The paused state, will, however, not trigger at the same time with the `pauseEverything` call, since the `Staking` contract is omitted here, both for pausing and resuming.

#### Impact

Should an emergency arise, `pauseEverything` will be called.

In this case, `Staking` will be omitted, which could put user funds in danger.

#### Recommendations

We recommend ensuring that the `Staking` contract is also paused in the `pauseEverything` function as well as un-paused in the `resumeEverything` function.

```solidity
function pauseEverything() external onlyDefender {
    ProtocolDAO dao = ProtocolDAO(getContractAddress(“ProtocolDAO”));
    dao.pauseContract(“TokenggAVAX”);
    dao.pauseContract(“MinipoolManager”);
    dao.pauseContract(“Staking”);
    disableAllMultisigs();
}

/// @notice Reestablish all contract's abilities
/// @dev Multisigs will need to be enabled separately, we don't know which ones to enable
function resumeEverything() external onlyDefender {
    ProtocolDAO dao = ProtocolDAO(getContractAddress(“ProtocolDAO”));
    dao.resumeContract(“TokenggAVAX”);
    dao.resumeContract(“MinipoolManager”);
    dao.resumeContract(“Staking”);
}
```

#### Remediation

The issue has been fixed by Multisig Labs in commit dbc499.

### 3.3 The reward amount manipulation.

* **Target** : ClaimNodeOp.sol
* **Category** : Business Logic
* **Likelihood** : Medium
* **Severity** : High
* **Impact** : **High**

#### Descriptions

A staker is eligible for the upcoming rewards cycle if they have staked their tokens for a long enough period of time. The reward amount is distributed in proportion to the amount of funds staked by the user from the total amount of funds staked by all users who claim the reward. But since the `rewardsStartTime` is the time of creation of only the first pool, and during the reward calculations all staked funds are taken into account, even if they have not yet been blocked and can be withdrawn, the attack described below is possible.

The attack scenario:

1. An attacker stakes ggp tokens and creates a minipool with a minimum `avaxAssignmentRequest` value.
2. The multisig initiates the staking process by calling the `claimAndInitiateStaking` function.
3. Wait for the time of distribution of rewards.
4.

Before the reward distribution process begins, the attacker creates a new minipool with the maximum `avaxAssignmentRequest` value.
5. Initiate the reward distribution process.
6. Immediately after that, the attacker cancels the minipool with `cancelMinipool` function before the `claimAndInitiateStaking` function call and returns most part of their staked funds.

#### Impact

The attacker can increase their reward portion without actually staking their own funds.

#### Recommendations

Take into account only the funds actually staked, or check that all minipools have been launched.

#### Remediation

The issue has been fixed by Multisig Labs in commits c90b2f and f49931.

### 3.4 Network registered contracts have absolute storage control.

* **Target** : Project-wide
* **Category** : Business Logic
* **Likelihood** : Low
* **Severity** : High
* **Impact** : **High**

#### Description

The network-registered contracts have absolute control over the storage that all the contracts are associated with through the `Storage` contract. This is inherent due to the overall design of the protocol,which makes use of a single `Storage` contract eliminating the need of local storage. For that reason any `registeredContract` can `update` **any** storage slot even if it “belongs” to another contract.

```solidity
modifier onlyRegisteredNetworkContract() {
  if (booleanStorage[keccak256(abi.encodePacked(“contract.exists”,
  msg.sender))] == false && msg.sender != guardian) {
    revertInvalidOrOutdatedContract();
  }
  _;
}

// ...

function setAddress (bytes32 key, address value) external onlyRegisteredNetworkContract {
  address Storage[key] = value;
}

function setBool (bytes32 key, bool value) external onlyRegisteredNetworkContract {
  boolean Storage[key] = value;
}

function setBytes(bytes32 key, bytes calldata value) external onlyRegisteredNetworkContract {
  bytes Storage[key] = value;
}
```

As an example, the setter functions inside the `Staking` contract have different restrictions for caller (e.g., the `setLastRewardsCycleCompleted` function can be called only by `ClaimNodeOp` contract), but actually the `setUint` function from it may be called by any `RegisteredNetworkContract`.

#### Impact

We believe that in a highly unlikely case,a malicious `networkRegistered` contract could potentially alter the entire protocol `Storage` to their will. Additionally, if it were possible to `setBool` of an arbitrary address, then this scenario would be further exploitable by a malicious developer contract.

#### Recommendations

We recommend paying extra attention to the registration of `networkContracts`, as well as closely monitoring where and when the `setBool` function is used, since the network registration is based on a boolean value attributed to the contract address.

#### Remediation

The issue has ben acknowledged by the Multisig Labs. Their official reply is reproduced below:

> While it is true that any registered contract can write to Storage, we view all of the separate contracts comprising the Protocol as a single system. A single entity (either the Guardian Multisig or in future the ProtocolDAO) will be in control of all of the contracts. In this model, if an attacker can register a single malicious contract, then they are also in full control of the Protocol itself. Because all of the contracts are treated as a single entity, there is no additional security benefit to be gained by providing access controls between the various contract’s storage slots.

As a mitigation, the Protocol will operate several distributed Watchers that will continually scan the central Storage contract, and alert on any changes.

### 3.5 Oracle may reflect an outdated price

* **Target** : Oracle
* **Category** : Business Logic
* **Likelihood** : Medium
* **Severity** : Medium
* **Impact** : **Medium**

#### Description

Some functions at protocol-level make use of the `getGGPPriceInAvax`. This getter retrieves the `price`, which is set by the `Rialto` multisig.

```solidity
/// @notice Get the price of GGP denominated in AVAX
/// @return price of ggp in AVAX
/// @return timestamp representing when it was updated
function getGGPPriceInAVAX() external view returns (uint256 price, uint256 timestamp) {
  price = getUint(keccak256(“Oracle.GGPPriceInAVAX”));

  if(price == 0) {
    revert InvalidGGPPrice();
  }
  timestamp = getUint(keccak256(“Oracle.GGPTimestamp”));
}
```

Due to the nature of on-chain price feeds, `Oracles` need to have an as-often-as-possible policy in regards to how often the price gets updated. For that reason, the reliance on the `Rialto` may be problematic should it fail to update the `price` often enough.

#### Impact

Should the price be erroneous, possible front-runs may happen at the protocol level, potentially leading to a loss of funds on the user-end side.

#### Recommendations

We recommend implementing a slippage check, which essentially does not allow a price to be used should it have been updated more than x blocks ago.

#### Remediation

The finding has been acknowledged by the Multisig Labs team. Their official reply is reproduced below:

> The price of GGP is used in the Protocol to determine collateralization ratios for minipools as well as slashing amounts. If the price of GGP is unknown or out- dated, the protocol cannot operate. So our remediation for this will be to have a distributed set of Watchers that will Pause the Protocol if the GGP Price becomes outdated. At some point in the future the Protocol will use on-chain TWAP price oracles to set the GGP price.

### 3.6 Fields are not reset exactly after their usage

* **Target** : MinipoolManager
* **Category** : Business Logic
* **Likelihood** : Low
* **Severity** : Low
* **Impact** : Low

### Description

Due to the nature of the protocol, some fields are queried and used in one intermediary state of the application and then reset in the last state of the application.

lFunds(address nodeID) external nonReentrant {
  int256 minipoolIndex = requireValidMinipool(nodeID);
  address owner = onlyOwner(minipoolIndex);
  requireValidStateTransition(minipoolIndex, MinipoolStatus.Finished);
  setUint(keccak256(abi.encodePacked(“minipool.item”, minipoolIndex, “.status”)), uint256(MinipoolStatus.Finished));

  uint256 avaxNodeOpAmt = getUint(keccak256(abi.encodePacked(“minipool.item”, minipoolIndex, “.avaxNodeOpAmt”)));

  uint256 avaxNodeOpRewardAmt = getUint(keccak256(abi.encodePacked(“minipool.item”, minipoolIndex, “.avaxNodeOpRewardAmt”)));

  uint256 totalAvaxAmt = avaxNodeOpAmt + avaxNodeOpRewardAmt;

  Staking staking = Staking(getContractAddress(“Staking”));
  staking.decreaseAVAXStake(owner, avaxNodeOpAmt);

  Vault vault = Vault(getContractAddress(“Vault”));
  vault.withdrawAVAX(totalAvaxAmt);
  owner.safeTransferETH(totalAvaxAmt);
  }
```

and then either reset in the `recordStakingEnd` function, to the new rounds’ `avaxNodeOpRewardAmt`, or set to 0 in `recordStakingError`.

The protocol’s structure assumes that the way in which the states are transitioned through is consistent.

#### Impact

Should major changes occur in the future of the protocol,we suspect that some states that are presumably reset in an eventual state of the protocol may be omitted. This could in turn lead to unexpected consequences to the management of the minipool.

#### Recommendations

We highly recommend that once important storage states are used, they should also be reset. In this way, future versions of the protocol will have a solid way of transitioning without requiring additional synchronization of storage state.

#### Remediation

The issue has ben acknowledged by the Multisig Labs. Their official reply is reproduced below:

> The Protocol maintains some fields in `Storage` so that data such as `avaxNodeOpRewardAmt` can be displayed to the end user. The fields will be reset if the user relaunches a minipool with the same `nodeID` again in the future. This is by design.

### 3.7 Contracts can deposit arbitrary tokens in the Vault

* **Target** : Vault.sol
* **Category** : Business Logic
* **Likelihood** : Medium
* **Severity** : Low
* **Impact** : Informational

#### Description

Multiple functions from the `Vault` contract allow arbitrary tokens to be deposited and withdrawn by `networkRegistered` contracts.

For example, see the `depositToken` function:

```solidity
function depositToken(string memory networkContractName, ERC20 tokenContract, uint256 amount) external guardianOrRegisteredContracts {
  // Valid Amount?
  if (amount == 0 ) {
    revert InvalidAmount();
  }
  // Make sure the network contract is valid (will revert if not)
  getContractAddress(networkContractName);

  // Get contract key
  bytes32 contractKey = keccak256(abi.encodePacked(networkContractName, address(tokenContract)));
  // Emit token transfer event
  emit TokenDeposited(contractKey, address(tokenContract), amount);
  // Send tokens to this address now, safeTransfer will revert if it fails
  tokenContract.safeTransferFrom(msg.sender, address(this), amount);
  // Update balances
  tokenBalances[contractKey] = tokenBalances[contractKey] + amount;
}
```

#### Impact

As per the current implementation, there are no security implications.

However, we consider that the `Vault` plays an essential role in the entire protocol, and thus we highly recommend fixing this issue for posterity.

#### Recommendations

Upon discussions with the Multisig Lab team, we settled that the best mitigation is `whitelisting` the `tokenContract` that are used in each function. This further allows flexibility and security in smoothly upgrading the `Vault` should it support more tokens. In that case, the mitigated version of the function could be:

```solidity
function depositToken(string memory networkContractName, ERC20 tokenContract, uint256 amount) external guardianOrRegisteredContracts {

  require(whitelisted[tokenContract], “tokenContract not whitelisted”);

  if (amount == 0 ) {
    revert InvalidAmount();
  }

  // ...
```

#### Remediation

The issue has been fixed by Multisig Labs in commit 644e8e.

## 4 Discussion

The purpose of this section is to document miscellaneous observations that we made during the assessment.

### 4.1 The `rewardsCycleEnd` calculation.

The `rewardsCycleEnd` value from the `TokenggAVAX` contract should always be evenly divisible by `rewardsCycleLength`. This condition, however, is only met during the contract initialization, where the `rewardsCycleLeng` this initially calculated. The `rewardsCycleLength` is eventually recalculated inside the `syncRewards` function, but this time, there is no check whether the value is evenly divisible or not.

#### Remediation

The issue has been fixed by Multisig Labs in commit 556ac4.

### 4.2 Lack of checks.

1. The `calculateAndDistributeRewards` function from the `ClaimNodeOp` contract does not explicitly verify that the `stakerAddr` is a valid staker address.
2. Add a check that `rewardsPool.getRewardsCycleCount()` is not zero to the `calculateAndDistributeRewards` function from the `ClaimNodeOpcontract`.
3.

The `registerMultisig` function in the `MultisigManager` contract does not check that the `multisig.count` value has reached 10 to ensure that `There will never be more than 10 total multisigs`, which is a comment on the `requireNextActiveMultisig` function.
4. The `recordStakingStart` function in the `MinipoolManager` contract does not validate that the `startTime` value is not greater than the current time.
5. The set `RewardsStartTime` function in the `Staking` contract does not validate that the `time` value is not greater than the current time or that it can be only the current time or 0.
6. The `getInflationAmt` in the `RewardsPool` contract does not process the case when the max amount of tokens are released (22\_500\_000, the total minted amount).

#### Remediation

The issue has been fixed by Multisig Labs in commit 878b2e.

### 4.3 The process of distributing ggp rewards

In order to receive a reward the staker must be registered for the required amount of time.

But the current implementation of the protocol allows users to stake most of the funds immediately before distribution of the reward. The `isEligible` function verifies that the staker should be registered at least `ProtocolDAO`. `RewardsEligibilityMinSeconds` amount of seconds before the rewards cycle starts (this happens after the first minipool is created), but this check takes into account only the first staking, and the first staked amount may be minimal. Therefore, users can use this possibility to their advantage.

#### Remediation

The discussion point has been acknowledged by the Multisig Labs team. Their official reply is reproduced below:

> We acknowledge that this attack is possible and is a side effect of the nature of our rewards protocol and the short duration of validating on Avalanche. There is some cost and difficulty to exploiting this. It depends on one getting a large amount of GGP before a rewards cycle.

If GGP is only available on one AMM, this would greatly move the price with no CEX to arbitrage against. The end result would most likely not be profitable to the attacker if their intention was to dump.

### 4.4 Checks-effects-interactions pattern

We recommend following the checks-effects-interactions pattern during the `claimAndRestake` function in the `ClaimNodeOp` contract by moving the `staking.decreaseGGPRewards(msg.sender, ggpRewards);` line above the external calls.

#### Remediation

The issue has been fixed by Multisig Labs in commit 750812.

### 4.5 Missing status update.

In `MinipoolManager` the `_cancelMinipoolAndReturnFunds` function should reset the `rewardsStartTime` if the `.minipoolCount` value for staker is zero.

#### Remediation

The discussion point has been acknowledged by the Multisig Labs team. Their official reply is reproduced below:

> We don’t think that resetting `rewardsStartTime` is the fix because of the scenario below.

>
> * Day 1: NodeOp1 creates minipool 1, and it gets launched. Reward startTime set to Day 1.
> * Day 14: Minipool 1 ends. mpCount = 0. But rewards is still Day 1 so we can get paid on day 28.
> * Day 15: NodeOp1 creates minipool 2, mpCount = 1
> * Day 15: NodeOp1 cancels it before launch. mpCount = 0. We can’t reset rewards time because we need to get paid on Day 28. We DO reset the `AVAXAssignedHighWatermark`, so the AVAX used for this cancelled minipool doesn’t count. Instead we remediated by splitting up `avaxAssignedHighWater` and `avaxAssigned` in this [PR](https://github.com/multisig-labs/gogopool-contracts/pull/181). Now the AVAX value used for rewards (`avaxAssignedHighWater`), will only be increased when the node is started in `recordStakingStart`.

The issue has been remediated by Multisig Labs in PR 181.

### 4.6 Unused variables

In `Storage`, the `intStorage` and `bytesStorage` mappings and related functions are not used and can be deleted.

#### Remediation

The issue has ben acknowledged by the Multisig Labs and they plan to use them in the future.

### 4.7 Contract upgrades

We recommend paying additional attention when upgrading the contracts. Should the same `Storage` be used, the contract itself might not be `re-initializable` since its storage would already be used by the previously initialized contract. For example, this could happen in the `RewardsPool` contract.

```solidity

function initialize() external onlyGuardian {
  if(getBool(keccak256(“RewardsPool.initialized”))) {

```

Notice that the `RewardPool.initialized` will always be true after the first contract has been initialized.

#### Remediation

The issue has ben acknowledged by the Multisig Labs. Their official reply is reproduced below:

> This is by-design. This specific contract was built to ensure even if upgraded that the `InflationIntervalStartTime` and `RewardsCycleStartTime` values would not be overwritten.

### 4.8 IWithdrawer inheritance

In the `withdrawAVAX` function from Vault, it is assumed that msg.sender has inherited the `IWithdrawer` interface. We consider that there could be a check for this during the registration process, since in `Vault`, for example, `withdrawAVAX` cannot be used (it will revert) unless `msg.sender` has the `IWithdrawer` interface implemented beforehand.

#### Remediation

The discussion point has been acknowledged by the Multisig Labs team. Their official reply is reproduced below:

> We added methods to register, unregister and upgrade contracts to the Protocol Dao. We’ll add a check to our deploy scripts to handle verifying that we inherit from IWithdrawer.

### 4.9 Protocol DAO setters range

In protocol DAO, setters that deal with rates should range from 0.0 - 1.0 ether. This is not directly enforced as of now. The same could be done for the rest of the setter functions in the contract.

#### Remediation

The issue has been fixed by Multisig Labs in commit f49931.

### 4.10 Leftover tokens in `RewardsPool`.

In the `startRewardsCycle`, the allotment each party is supposed to receive is calculated; however, due to the nature of the arithmetics, some tokens might be left out due to rounding errors.

#### Remediation

The issue has ben acknowledged by the Multisig Labs and they have determined that the amounts would not be significant.

## 5 Threat Model

The purpose of this section is to provide a full threat model description for each function.

As time permitted, we analyzed each function in the smart contracts and created a written threat model for some critical functions. A threat model documents a given function’s externally controllable inputs and how an attacker could leverage each input to cause harm.

### 5.1 File: `TokenggAVAX`

#### Function: `initialize()`

**Intended behavior:**

* Should initialize all state variables and function calls required for the contract to function.

**Branches and code coverage:**

**Intended branches:**

* Should be callable by anyone?
  * [ ] Test coverage
* Should be called after every upgrade.
  * [ ] Test coverage

**Negative behavior:**

* Shouldn’t allow 2 x calling this.
  * [x] Negative test?

**Preconditions:**

* Assumes it’s not callable by anyone, or that there’s no way someone can frontrun this transaction
* Assumes that the `Storage` is adequately configured (should be fine, since `guardian` role is assigned in the constructor, for the `msg.sender`)

**Inputs:**

* `asset`:
  * **Control** : full control
  * **Checks** : no checks
  * **Impact** : used as underlying asset for the vault
* `storageAddress`:
  * **Control** : full control
  * **Checks** : no checks
  * **Impact** : used as upgradeable storage contract.

#### Function: `receive()`

**Intended behavior:**

This function is used for receiving native tokens. It can be called only by the `asset` address.

**Branches and code coverage:**

**Intended branches:**

* Allow `asset` contract to send native tokens to contract.
  * [x] Test coverage

**Negative behavior:**

* It cannot be called from any other address.
  * [x] Negative test?

**Preconditions:**

* the `asset` should be set after `initialize` call

**Inputs:**

* `msg.value`:
  * **Control** : controllable
  * **Authorization** : no
  * **Impact** : -
* `msg.sender`:
  * **Control** : controllable
  * **Authorization** : `assert(msg.sender == address(asset));`
  * **Impact** : `only accept AVAX via fallback from the WAVAX contract`. Otherwise, the balance information may be out of sync.

**External call analysis**

There are no external calls here.

#### Function: `syncRewards()`

**Intended behavior:**

* Should “distribute rewards” to **TokenggAVAX** holders. Anyone may call this.

`lastSync` - time of last successful call to this function

`rewardsCycleEnd` - the time when the total reward will be available;

`totalReleasedAssets` - the full amount of available tokens for withdrawal + the last reward value from the previous cycle. If the reward was not withdrawn immediately after the end of the cycle when the function `syncRewards` is called for the next cycle, `lastRewardsAmt` value will be added to the value `totalReleasedAssets`, and this reward still will be available for withdrawal.

**Branches and code coverage:**

**Intended branches:**

* `rewardsCycleEnd` = deadline for next `rewardsCycle`
  * [ ] Test coverage
* `lastSync` = current timestamp
  * [ ] Test coverage
* `lastRewardsAmt\_` = to the amount that rewards will deplete from.

* [x] Test coverage
* `totalReleasedAssets` is calculated correctly for the next cycle - not sure that it is calculated correctly because it happens differently during `initialize` call
  * [ ] Test coverage
* `lastRewardsAmt` is calculated for the next cycle if the new reward was deposited.

* [ ] Test coverage
* if rewards didn’t deposit, the `lastRewardsAmt` will equal 0 for the next cycle
  * [ ] Test coverage
* `lastRewardsAmt` is calculated correctly and equals 0 for the first cycle
  * [ ] Test coverage
* if nothing changed since the past cycle `lastRewardsAmt` is calculated correctly and equals 0 and `totalReleasedAssets` was increased by the previous `lastRewardsAmt`
  * [ ] Test coverage
* current `block.timestamp` should be less than `rewardsCycleEnd`
  * [x] Test coverage

**Negative behavior:**

* It basically shouldn’t update unless stuff unless it’s really time to update stuff (see below)
  * [ ] Negative test?
* Shouldn’t allow calling unless the `rewardsCycle` has passed the `block.timestamp`.
  * [x] Negative test?

**Preconditions:**

* Assumes that the state variables (`lastRewardsAmt`, `lastSync`, `rewardsCycleEnd` and `totalReleasedAssets` are properly updated)
* Can be called by anyone.

**Inputs:**

**Function call analysis**

* `asset.balanceOf(address(this))`
  * **What is controllable?** The amount of returned value
  * **If return value controllable, how is it used and how can it go wrong?** It can grow if the asset is artificially pumped in the contract;
  * **What happens if it reverts, reenters, or does other unusual control flow?** Doesn’t revert.

#### Function: `totalAssets()`

**Intended behavior:**

* This function returns the total amount of underlying assets held by the vault.

**Branches and code coverage:**

**Intended branches:**

* After the current cycle ends and the new one starts, the `totalAssets` amount will contain the past `lastRewardsAmt` value.
  * [ ] Test coverage
* `totalAssets` is calculated correctly if the current cycle is going.

* [ ] Test coverage
* If the current cycle ends and the new one doesn’t start, the `totalAssets` should be equal `totalReleasedAssets\_` + `lastRewardsAmt`
  * [ ] Test coverage

**Negative behavior:**

* There’s multiple types of uints there, should ensure that there’s no way that any of them can overflow and block the functionality of the contract.
  * [ ] Negative test?
* must not revert (as per eip4626)
  * [ ] Negative test?

**Preconditions:**

* Assumes `lastSync` is different than 0 (default value, which is never initialized)? this is missing
* assumes that `block.timestamp` is safecasted? just as in syncRewards (currently missing)

**Inputs:**

There aren’t input values here.

**Function call analysis**

There aren’t function calls here.

#### Function: `depositFromStaking()`

**Intended behavior:**

* Should allow converting `native` AVAX tokens to `wAVAX` (just like `wETH`)
* Allows to `MinipoolManager` contract return with drawn funds and deposit reward.

* It is assumed that, at first will be called `MinipoolManager.sol:createMinipool` function, which call `depositAVAX` and after that caller will be able to call `withdrawForStaking` for previously deposited value over `MinipoolManager.sol:claimAndInitiateStaking` and only after that `depositFromStaking` can be called over `recordStakingEnd` or `recordStakingError` functions from `MinipoolManager.sol`

**Branches and code coverage:**

**Intended branches:**

* the `asset` balance of the current contract will increase by the `msg.value` after the call
  * [ ] Test coverage
* `stakingTotalAssets` will decrease by the `baseAmt` value after the call
  * [ ] Test coverage
* `baseAmt` + `rewardAmt` should be equal `msg.value`
  * [ ] Test coverage

**Negative behavior:**

* Shouldn’t be callable by anyone (there’s a check put in place, such that only `onlySpecificRegisteredContract` can call the function.

* [x] Negative test?
* if `stakingTotalAssets` is less than `baseAmt` transaction will be rejected
  * [x] Negative test?

**Preconditions:**

* `stakingTotalAssets` should contain a value more or equal to `baseAmt`.

, how is it used and how can it go wrong?** na
  * **What happens if it reverts, reenters, or does other unusual control flow?** na

#### Function: `withdrawForStaking()`

**Intended behavior:**

* Should perform the `withdrawalfromwAVAX`, for the `MinipoolManager`

**Branches and code coverage:**

**Intended branches:**

* `wAVAX.balanceOf(address(this)) -= assets` and `balanceOf(msg.sender) += as sets`
  * [ ] Test coverage

**Negative behavior:**

* Shouldn’t allow unlimited amount to be withdrawn
  * [x] Negative test?
* Shouldn’t be callable when it’s `paused` (has the `whenNotPaused`) modifier
  * [x] Negative test?
* if `assets` more than the `amountAvailableForStaking` transaction will be rejected
  * [x] Negative test?
* if `asset.balanceOf(address(this))` is less than `assets` transaction will be rejected
  * [ ] Negative test?
* if `msg.sender` is not approved transaction will be rejected
  * [ ] Negative test?

**Preconditions:**

* Assumes that there has been some `depositFromStaking` beforehand.

* Assumes that the same `MinipoolManager` deposited the amount. And that there cannot be any issues should one deposit and someone else (with same role) withdraw.

**Inputs:**

* `assets`:
  * **Control** : full control
  * **Checks** : `assets > amountAvailableForStaking()`
  * **Impact** : arbitrary input for the amount of `assets` that are to be withdrawn from the `wAVAX`
* `msg.sender`:
  * **Control** : only approved MinipoolManager contract
  * **Checks** : `onlySpecificRegisteredContract(“MinipoolManager”, msg.sender)`
  * **Impact** : since the caller can withdraw any amount of funds through this function, it is critically important that it is called only by a trusted contract.

**Function call analysis**

* `withdrawer.receiveWithdrawalAVAX{value: assets}();`
  * **What is controllable?** the `assets,withdrawer;` it basically calls the `receiveWithdrawalAVAX` on the `msg.sender`!!! Really important
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** reenters: no problems because the contract being called is trusted. reverts: no problems
* `IWAVAX(address(asset)).withdraw(assets);`
  * **What is controllable?** the `assets` value; the `asset` address is state var
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

#### Function: `depositAVAX` compare with `deposit()` from inherited

**Intended behavior:**

* Allows any user to deposit `AVAX` in exchange for `wAVAX`.

It basically doesn’t transfer the `wAVAX` back to the user, it keeps it and issues shares to the user.

**Branches and code coverage:**

**Intended branches:**

* `previewDeposit` should issue the amount of shares correctly!!
  * [x] Test coverage
* Should transfer the \`wAVAX back to the user.
  * [x] Test coverage
* Should exchange user’s supplied `AVAX` into `wAVAX`
  * [x] Test coverage

**Negative behavior:**

* Shouldn’t issue more or less shares than intended.
  * [x] Negative test?

**Preconditions:**

* Assumes users would use this function to deposit, rather than depositing on their own.
* Assumes `previewDeposit` calculates the amount of shares correctly.

n’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `afterDeposit()`
  * **What is controllable?** `assets` - the amount of deposited native tokens
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `\_mint()`
  * **What is controllable?** `msg.sender` - is minted tokens receiver address
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `previewDeposit()` & `convertToShares()`
  * **What is controllable?** `assets`- the amount of deposited native tokens
  * **If return value controllable, how is it used and how can it go wrong?** if there are any mistakes during shares value calculations, then caller will get more or less shares than expected.

If more then caller will be able to drain other users funds, if less then caller will withdraw less native tokens that was deposited.
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

#### Function: `withdrawAvax()` compare this with `withdraw()`from inherited

**Intended behavior:**

* Supposed to `withdrawwAVAX` on behalf of the `msg.sender`, and then transfer the native `AVAX` back to the `msg.sender`.

**Branches and code coverage:**

**Intended branches:**

* the `wavax` balance of the contract should decrease(by `assets`)
  * [x] Test coverage
* the `avax` balance of user should increase (by `assets`)
  * [ ] Test coverage
* the `shares` of the user should decrease (by `shares`)
  * [x] Test coverage
* make sure that `preivewWithdraw` calculates the shares properly, in all market conditions
  * [ ] Test coverage

**Negative behavior:**

* shouldn’t allow withdrawing if `_burn` reverted
  * [ ] Negative test?
* shouldn’t allow burning on behalf of other users
  * [x] Negative test?

**Preconditions:**

* Assumes there are no rounding errors in `previewWithdraw` or other similar arithmetic issues.
* Assumes that user has enough `shares` to actually withdraw enough `wAVAX`

**Inputs:**

* `assets`:
  * **Control** : full control; the amount of assets that the user `intends` to withdraw.

* **Checks** : there is no check here, however, it’s assumed that `previewWithdraw` calculates the amount of shares properly,and then that `_burn` fails should the `msg.sender` not have enough shares to actually receive the amount of assets.
  * **Impact** : arbitrary input for the amount of `assets` that are to be withdrawn from the `wAVAX`
* `msg.sender`:
  * **Control** : any caller
  * **Checks** : must have the appropriate amount of shares
  * **Impact** : the caller will receive the appropriate amount of native tokens

**Function call analysis**

* `previewWithdraw(assets)`
  * **What is controllable?** the assets parameter;
  * **If return value controllable, how is it used and how can it go wrong?** return the amount of shares. In case of wrong calculations a caller can burn an excessive number of shares or, conversely, burn too few and receive disproportionately many native tokens.

* **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `IWAVAX(address(asset)).withdraw(assets);`
  * **What is controllable?** the `assets` value; the `asset` address is state var
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

#### Function: `redeemAVAX()` compare with `redeem()` from inherited

**Intended behavior:**

* Should redeem the `shares` for underlying native `avax`. Similar to how `withdraw` works.

**Branches and code coverage:**

* No test coverage

**Intended branches:**

* `assets` value is calculated correctly
  * [ ] Test coverage
* `totalReleasedAssets` is decreased by `assets` value
  * [ ] Test coverage
* `msg.sender` received the `assets` amount of native tokens
  * [ ] Test coverage
* token gg balance of `msg.sender` is decreased by `shares` value
  * [ ] Test coverage

**Negative behavior:**

* shouldn’t allow withdrawing if `_burn` reverted
  * [x] Negative test?
* shouldn’t allow burning on behalf of other users
  * [ ] Negative test?
* revert if `contract.paused` is `True`
  * [x] Negative test?

**Preconditions:**

* Assumes that user has enough `shares` to burn.

**Inputs:**

* `shares`:
  * **Control** : controlled
    * **Checks** : balance of `msg.sender` should be more or equal of `shares` amount
  * **Impact** : the number of gg tokens that the user can burn and receive a certain number of native tokens.

* \`msg.sender\`\`:
  * **Control** : any caller
    * **Checks** : must have the appropriate amount of shares
  * **Impact** : the caller will receive the appropriate amount of native tokens

**Function call analysis**

* `previewRedeem(shares)`
  * **What is controllable?** the shares parameter;
  * **If return value controllable, how is it used and how can it go wrong?** return the amount of `assets`. In case of wrong calculations a caller can receive a lot (thereby stealing other users funds) or, conversely, too few native tokens.

* **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `IWAVAX(address(asset)).withdraw(assets);`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

### 5.2 File: `ClaimNodeOP`

#### Function: `calculateAndDistributeRewards()`

**Intended behavior:**

* Set the share of rewards that a `staker` is owed. (Fraction of 1 ether)

**Branches and code coverage:**

_Lacks extensive testing._

**Intended branches:**

* Update the `rewardsCycleCount` of staker.
  * [ ] Test coverage
* Ensure calculations are properly performed.
  * [ ] Test coverage
* Increase the `ggpRewards` for the `stakerAddr` based on the input `totalEligibleGGPStaked`.
  * [x] Test coverage

**Negative behavior:**

* Should fail if `stakerAddr` is not eligible for rewards.

* [x] Negative test?

**Preconditions:**

* Assumes `stakerAddr` is a valid one.
* Assumes that the caller has used the correct `totalEligibleGGPStaked` amount.

**Inputs:**

* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlyMultisig`
  * **Impact** : the access to this function should be restricted because this function allows to assign any part of reward budget to any `stakerAddr`.
* `stakerAddr`:
  * **Control** : full control
  * **Checks** : no checks at this level; But will revert during the `increaseGGPRewards` function call.
  * **Impact** : the address of valid staker who can claim the reward.
* `totalEligibleGGPStaked`:
  * **Control** : full control
  * **Checks** : there aren’t checks
  * **Impact** : the total amount of staked funds, from which the percentage of reward to `stakerAddr` will be calculated. So this value allow to control the reward part for `stakerAddr`.

**Function call analysis**

* `staking.getLastRewardsCycleCompleted(stakerAddr)`
  * **What is controllable?** `stakerAddr` is controllable
  * **If return value controllable, how is it used and how can it go wrong?** if someone will be able to manipulate `lastRewardsCycleCompleted` value, the `stakerAddr` will be able to double receive the reward.
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `staking.getEffectiveGGPStaked(stakerAddr);`
  * **What is controllable?** `stakerAddr` is controllable
  * **If return value controllable, how is it used and how can it go wrong?** the amount of staked tokens is used to calculate the percentage of the total staked tokens.

* **What happens if it reverts, reenters, or does other unusual control flow?** no problem
* `staking.setLastRewardsCycleCompleted(stakerAddr, rewardsPool.getRewardsCycleCount());`
  * **What is controllable?** `stakerAddr` is controllable
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value.
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problem
* `staking.resetAVAXAssignedHighWater(stakerAddr);`
  * **What is controllable?** `stakerAddr` is controllable
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value.
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problem
* `staking.increaseGGPRewards(stakerAddr, rewardsAmt);`
  * **What is controllable?** `stakerAddr` is controllable
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value.

* **What happens if it reverts, reenters, or does other unusual control flow?** no problem
* `staking.setRewardsStartTime(stakerAddr, 0);`
  * **What is controllable?** `stakerAddr` is controllable
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value.
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problem

#### Function: `claimAndRestake()`

**Intended behavior:**

* Allows `msg.sender` to claim the `rewards` they were allocated.

**Branches and code coverage:**

_Lacks extensive testing._

**Intended branches:**

* Should decrease rewards balance of `msg.sender`
  * [x] Test coverage
* Restake the amount of `ggpRewards - claimAmt`
  * [ ] Test coverage

**Negative behavior:**

* Should not allow claiming more than `msg.sender` was owed
  * [x] Negative test?

**Preconditions:**

* Assumes `msg.sender` has some rewards
* Assume that the `vault` holds enough tokens to pay the rewards for `msg.sender`.

**Inputs:**

* `msg.sender`:
  * **Control** : -
  * **Checks** : if the `ggpRewards` value is zero, will revert.
  * **Impact** : the address who owns non zero reward value.
* `claimAmt`:
  * **Control** : full control
  * **Checks** : should not be more that the reward: claimAmt > ggpRewards
  * **Impact** : the amount of withdrawn funds, the surplus will be restake.

**Function call analysis**

* `vault.withdrawToken(address(this), ggp, restakeAmt)`
  * **What is controllable?** `restakeAmt` is controllable
  * **If return value controllable, how is it used and how can it go wrong?** there is no return value here.
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if there are not enough tokens.
* `staking.getGGPRewards(msg.sender)`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** return value is used for calculating the amount of rewards that `msg.sender` is owed.

* **What happens if it reverts, reenters, or does other unusual control flow?** no problems

### 5.3 File: `ClaimProtocolDAO.sol`

#### Function: `spend()`

**Intended behavior:**

Allows to spend the ProtocolDAO’s GGP rewards

**Branches and code coverage:**

**Intended branches:**

* The balance of `recipientAddress` is increased by `amount;` there is a revert put in place in case `transfer` fails.

* [x] Test coverage

**Negative behavior:**

* should be rejected if this contract has not enough ggp tokens in the `vault.tokenBalance`
  * [x] Negative test?
* should reject if `msg.sender` isn’t the guardian
  * [x] Negative test?

**Preconditions:**

* `msg.sender` is the guardian
* tokens should be transferred to `ClaimProtocolDAO` contract over the `vault.transferToken` function

**Inputs:**

* `amount`:
  * **Control** : limited control
  * **Checks** : `amount==0||amount>vault.balanceOfToken(“ClaimProtocolDAO”, ggpToken)`
  * **Impact** :
* `recipientAddress`:
  * **Control** : controlled
  * **Checks** : there aren’t checks here
  * **Impact** : since there are no address checks, in case of a mistake, tokens can be transferred to the wrong user.

* `invoiceID`:
  * **Control** : controlled
  * **Checks** : there aren’t checks here
  * **Impact** : no impact
* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlyGuardian`
  * **Impact** : it allows caller to withdraw the entire balance of ggpToken of this contract from vault. The access to this function should be restricted.

**Function call analysis**

* `vault.withdrawToken()`
  * **What is controllable?** recipientAddress, amount
  * **If return value controllable, how is it used and how can it go wrong?** there is no return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if msg.sender doesn’t have enough tokens

### 5.4 File:BaseUpgradeable.sol

The contract is inherited from `BaseAbstract.sol` and `Initializable.sol` (@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol);

#### Function: `_BaseUpgradeable_init()`

Allows to initialize the `gogoStorage` storage address.

The function is internal and can be called only once due to `onlyInitializing` modifier.

### 5.5 File: `Base.sol`

The contract is inherited from `BaseAbstract.sol`; The contract contains only constructor with initialization of `gogoStorage` address.

### 5.6 File: `BaseAbstract.sol`

#### Function: `setters()`

**Intended behavior:**

Allows you to make changes to the data stored in the shared storage. All function is internal, therefore, they cannot be called directly. But they are called from various functions from inherited contracts.

### 5.7 File: `Storage.sol`

#### Function: `setGuardian()`

**Intended behavior:** Allow to reassign the guardian address. But to complete this process the new guardian should call `confirmGuardian` function.

**Branches and code coverage:**

**Intended branches:**

* After successful call the `guardian` address didn’t change.
  * [x] Test coverage

**Negative behavior:**

* Reject if `msg.sender` isn’t the guardian; check put in place.

* [x] Negative test?

**Preconditions:**

`msg.sender` is current guardian.

**Inputs:**

* msg.sender:
  * **Control** : -
  * **Checks** : msg.sender != guardian
  * **Impact** : due to the guardian having a lot of control over the protocol, it’s critically important that an untrusted caller doesn’t have access to this function.

**Function call analysis**

There aren’t external calls here.

#### Function: `confirmGuardian()`

**Intended behavior:** Allow to reassign the guardian address. But to complete this process the new guardian should call `confirmGuardian` function.

**Branches and code coverage:**

**Intended branches:**

* After successful call the `guardian` address is equal to `msg.sender` and `newGuardian`.
  * [x] Test coverage

**Negative behavior:**

* Reject if `msg.sender` isn’t the `newGuardian`; check put in place.
  * [x] Negative test?

**Preconditions:**

The current guardian called the `setGuardian` function and `msg.sender` became the `newGuardian`.

**Inputs:**

* msg.sender:
  * **Control** : -
  * **Checks** : msg.sender !=newGuardian
  * **Impact** : due to the guardian having a lot of control over the protocol, it’s critically important that an untrusted caller doesn’t have access to this function.

**Function call analysis**

There aren’t external calls here.

#### Function: `setters()`

**Intended behavior:**

* Should be used among more contracts as a shared means of storage

**Branches and code coverage:**

**Intended branches:**

* Should update the {type} of value located at each particular key.
  * [ ] Test coverage; Limited test coverage

**Negative behavior:**

* Network registered contracts shouldn’t abuse the `booleanStorage[keccak256(a bi.encodePacked(“contract.exists”, msg.sender))]` modifier. Basically once a contract is `whitelisted`, it can remove/register other contracts as `network` registered, or modify any other states altogether.

* [ ] Negative test?

**Preconditions:**

* Assumes that `msg.sender` handles the states properly, and doesn’t have typos when reading/updating specific states. Basically allf unctions that interact with the getters/ setters/ deleters from other contracts should be extremely well tested.

### 5.8 File: `TokenGGP.sol`

The contract is standard `ERC20` from `@rari-capital/solmate/src/tokens/ERC20.sol`.

### 5.9 File: `Vault.sol`

#### Function: depositAVAX()`\*\*`

**Intended behavior:**

Allows registered contract to deposit avax.

**Branches and code coverage:**

**Intended branches:**

* `avaxBalances` of `msg.sender` increased by `msg.value`
  * [x] Test coverage

**Negative behavior:**

* if `msg.sender` is not `RegisteredNetworkContract` transaction will be reverted
  * [x] Negative test?
* if msg.value == 0, will be reverted
  * [x] Negative test?

**Preconditions:**

* `msg.sender` should be registered by the guardian

**Inputs:**

* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlyRegisteredNetworkContract`
  * **Impact** : no impact
* `msg.value`:
  * **Control** : limited control
  * **Checks** : msg.value == 0
  * **Impact** : no impact

**Function call analysis**

There aren’t external calls here.

#### Function: `withdrawAVAX()`

**Intended behavior:**

Allows registered contract to withdraw the deposited avax.

steredNetworkContract` transaction will be reverted
  * [ ] Negative test?
* if `avaxBalances[msg.sender] < amount`, transaction will be reverted
  * [x] Negative test?

**Preconditions:**

* avaxBalances of msg.sender & amount
* msg.sender should be registered contract by guardian

**Inputs:**

* `msg.sender`:
  * **Control** : -
  * **Checks** : onlyRegisteredNetworkContract
  * **Impact** : should has non zero balance for withdraw
* `amount`:
  * **Control** : controlled
  * **Checks** : avaxBalances\[getContractName(msg.sender)] < amount
  * **Impact** : must withdraw only his tokens

**Function call analysis**

* `withdrawer.receiveWithdrawalAVAX()`
  * **What is controllable?** amount - partly controlled, the `avaxBalances[msg.sender] > amount`
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t a return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** function is nonReentrant and state is updated before the external call.

#### Function: `transferAVAX()`

**Intended behavior:**

Allows transferring the balance from one registered contract to another.

Allows a transfer, not from the owner, and there is also no check for an allowance from the owner

**Branches and code coverage:**

**Intended branches:**

* `avaxBalances[toContractName]` is increased amount
  * [x] Test coverage
* `avaxBalances[fromContractName]` is decreased by amount
  * [x] Test coverage

**Negative behavior:**

* Should be rejected if `avaxBalances[fromContractName] < amount`
  * [x] Negative test?
* Should be rejected if `toContractName` and `fromContractName` is not added to `gogoStorage`
  * [x] Negative test?
* Should be rejected if msg.sender is not`fromContractName`
  * [ ] Negative test?

**Preconditions:**

* `toContractName` and `fromContractName` is added to `gogoStorage`
* `msg.sender` is `RegisteredNetworkContract`
* `avaxBalances[fromContractName] & amount`

**Inputs:**

* `toContractName`:
  * **Control** : controlled
  * **Checks** : contract name should be saved inside gogoStorage
  * **Impact** : in the case of an incorrect recipient, funds may be lost.

* `fromContractName`:
  * **Control** : controlled
    * **Checks** : contract name should be saved inside gogoStorage
  * **Impact** : the contract which funds will be transferred, in this case the `msg.sender` has full control
* `msg.sender`:
  * **Control** : -
  * **Checks** : onlyRegisteredNetworkContract
  * **Impact** : -
* amount:
  * **Control** : controlled
  * **Checks** : `avaxBalances[fromContractName] < amount`
  * **Impact** : -

**Function call analysis**

There aren’t external calls here.

#### Function: `depositToken()`

**Intended behavior:**

Allows registered contract to deposit any tokens

**Branches and code coverage:**

**Intended branches:**

* `tokenBalances` of networkContractName & contractKey is increased by `amount`
  * [x] Test coverage

**Negative behavior:**

* Should reject if `msg.sender` is not `guardianOrRegisteredContracts`
  * [x] Negative test?

**Preconditions:**

* msg.sender has enough tokens
* msg.sender is guardianOrRegisteredContracts

**Inputs:**

* `amount`:
  * **Control** : limited control
  * **Checks** : amount == 0
  * **Impact** : no problems
* `tokenContract`:
  * **Control** : full control
  * **Checks** : there isn’t checks here
  * **Impact** : address of external contract to be called
* `networkContractName`:
  * **Control** : limited control
  * **Checks** : contract name should be saved inside gogoStorage
  * **Impact** : the recipient of tokens, in the case of an incorrect recipient, funds may be lost.

**Function call analysis**

* `tokenContract.safeTransferFrom()`
  * **What is controllable?** amount
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `msg.sender` doesn’t have enough tokens

#### Function: `withdrawToken()`

**Intended behavior:**

* Allow `registered msg.sender` to withdraw ERC20 tokens.

**Branches and code coverage:**

**Intended branches:**

* Check `withdrawalAddress`?
  * [x] Test coverage
* Decrease `tokenBalance[paid(caller, token)]`
  * [x] Test coverage
* Validate the `tokenContract`, such that no arbitrary tokens can be used.
  * [ ] Test coverage

**Negative behavior:**

* Shouldn’t allow withdrawing more than `msg.sender` owns.

* [x] Negative test?

**Preconditions:**

* Assumes `msg.sender` is registered;
* Assumes that the `tokenAddress` is legit and not some malicious token

**Inputs:**

* `withdrawalAddress`:
  * **Control** : full control
  * **Checks** : no checks
  * **Impact** : in the case of an incorrect recipient, funds may be lost.
* `tokenAddress`:
  * **Control** : full control
  * **Checks** : no checks
  * **Impact** : should allow to pass only trusted contracts.
* `amount`:
  * **Control** : limited control
  * **Checks** : check that it’s != 0 and that user has more balance than it.
  * **Impact** : shouldn’t allow to pass more tokens amount than caller owns.

**Function call analysis**

* `tokenContract.safeTransfer(withdrawalAddress, amount)`
  * **What is controllable?** `withdrawalAddress`, `amount`
  * **If return value controllable, how is it used and how can it go wrong?** no checks on `withdrawalAddress`.

* **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `msg.sender` doesn’t have enough tokens

#### Function: `transferToken()`

**Intended behavior:**

* Transfer token from one contract(msg.sender) to another

**Branches and code coverage:**

**Intended branches:**

* Validate the `tokenContract`, such that no arbitrary tokens can be used.
  * [ ] Test coverage
* Assure both contracts are registered.
  * [x] Test coverage
* Compared to the `transferAVAX`, this function does not allow the transfer from arbitrary tokens, and only from `msg.sender`
  * [ ] Test coverage
* Increase `tokenBalances[to]` **AND** decrease `tokenBalances[from]`.
  * [x] Test coverage

**Negative behavior:**

* Revert if `msg.sender` is not a registered contract.
  * [x] Test coverage
* Revert ifmsg.senderdoesn’t have enough tokens amount.
  * [ ] Test coverage

**Preconditions:**

* Assumes both contracts have been registered beforehand.

**Inputs:**

* `networkContractName`:
  * **Control** : full
  * **Checks** : check that it’s registered
  * **Impact** : in the case of an incorrect recipient, funds may be lost.
* `tokenAddress`:
  * **Control** : full control
  * **Checks** : No checks! Any token
  * **Impact** : should allow to pass only trusted contract address.

**Function call analysis**

There aren’t external calls here.

### 5.10 File: `MinipoolManager`

#### Function: `createMinipool()`

**Intended behavior:**

* Create a Minipool. Accepts avax native deposit (which have to be staked in) and it’s open to public.
* Allows to any caller to recreate a minipool is current state is finished or canceled.

**Branches and code coverage:**

**Intended branches:**

* Ensure that the `msg.sender` is a registered staker (required checks are added in each underlying function)
  * [x] Test coverage
* Should ensure that the `avaxAssignmentRequest` can be fulfilled (or that it is atleast achievable)
  * [ ] Test coverage
* User’s `avax` balance should deplete, and the contract’s balance should increase.

`assets` balance of `vault` contract should increase by `msg.value`
  * [x] Test coverage
* if the pool for `nodeID` exists and the current state is Finished or Canceled minipool data should be reset
  * [ ] Test coverage
* create a new poll if the pool for `nodeID` did not exist before
  * [ ] Test coverage
* `Staking.sol:getRewardsStartTime(msg.sender)` should be equal `block.timestamp` if `RewardsStartTime` was zero before the call
  * [x] Test coverage
* `Staking.sol:getMinipoolCount(msg.sender)` should increase by 1
  * [x] Test coverage
* `Staking.sol:getAVAXAssigned(msg.sender)` should increase by `avaxAssignmentRequest`
  * [x] Test coverage
* `Staking.sol:getAVAXStake(msg.sender)` should increase by `msg.value`
  * [x] Test coverage

**Negative behavior:**

* Shouldn’t work when the contract is paused?/
  * [x] Negative test? There isn’t test, but function has modifier `whenNotPaused`
* Should assure that the `nodeId` hasn’t registered beforehand and is unique basically, so no overwrites can be made.

* [ ] Negative test?
* should revert if minipool for `nodeID` already exists and the currentStatus is not Finished or currentStatus is not Canceled
  * [ ] Negative test?
* should revert if `msg.sender` invalid staker
  * [x] Negative test?

**Preconditions:**

* Assumes that the supplied `msg.value` surpasses the minimum staking amount.
* Assumes that the `multisig` that is to be assigned is ≠ 0.
* Assumes that should the`miniPool` exist, it can only be overwritten if the node is either finished or cancelled.

* In the case that an already existing `miniPoolId` exists, it assumes that ALL PRIOR STATES HAVE BEEN RESET (FROM ALL CONTRACTS THAT WOULD HAVE INTERACTED WITH THIS ONE IN THE FIRST)
* `msg.sender` should be registered staker
* msg.sender should stake ggp over Staking.stakeGGP() function

**Inputs:**

* `msg.sender`:
  * **Control** : controlled
  * **Checks** : `staking.increaseAVAXStake()`, `requireValidStaker()` checks `msg.sender` address (should stake ggp over stakeGGP() function)
  * **Impact** : N/A
* `msg.value`:
  * **Control** : N/A
  * **Checks** : `msg.value` should be equal `avaxAssignmentRequest`
  * **Impact** : N/A
* `nodeId`:
  * **Control** : full control
  * **Checks** : there are some checks on whether the `nodeID` has been registered before; need to look into this
  * **Impact** : could potentially be overwritten.

* `duration`:
  * **Control** : full control
    * **Checks** : There are no checks on the duration amount
  * **Impact** : N/A
* `delegationfee`:
  * **Control** : full
  * **Checks** : No checks
  * **Impact** : N/A
* `avaxAssignmentRequest`:
  * **Control** : full control; needs to match `msg.value` since it’s the amount of requested `AVAX` TO BE MATCHED IN THE POOL.
  * **Checks** : there are checks on whether it matches `msg.value`
* there are also some checks on whether it matches the `dao` details; assure that the data returned from there is not 0?
  * **Impact** : N/A

**Function call analysis**

!!! Important functions (withdraw/ deposit/ etc) shouldn’t work when the contract is paused.

t()`
  * **What is controllable?** msg.sender (had to deposit ggp before)
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `increaseAVAXAssigned()`
  * **What is controllable?** msg.sender (had to deposit ggp before), avaxAssignmentRequest
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `increaseAVAXStake()`
  * **What is controllable?** msg.sender (had to deposit ggp before), msg.value
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

#### Function: `cancelMinipool()`

**Intended behavior:**

* Allows owner to cancel existing minipool and get back the deposited funds.

**Branches and code coverage:**

**Intended branches:**

* Should update all details related to the specific `nodeId`. In such a way that one can then be reused eventually (create with same `nodeId`)
  * [x] Test coverage
* Refund all invested funds to the `owner` (deployer)
  * [ ] Test coverage
* Make sure that the minipool is prelaunch (NOT CHECKED); it’s assured though in `requireValidStateTransition` basically, since it checks the current status against the wanted status update.
  * [ ] Test coverage
* `Staking.sol:getAVAXAssigned(msg.sender)` should decrease by `avaxLiquidStakerAmt`
  * [x] Test coverage
* `Staking.sol:getAVAXStake(msg.sender)` should decrease by `avaxNodeOpAmt`
  * [x] Test coverage
* `Staking.sol:getMinipoolCount(msg.sender)` should decrease by 1
  * [x] Test coverage
* the native tokens balance of the caller should increase by the amount of funds previously deposited.

* [x] Test coverage
* After the call, the current state of the minipool is `Canceled`
  * [x] Test coverage

**Negative behavior:**

* Shouldn’t leave previously set fields to their value (eg. the `avaxLiquidStakerAmt`)
  * [x] Negative test?
* Shouldn’t allow unauthorized access(`msg.sender` has to be the `owner`)
  * [x] Negative test?
* should revert if the current state of mini pool isn’t `Prelaunch`
  * [x] Negative test?
* should revert if called non-owner of minipool
  * [x] Negative test?
* should revert if minipool for nodeID doesn’t exist
  * [x] Negative test?

**Preconditions:**

* the minipool should be created over the `createMinipool` function
* the current state of the minipool should be `Prelaunch`
* Assumes that the `nodeId` has been created beforehand and that it’s in the `prelaunch` stage
* Assumes that the `owner` of the `nodeID` calls it

**Inputs:**

* `nodeId`:
  * **Control** : full control
  * **Checks** : there’s a check on whether the minipool is valid.

* **Impact** : Id of minipool which will be canceled and funds will returned to owner.
* `msg.sender`:
  * **Control** : onlyOwner of minipool can call
  * **Checks** : `onlyOwner(index);`
  * **Impact** : only the owner should be able to call this function. otherwise, users will maliciously close other people’s pools to get more rewards.

**Function call analysis**

* `\_cancelMinipoolAndReturnFunds()`
  * **What is controllable?** the `nodeID` is controllable.
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here.
  * **What happens if it reverts, reenters, or does other unusual control flow?** can be reverted if there aren’t enough native tokens for withdraw.
* `owner.safeTransferETH()`
  * **What is controllable?** nothing controllable
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here.

* **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `vault.withdrawAVAX()`
  * **What is controllable?** nothing controllable
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t a return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if contract has not enough shares

#### Function: `_cancelMinipoolAndReturnFunds()`

**Intended behavior:**

* Internal function.
* Main logic of cancelling a minipool and returning the funds that were initially attributed to it.

**Branches and code coverage:**

**Intended branches:**

* Ensure that all states are reset after a Minipool has been cancelled and that `owner` no longer has access to it.
  * [ ] Test coverage
* Ensure that current state allows `cancellation`.
  * [x] Test coverage
* Ensure that `avaxNodeOpAmt` is decreased.

t has a check that `msg.sender == owner of market`)

**Inputs:**

* `nodeID`:
  * **Control** : full control
  * **Checks** : no checks at this level
  * **Impact** : nothing is done on the \`nodeId at this level, so not that important
* `index`:
  * **Control** : full control (it’s generated in previous function)
  * **Checks** : no checks
  * **Impact** : important, as it allows altering states of the `minipool`

**Function call analysis**

* `decreaseAVAXStake()`
  * **What is controllable?** the `owner` (who’s supposed to be the caller of the function)
* it basically decreases the `avaxNodeOpAmt` value which is originally `increased` in the pool creation! The detail here is that it uses `.avaxNodeOpAmount` to store the `amount`, while it decreases the `avaxNodeOpAmt`
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?**
* if it reverts it could affect cancelling the pool.

(that’s why it’s better to only use one type of amount ^ )
* `decreaseAVAXAssigned()`
  * **What is controllable?** nothing, the values are taken from the storage.
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** if current `avaxAssigned` is not enough function will be reverted
* `resetAVAXAssignedHighWater()`
  * **What is controllable?** nothing, the value is taken from the storage.
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** allows to set the `avaxAssignedHighWater` to the previous value, so that the current value is not used when calculating the reward.
* `decreaseMinipoolCount()`
  * **What is controllable?** nothing, the value is taken from the storage.

* **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** reduces the number of pools, if it is reset to zero, this staker will not be taken into account when calculating the reward.

*Branches and code coverage:**

**LIMITED TESTING**

**Intended branches:**

* Should decrease `msg.sender` stake in the`minipool` by `avaxNodeOpAmt`
  * [ ] Test coverage
* the native tokens balance of minipool owner should increase by `totalAvaxAmt` value (deposited amount + reward)
  * [x] Test coverage

**Negative behavior:**

* Shouldn’t be callable by any `msg.sender` or on any `nodeId`
  * [x] Negative test?
* should revert if the owner calls it a second time after the successful first execution
  * [ ] Negative test?
* should revert if the current state of minipool isn’t `Withdrawable` or `Error`
  * [ ] Negative test?
* should revert if called non-owner of minipool
  * [x] Negative test? There isn’t test, but there is a check `onlyOwner` inside the function
* should revert if minipool for nodeID doesn’t exist
  * [x] Negative test? There isn’t test, but there is a check `requireValidMinipool` inside the function

**Preconditions:**

* The minipool should be created over the `createMinipool` function.

* Assumes that the state can transition tofinished, and that the current state of the minipool should be `Withdrawable` (after `recordStakingEnd` call) or `Error`.

**Inputs:**

* `msg.sender`:
  * **Control** : -
  * **Checks** : there is a check that msg.sender is owner of minipool
  * **Impact** : allows to owner of minipool withdraw funds when staking finished
* `nodeID`:
  * **Control** : controlled
  * **Checks** : there are a check of the status of the minipool and a check of the owner
  * **Impact** : allows to return the funds to the owner of minipool if staking was finished

**Function call analysis**

* `owner.safeTransferETH()`
  * **What is controllable?** nothing controllable
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here.

* **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `vault.withdrawAVAX()`
  * **What is controllable?** nothing controllable
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t a return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if contract has not enough shares

#### Function: `claimAndInitiateStaking()`

**Intended behavior:**

* Remove the `minipool's` avax from the protocol and stake it on avalanche, register node as validator.

**Branches and code coverage:**

**Intended branches:**

* Ensure only `multisig rialto` can call this.

* [x] Test coverage
* Should ensure the status of the `minipool` is such that it can be launched
  * [x] Test coverage
* Should decrease the `avax` associated to the pool (something with `.avaxLiquidStakerAmt`)
  * [ ] Test coverage

**Negative behavior:**

* transaction should be rejected if current status != Prelaunch
  * [x] Negative test?
* transaction should be rejected if msg.sender isn’t approved address
  * [x] Negative test?

**Preconditions:**

* Assumes that contract has enough `wavax` staked that can be withdrawable.

**Inputs:**

* msg.sender:
  * **Control** : -
  * **Checks** : `onlyValidMultisig(nodeID)` : msg.sender == assignedMultisig\`
  * **Impact** : only valid multisig can call this function, because the all deposit funds will be transferred to caller.

ontrollable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert in case of error
* `vault.withdrawAVAX()`
  * **What is controllable?** nothing is controlled
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** allows to withdraw `avaxNodeOpAmt` from vault and transfer this funds to caller
* `ggAVAX.withdrawForStaking()`
  * **What is controllable?** nothing is controlled
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** allows to withdraw `avaxLiquidStakerAmt` from vault and transfer this funds to caller

#### Function: `recordStakingStart()`

**Intended behavior:**

* Rialto calls after `claimAndInitiateStaking` succeeded.

**Branches and code coverage:**

**Intended branches:**

* Changes the `start` time. Make sure it’s not in past or future?
  * [ ] Test coverage
* Should transition a `nodeID` into “staking” period.
  * [x] Test coverage

**Negative behavior:**

* Anyone other than `rialto` shouldn’t be able to call this.

* [x] Negative test?
* transaction should be rejected if current status != Launched
  * [x] Negative test?

**Preconditions:**

* Has to assure that enough values are in the `minipool`

**Inputs:**

* `startTime`:
  * **Control** : controllable
  * **Checks** : there isn’t check
  * **Impact** : if the value is far in the future it will be impossible to complete the stacking successfully only with error state
* `txID`:
  * **Control** : controllable
  * **Checks** : there isn’t check
  * **Impact** : n/a
* `nodeID`:
  * **Control** : partly controllable
    * **Checks** : `requireValidMinipool(nodeID)`
  * **Impact** : n/a
* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlyValidMultisig(nodeID) : msg.sender == assignedMultisig`
  * **Impact** : if a malicious user is able to call the function, he will be able to set `startTime` value, at which it will be impossible to successfully complete the stacking with only an error state

**Function call analysis**

There aren’t external function calls here.

#### Function: `recordStakingEnd()`

**Intended behavior:**

* Finish the `validation` period of the `staking` for th `nodeid`.

**Branches and code coverage:**

**Intended branches:**

* Should update all states accordingly after the transfers occur.
  * [x] Test coverage
* End time should be in the future (`starttime` and not in past compared to `block.timestamp`?)
  * [ ] Test coverage
* Should only be callable when the `endtime` is reached.
  * [x] Test coverage

**Negative behavior:**

* Shouldn’t be callable twice or in any other circumstance other than the transition to `withdrawable`
  * [x] Negative test?
* transaction should be rejected if msg.value is not enough
  * [x] Negative test?
* transaction should be rejected if msg.sender isn’t approved address
  * [x] Negative test?
* transaction should be rejected if current status != Staking
  * [x] Negative test?

**Preconditions:**

* the current state of the minipool should be `Staking`.

**Inputs:**

* `msg.value`:
  * **Control** : -
  * **Checks** : `msg.value` should be equal `totalAvaxAmt + avaxTotalRewardAmt`
  * **Impact** :
* `avaxTotalRewardAmt`:
  * **Control** : full control
  * **Checks** : `msg.value` should be `equaltotalAvaxAmt + avaxTotalRewardAmt`
  * **Impact** : the value completely controls how much reward the owner of the pool will receive.

ontrol when staking will be finished

**Function call analysis**

* `slash()`
  * **What is controllable?** minipoolIndex
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** can be reverted if
* `ggAVAX.depositFromStaking`
  * **What is controllable?** `avaxLiquidStakerRewardAmt` - partly controlled
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** revert if `stakingTotalAssets` value is less than `avaxLiquidStakerAmt`
* `vault.depositAVAX()`
  * **What is controllable?** `avaxNodeOpRewardAmt` - partly controlled
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** revert if `previewDeposit` returns 0.

#### Function: `recordStakingError()`

**Intended behavior:**

A staking error occurred while registering the node as a validator.

Can be called after `claimAndInitiateStaking` or `recordStakingStart`

**Branches and code coverage:**

**Intended branches:**

* After the call the new status is `Error`
  * [x] Test coverage

**Negative behavior:**

* transaction should be rejected if current status != `Staking` or `Launched`
  * [x] Negative test?

**Preconditions:**

* current status should be`Launched` or `Staking`

**Inputs:**

* `msg.value`:
  * **Control** : -
  * **Checks** : `msg.value` should be equal `avaxNodeOpAmt + avaxLiquidStakerAmt` - the withdrawn funds
  * **Impact** : amount of returned to staker funds. must not be less than the funds taken.

* `errorCode`:
  * **Control** : controlled
    * **Checks** : there isn’t check here
  * **Impact** : no problems
* `nodeID`:
  * **Control** : controlled
    * **Checks** : check that minipool exists
  * **Impact** : the ID of the minipool that will be completed with an error without issuing a reward.

**Function call analysis**

* `ggAVAX.depositFromStaking()`
  * **What is controllable?** nothing is controlled
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `stakingTotalAssets` is less than `avaxLiquidStakerAmt`
* `vault.depositAVAX()`
  * **What is controllable?** `avaxNodeOpRewardAmt` - partly controlled
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** revert if `previewDeposit` returns 0.

### 5.11 File: `MultisigManager`

#### Function: `registerMultisig()`

**Intended behavior:**

* Register a multisig. Defaults to disabled when first registered. The index where the `multisig` is to be added should be the previously increased `multisig.count`

**Branches and code coverage:**

**Intended branches:**

* “There will never be more than 10 total multisigs” There should be a check that 10 total multisigs can be registered (index != 9) and no more
  * [ ] Test coverage
* Should register the `addr` as a new multisig, only if it doesn’t exist already.
  * [x] Test coverage

**Negative behavior:**

* Shouldn’t allow anyone else other than the guardian to call it
  * [x] Negative test?
* Shouldn’t overwrite already existing multisig
  * [x] Negative test?
* Shouldn’t also enable the multisig
  * [x] Negative test?

**Preconditions:**

* Assumes `getIndexOf` calculates the `index` properly and that two addresses cannot point to same `index`.

* Assumes there’s a way to deregister a `Multisig`? Currently, there’s none; there’s only a way to disable them.

**Inputs:**

**Function call analysis**

#### Function: `enableMultisig()`

**Intended behavior:**

* Should enable a registered multisig.

**Branches and code coverage:**

**Intended branches:**

* The “enabled” of the `index` should be set to `true`.
  * [x] Test coverage

**Negative behavior:**

* Shouldn’t update the index of another multisig.
  * [x] Negative test?
* Shouldn’t be callable by anyone.
  * [ ] Negative test? Not directly, but the `registerMultisig` which has the same modifier is tested when `msg.sender != guardian`
* Shouldn’t enable a multisig that doesn’t exist.
  * [x] Negative test? Not tested, there is a check in the code that prevents this from happening.

**Preconditions:**

* Assumes that the `multisig` has been created beforehand.

**Inputs:**

**Function call analysis**

#### Function: `disableMultisig()`

**Intended behavior:**

* Should disable a registered multisig.

**Branches and code coverage:**

**Intended branches:**

* The “enabled” of the `index` should be set to `false`.
  * [x] Test coverage

**Negative behavior:**

* Shouldn’t be callable by any `msg.sender`
  * [x] Negative test?
* Shouldn’t update an non-existing `index`
  * [x] Negative test? Not tested, there is a check in the code that prevents this from happening.

**Preconditions:**

* Assumes that it can be called under any circumstances. What if it’s called during a transaction where it needs to approve it?

**Inputs:**

**Function call analysis**

### 5.12 File: `Ocyticus`

#### Function: `addDefender()`, `removeDefender()`

**Intended behavior:**

* Allow guardian to `add` or `remove` defenders.

**Branches and code coverage:**

**Lacks testing**

**Intended branches:**

* Should update the `defenders` states properly.
  * [ ] Test coverage

**Negative behavior:**

* Should only be callable by `guardian`; covered by `onlyGuardian` modifier.

* [x] Negative test?

**Preconditions:**

* Assumes they are called by external accounts.

**Inputs:**

n/a

**Function call analysis**

#### Function: `pauseEverything()`

**Intended behavior:**

* Allows the `defender` to `pause` every contract that can be paused.

**Branches and code coverage:**

**Intended branches:**

* Pause `TokenGGAVAX`
  * [x] Test coverage
* Pause `MinipoolManager`
  * [x] Test coverage
* Pause `Staking`(MISSING!) - added as remediation
  * [ ] Test coverage

**Negative behavior:**

**Preconditions:**

* Assumes that the contracts can be `paused`.

* Assumes that when paused, no important functions from these contracts can be called! Double check this

**Inputs:**

n/a

**Function call analysis**

n/a

#### Function: `resumeEverything()`

**Intended behavior:**

**Branches and code coverage:**

**Intended branches:**

* Unpause `TokenGGAVAX`
  * [x] Test coverage
* Unpause `MinipoolManager`
  * [x] Test coverage
* Unpause `Staking` - added as remediation
  * [ ] Test coverage

**Negative behavior:**

**Preconditions:**

* Assumes that some other function will reenable all `multisigs`? That’s not covered in this contract

**Inputs:**

n/a

**Function call analysis**

n/a

### 5.13 File: `Oracle`

#### Function: `setGGPPriceInAVAX()`, `getGGPPriceInAVAXFromOneInch` , `getGGPPriceInAVAX`

**Intended behavior:**

* Interface for off-chain aggregated data, used for pricing the tokens and calculating amounts. The `getGGPPriceInAVAXFromOneInch` should never be used on chain.

**Branches and code coverage:**

**Lacks testing.**

**Intended branches:**

* The functions/contracts that make use of the `GetGGPPriceInAvax` SHOULD have some slippage check in regards to the timestamp when the price has been updated: eg. If the price update happened more than 5 blocks away, revert the transaction.
  * [ ] Test coverage

**Negative behavior:**

* Shouldn’t be callable by anyone. Only Multisig modifier put in place.
  * [x] Negative test?

**Preconditions:**

* `getGGPPriceInAVAXFromOneInch` should only be called off-chain; it’s not reliable enough to be called on chain directly.
* Assumes the Multisig update the `getGGPPRiceInAvax` quite often and that they are trustworthy.

**Inputs:**

There aren’t input values here.

#### Function: `setOneInch()`

**Intended behavior:**

* Allows to guardian to set the address of the One Inch price aggregator contract

**Branches and code coverage:**

**Intended branches:**

* after the call `Oracle.OneInch` is updated to new address
  * [ ] Test coverage

**Negative behavior:**

* Revert if caller is not Guardian.
  * [x] Negative test?

**Preconditions:**

* `msg.sender` is Guardian

**Inputs:**

* `addr`:
  * **Control** : controlled
    * **Checks** : There isn’t check here.
  * **Impact** : The contract address which will be called inside view `getGGPPriceInAVAXFromOneInch` function

**Function call analysis**

There aren’t external calls here.

#### Function: `setGGPPriceInAVAX()`

**Intended behavior:**

* The function is used by the Multisig to update the on-chain prices, with presumably the data retrieved off-chain from `OneInch`.

**Branches and code coverage:**

**Intended branches:**

* Should update the `GGPTimestamp`
  * [ ] Test coverage
* Should update the `GGPPriceInAvax`
  * [ ] Test coverage

**Negative behavior:**

* Revert if caller is not Multisig
  * [ ] Negative test?

**Preconditions:**

* `msg.sender` is Multisig

**Inputs:**

* `price`:
  * **Control** : controlled
  * **Checks** : price != 0
  * **Impact** : the price value is used during `calculateGGPSlashAmt` call
* `timestamp`:
  * **Control** : controlled
  * **Checks** : `timestamp` should be >= `lastTimestamp` or `timestamp` should be <= `block.timestamp`
  * **Impact** : n/a

**Function call analysis**

There aren’t external calls here.

### 5.14 File: `ProtocolDAO`

#### Function: `initialize()`

**Intended behavior:**

* Initialize the contract
* `TotalGGPCirculatingSupply = 18.000.000` but `totalTokenGGPsupply = 22.500.000`

**Branches and code coverage:**

* Not tested in the case of a re-deployment (or upgrade, as discussed with the team).

**Intended branches:**

* All set parameters should have a getter.
  * [x] Test coverage; not test covered, but verified in the code.

**Negative behavior:**

* Setters that deal with rates should range from `0.0 - 1.0 ether`. This is not directly enforced; The same should be done for the rest of the `setter` functions from the contract. This was mitigated.
  * [ ] Negative test?

**Preconditions:**

* Assumes that it can only be called once, and that is through the `onlyGuardian`
* Assumes it will be called BEFORE any other functions that would use the initialized variables will be called.

Maybe assure in important functions that
  * `getBool(keccak256(“ProtocolDAO.initialized”))` is TRUE

**Inputs:**

**Function call analysis**

### 5.15 File: `RewardsPool`

#### Function: `initialize()`

**Intended behavior:**

* Re-initialize all `RewardsPool` variables for a new `RewardsPool`; This is upgradeable

**Branches and code coverage:**

* Not tested in the case of a re-deployment (or upgrade, as discussed with the team).

**Intended branches:**

* Should set the `RewardsPool` variables to their initial values.
  * [ ] Test coverage

**Negative behavior:**

**Preconditions:**

* Assumes it’s the first the this type of contract has been deployed.

**Inputs:**

There aren’t input values here.

**Function call analysis**

There aren’t external calls here.

#### Function: `inflate()`

**Intended behavior:**

* Called to release more `GGP` from the total supply.
* says “mint” new tokens, but all of them are already minted.

**Branches and code coverage:**

**Intended branches:**

* Should update the rewardsCycle total amount.
  * [ ] Test coverage
* Should update the `inflationIntervalElapsedSeconds`
  * [ ] Test coverage
* Should increase circulating supply of tokens.
  * [ ] Test coverage

**Preconditions:**

* Assumes it won’t be called that often

**Inputs:**

There aren’t input values here.

**Function call analysis**

* `dao.setTotalGGPCirculatingSupply(newTotalSupply)`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

#### Function: `startRewardsCycle()`

**Intended behavior:**

* Runs aggprewards cycle if possible.

**Branches and code coverage:**

* More extensive testing required.

**Intended branches:**

* if `dao allotment` exists != transfer `daoAllotment` to DAO != its balance should increase
  * [x] Test coverage
* if `nop allotment` exists != transfer `nopAllotment` to NOP != its balance should increase
  * [x] Test coverage
* if `multisig allotment` exists != transfer `multisigAllotment` to MULTISIG != its balance should increase
  * [x] Test coverage
* Make sure allotments add up to 100% (the percentages)
  * [ ] Test coverage

**Negative behavior:**

* Shouldn’t be callable whenever (`rewardscycle` should be scheduled)
  * [x] Negative test?

**Preconditions:**

* Assumes that the `rewardsCycle` is startable.
* Also assumes that each allotment is > 0. works even if that’s not the case.

**Inputs:**

There aren’t input values here.

**Function call analysis**

* `nopClaim.setRewardsCycleTotal(nopClaimContractAllotment)`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `vault.transferToken()`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here
  * **What happens if it reverts, reenters, or does other unusual control flow?** revert if `tokenBalance` is less than `amount` value, or if `amount` is zero

#### Function: `distributeMultisigAllotment()`

**Intended behavior:**

* Should distribute the `ggp` to the multisigs.

**Branches and code coverage:**

**Intended branches:**

* Should only be called with legitimate `ggp` tokens.
  * [x] Test coverage

**Negative behavior:**

**Lacks negative testing**

* Should not distribute rewards to deactivated `multisigs`.

* [ ] Test coverage

**Preconditions:**

* Assumes there aren’t that many multisigs
* Assumes that if multisigs gets deleted, they won’t be eligible for `rewards`.

**Inputs:**

* `allotment`:
  * **Control** : value is calculated inside `getClaimingContractDistribution(“ClaimMultisig”)`
  * **Checks** : no checks at this function level, however, there maybes ome leftover tokens due to rounding errors; assure that these are sent somewhere after all allotments? (in `startRewardsCycle`)
  * **Impact** : determines the total amount of tokens that will be sent to multisigs.
* `vault`:
  * **Control** : address is taken from `Vault(getContractAddress(“Vault”))`
  * **Checks** : passed from previous function; same as`ggp` parameter.

* **Impact** : n/a
* `ggp`:
  * **Control** : address is taken from `TokenGGP(getContractAddress(“TokenGGP”))`
  * **Checks** : full control; it’s passed from the previous function; ENSURE that it’s never called somewhere else or with a different GGP than here
  * **Impact** : n/a

**Function call analysis**

* `mm.getCount();`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** out of gas inside the for loop if count value is too big
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `mm.getMultisig(i)`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** returns address and status of multisig, if enabled then this address will receive ggp tokens.

* **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `vault.withdrawToken(enabledMultisigs[i], ggp, tokensPerMultisig)`
  * **What is controllable?** since this is an internal call, all input values are taken from storage.
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value here.
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `safeTransfer` call reverts and if `tokenBalances` less than amount value

### 5.16 File: `Staking`

#### Function: `GGP staking components`

**Intended behavior:**

* Limited negative testing
* `getGGPStake` = view current stake
* `increaseGGPStake` = increase `.ggpStaked`
* `decreaseGGPStake` = decrease `.ggpStaked`

**Branches and code coverage:**

**Intended branches:**

* Should retrieve / increase / decrease the `ggpStaked`.
  * [ ] Test coverage

**Negative behavior:**

* Shouldn’t update an unregistered `stakerIndex`.

* [ ] Negative test?

**Preconditions:**

* `increase` assumes that user has `deposited` the `ggp` and that the contract’s balance has/will increase
* `decrease` assumes that the user has `withdrawn` and that the `ggp` balance of the contract will `decrease + ggp` balance of user will `increase`.

**Where are the functions used:**

* `increaseGGPSTake`: Used in `_stakeGGP`
* `decreaseGGPStake`: Used in `slashGGP`, `withdrawGGP`

#### Function: `increaseAVAXStake()`

**Intended behavior:**

Increase the amount of AVAX for stakerAddr.

The function is called only from `MinipoolManager.createMinipool`.

**Branches and code coverage:**

**Intended branches:**

* After the function call the `getAVAXStake` for `stakerAddr` increased by the `amount` value
  * [x] Test coverage

**Negative behavior:**

* The function will revert if `stakerAddr` is not valid staker
  * [ ] Negative test?
* The function will revert if msg.sender is not `MinipoolManager` contract
  * [ ] Negative test?

**Preconditions:**

* `stakerAddr` called `stakeGGP` and was registered as a staker.

**Inputs:**

* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlySpecificRegisteredContract(“MinipoolManager”, msg.sender)`
  * **Impact** : access to the function by untrusted addresses will allow manipulating the number of tokens staked.
* `amount`:
  * **Control** : `msg.value` is passed from the function `MinipoolManager.createMinipool` to ths function. limited control.
  * **Checks** : there are no checks.
  * **Impact** : this value reflects the number of stacked tokens.

manipulating this value will allow an attacker to specify the number of tokens that have not actually been deposited.
* `stakerAddr`:
  * **Control** : `msg.sender` from `MinipoolManager.createMinipool`. not controlled.
  * **Checks** : the `requireValidStaker` function checks the address. If this address isn’t staker, will revert.
  * **Impact** : in case of full access it will allow any user to increase the number of tokens deposited.

**Function call analysis**

* `requireValidStaker()`
  * **What is controllable?** `stakerAddr`
  * **If return value controllable, how is it used and how can it go wrong?** return the `stakerIndex` corresponding to the `stakerAddr`. The Index must be unique, otherwise will be possible to lose funds.
  * **What happens if it reverts, reenters, or does other unusual control flow?** will be reverted if `stakerAddr` is not a valid staker.

* `addUint()` **- What is controllable? amount**
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** it can be reverted in overflow case,

#### Function: `decreaseAVAXStake()`

**Intended behavior:**

Decrease the amount of AVAX for stakerAddr.

The function is called from `MinipoolManager.withdrawMinipoolFunds` and `MinipoolManager._cancelMinipoolAndReturnFunds`.

**Branches and code coverage:**

**Intended branches:**

* After the function call the `getAVAXStake` for `stakerAddr` decreased by the `amount` value
  * [x] Test coverage

**Negative behavior:**

* The function will revert if `stakerAddr` is not valid staker
  * [ ] Negative test?
* The function will revert if the `avaxStaked` for the `stakerAddr` is less than `amount`
  * [ ] Negative test?
* The function will revert if msg.sender is not `MinipoolManager` contract
  * [ ] Negative test?

**Preconditions:**

* `stakerAddr` have called `stakeGGP` and was registered as a staker.

* `stakerAddr` has non zero `avaxStaked` value

**Inputs:**

* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlySpecificRegisteredContract(“MinipoolManager”, msg.sender)`
  * **Impact** : access to the function by untrusted addresses will allow manipulating the number of tokens staked
* `amount`:
  * **Control** : `getUint(keccak256(abi.encodePacked(“minipool.item”, minipoolIndex, “.avaxNodeOpAmt”)))` value from `gogoStorage`, limited control.
  * **Checks** : this value cannot be more than current the `avaxStaked` value
  * **Impact** : this value reflects the number of stacked tokens. manipulating this value will allow an attacker to specify the number of tokens that have not actually been withdrawn.
* `stakerAddr`:
  * **Control** : owner of minipool. not controlled.
    * **Checks** : the `requireValidStaker` function checks the address. If this address isn’t staker, will revert.
  * **Impact** : in case of full access it will allow any user to decrease the number of tokens deposited.

**Function call analysis**

* `subUint()`
  * **What is controllable?** amount
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `avaxStaked` less than `amount`.
* `requireValidStaker()`
  * **What is controllable?** stakerAddr
  * **If return value controllable, how is it used and how can it go wrong?** re- turn the `stakerIndex` corresponding to the `stakerAddr`. The Index must be unique, otherwise will be possible to lose funds.
  * **What happens if it reverts, reenters, or does other unusual control flow?** will be reverted ifstakerAddris not a valid staker.

#### Function: `increaseAVAXAssigned()`

**Intended behavior:**

Increase the amount of AVAX a given staker is assigned by the protocol

The function is called only from `MinipoolManager.createMinipool`.

**Branches and code coverage:**

**Intended branches:**

* After the function call the `getAVAXAssigned` for `stakerAddr` increased by the `amount` value
  * [x] Test coverage

**Negative behavior:**

* The function will revert if `stakerAddr` is not valid staker
  * [ ] Negative test?
* The function will revert if msg.sender is not `MinipoolManager` contract
  * [ ] Negative test?

**Preconditions:**

* `stakerAddr` have called `stakeGGP` and was registered as a staker.

**Inputs:**

* `amount`:
  * **Control** : `avaxAssignmentRequest` is passed from the function `MinipoolManager.createMinipool` to ths function and should be equal the `msg.sender` value. limited control.
  * **Checks** : there are no checks
  * **Impact** : this value reflects the number of assigned tokens. Manipulating this value will allow an attacker to specify the number of tokens that have not actually been assigned.

* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlySpecificRegisteredContract(“MinipoolManager”, msg.sender)`
  * **Impact** : access to the function by untrusted addresses will allow manipulating the number of tokens assigned.
* `stakerAddr`:
  * **Control** : `msg.sender` from `MinipoolManager.createMinipool`. not controlled.
  * **Checks** : the `requireValidStaker` function checks the address. If this address isn’t staker, will revert.
  * **Impact** : in case of full access it will allow any user to increase the number of tokens assign.

**Function call analysis**

* `setUint(...))“.avaxAssignedHighWater”)`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `addUint(...))“.avaxAssigned”)`
  * **What is controllable?** amount
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

#### Function: `decreaseAVAXAssigned()`

**Intended behavior:**

Allows to decrease the amount of AVAX a given staker is assigned by the protocol

The function is called from `MinipoolManager.recordStakingEnd`and `MinipoolManager. recordStakingError` and `MinipoolManager._cancelMinipoolAndReturnFunds`.

**Branches and code coverage:**

**Intended branches:**

* After the function call the `getAVAXAssigned` for `stakerAddr` decreased by the `amount` value
  * [x] Test coverage

**Negative behavior:**

* The function will revert if `stakerAddr` is not valid staker
  * [ ] Negative test?
* The function will revert if the `avaxAssigned` for the `stakerAddr` is less than `amount`
  * [ ] Negative test?
* The function will revert if msg.sender is not `MinipoolManager` contract
  * [ ] Negative test?

**Preconditions:**

* `stakerAddr` have called `stakeGGP` and was registered as a staker.
* `stakerAddr` has non zero `avaxAssigned` value

**Inputs:**

* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlySpecificRegisteredContract(“MinipoolManager”, msg.sender)`
  * **Impact** : access to the function by untrusted addresses will allow manipulating the number of tokens assign.

* `amount`:
  * **Control** : `getUint(keccak256(abi.encodePacked(“minipool.item”, minipoolIndex, “.avaxLiquidStakerAmt”)))` value from `gogoStorage`, limited control.
  * **Checks** : this value cannot be more than current the `avaxAssigned` value
  * **Impact** : this value reflects the number of staked tokens. Manipulating this value will allow an attacker to specify the number of tokens that have not actually been deposited.
* `stakerAddr`:
  * **Control** : owner of minipool. not controlled.
  * **Checks** : the `requireValidStaker` function checks the address. If this address isn’t staker, will revert.
  * **Impact** : incase of full access i will allow any user to decreased the number of tokens assigned.

**Function call analysis**

* `subUint()`
  * **What is controllable?** amount
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `avaxAssigned` less than `amount`.
* `requireValidStaker()`
  * **What is controllable?** stakerAddr
  * **If return value controllable, how is it used and how can it go wrong?** return the `stakerIndex` corresponding to the `stakerAddr`. The Index must be unique, otherwise will be possible to lost funds.
  * **What happens if it reverts, reenters, or does other unusual control flow?** will be reverted if `stakerAddr` is not a valid staker.

#### Function: `setRewardsStartTime`

**Intended behavior:**

* Rewards start time refers to the `timestamp` when the staker registered for `GGPRewards`

**Branches and code coverage:**

**Intended branches:**

* Ensure that `time` is in the future?
  * [ ] Test coverage
* Should allow `setting` the `rewardStartTime`
  * [ ] Test coverage

**Negative behavior:**

* Also, assuming that `onlyRegisteredNetworkContract` calls it. Also I think they whitelist their own `Staking` contract (basically address(this))
  * [ ] Negative test?

**Preconditions:**

* Assumes that it’s called from `onlySpecificRegisteredContract(“ClaimNodeOp”, msg.sender)`

**Inputs:**

* `time`:
  * **Control** : full control
  * **Checks** : there’s no check on whether the `time` is in the future or not
  * **Impact** : the value is used during reward distribution, if zero, the staker will not receive reward

**Function call analysis**

There aren’t external calls here.

**Where are the functions used:**

* `setRewardsStartTime`: used in `MinipoolManager` and `ClaimNodeOp`

#### Function: `GGP Rewards()`

**Intended behavior:**

* Should `get, increase, decrease` the `GGPRewards` assigned to a staker.

**Branches and code coverage:**

**Intended branches:**

* These should update whenever the staker claims / is issued rewards.
  * [ ] Test coverage
* Should retrieve/increase/decrease the amount of `GGPrewards` a staker has **earned** and **not claimed yet.**
  * [ ] Test coverage

**Negative behavior:**

* Should revert if anyone other than the `ClaimNodeOp` contract calls them.
  * [ ] Negative test?

**Preconditions:**

* Assumes that the calling contract holds the correct accounting for how the `ggp` rewards are issued and maintained.

**Function call analysis**

There aren’t external calls here.

**Where are the functions used:**

* `increaseGGPRewards`: used in `ClaimNodeOP`
* `decreaseGGPrewards`: used in `ClaimNodeOP`

#### Function: `increaseMinipoolCount()`

**Intended behavior:**

The function is called from `MinipoolManager.createMinipool`

Increase the number of minipools the given staker has

**Branches and code coverage:**

**Intended branches:**

* After the function call the `.minipoolCount` increased by 1
  * [x] Test coverage

**Negative behavior:**

* The function will revert if the `.minipoolCount` is zero
  * [ ] Negative test?
* The function will revert if msg.sender is not `MinipoolManager` contract
  * [ ] Negative test?

**Preconditions:**

* `stakerAddr` have called `stakeGGP` and was registered as a staker.

**Inputs:**

* `stakerAddr`:
  * **Control** : owner of minipool. not controlled.
  * **Checks** : the `requireValidStaker` function checks the address. If this address isn’t staker, will revert.

* **Impact** : in case of full access it will allow any user to increase the amount of minipools
* `msg.sender`:
  * **Control** : -
    * **Checks** : `onlySpecificRegisteredContract(“MinipoolManager”, msg.sender)`
  * **Impact** : access to the function by untrusted addresses will allow manipulating the number of the given staker minipools. The `setRewardsStartTime` value depends of the amount of minipools, if minipoolCount = 0 `RewardsStartTime` will be reset. If `RewardsStartTime == 0` then `RewardsStartTime` will be set during minipool creation.

And if `RewardsStartTime == 0` then owner of minipool doesn’t get the GGP rewards

**Function call analysis**

* `addUint()`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `requireValidStaker()`
  * **What is controllable?** stakerAddr
  * **If return value controllable, how is it used and how can it go wrong?** return the `stakerIndex` corresponding to the `stakerAddr`. The Index must be unique, otherwise will be possible to lost funds.
  * **What happens if it reverts, reenters, or does other unusual control flow?** will be reverted if `stakerAddr` is not a valid staker.

#### Function: `decreaseMinipoolCount()`

**Intended behavior:**

Decrease the number of minipools the given staker has

The function is called from `MinipoolManager.recordStakingEnd` and `MinipoolManager._cancelMinipoolAndReturnFunds`

**Branches and code coverage:**

**Intended branches:**

* After the function call the `.minipoolCount` decreased by 1
  * [x] Test coverage

**Negative behavior:**

* The function will revert if `stakerAddr` is not valid staker
  * [ ] Negative test?
* The function will revert if the `.minipoolCount` is zero
  * [ ] Negative test?
* The function will revert if msg.sender is not `MinipoolManager` contract
  * [ ] Negative test?

**Preconditions:**

* `stakerAddr` have called `stakeGGP` and was registered as a staker.
* The `.minipoolCount` is not zero

**Inputs:**

* `stakerAddr`:
  * **Control** : owner of minipool. not controlled.
  * **Checks** : the `requireValidStaker` function checks the address. If this address isn’t staker, will revert.

* **Impact** : in case of full access it will allow any user to decrease the amount of minipools
* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlySpecificRegisteredContract(“MinipoolManager”, msg.sender)`
  * **Impact** : access to the function by untrusted addresses will allow manipulating the number of the given staker minipools. The `setRewardsStartTime` value depends of the amount of minipools, if minipoolCount = 0 `RewardsStartTime` will be reset. if `RewardsStartTime == 0` then `RewardsStartTime` will be set during minipool creation. And if `RewardsStartTime == 0` then owner of minipoll doesn’t get the GGP rewards

**Function call analysis**

* `subUint()`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `.minipoolCount` is 0.

* `requireValidStaker()`
  * **What is controllable?** stakerAddr
  * **If return value controllable, how is it used and how can it go wrong?** return the `stakerIndex` corresponding to the `stakerAddr`. The Index must be unique, otherwise will be possible to lost funds.
  * **What happens if it reverts, reenters, or does other unusual control flow?** will be reverted if `stakerAddr` is not a valid staker.

#### Function: `setRewardsStartTime()`

**Intended behavior:**

Set the timestamp when the staker registered for GGP rewards.

The `setRewardsStartTime` value depends of the amount of minipools, if minipoolCount = 0 `RewardsStartTime` will be reset inside the `calculateAndDistributeRewards()` function, which called from `processGGPRewards` if `isEligible` true (is not true if `RewardsStartTime == 0`). if `RewardsStartTime == 0` then `RewardsStartTime` will be set during minipool creation.

**Branches and code coverage:**

**Intended branches:**

* After the function call the `.rewardsStartTime` is equal to `time`
  * [x] Test coverage

**Negative behavior:**

* The function will revert if `stakerAddr` is not valid staker
  * [ ] Negative test?
* The function will revert if `msg.sender` is not `RegisteredNetworkContract`
  * [ ] Negative test?

**Preconditions:**

* `stakerAddr` have called `stakeGGP` and was registered as a staker.

**Inputs:**

* `time`:
  * **Control** : partly controlled: during minipool creation `block.timestamp` is passed
  * **Checks** : there aren’t any checks
  * **Impact** : if set to 0 than owner of minipool cannot get the GGP rewards and if non zero will be able to get `(isEligible(): if (block.timestamp - rewardsStartTime) != dao.getRewardsEligibilityMinSeconds())`
* `stakerAddr`:
  * **Control** : owner of minipool. not controlled.
  * **Checks** : the `requireValidStaker` function checks the address. If this address isn’t staker, will revert.

* **Impact** : in case of full access it will allow any user to set the `RewardsStartTime` and bypass the `isEligible` check.
* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlyRegisteredNetworkContract`
  * **Impact** : access to the function by untrusted addresses will allow manipulating the `RewardsStartTime` value. If `RewardsStartTime != 0` then owner of minipool will be able to get the GGP rewards

**Function call analysis**

* `setUint()`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems
* `requireValidStaker()`
  * **What is controllable?** stakerAddr
  * **If return value controllable, how is it used and how can it go wrong?** re- turn the `stakerIndex` corresponding to the `stakerAddr`. The Index must be unique, otherwise will be possible to lost funds.

* **What happens if it reverts, reenters, or does other unusual control flow?** will be reverted if `stakerAddr` is not a valid staker.

#### Function: increaseGGPRewards()\`

**Intended behavior:**

Increase the amount of GGP rewards the staker has earned and not claimed

The function is called from `ClaimNodeOp.calculateAndDistributeRewards`

**Branches and code coverage:**

**Intended branches:**

* After the call the `.ggpRewards` amount will be increased by `amount`
  * [x] Test coverage

**Negative behavior:**

* The function will revert if `stakerAddr` is not valid staker
  * [ ] Negative test?
* The function will revert if `msg.sender` is not `ClaimNodeOp` contract
  * [ ] Negative test?

**Preconditions:**

* `stakerAddr` have called `stakeGGP` and was registered as a staker.

**Inputs:**

* `amount`:
  * **Control** :
  * **Checks** : there aren’t checks
  * **Impact** : The value determines how much the user will be able to receive rewards.

In case of full access to the function, users will be able to steal all funds from the vault.
* `stakerAddr`:
  * **Control** : owner of minipool. not controlled.
  * **Checks** : the `requireValidStaker` function checks the address. If this address isn’t staker, will revert.
  * **Impact** : in case of full access it will allow any user to increase the.ggpRewards
* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlySpecificRegisteredContract(“ClaimNodeOp”, msg.sender)`
  * **Impact** : access to the function by untrusted addresses will allow manipulating the `.ggpRewards` value.

**Function call analysis**

* `requireValidStaker()`
  * **What is controllable?** stakerAddr
  * **If return value controllable, how is it used and how can it go wrong?** re- turn the `stakerIndex` corresponding to the `stakerAddr`. The Index must be unique, otherwise will be possible to lost funds.

* **What happens if it reverts, reenters, or does other unusual control flow?** will be reverted if `stakerAddr` is not a valid staker.
* `addUint()`
  * **What is controllable?** amount
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

#### Function: `decreaseGGPRewards()`

**Intended behavior:**

Decrease the amount of GGP rewards the staker has earned and not claimed.

The function is called from `ClaimNodeOp.claimAndRestake`

**Branches and code coverage:**

**Intended branches:**

* After the call the `.ggpRewards` is decreased by the `amount` value.

* [x] Test coverage

**Negative behavior:**

* The function will revert if `stakerAddr` is not valid staker
  * [ ] Negative test?
* The function will revert if the `.ggpRewards` is less than `amount`
  * [ ] Negative test?
* The function will revert if msg.sender is not `ClaimNodeOp` contract
  * [ ] Negative test?

**Preconditions:**

* `stakerAddr` have called `stakeGGP` and was registered as a staker.
* The `.ggpRewards` is set by the `ClaimNodeOp.calculateAndDistributeRewards` function call

**Inputs:**

* `amount`:
  * **Control** : not controlled
  * **Checks** : there aren’t checks
  * **Impact** : in case of an untrusted caller, the `.ggpRewards` can be reset and owner of pool will not be able to get reward
* `stakerAddr`:
  * **Control** : owner of minipool. not controlled.
    * **Checks** : the `requireValidStaker` function checks the address. If this address isn’t staker, will revert.

* **Impact** : in case of full access it will allow any user to decrease the `.ggpRewards`
* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlySpecificRegisteredContract(“ClaimNodeOp”, msg.sender)`
  * **Impact** : access to the function by untrusted addresses will allow manipulating the `.ggpRewards` value.

**Function call analysis**

* `requireValidStaker()`
  * **What is controllable?** stakerAddr
  * **If return value controllable, how is it used and how can it go wrong?** return the `stakerIndex` corresponding to the `stakerAddr`. The Index must be unique, otherwise will be possible to lost funds.
  * **What happens if it reverts, reenters, or does other unusual control flow?** will be reverted if `stakerAddr` is not a valid staker.

* `subUint()`
  * **What is controllable?** amount
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `.ggpRewards` is less than `amount`.

#### Function: `setLastRewardsCycleCompleted()`

**Intended behavior:**

Set the most recent reward cycle number that the staker has been paid out for.

The function is called from `ClaimNodeOp.calculateAndDistributeRewards`

**Branches and code coverage:**

**Intended branches:**

* After the call the `.lastRewardsCycleCompleted` is equal to the `cycleNumber` value
  * [ ] Test coverage

**Negative behavior:**

* The function will revert if `stakerAddr` is not valid staker
  * [ ] Negative test?
* The function will revert if msg.sender is not `ClaimNodeOp` contract
  * [ ] Negative test?

**Preconditions:**

* `stakerAddr` have called `stakeGGP` and was registered as a staker.

**Inputs:**

* `cycleNumber`:
  * **Control** : the value from the `rewardsPool.getRewardsCycleCount()` function call
  * **Checks** : there aren’t checks
  * **Impact** : prevents rereceiving the reward in the same cycle.
* `stakerAddr`:
  * **Control** : owner of minipool. not controlled.
  * **Checks** : the `requireValidStaker` function checks the address. If this address isn’t staker, will revert.
  * **Impact** : in case of full access it will allow any user to decrease the `.ggpRewards`
* `msg.sender`:
  * **Control** : -
  * **Checks** : `onlySpecificRegisteredContract(“ClaimNodeOp”, msg.sender)`
  * **Impact** : access to the function by untrusted addresses will allow manipulating the `.lastRewardsCycleCompleted` value.

**Function call analysis**

* `requireValidStaker()`
  * **What is controllable?** stakerAddr
  * **If return value controllable, how is it used and how can it go wrong?** re- turn the `stakerIndex` corresponding to the `stakerAddr`.

The Index must be unique, otherwise will be possible to lost funds.
  * **What happens if it reverts, reenters, or does other unusual control flow?** will be reverted if `stakerAddr` is not a valid staker.
* `setUint()`
  * **What is controllable?** `cycleNumber`
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

#### Function: `getMinimumGGPStake()`

**Intended behavior:**

* Retrieve staker’s minimum `GGP` stake, based on current `GGP` price.

**Branches and code coverage:**

**Intended branches:**

* Ensure that `stakerAddr` is valid; currently not checked
  * [ ] Test coverage

**Preconditions:**

* Assumes that the `stakerAddr` has some `avaxAssigned` to them.

**Function call analysis**

* `(uint256 ggpPriceInAvax, ) = oracle.getGGPPriceInAVAX();`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** Part of the return value is ignored (that refers to the block.timestamp when the price has been updated) Maybe it’s a good idea to also return that? The price could be really outdated; Add something like a max amount of blocks that go without update?
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `price` is zero

#### Function: `getCollateralizationRatio()`

**Intended behavior:**

* Return collateralization ratio based on current `GGP` price.

**Branches and code coverage:**

**Intended branches:**

* Ensure that `stakerAddr` is valid; currently not checked
  * [ ] Test coverage

**Preconditions:**

* Assumes that the `stakerAddr` has some `avaxAssigned` to them.

**Function call analysis**

* `(uint256 ggpPriceInAvax, ) = oracle.getGGPPriceInAVAX();`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** Part of the return value is ignored (that refers to the block.timestamp when the price has been updated) Maybe it’s a good idea to also return that? The price could be really outdated; Add something like a max amount of blocks that go without update?
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `price` is zero

**Where is the function used:**

* `MinipoolManager`:
* `Staking`:

#### Function: `getEffectiveRewardsRatio()`

**Intended behavior:**

* return effective collateralization ratio used to pay rewards based on `GGP` price and `AVAX` high water.

**Branches and code coverage:**

**Intended branches:**

* Ensure that `stakerAddr` is valid; currently not checked
  * [ ] Test coverage

**Preconditions:**

* Assumes that the `stakerAddr` has some `GGPstaked` already.

**Function call analysis**

* `(uint256 ggpPriceInAvax, ) = oracle.getGGPPriceInAVAX();`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** Part of the return value is ignored (that refers to the block.timestamp when the price has been updated) Maybe it’s a good idea to also return that? The price could be really outdated; Add something like a max amount of blocks that go without update?
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `price` is zero
* `dao.getMaxCollateralizationRatio();`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** re- turn the max collateralization ratio of GGP to Assigned AVAX eligible for rewards.

This value is used for `EffectiveGGPStaked` value calculations for reward distribution process
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

#### Function: `getEffectiveGGPStaked()`

**Intended behavior:**

* Get amount of `ggp` that will count towards the `rewards` cycle.

**Branches and code coverage:**

**Intended branches:**

* Ensure that `stakerAddr` is valid; currently not checked
  * [ ] Test coverage

**Preconditions:**

* the `price` value is set inside Oracle contract

**Function call analysis**

* `(uint256 ggpPriceInAvax, ) = oracle.getGGPPriceInAVAX();`
  * **What is controllable?** -
  * **If return value controllable, how is it used and how can it go wrong?** Part of the return value is ignored (that refers to the block.timestamp when the price has been updated) Maybe it’s a good idea to also return that? The price could be really outdated; Add something like a max amount of blocks that go without update?
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if `price` is zero

**Where is the function used:**

* `ClaimNodeOp`:

#### Function: `stakeGGP()` and `_stakeGGP`

**Intended behavior:**

* Should allow any user to stake `GGP` into the contract.

**Branches and code coverage:**

**Intended branches:**

* Should revert if `msg.sender` transferred less than `amount` tokens.
  * [x] Test coverage
* The ggp balance of the `msg.sender` should deplete by amount, whilst the `contract` should have enough to `deposit` into the `vault(like a middleman)`
  * [x] Test coverage
* The `GGPStake` of the user should be increased by the `staked` amount.
  * [x] Test coverage

**Negative behavior:**

* Limited negative testing
* Shouldn’t allow transferring arbitrary tokens
  * [x] Negative test?

**Preconditions:**

* Assumes `msg.sender` is registered as a staker in the contract; however, if that’s not the case, it creates an index for a new staker:
* Assumes that `msg.sender` has previously approved the amount that is to be transferred by `stakeGGP`.

**Inputs:**

* `amount`:
  * **Control** : full control
    * **Checks** : there are no 0 checks, however, they do `safeTransferFrom` user with the `amount`
  * **Impact** : n/a

**Function call analysis**

* `ggp.safeTransferFrom()`
  * **What is controllable?** amount
  * **If return value controllable, how is it used and how can it go wrong?** there ins’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if msg.sender doesn’t have enough ggp tokens.

ranches and code coverage:**

**Intended branches:**

* after the call the `.ggpStaked` value of `stakerAddr` will be increased by `amount` value
  * [x] Test coverage

**Negative behavior:**

Limited negative testing

* if msg.sender doesn’t have enough ggp tokens, transaction will be reverted
  * [ ] Negative test?
* if msg.sender is not trusted ClaimNodeOp contract, transaction will be reverted
  * [ ] Negative test?

**Preconditions:**

* Assumes `msg.sender` is `ClaimNodeOp`
* msg.sender must have at least the amount value of ggp tokens

**Inputs:**

* `amount`:
  * **Control** : limited control
  * **Checks** : safeTransferFrom will revert if msg.sender balance less than `amount`
  * **Impact** : -
* `stakerAddr`:
  * **Control** : full control
  * **Checks** : there aren’t any checks
  * **Impact** : -
* `msg.sender`:
  * **Control** : -
    * **Checks** : `onlySpecificRegisteredContract(“ClaimNodeOp”, msg.sender)`
  * **Impact** : the function allows caller to increase `.ggpStaked` value for any user.

but caller should send this value of ggp tokens to contract

**Function call analysis**

* `ggp.safeTransferFrom()`
  * **What is controllable?** amount
  * **If return value controllable, how is it used and how can it go wrong?** there ins’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** will revert if msg.sender doesn’t have enough ggp tokens.
* `_stakeGGP()`
  * **What is controllable?** amount
  * **If return value controllable, how is it used and how can it go wrong?** there isn’t return value
  * **What happens if it reverts, reenters, or does other unusual control flow?** no problems

#### Function: `withdrawGGP()`

**Intended behavior:**

* Allows withdrawing `GGP` tokens.

**Branches and code coverage:**

**Intended branches:**

* Should ensure that the `.ggpStaked` decreases.

* [ ] Test coverage

**Negative behavior:**

* Should never lock-up ggp; this could happen i a scenario where the `msg.sender` is never over 150% collateralization
  * [ ] Negative test?

**Preconditions:**

* Assumes that the user is over `150%` in collateralization ratio.
* Assure that `maxCollateralizationRatio` is synced up! Maybe check the last block and compare it with the last block from `getCollateralizationRatio` as well?! a de-sync could lead to lower threshold of withdrawals. Any huge fluctuations would greatly affect this.

**Inputs:**

* `amount`:
  * **Control** : full controll
    * **Checks** : checks that `amount > getGGPStake` and check that `getCollateralizationRatio(msg.sender)` at least 150 after withdraw
  * **Impact** : could lead to loss of funds if not depleted properly.

#### Function: `slashGGP()`

**Intended behavior:**

* Should be used by the `MinipoolManage` in case that a `minipool` has ended; this happen

**Branches and code coverage:**

**Intended branches:**

* Decrease the `ggpStake` of the `staker`(assuming `staker` has some left)
  * [x] Test coverage
* `StakerAddr` must be registered.
  * [ ] Test coverage

**Negative behavior:**

* Only allow `minipoolmanager` to call this.
  * [ ] Negative test?

**Preconditions:**

* Assumes that `decreaseGGPSTake` can be called on the `stakerAddr` (this implies that `stakerAddr` has been registered beforehand)

**Inputs:**

* `ggpAmt`:
  * **Control** : full control
  * **Checks** : assumes that `decreaseGGPStake` properly decreases the amount that the `stakerAddr` has
  * **Impact** : n/a

### 6 Audit Results

At the time of our audit, the code was not deployed to mainnet Avalanche.

During our assessment on the scoped GoGoPool contracts, we discovered seven findings.

Of the seven findings, four were of high severity, one was of medium severity, one was of low severity and the remaining finding was informational. Multisig Labs acknowledged all findings and implemented fixes.

#### 6.1 Disclaimers

This assessment does not provide any warranties about finding all possible issues within its scope; in other words, the evaluation results do not guarantee the absence of any subsequent issues. Zellic, of course, also cannot make guarantees about any additional code added to the assessed project after the audit version of our assessment. Furthermore, because a single assessment can never be considered comprehensive, we always recommend multiple independent assessments paired with a bug bounty program.

For each finding, Zellic provides a recommended solution. All code in these recommendations are intended to convey how an issue may be resolved (i.e., the idea), but they may not be tested or functional code.

Finally, the contents of this assessment report are for informational purposes only; do not construe any information in this report as legal, tax, investment, or financial advice. Nothing contained in this report constitutes a solicitation or endorsement of a project by Zellic.

---
description: Our goals and an overview of the protocol.
---

# 🧠 Litepaper

## GoGoPool: A Permissionless Staking Protocol for Subnets

## **Abstract**

GoGoPool allows Avalanche node operators to launch a validator node with a minimum of 1100 AVAX, while providing instant liquidity to stakers. As a permissionless protocol, any individual, business, or Subnet can use the protocol to stake or launch new validator nodes. Our mission is to make is as easy as possible to launch a Subnet. Our vision is to enable the Wordpress moment for web3 via open source tooling, strong community, and an open staking protocol.

## **Introduction**

Avalanche aims to be a blazingly fast, eco friendly, and low-fee platform that any developer may build on. They achieve this with a horizontal scaling technique called Subnets.

At a high level, Subnets are a group of validators nodes that come to consensus on something (typically, a blockchain).

This gives an appchain developer Avalanche’s best features for free (consensus algorithm, validator set, liquidity) and allows them to focus on creating a great experience for users without worrying about web3 infrastructure.

The problem is that Subnets are expensive to start, grow and manage. Every validator of a Subnet must also validate the Avalanche Primary Network (which requires paying 2000 AVAX as a minimum staking amount, and managing your own hardware).

For builders that wish to experiment with building new Subnets on top of Avalanche, the cost of paying 2000 AVAX per node and managing all the hardware is prohibitively high. For established projects wanting to run a 5 node blockchain, they must pay 10,000 AVAX upfront before launching.

GoGoPool aims to trivialize the cost of starting, growing and managing a Subnet with an open staking protocol that has built in Subnet compatibility - enabling rapid experimentation with new business models and ideas in the web3 ecosystem.

## **Goals**

Our mission is to be the easiest way to launch a Subnet by lowering the cost of staking. This has 3 components:

1. liquid staking
2. decentralized and permissionless hardware operators
3.

urrent state of Avalanche staking + validation
* Ensure that staking infrastructure and components are as decentralized, trustless and scalable as possible
* Minimize deposit risk and maximize rewards by socializing staking losses and rewards across the network
* Decentralize protocol development, governance, and security using GGP tokenomics to create a healthy self sustaining community
* Maximize network rewards by allowing hardware operators and liquid stakers to easily validate Subnets, earning Subnet rewards
* Create a scalable network that can support Avalanche’s projected Subnet growth, both now and in the long term future
* Trivialize the cost of starting, growing, and managing a Subnet’s infrastructure
* Inspire future projects by being a model example of a web3 protocol, helping proliferate the web3 ethos in the developer community

## **Protocol Overview**

The GoGoPool protocol emphasizes trustlessness and peerlessness wherever possible, to maximize its decentralization, security, and scalability.

There are 3 main components to the protocol: the users, community (tokenomics/DAO), and custom node software.

### **Users Primer**

There are two main users of the GoGoPool protocol, each with their own use cases.

#### Node Operators

Contribute their own hardware to the pool, and stake 1000 AVAX + minimum of 100 AVAX (in GGP tokens). Operators maintain their server infrastructure, and are matched with the other 1000 AVAX from a deposit pool of stakers. Operators charge a small operating fee (not unlike the existing delegator fee) for the use of the hardware, and are also incentivized with GGP tokens to maintain good behavior. This allows a node operator to begin staking with less AVAX than is normally required, earn rewards on their staked AVAX, and earn rewards via the operating fee and GGP network rewards. Lastly, minipools earn compound interest and automatically restake at the end of each validation period. This maximizes the amount of rewards minipool operators earn.

This triple incentive structure allows them to earn much higher rewards than staking solo, while providing hardware to generate yield for liquid stakers, and derisks the cost of Subnet development.

#### Liquid Stakers

Liquid Stakers are either individuals or users from an API integrated business (e.g. a wallet). Stakers deposit AVAX into the deposit pool, and receive ggAVAX which accrues value over time based on the performance of the protocol. The deposited AVAX is automatically matched to node operators for staking.

Stakers are given access to instant liquidity, being able to use ggAVAX in any place AVAX could be used. But unlike AVAX, ggAVAX steadily increases in value over time based on the performance of the pool - while not needing to trust any individual node operator (in contrast to the current delegator system, where trust is an explicit requirement).

Anyone can safely become a staker for as little as .01 AVAX - including individuals or businesses.

In this way, GoGoPool opens up the entire AVAX economy by providing much needed liquidity to stakers and DeFi apps in a trustless manner.

GoGoPool uses a mix of smart contracts and DAOs to achieve this level of decentralization, despite technical challenges that prevent a pure trustless solution.

### **Tokenomics Primer**

There is much room for innovation in community-driven organizations, and GoGoPool plans to be on the forefront.

We have two tokens: ggAVAX (liquid staking token described above), and GGP (protocol token used for DAO governance, rewards, insurance, and incentivizing long term behavior).

#### **ggAVAX**

When a user deposits AVAX into the deposit pool, they receive a synthetic derivative token called ggAVAX.

ggAVAX represents a staker’s deposit plus the rewards it gains over time. This token is considered liquid and can be used like AVAX - users can hold it to accrue staking rewards, sell it, or use it in DeFi to earn additional yield.

If there is floating AVAX in the deposit pool, users will be able to exchange ggAVAX back for AVAX (which burns the ggAVAX, and draws AVAX from the deposit pool). Alternatively, they will have the option to list it on any exchange listing the token and exchange it for any token they would like.

#### **GGP**

GGP is an ERC20 token, and serves as the protocol token for GoGoPool.

The GGP tokens allows Node Operators to launch minipools (full Avalanche Validator nodes matched with user funds) for 1000 AVAX.

Node Operators have to stake a minimum amount of GGP tokens to secure their assigned staking funds as insurance of good behavior. At genesis the minimum will be 10% of their AVAX staked amount, but the operator can choose to stake as much as 150%. The higher their GGP stake, the higher their monthly GGP rewards will be. Node Operators can use these GGP rewards to launch new validator nodes, increasing their overall yield.

In the future, Node Operators may restake their monthly GGP rewards to request AVAX delegation from liquid stakers onto existing minipools.

If a node operator has excessively low uptime and causes a loss of rewards for the protocol, stakers are compensated from the GGP insurance put up by the Node Operator. This socializes the risk of being matched with a bad operator, and minimizes any potential losses. Slashed GGP can be sold to token holders at a discounted rate, with AVAX proceeds awarded to Liquid Stakers.

GGP token holders will have the ability to participate in the GoGoPool Protocol DAO, which allows members to propose and vote on a range of governance issues including inflation schedule of GGP, removing/replacing bad actors, smart contract upgrades, payment of community developers for future work, and rewarding outstanding members of the community (as well as other minor changes to the settings of the protocol).

### **DAO Primer**

There are two DAOs at play: RialtoDAO and ProtocolDAO.

These DAOs work together to keep the protocol running in a decentralized and community owned way.

Because of the open community orientation of this protocol, no platform fees will be charged. Instead, all rewards are maintained by the ProtocolDAO treasury, and losses due to bad behavior socialized amongst members. This way all members are guaranteed the maximum possible rewards.

#### **OracleDAO**&#x20;

The OracleDAO is initially made up of the core developer team, and will be decentralized over time. This DAO operates Rialto (MPC software) and maintains a few important functions for the GoGoPool protocol:

1. Facilitate cross chain staking (moving collected funds from C Chain to the P Chain).
2. Facilitate distribution of staking rewards (moving rewards from P Chain to C Chain).
3. If no node operators are present and the amount of unstaked AVAX in the deposit pool is over a decided upon threshold, OracleDAO members may form pools with their own hardware.
4.

Serve as an initial price oracle to smart contracts.
5. Further the GGP community and protocol in the wider Avalanche community.

To join the OracleDAO, members must stake a sizable sum of GGP tokens.

If the majority of members vote that a member of the DAO is not fulfilling their duties appropriately, their stake is burned and the member is kicked/replaced. Stakes must be refreshed at a decided upon time interval.

To incentivize good behavior, 10% of reward GGP is paid out to the DAO.

#### ProtocolDAO

Our goal is to have every component of the protocol be configurable by the ProtocolDAO. Anyone with a GGP token has the ability to partake in the ProtocolDAO, proposing and voting on new items. Members of this DAO will be responsible for pushing the limits on what DAO members can and will do, and set the standard for other web3 projects.

The ProtocolDAO will maintain a treasury to pay for security audits and reward community/developer contributions.

Some of the governance factors the ProtocolDAO members have influence over are listed below:

* Depositing funds into the treasury wallet.
* The GGP token inflation schedule and rate. At genesis, there will be 0% inflation for 4 years, at which point the DAO can contemplate adding a 2-5% inflation rate to be used as rewards.
* GGP reward distribution between Node Operators and DAOs.
* Configure min/max staking amounts, enabling/disabling registration, etc.
* Decide on liquidity mining and boostrap reward programs
* Proposing and choosing a donation or charitable cause to donate a percentage of AVAX/GGP rewards to. At genesis, the percentage will be 1% annually.
* Blacklisting / whitelisting Subnets.

## **Enabling Subnets & Subnet Compatibility**

Validators of a Subnet must also be a validator for the Avalanche Primary Network. Validators can participate in any arbitrary number of Subnets.

The minimum staking amount for the Avalanche Primary Network is 2,000 AVAX for a single validator node and 10,000 AVAX for a 5 node subnet. It is cost prohibitive for a Subnet to start building on top of Avalanche, as they need to bear the cost of running validators for their own network as well as sourcing the AVAX required validate the Primary Network.

GoGoPool gives Subnet operators a way to directly contact and whitelist minipool operators to validate the Subnet. This lets hardware operators earn more yield, while getting the Subnet access to validators in a much cheaper and frictionless way.

For Subnets that want to start as closed system, GoGoPool provides a more effective way of using their AVAX by matching their funds with liquid stakers. Subnets launch non-custodial minipools, able to use the hardware for their own purposes. If this permissioned Subnet wants to explore decentralization, they have a direct path to doing so by utilizing other minipools in the protocol.

Subnets that have specific hardware or validator requirements will be able to select node operators based on different attributes that fit the requirements of the Subnet. For example, a Subnet will be able to incentivize node operators that are US citizens (if that were a requirement for the Subnet).

Subnets that join the GoGoPool DAO to have a direct say in the future of the protocol roadmap, gain access to early Subnet tooling and features, and interface with liquid stakers and node operators.

## **Acknowledgements**

* The Rocketpool team, for pioneering permissionless staking protocols before anyone was thinking about it.
* Ava Labs, for creating a flexible, green and fast L0 and L1 solution with a focus on Developer primitives.
* The GoGoPool Dev team, for seeing and building the dream in the very early days.
* The Ethereum Foundation and Bitcoin for laying the first pieces of a foundation for web3.

# ❓ FAQ

## What is Avalanche?

Avalanche is a new blockchain created by Ava Labs, and solves the [Trilemma](https://medium.com/certik/the-blockchain-trilemma-decentralized-scalable-and-secure-e9d8c41a87b3). It is:

1. Secure
2. Decentralized
3. Fast

If Bitcoin and Ethereum are L1s, Avalanche is an L0 and an L1. Any L1 can be created on top of Avalanche, inheriting the platform’s properties and allowing builders to focus on customizing the L1 to their own purposes.

## What is a subnet?

[Tweet storm on Subnets](https://twitter.com/das\_connor/status/1456592161420587017)\
[Avalanche's Official Subnet Docs](https://docs.avax.network/subnets)

Subnets are Avalanche’s secret weapon. They are private blockchains, with batteries included. \
\
Through subnets, any user can effortlessly create a new L1 blockchain that is equipped to function seamlessly as an L2. Subnets are revolutionary, consolidating all our knowledge of blockchain scaling into a single, interoperable package.

Picture a network of interconnected blockchains, each small enough to process transactions quickly, yet fully compatible with one another.&#x20;

Avalanche’s C-Chain is an example of one subnet. It serves as a blockchain that is optimized for running smart contract code.

## What is staking for node operators?

In [Proof of Stake](https://www.avax.network/proof-of-stake-pos) blockchains, validator nodes validate the blockchain and earn staking rewards as compensation.

For Avalanche, a node operator must set up their hardware to validate the chain and put up a minimum of 2000 AVAX as their stake. The AVAX is locked up for the duration of the staking window, and accrues rewards. After the staking window (max of 1 year), the AVAX is returned as well as any staking rewards they earned.

## What is liquid staking?

Liquid staking is an alternative to locking up a user’s stake!

It allows anyone to effectively stake any amount of AVAX, and receive instant liquidity via a wrapped AVAX token.

This wrapped token can be spent like normal AVAX, and can be exchanged for normal AVAX at any time.

## How is GoGoPool different from Lido?

There are a few differences.

1. Lido is a (very successful) liquid staking protocol.
2. Lido centralizes their hardware providers.
3. A Lido-like staking protocol only provides liquidity to stakers, and does not help bring about the promised future of subnets.

In contrast, GoGoPool:

1. Is a permissionless staking protocol.
2. Decentralizes hardware operators via community rewards.
3. Allows subnets to join the pool, incentivizing hardware operators to validate the subnet.

Avalanche has a big liquid staking problem (60% of AVAX is currently locked up in staking windows), but an even bigger subnet problem (only 17 subnets in production).

While Lido addresses the first problem, we have set out to tackle the more challenging task of developing a protocol that provides a solution for both issues at hand.

## How did you come up with the idea for GoGoPool?

Steven wanted to create and launch subnets on Avalanche which allows creators to incentivize their fans to grow the creator’s business using community DAOs.

But launching and growing a subnet is super expensive — each validator has to also validate the Avalanche chain, and he didn’t have a way to contact existing nodes to pick up my chain for validation. So he went to run his own validator node, and saw that each node must have a minimum stake of 2000 AVAX - making growing the subnet unfeasible, and locking me out of experimenting with the idea!

After doing research and seeing that no staking protocol was even close to existing, he decided to do something about it.

GoGoPool lets the next entrepreneur focus on their vision instead of having to worry about the node infrastructure of their blockchain.

# 🫂 Our Mission

<figure><img src="../.gitbook/assets/intro_gogopool_subnet.jpeg" alt=""><figcaption></figcaption></figure>

### Subnets have 3 barriers to massive adoption: financial, technical, and community.

The GoGoPool protocol immediately solves the **financial** barrier for subnets with a liquid staking protocol. Our team is actively working on tackling the others.

Our mission is to simplify developing, launching, and managing a Subnet to such an extent that it becomes effortless.

We are committed to making the Subnet ecosystem accessible to all, and we firmly believe that Subnets should be the primary choice for launching new appchains.

---
description: A Permissionless Staking Protocol For Avalanche Subnets.
---

# 👀 Primer

## A Permissionless Staking Protocol For Avalanche Subnets.

## **TL;DR**

1. Subnets are Avalanche’s main scaling mechanism but aren’t realistic right now because of the cost and limitations of staking
2. Liquid staking is just a small part of the problem, and everyone is focused on that (leaving builders out to dry)
3. GoGoPool solves the problem of Subnet adoption with a permissionless staking protocol that combines liquid staking, decentralized hardware, and subnet compatibility. These three elements work together to trivialize the cost of staking + validating -- powering the growth of subnets, and the future of Avalanche

## **The Subnet Vision**

Thanks to **Subnets,** [Avalanche](https://www.avax.network/) promises to be a fast, low-cost, eco-friendly blockchain**.** Subnets let anyone build a blockchain without worrying about its infrastructure, getting Avalanche’s best features for free.

One example, DeFi Kingdoms, which is the most popular blockchain game running on the Harmony network, plans to launch an expansion. But, if they launch on Harmony, they face two main challenges. Firstly, the launch would be slow and costly for their users and require additional customization. Creating a Subnet on the Avalanche network will help them overcome these issues. It will allow them to take advantage of the network's fast transaction times and create a dedicated set of validators, resulting in a faster and more affordable experience for their users. Additionally, launching via subnets will enable DeFi Kingdoms to experiment with tokenomics, which means they can tie their blockchain's tokenomics directly to the game mechanics.

In short, Subnets power the explosive growth of Avalanche by allowing infinite horizontal scaling and rapid experimentation with new models and ideas.

But in reality, Subnets are expensive to start, grow, and manage, and continue to be held back by the cost and limitations of staking.

Subnets should ideally offer a streamlined launch and growth process, with a user-friendly one-click experience and minimal concern regarding validators, as the staking cost is kept low.

A handful of projects are focused on **liquid staking** as a way to lower the cost of staking on Avalanche, but they are focused on a small part of the problem. Having liquid staking will definitely help the ecosystem grow by providing liquidity, but does not lower the cost of validation for subnets. Entrepreneurs remain locked out of the next generation of opportunities, and Avalanche misses out on its next step function of growth.

We’re doing the hard thing, and building a permissionless staking protocol that has:

1. Decentralized hardware pools
2. Liquid staking
3.

Subnet compatibility

Hardware operators join the protocol with 1000 AVAX, get matched with funds from liquid stakers, and begin validating the Avalanche Primary Network with the required 2000 AVAX (earning both staking and GGP community rewards). Stakers receive the benefit of liquid staking, getting a wrapped ggAVAX token and having instant liquidity while earning rewards in real time. Over time, the hardware operators in our protocol grows. In the future, when a subnet launches, they will join our protocol by staking the GGP token and, in return, will get access to the protocol's validator marketplace. Subnets will receive validators right away, eliminating their biggest upfront cost. Liquid stakers and subnets will work together to incentivize hardware operators, lowering the cost of launching subnets further.

If you want to launch a subnet partnership today, don't hesitate to [reach out to us](https://www.gogopool.com/getting-started-with-subnets)!

Subnets are a flywheel for our protocol - they do our best acquisition for us for free by incentivizing hardware operators to join, and we provide them with a liquidity pool and node operators to validate their subnet in exchange. This network effect at scale trivializes the cost of growing subnets for entrepreneurs, and leads to GoGoPool powering the explosive growth of Avalanche.

---
description: The math behind the numbers.
---

# Grafana Explained

GoGoPool contains a great deal of information that feels pretty inside baseball until you fully grasp 
the mechanics of the protocol. Much of the important protocol information we have displayed on 
[Grafana](https://multisiglabs.grafana.net/public-dashboards/4d21b06344684b8ab05ddd2828898ec8?orgId=1).
Lets go through Grafana's page number by number. 

### Protocol TVL 

Total Value Locked (TVL) is a metric for the total value of locked digital assets in the protocol, in this 
case it is a combination of the assets that are used for staking in our protocol. There are three:

1. GGP Stake
2. ggAvax Stake
3. Minipool Avax Stake

$$ \text{TVL} = GGP Stake + ggAvax Stake + Minipool Avax Stake $$

### Liquid Staking APY

This number is an estimate.

The way we calculate liquid staking APY is by viewing the real performance 
of ggAvax over the course of 90 days, and multiplying by 4 to get an estimate of it's performance over 
the course of the year.

$$ \text{ggAVAX APY} = \left(\frac{\text{Current Exchange} - \text{90 days ago Exchange}}{\text{90 days ago Exchange}} \right) \times 100\% \times 4\ $$

### NodeOp APR

This number is an estimate. Node Operator APR is determined by the rewards gained by a minipool for 
a one month cycle multiplied by 12 to get an estimate for a year. 

$$ \text{APR} = \left( \frac{{ggpRewardsAsAvax} + {AvaxRewards}}{{AvaxStaked + ggpStakedAsAvax}} \right) \times 100\% \times 12 $$

### Available Minipools

In order for minipools to be available, there must be 1000 available staking avax. For every 
1000 staking Avax, 1 new minipool can be made.

Therefore:

$$ \text{Available Minipools} = \left(\frac{Available Staking Avax}{1000}\right) $$

### Active Minipools 

Minipools can be in 7 distinct states:

- Cancelled
- Error
- Finished
- Withdrawable
- Launched
- Prelaunch
- Staking

These states are mutually exclusive. When a minipool is made it first is in `Prelaunch` state, where 
the user has created a minipool but their funds have not yet been matched. When their funds have been matched 
they are placed in the `Launched` state. During this state contract calls are made to make the minipool available 
for staking. When the appropriate contract calls are confirmed, the minipool begins `Staking`. A minipool 
is considered `Active` if it is in the `Staking` state. This means the assets are locked in the minipool 
for the staking duration of the minipool which is set by the user upon creation. When a minipool is done 
staking it moves to the `Withdrawable` state until the funds are removed, where it's finally moved to `Finished`.

### GGP Staked
The total amount of GGP staked by users. 

### GGP Price
The current price of the GGP Token. 

### Reward Cycle's Explained
Reward cycles are on a 30 day timeframe. There are 4 related variables in grafana: 

- Reward Cycle Start
- Reward Cycle End
- Rewards Eligibility Cutoff Date
- Next Rewards Eligibility Date

Start and end are self explanatory. A minipool must be created before the `Rewards Eligibility Cutoff Date` 
in order to earn rewards for the 30 day cycle. If you missed the current cutoff date, our grafana page also 
displays the following cutoff date for the next 30 day cycle. 

### ggAvax Last Rewards

ggAvax is our protocol's liquid staking token. This token accrues value by rewards from each 30 day 
reward cycle. When a rewards cycle ends some of the money that the minipool made from staking on the Avax 
network is returned to the assets pool. Just over 50% the amount made from staking on the Avax network
is given to node operators because of an included node op fee.

Just under 50% is returned to the liquid 
staking pool to accrue value. 

$$ \text{Half Rewards} = \left(\frac{avaxTotalRewards}{2}\right) $$

$$ \text{Liquid Staker Reward Amount} = {Half Rewards} - \left(Half Rewards\times{Node Op Fee Percent}\right) $$
$$ \text{Node Operator Reward Amount} = {Total Rewards} - {Liquid Staker Reward Amount}  $$

*As of 01/10/2024 the node op commision fee percent is 15%. Meaning liquid 
stakers will receive 42.5% of rewards and node operators 57.5%.*

### How ggAvax Works

ggAvax is the protocol's liquid staking token. It uses ERC-4626 which is a tokenized vault contract. 
You can think of ggAvax as shares that accrue value over time. The value increases as the asset pool 
increases in relation to the supply. Liquid staking puts Avax into the Avax Total Assets and the Avax 
Total Supply. The ratio is increased by ggAvax last rewards, when the rewards from the minipool are 
put into the assets, but not the total supply.

|Event|Avax Total Assets|Avax Total Supply|
|----|----|----|
|Liquid Stake| + | + |
|Rewards Cycle| + |  |

In this way ggAvax will become more valuable over time due to the always decreasing ratio of supply 
to assets.

---
description: >-
  GoGoPool has two tokens - the liquid staking token ggAVAX and the protocol
  token GGP.
---

# 🪙 Tokens and Utility

## GGAVAX

When a user deposits AVAX into the deposit pool, they receive a synthetic derivative token called ggAVAX.

ggAVAX represents a staker’s deposit plus the rewards it gains over time. This token is considered liquid and can be used like AVAX whereby users can:

* Hold it to accrue staking rewards
* Sell it, or&#x20;
* Use it to earn additional yield.&#x20;

If there is floating AVAX in the deposit pool, users will be able to exchange ggAVAX back for AVAX (which burns the ggAVAX, and draws AVAX from the deposit pool). Alternatively, they will have the option to exchange it for any token they would like on exchanges that list the token.

## GGP

GGP is an ERC20 token and serves as the protocol token for GoGoPool. The GGP tokens allow Node Operators to launch minipools i.e. full Avalanche Validator nodes matched with liquid staking funds for 1000 AVAX.

Node Operators have to stake a minimum amount of GGP tokens to secure their assigned staking funds as insurance for good behavior. At genesis the minimum will be 10% of their AVAX staked amount, but the operator can choose to stake as much as 150%. The higher their GGP stake, the higher their monthly GGP rewards will be. Node Operators can use these GGP rewards to launch new validator nodes, increasing their overall yield. In the future, Node Operators may restake their monthly GGP rewards to request AVAX delegation from liquid stakers onto existing minipools.

If a node operator has excessively low uptime and causes a loss of rewards for the protocol, stakers can be compensated from the GGP insurance put up by the Node Operator. This socializes the risk of being matched with a bad operator, and minimizes any potential losses. Slashed GGP can be sold to token holders at a discounted rate, with AVAX proceeds awarded to Liquid Stakers.

GGP token holders will have the ability to participate in the GoGoPool Protocol DAO, which allows members to propose and vote on a range of governance issues including inflation schedule of GGP, removing/replacing bad actors, smart contract upgrades, payment of community developers for future work, and rewarding outstanding members of the community (as well as other configuring the settings of the protocol).

### SUPPLY BREAKDOWN & VESTING

**Total Supply:** 22,500,000 GGP

* GoGoPool Foundation: 41.42% | The below allocations are subject to change according to DAO voting. Snapshot voting will be used to gauge sentiment, with recommendations executed by the Foundation.
  * DAO Fund: 16.42% | allocated as per the DAO — eg. growth capital, additional grants, liquidity incentives, airdrop schemes, strategic alliances, advisors, etc.
  * Ecosystem Development Grants: 15% | To fund engineering, business development, and marketing.
  * Liquidity Incentives: 10% | To be deployed as the DAO sees fit.

* Original Team: 20%
* Seed Round: 15.58%
* GGP Staking Rewards: 15%\*\*\*
* Advisors: 3%
* Pre-IDO Partner Sale: up to 3%
* Liquidity: 1%&#x20;
* IDO: up to 1%. Any remainder rolls over to Foundation

\*\*\*GGP Staking Rewards are split between 3 parties, and unlocked when issued:

* 70% to node operators
* 10% to Oracle DAO
* 20% to Protocol DAO Treasury

#### Vesting Following TGE:

* GoGoPool Foundation: Locked for 3 months, to be deployed under DAO snapshot voting over the following 48 months.
* Original Team: 12-month lock up, 36-month with quarterly vesting.
* Seed Round: 12-month lock, 36-month with quarterly vesting.
* GGP Staking Rewards: 48 months, monthly vesting.&#x20;
* Advisors: 12-month lock, 36-month with quarterly vesting.
* Pre-IDO Partner Sale:&#x20;
  * Tickets under 100k USD: minimum 12-month lock with 12-month quarterly vesting.
  * Tickets over 100k USD: 12-month lock, 36 month quarterly vesting.&#x20;
* Liquidity: Fully unlocked at TGE.&#x20;
* Avalaunch IDO: Fully unlocked at TGE.

#### Initial Supply: 187,970 GGP

* Liquidity pool—500K ($250K AVAX + \~188K GGP)
* IDO sale: 300k USD—225,000 GGP tokens
* Initial Market Cap (excluding liquidity): \~250K USD

Note: The only day 1 circulating tokens, excluding liquidity, will belong to Avalaunch IDO participants.

---
description: How to use GoGoPool as a Liquid Staker
---

# As a Liquid Staker

## Overview

When you liquid stake with GoGoPool, your $AVAX goes directly towards growing the Avalanche network and getting more subnets and validators launched.\
\
Your AVAX is staked into a deposit pool. These deposit pool funds are then used to match with node operators who want to become a validator for Avalanche's primary network. To learn more about how Avalanche utilizes proof-of-stake validation, check out [Avalanche's official documentation](https://www.avax.network/proof-of-stake-pos).\
\
Every Subnet requires validators to operate, and every Subnet validator must also validate the Avalanche Primary network. Currently, there is no cohesive way for Subnets in need of validators and validators who want to validate Subnets to get in contact.

GoGoPool aims to solve this by incentivizing node operators to run through the protocol, in order to create a set of validators that are oriented towards helping Subnets.&#x20;

Learn more about how Liquid Staking on GoGoPool works [here](../design/how-liquid-staking-works/).

{% hint style="info" %}
The visuals below show how to liquid stake on Fuji. The steps are the same as on Mainnet.&#x20;
{% endhint %}

To test GoGoPool on Fuji, use our [faucet](https://anr-ggp-faucet.fly.dev/) to get test GGP.

## How Stake with GoGoPool

### Step 1: Deposit AVAX

Your wallet provider will prompt you to transfer AVAX

<figure><img src="../.gitbook/assets/gogopool_liquid_stake_avax.png" alt=""><figcaption></figcaption></figure>

### Step 2: Receive ggAVAX

Check your wallet to see the ggAVAX.

<figure><img src="../.gitbook/assets/gogopool_ui_liquid_stake_success.png" alt=""><figcaption><p>A success message will be visible at the top of the screen</p></figcaption></figure>

<figure><img src="../.gitbook/assets/gogopool_metamask_wallet_sees_ggavax.png" alt=""><figcaption><p>The ggAVAX should be visible in your wallet.

# Manual Setup

To test GoGoPool on Fuji, use our [faucet](https://anr-ggp-faucet.fly.dev/) to get test GGP.

{% hint style="info" %}
The visuals for each setup below show how to create a Minipool on Fuji. The steps are the same as on Mainnet, but the AVAX and GGP requirements are different.
{% endhint %}

## Creating a Fuji or Mainnet node

To use GoGoPool as a node operator, and earn rewards on your staked GGP, you have to have an Avalanche node. To create a node, see the [Official Avalanche guides](https://docs.avax.network/nodes). Once you have a NodeId, come back to GoGoPool to register as a validator.

## How to make a Minipool with Manual Setup

### Step 1: Register a NodeId with GoGoPool

<figure><img src="../../.gitbook/assets/gogopool_register_node.png" alt=""><figcaption><p>Place your NodeId in the input box as shown, then press next.</p></figcaption></figure>

### Step 2: Approve and Deposit GGP

Your wallet provider will prompt you to approve and transfer GGP

<figure><img src="../../.gitbook/assets/gogopool_stake_ggp.png" alt=""><figcaption><p>This wallet already has 1 GGP staked, by staking another 0.5 GGP, the collateralization ratio will be 150%.

The user is prompted to approve the transfer of GGP.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/gogopool_deposit_ggp_success.png" alt=""><figcaption><p>Once the GGP transfer is approved by the user, the user can deposit GGP.</p></figcaption></figure>

### Step 3: Stake AVAX

Your wallet provider will prompt you to transfer AVAX

<figure><img src="../../.gitbook/assets/gogopool_deposit_avax.png" alt=""><figcaption><p>Deposit AVAX</p></figcaption></figure>

### Step 4: Minipool created!

Once you deposit AVAX, your Minipool is created! You can use the hash to see the transaction on your block explorer of choice.

<figure><img src="../../.gitbook/assets/gogopool_minipool_successfully_created.png" alt=""><figcaption><p>Minipool successfully created! Use the hash to view the transaction on a block explorer.

---
description: How to use GoGoPool as a Node Operator
---

# As a Node Operator

## How to make a Minipool

A Minipool is a term we borrowed from RocketPool. It represents a validator that was funded via AVAX contributed from liquid stakers using the deposit pool and AVAX contributed from node operators during their registration with GoGoPool.

Currently, we offer two different experiences to create Minipools. Our original experience, which we call Manual Setup, and our new one-click launcher experience, Minipools 2.0.

# One-Click Launcher

{% embed url="https://youtu.be/1Fmm88kQADE" %}

In our one-click launch experience, you only need AVAX to launch your minipool. We have partnered with [ooNodz.network](https://oonodz.network/) to instantly spin up an avalanche node when you launch your minipool. We have handled buying and staking ggp on your behalf, with the collateralization ratio starting between 10-11%. If you want to use your existing GGP holdings, you can add to this collateralization ratio after your minipool is created, on your [Dashboard](https://app.gogopool.com/dashboard/).

To test GoGoPool on Fuji, use our [faucet](https://anr-ggp-faucet.fly.dev/) to get test GGP.

{% hint style="info" %}
The visuals for each setup below show how to create a Minipool on Fuji. The steps are the same as on Mainnet, but the AVAX and GGP requirements are different.

---
description: About our hosted testnet.
---

# Using the Alpha Testnet

To test our product, we needed total control over the staking reward timings. Our testnet has a reward payout period of 2 minutes, with a flat rate of 10% rewards. This allows our testers to quickly get feedback on their testnet nodes.&#x20;

### Creating A Wallet

See [here](wallet-configuration.md).

### Adding our Tokens

First, navigate to our [welcome page](https://app.gogopool.com/alphaWelcome) and connect your wallet. Only Metamask is supported in our Alpha.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Next, click the "Add GGP Token" and "Add ggAVAX" to add the respective tokens to your wallet!

### Getting Funds

Head over to the [faucet](https://anr-ggp-faucet.fly.dev/) and switch the network to "Avalanche Node Runner".

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption><p>Our faucet.</p></figcaption></figure>

From here, you can copy your wallet address into the box and request AVAX and GGP!

### [How to Liquid Stake](staking-with-gogopool/liquid-staking.md)

### Getting a Node ID

During our testnet alpha we will not be supporting the creation of additional nodes. However, you can borrow on of our nodes temporarily so you can test out our Dashboard and the Minipool Creation process.

---
description: Configuring your wallet for GoGoPool.
---

# Wallet Configuration

## Supported Wallets & Browsers

During our initial alpha and beta period, we will only be supporting the [Metamask](https://metamask.io/) browser wallet, and will only be supporting desktop usage via [Chrome](https://www.google.com/chrome/), [Firefox](https://www.mozilla.org/en-US/firefox/new/), and [Brave](https://brave.com/).

## Adding the Alpha Network to Metamask

We are using our own custom test network for our Alpha tests.

---
description: How to stake your AVAX with GoGoPool.
---

# Liquid Staking

The process of liquid staking on all networks (Our private testnet, Fuji, and Mainnet) is identical! Before continuing, identify which network you want to test out liquid staking on.

## Adding Funds on Testnets

If you are testing out GoGoPool on our private testnet, head over to [our faucet](https://anr-ggp-faucet.fly.dev/) and add some funds!

If you are testing out GoGoPool on Fuji, head over to the [official faucet](https://faucet.avax.network/) and add some funds!

## Liquid Staking on GoGoPool

1. Navigate to our [Liquid Staking](https://beta.gogopool.com/liquidStaking) page.
2.  Connect your wallet to the app.

    <figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption><p>Connect Wallet Button</p></figcaption></figure>
3.  Switch to the network you are trying to interface with.

<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption><p>Network Select Button</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption><p>Network Select Modal</p></figcaption></figure>
4.  Enter the amount of AVAX you want to deposit.

    <figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption><p>Liquid Staking Form</p></figcaption></figure>
5. Click Deposit!
6.

# On the Multisig Labs Testnet

Make sure you [added our network to Metamask](../../wallet-configuration.md#multisig-labs-testnet-settings).

---
description: How to stake AVAX on the GoGoPool protocol!
---

# Registering a GoGoPool Node

Navigate to our [node registration page](https://app.gogopool.com/nodeOperator). Connect your wallet with the funds you want to stake and select your appropriate network (for our alpha tests, this would be GGP ANR).

Once you have an appropriate amount of funds, (for our alpha you need 1001 AVAX and 200 GGP token). If you lack the correct token amount on our testnet or Fuji, head over to the [faucets](../liquid-staking.md#adding-funds-on-testnets).

Then enter your node's ID in the form below!

<figure><img src="../../../.gitbook/assets/image (6).png" alt=""><figcaption><p>Node ID Register Form</p></figcaption></figure>

After you've registered your node ID, you have to approve and stake your GGP tokens. The minimum GGP tokens to stake is 100 GGP when depositing 1000 AVAX.

If you don't have any GGP on either our testnet or fuji, head over to [the faucet](https://anr-ggp-faucet.fly.dev/) and get some!

<figure><img src="../../../.gitbook/assets/image (3) (3).png" alt=""><figcaption><p>Approve and Stake Form</p></figcaption></figure>

After the GGP is approved, you now enter your AVAX staking amount and duration! On our testnet, staking duration is set at 15 minutes, and on the Fuji testnet it is statically set to 2 weeks, so this cannot be changed. In the future on the Avalanche mainnet, there will be more options for duration.

---
description: How to run a GoGoPool Node.

---
description: How to create an AVAX node and stake AVAX using GoGoPool!
---

# Creating a Node

During our intial alpha phase on our private testnet, users will not be able to create nodes. To test out our features using an existing node on our testnet, see [here](../staking-with-gogopool/running-a-gogopool-node/on-the-multisig-labs-testnet.md).

## Creating a Fuji or Mainnet node

To create a node, see the [Official Avalanche guides](https://docs.avax.network/nodes).