Braintree_Merchant_ID = cy6sjx8n593s73g7
Braintree_Public_Key = sypktxz476sr7yqx
Braintree_Private_Key = eae0177e3d543e9244556f5d6521d31d

from braintree import configuration,Environment
Configuration.configure(Environment.Sandbox,Braintree_Merchant_ID,Braintree_Public_Key,Braintree_Private_Key)
