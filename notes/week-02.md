# Week 02

## Project: First GPIO output on Raspberry Pi

Goal:
Control a real GPIO from Linux userspace.

Hardware:
- Raspberry Pi 3
- LED
- resistor
- logic analyzer

GPIO used:
- GPIO17
- physical pin 11
- GND on physical pin 6

Commands used:

```bash
gpioinfo -c gpiochip0 17
gpioset -c gpiochip0 17=1
gpioset -c gpiochip0 -t 2s,0 17=1
gpioset -c gpiochip0 -t 500ms,500ms 17=1
```