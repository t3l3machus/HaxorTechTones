## Frequency Band Table with Device Compatibility
To understand which modules are compatible with which frequency bands (Generated with ChatGPT):

| **Band**       | **Frequency Range**      | **Region / Regulation**          | **Common Uses**                                                | **Examples of Devices / Protocols**                            | **Compatible Modules / Tech**              | **Notes**                                  |
|----------------|--------------------------|----------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------|--------------------------------------------|
| **Low LF**     | 125–134 kHz              | Worldwide (ISM)                  | Short-range RFID, access control                                | RFID badges, pet microchips, proximity cards                   | 🟢 RFID                                      | Very short range (~cm), inductive coupling |
| **HF (13.56)** | 13.56 MHz                | Worldwide (ISM)                  | NFC, smart cards, HF RFID                                       | Contactless payments, passports, library tags                  | 🟢 RFID                                      | Standard for smart cards and NFC           |
| **27 MHz**     | 26.965–27.405 MHz        | Worldwide                        | CB radio, toy RC cars, garage doors                             | Hobby RC cars, walkie-talkies                                  | 🔴 None (common hobby radios)               | Shared with CB radio                       |
| **49 MHz**     | 49.82–49.90 MHz          | USA (FCC Part 15)                | Baby monitors, old wireless phones                              | Wireless toys, baby monitors                                   | 🔴 None                                      | Legacy band                                |
| **72–76 MHz**  | 72–76 MHz                | USA                              | RC aircraft control                                              | RC aircraft remotes                                            | 🔴 None                                      | Used in model aircraft                     |
| **315 MHz**    | 310–320 MHz              | USA (Part 15)                    | Garage doors, tire pressure sensors                             | Car remotes, TPMS                                              | 🟡 CC1101 (region dependent)                | Not allowed in EU                          |
| **433 MHz**    | 433.05–434.79 MHz        | EU / Asia                        | ISM: RF remotes, IoT, weather stations                          | RF remotes (garage doors, car keys), weather stations, wireless sensors, IoT devices | 🟢 CC1101                                    | Very common for sub-GHz IoT devices        |
| **470–512 MHz**| 470–512 MHz              | USA                              | Land mobile radio, paging                                       | Police radios, commercial systems                              | 🟡 CC1101 (limited)                         | Regulated, mostly voice comms              |
| **868 MHz**    | 863–870 MHz              | Europe (ISM)                     | LoRa, smart meters, automation                                  | LoRaWAN gateways, Zigbee EU                                    | 🟢 CC1101, 🟡 Some BLE (new tech)            | Duty cycle limits apply                    |
| **902–928 MHz**| 902–928 MHz              | USA / Canada (ISM)               | LoRa, Zigbee, RFID, telemetry                                   | LoRa, Zigbee (US), industrial sensors, RFID UHF tags, smart meters  | 🟢 CC1101                                    | Better range than 2.4 GHz                  |
| **1.2 GHz**    | 1.2–1.3 GHz              | Amateur / FPV                    | FPV video transmission                                          | Analog FPV for drones                                          | 🔴 None (analog only)                       | Licensed amateur band                      |
| **1.9 GHz**    | 1880–1930 MHz            | Europe, Japan, USA               | Cordless phones (DECT)                                          | DECT phones                                                    | 🔴 None                                      | DECT-specific                              |
| **2.4 GHz**    | 2400–2483.5 MHz          | Worldwide (ISM)                  | Wi-Fi, Bluetooth, Zigbee                                        | Wi-Fi (802.11b/g/n), Bluetooth classic, BLE, Zigbee, microwave ovens, cordless phones, wireless keyboards, mice, drones, wireless game controllers, wireless headsets, smart home devices, nRF24L01 modules                      | 🟢 Wi-Fi, 🟢 BLE, 🟢 nRF24L01                 | Crowded band, short range                  |
| **3.6–3.8 GHz**| 3600–3800 MHz            | Region-specific                  | 5G, private LTE (CBRS)                                          | 5G base stations                                               | 🔴 None (cellular modules only)             | Enterprise use                             |
| **5.0 GHz**    | 5.15–5.875 GHz           | Worldwide (ISM / DFS)            | Wi-Fi (5GHz), radar                                              | Modern routers, radar systems                                  | 🟢 Wi-Fi                                     | DFS applies in many regions                |
| **5.8 GHz**    | 5725–5850 MHz            | Worldwide (ISM)                  | FPV drones, PTP wireless links                                  | FPV video, Wi-Fi APs                                           | 🟢 Wi-Fi (some devices)                     | Higher loss through walls                  |
| **24 GHz**     | 24–24.25 GHz             | Worldwide (ISM)                  | Radar, automation, motion detection                             | Car sensors, motion radars                                     | 🔴 None (radar modules only)                | Very short range                           |
| **60 GHz**     | 57–71 GHz                | Worldwide (V-band)               | Ultra-fast Wi-Fi (WiGig), wireless VR                           | VR headsets, WiGig                                             | 🔴 None (WiGig chipsets only)               | LOS only, very limited range               |
| **77–81 GHz**  | 76–81 GHz                | Automotive (Radar)               | Adaptive cruise control, collision detection                    | Car radar systems                                              | 🔴 None                                      | Used in automotive industry                |

## Notes:
- nRF24L01 operates only in 2.4 GHz ISM band.
- CC1101 supports a wide range of Sub-GHz bands (300–928 MHz depending on configuration).
- BLE is a subset of Bluetooth, using 2.4 GHz with low power protocols.
- RFID is frequency-dependent — LF (~125 kHz), HF (13.56 MHz), and UHF (850–960 MHz) all exist, and require different readers.
- Wi-Fi modules (e.g., ESP8266/ESP32) cover 2.4 GHz, while others support both 2.4 and 5 GHz bands.

## Key Terms:
- ISM: Industrial, Scientific, and Medical band — unlicensed, but regulated (power limits, duty cycles).
- FPV: First-person view — used in drones for live video feed.
- DECT: Digital Enhanced Cordless Telecommunications — cordless phone tech.
- LoRa: Long Range low-power wireless communication.
- Zigbee: Mesh network protocol used for home automation.
