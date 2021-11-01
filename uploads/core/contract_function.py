from os import PRIO_PGRP
import time
import json
import base64
import mimetypes
from io import BytesIO
from web3 import Web3
from django.db import connection
from web3.middleware import geth_poa_middleware
from uploads.core.contract_config import PRIVATE_KEY, contract_address,contract_abi,chainId,rpc_url,PUBLIC_KEY
import logging
logger = logging.getLogger(__name__)


class Contract:
    def __init__(self, rpc_url, contract_address, contract_abi):
        try:
            self.web3 = Web3(Web3.HTTPProvider(rpc_url))
            self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            self.instance = self.web3.eth.contract(address=self.web3.toChecksumAddress(contract_address),
                                                   abi=contract_abi)
        except Exception as e:
            raise str(e)

def create_nft(address,token_id,base_uri):
    try:
        W3 = Web3(Web3.HTTPProvider(rpc_url))
        if W3.isConnected():          
            W3.middleware_onion.inject(geth_poa_middleware, layer=0)
            try:

                contract = W3.eth.contract(address = W3.toChecksumAddress(contract_address),abi=contract_abi)
            except Exception as e:
                return str(e)
            transaction=contract.functions.mint(str(address),int(token_id),str(base_uri)).buildTransaction()
            transaction.update({'gas':500000})
            transaction.update({'nonce':contract.web3.eth.getTransactionCount(PUBLIC_KEY,'latest')})
            signed_tx = W3.eth.account.sign_transaction(transaction,PRIVATE_KEY)
            txn_hash = W3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print("Transaction Hash",W3.toHex(txn_hash))
            txn_recipt=W3.eth.waitForTransactionReceipt(txn_hash)
           
            
            # txn_json = txn_recipt
            return W3.toHex(txn_hash)

    except Exception as e:
        return str(e)


