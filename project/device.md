
# Jimini device

The jimini device is developed by our company.
It consists of a pen-like device than can be plunged into a liquid sample (ie air, water, urine).
With its companion app, we can generate signals from sensors or emitters-sensors couples.

## Signals:
**SLC naming:** `{sensor}-{emitter}-{amplitude}
- Emitter:
  - Emitter: wavelength nm (`275`, `365`, `405`, `455`), `VIS` (broadband visible,opposite side than the sensor), `VISD` (visible same side than the sensor), `R405` (same side than the sensor 405)
  - Amplitude: drive current in mA (e.g. `100.0mA`, `50.0mA`, `2.5mA`)
  - Suffixes: `-hdrl`/`-hdrs` (high dynamic range long/short), `-ADS` (analog-to-digital scaling)
  - Special SLCs: `C12-off`/`C14-off` (dark/reference), `EIS` (electrochemical impedance spectroscopy), `IRM-{wavelength}` (IR matrix, e.g. `IRM-1070-100.0mA`)
  - all sensors are on the opposite side of the sensor except VISD and R405 that are on the same side.

- sensors:
  - C12: with a sensing range of 321nm-870nm
  - C14: with a sensing range of 570-1078nm
  - EIS: sensing electroimpedance signals.
  - IRM: matrix of IR sensors
