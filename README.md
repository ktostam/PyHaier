# PyHaier

Very simple library to manipulate the basic parameters of the Haier heat pump.

## Version

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
---
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

## Example script

```Python
import PyHaier
```