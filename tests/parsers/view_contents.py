"""
tests.parsers.view_contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~
View Contents list table tests

"""
from eveparser import parse_view_contents
from tests import TableTestGroup


VIEW_CONTENTS_TABLE = TableTestGroup(parse_view_contents)
VIEW_CONTENTS_TABLE.add_test(
    '''
1600mm Reinforced Steel Plates II\tArmor Reinforcer\tLow Slot\t1
100MN Microwarpdrive II\tPropulsion Module\tMedium Slot\t1
Bouncer II\tCombat Drone\tDrone Bay\t1
Bouncer II\tCombat Drone\tDrone Bay\t1
Nitrogen Isotopes\tIce Product\tFuel Bay\t20000
Drone Link Augmentor II\tDrone Control Range Module\tHigh Slot\t1
Large Micro Jump Drive\tMicro Jump Drive\tCargo Hold\t1
Tengu Defensive - Adaptive Shielding\tDefensive Systems\tSubsystem\t1
Large Trimark Armor Pump I\tRig Armor\tRig Slot\t1
Medium Electrochemical Capacitor Booster I\tCapacitor Booster\tMedium Slot\t1
Giant Secure Container\tSecure Cargo Container\t\t1''',
    ([{'group': 'Propulsion Module',
       'location': 'Medium Slot',
       'name': '100MN Microwarpdrive II',
       'quantity': 1},
      {'group': 'Armor Reinforcer',
       'location': 'Low Slot',
       'name': '1600mm Reinforced Steel Plates II',
       'quantity': 1},
      {'group': 'Combat Drone',
       'location': 'Drone Bay',
       'name': 'Bouncer II',
       'quantity': 2},
      {'group': 'Drone Control Range Module',
       'location': 'High Slot',
       'name': 'Drone Link Augmentor II',
       'quantity': 1},
      {'group': 'Secure Cargo Container',
       'location': '',
       'name': 'Giant Secure Container',
       'quantity': 1},
      {'group': 'Micro Jump Drive',
       'location': 'Cargo Hold',
       'name': 'Large Micro Jump Drive',
       'quantity': 1},
      {'group': 'Rig Armor',
       'location': 'Rig Slot',
       'name': 'Large Trimark Armor Pump I',
       'quantity': 1},
      {'group': 'Capacitor Booster',
       'location': 'Medium Slot',
       'name': 'Medium Electrochemical Capacitor Booster I',
       'quantity': 1},
      {'group': 'Ice Product',
       'location': 'Fuel Bay',
       'name': 'Nitrogen Isotopes',
       'quantity': 20000},
      {'group': 'Defensive Systems',
       'location': 'Subsystem',
       'name': 'Tengu Defensive - Adaptive Shielding',
       'quantity': 1}], []))
VIEW_CONTENTS_TABLE.add_test(
    '''Festival Launcher\tFestival Launcher\t1
Festival Launcher\tFestival Launcher\t1
Hornet EC-300\tElectronic Warfare Drone\t50
Men's 'Esquire' Coat (red/gold)\tOuter\t1
''', ([{'group': 'Festival Launcher',
        'name': 'Festival Launcher',
        'quantity': 2},
       {'group': 'Electronic Warfare Drone',
        'name': 'Hornet EC-300',
        'quantity': 50},
       {'group': 'Outer',
        'name': "Men's 'Esquire' Coat (red/gold)",
        'quantity': 1}], []))
