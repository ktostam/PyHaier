# PyHaier

Very simple (for now) library to manipulate the basic parameters of the Haier heat pump.

## Donation
If you like My work and want to support me, you can:

[<img width="150px" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png">](https://www.buymeacoffee.com/jacekbrzozZ)

Or if you from Poland:

[<img width="150px" src="https://buycoffee.to/btn/buycoffeeto-btn-primary.svg">](https://buycoffee.to/jacekbrzozz)


## Version
### 0.1.1
New function:
- Get current DHW tank temperature

### 0.1.0
Basic function:
- Get current state
- Get current mode
- Get current Heating temperature
- Get current DHW temperature
- Set state
- Set mode
- Set Heating temperature
- Set DHW temperature

## Tested with
1. AU082FYCRA(HW)
2. AU162FYCRA(HW)

However, it should work with all pumps that feature the YR-e27 remote control

## Instalation

**Install from source**
```shell
$ git clone https://github.com/ktostam/PyHaier.git
$ cd PyHaier
$ python setup.py install
```

## Usage

### PyHaier.GetState(payload)

Display current state (Cool/Heat/Tank/Cool+Tank/Heat+Tank/Off).

You need provide **payload** for GetState function.
**payload** is the contents of holding registers 101-106
___
### PyHaier.GetMode(payload)

Display current Mode (ECO/Silent/Turbo).

You need provide **payload** for GetMode function.
**payload** is the contents of holding register 201
___
### PyHaier.GetCHTemp(payload)

Display current water temperature with precision 0.5&deg;C

You need provide **payload** for GetMode function.
**payload** is the contents of holding registers 101-106
___
### PyHaier.GetDHWTemp(payload)

Display current DHW temperature with precision 1&deg;C

You need provide **payload** for GetMode function.
**payload** is the contents of holding registers 101-106
___
### PyHaier.GetDHWCurTemp(payload)

Display current DHW temperature in Tank with precision 0.1&deg;C

You need provide **payload** for GetMode function.
**payload** is the contents of holding registers 154
___
### PyHaier.SetState(current,new)

Create Modbus frame to set new pump state

You need provide **payload** for SetState function.
**payload** is the contents of holding registers 101-106

**new** can be:
- `off`
- `on`
- `C` for Cool
- `H` for Heat
- `T` for Tank
- `CT` for Cool+Tank
- `HT` for Heat+Tank
___
### PyHaier.SetMode(new)

Set mode (eco/silent/turbo).

You need provide **new** for SetMode function.
**new** can be:
- `eco`
- `silent`
- `turbo`
___
### PyHaier.SetCHTemp(current, new)

Set water temperature with precision 0.5&deg;C

You need provide **current** for SetCHTemp function.
**current** is the contents of holding registers 101-106

**new** is new temperature with precision 0.5&deg;C
___
### PyHaier.SetDHWTemp(current, new)

Set DHW temperature with precision 1&deg;C

You need provide **current** for SetDHWTemp function.
**current** is the contents of holding registers 101-106

**new** is new temperature with precision 1&deg;C

## Example script 1

```Python
from pymodbus.client.sync import ModbusSerialClient
import PyHaier

# Serial setting
client = ModbusSerialClient(method = "rtu", port="/dev/ttyAMA0", stopbits=1, bytesize=8, parity='E', baudrate=9600)

# connect to serial
client.connect()

#read holding registers from 101 to 106
payload=client.read_holding_registers(101, 6, unit=17)
state=PyHaier.GetState(payload)
htemp=PyHaier.GetCHTemp(payload)
dhwtemp=PyHaier.GetDHWTemp(payload)
payload=client.read_holding_registers(201, 1, unit=17)
mode=PyHaier.GetMode(payload)
client.close()
print("Pump status:\t"+state+"\nPump mode:\t"+mode+"\nWater temp:\t"+str(htemp)+"\nDHW temp:\t"+str(dhwtemp))
```
### Output

```shell
$ python script.py
Pump status:	Heat+Tank ON
Pump mode:	silent
Water temp:	25.0
DHW temp:	43.0
```

## Example script 2

```Python
from pymodbus.client.sync import ModbusSerialClient
import PyHaier

# Serial setting
client = ModbusSerialClient(method = "rtu", port="/dev/ttyAMA0", stopbits=1, bytesize=8, parity='E', baudrate=9600)

# connect to serial
client.connect()

#read holding registers from 101 to 106
payload=client.read_holding_registers(101, 6, unit=17)
state=PyHaier.GetState(payload)
print("Current state:\t"+state)
new=PyHaier.SetState(payload,"CT")
client.write_registers(101, new , unit=17)
payload=client.read_holding_registers(101, 6, unit=17)
state=PyHaier.GetState(payload)
print("New state:\t"+state)
client.close()
```
### Output

```shell
$ python script.py
Current stete:	Heat+Tank ON
New state:	Cool+Tank ON

```
## License

 GNU GPL [©Jacek Brzozowski](https://github.com/ktostam)