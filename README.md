# flask_knesset_backend


## Database models

1. Table: Yeshuv, store the Yeshuv's metadata.

2. Table: Kalfi, store a single Kalfi metadata.

Important note: each kalfis number start from 1 for each Yeshuv, so a Kalfi's primary key is composed of:
  *. The yesuv primary key
  * The kalfi number
  * Klafi sub-number ( some Kalfi's host multiple sub-kalfi's ).
  
3. Table Knesset_22, store the result for each kalfi.

4. YeshuvKnesset, store aggreated elections result per Yeshuv for the last 5 Knesssets.

Since the data size is small, i pre proccessed the result into a DB table that fit well to the 
website needs, to make the API queries less complicated.

5. YeshuvType, store yeshuv types metadata. 
