"""
tests.parsers.wallet
~~~~~~~~~~~~~~~~~~~~
Loot history table tests

"""
from eveparser import parse_wallet
from tests import TableTestGroup


WALLET_TABLE = TableTestGroup(parse_wallet)
WALLET_TABLE.add_test("2014.01.04 05:49:31\tMarket Escrow\t-251.00 ISK\t"
                      "325.22 ISK\tMarket escrow authorized by: Me",
                      ([{'amount': '-251.00 ISK',
                         'balance': '325.22 ISK',
                         'time': '2014.01.04 05:49:31',
                         'description': 'Market escrow authorized by: Me',
                         'transaction_type': 'Market Escrow'}], []))
WALLET_TABLE.add_test(
    "2014.01.04 16:08\tStorm Command Center\t200,000.00 ISK\t1\t"
    "-200,000.00 ISK\tISK\tlady scarlette\t"
    "Otanuomi IV - Moon 4 - Ishukone Corporation Factory",
    ([{'client': 'lady scarlette',
       'credit': '-200,000.00 ISK',
       'currency': 'ISK',
       'name': 'Storm Command Center',
       'price': '200,000.00 ISK',
       'quantity': 1,
       'time': '2014.01.04 16:08',
       'where': 'Otanuomi IV - Moon 4 - Ishukone Corporation Factory'}], []))
WALLET_TABLE.add_test(
    "2014.12.19 20:04\tMedium Core Defense Capacitor Safeguard II\t"
    "7'999'996.10 ISK\t1\t7'999'996.10 ISK\tISK\tOrmand Ishikela\t"
    "Jita IV - Moon 4 - Caldari Navy Assembly Plant",
    ([{'client': 'Ormand Ishikela',
       'credit': "7'999'996.10 ISK",
       'currency': 'ISK',
       'name': 'Medium Core Defense Capacitor Safeguard II',
       'price': "7'999'996.10 ISK",
       'quantity': 1,
       'time': '2014.12.19 20:04',
       'where': 'Jita IV - Moon 4 - Caldari Navy Assembly Plant'}], []))
