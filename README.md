# PyHaier

Very simple (for now) library to manipulate the basic parameters of the Haier heat pump.

## Donation
If you like My work and want to support me, you can:

[<img width="150px" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png">](https://www.buymeacoffee.com/jacekbrzozZ)

Or if you from Poland:

[<img width="150px" src="https://buycoffee.to/btn/buycoffeeto-btn-primary.svg">](https://buycoffee.to/jacekbrzozz)

## Support
For support, join our Discord channel https://discord.gg/7aF38puD

## Contributors
- Daniel Mentel he found all information from functions added in 0.2.1 and 0.2.2 version

## Version
### 0.3.6
- Tdef (thanks to Daniel Mentel)
- Defrost status

### 0.3.5
- small fixes

### 0.3.4
- new function GetTSatPd, GetTsatPs, GetEEVLevel by Daniel Mentel

### 0.3.1
- new function GetThiTho by Daniel Mentel
- fixed functions GetTao, GetTdTs, SetCHTemp

### 0.3.0
- few fixed for GetTdTs and GetPump functions
- add error handling when frame passed to function has bad length

### 0.2.9
- one more fix

### 0.2.8
- few more fix

### 0.2.7
- one more fix

### 0.2.6
- fix function name

### 0.2.5
- add GetPump function to show if buildin pump is on or off
- add Get3way function to show what position the 3-way valve is in

### 0.2.4
- some fixes

### 0.2.3
- use divmod

### 0.2.2
- add GetTdTs function showing Td and Ts parameters as array
- add GetPdPs function showing current and set Pd parameter (for now only Pd) as array
- add GetFanRpm function showing Fan1 and Fan2 rpm, as array
- add GetTao function showwing ambient temperatura
- rename GetCompFreq function to GetCompInfo and add to this function other information like temperature, voltage and current about compressor, display as array

### 0.2.1
- add GetCompFreq function showing current and set compressor frequency
- add GetArchError function showing three archive errors as array
- add GetEEVLevel function showing current EEV opening level

### 0.2.0
- rename 'silent' to 'quiet' in GetMode and SetMode function to be consistent with haier nomenclature

### 0.1.9
- fix for SetState. Now turning on/off emulate "leaf" button on YR-e27

### 0.1.8
- fix for previous fix :D

### 0.1.7
- fix turning on pump in SetState function

### 0.1.6
- Just for pip upload

### 0.1.5
- More error handling

### 0.1.4
- Update in error handling

### 0.1.3
New function
- Add function to read Compressor frequency

### 0.1.2
New function:
- Get value of Twi and Two parameters (not 100% sure if this is OK.)

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

**Install from pip**

```shell
$ pip install PyHaier
```

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

You need provide **payload** for GetDHWCurTemp function.
**payload** is the contents of holding registers 141-156
___
### PyHaier.GetTwiTwo(payload)

Display Twi and Two parameters with precision 0.1&deg;C, output is an array

You need provide **payload** for GetTwiTwo function.
**payload** is the contents of holding registers 141-156
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
___
### PyHaier.GetCompFreq(payload)

Display set and actual compressor frequency, output is an array

You need provide **payload** for GetCompFreq function.
**payload** is the contents of holding registers 241-261

___
### PyHaier.GetArchError(payload)

Display archve error codes, output is an array

You need provide **payload** for GetArchError function.
**payload** is the contents of holding registers 241-261

___
### PyHaier.GetEEVLevel(payload)

Display actual EEV opening level

You need provide **payload** for GetEEVLevel function.
**payload** is the contents of holding registers 241-261


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
state=PyHaier.GetState(payload.registers)
htemp=PyHaier.GetCHTemp(payload.registers)
dhwtemp=PyHaier.GetDHWTemp(payload.registers)
payload=client.read_holding_registers(201, 1, unit=17)
mode=PyHaier.GetMode(payload.registers)
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
state=PyHaier.GetState(payload.registers)
print("Current state:\t"+state)
new=PyHaier.SetState(payload.registers,"CT")
client.write_registers(101, new , unit=17)
payload=client.read_holding_registers(101, 6, unit=17)
state=PyHaier.GetState(payload.registers)
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
