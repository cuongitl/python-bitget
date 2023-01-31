Broker
===============

Sub Account Interface
------------

`Get Broker Info <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_get_info()

`Create Sub Account <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_sub_create(subName, remark=None)

`Get Sub List <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_get_sub_list(pageSize=10, lastEndId=None, status=None)

`Modify Sub Account <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_sub_modify_account(subUid, perm, status)

`Modify Sub Email <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_sub_modify_email(subUid, subEmail):

`GET Sub Email <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_get_sub_email(subUid)

`Get Sub Spot Assets <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_get_sub_spot_assets(subUid)

`Get Sub Future Assets <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_get_sub_future_assets(subUid, productType)

`Get Sub Deposit Address (Only Broker) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_get_sub_deposit_address(subUid, coin, chain=None)

`Sub Withdrawal (Only Broker) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_sub_withdrawal(subUid, coin, address, chain, amount,
                              tag=None, clientOrderId=None, remark=None)

`Sub Deposit Auto Transfer (Only Broker) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_sub_auto_transfer(subUid, coin, toAccountType)

Sub API Interface
------------

`Create Sub ApiKey (Only Broker) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_sub_create_api(subUid, passphrase, remark, ip, perm)

`Get Sub ApiKey List <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_get_sub_api_list(subUid)

`Modify Sub ApiKey (Only Broker) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.broker_sub_modify_api(subUid, apikey, remark=None, ip=None, perm=None)
