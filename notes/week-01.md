# Week 01

## Current System

- Board: Raspberry Pi 3
- Access: SSH working
- IP: `192.168.0.50`

## OS Information

Output of `uname -a`:

```bash
Linux raspberrypi 6.12.61-v8+ #1924 SMP PREEMPT Mon Dec 8 17:47:47 GMT 2025 aarch64 GNU/Linux
```
Output of lsb_release -a:
```bash
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 13 (trixie)
Release:        13
Codename:       trixie
```
Important Finding

I initially thought the board was running Ubuntu 22.04 64-bit, but the actual system reports:

Debian GNU/Linux 13 (trixie)
64-bit (aarch64)
Raspberry Pi kernel 6.12.61-v8+

So the current setup is Debian 13, not Ubuntu 22.04.

Boot Analysis Attempt

When I ran:
```bash
systemd-analyze time
systemd-analyze critical-chain
```
I got:
```bash
Bootup is not yet finished (org.freedesktop.systemd1.Manager.FinishTimestampMonotonic=0).
Please try again later.
Hint: Use 'systemctl list-jobs' to see active jobs
```
This means the system was still starting services and boot was not complete yet.

Slow Services Observed

Output of:
```bash
systemd-analyze blame | head -20
```
```bash
8.678s cloud-init-main.service
7.605s NetworkManager.service
5.920s NetworkManager-wait-online.service
5.270s apt-daily-upgrade.service
3.722s dev-mmcblk0p2.device
2.270s user@1000.service
1.884s cloud-init-local.service
1.808s accounts-daemon.service
1.702s udisks2.service
1.488s polkit.service
1.444s plymouth-read-write.service
1.334s lm-sensors.service
1.169s rpi-resize-swap-file.service
1.154s systemd-udev-trigger.service
1.124s avahi-daemon.service
1.123s keyboard-setup.service
1.104s bluetooth.service
1.090s ModemManager.service
1.034s lightdm.service
964ms plymouth-quit-wait.service
```
**Notes**

The system appears to be a full general-purpose image rather than a minimal embedded-style image.
Boot timing should be collected again after boot fully finishes.
Next time, run:

systemctl list-jobs
systemd-analyze time
systemd-analyze critical-chain

## One engineering note

Since your output shows `lightdm`, `NetworkManager`, `cloud-init`, and desktop-oriented services, I’d classify this system as:

**good for learning Linux now, not yet optimized for embedded work**

That is fine in phase 1.

## Your next step

Run these after the Pi has been up for at least a minute:

```bash
systemctl list-jobs
systemd-analyze time
systemd-analyze critical-chain
```

## Boot Analysis Update

Cloud-init is no longer blocking boot.

Current remaining jobs show that the system is still waiting on the graphical / VNC path:

```bash
JOB UNIT                   TYPE  STATE
166 wayvnc.service         start running
168 wayvnc-control.service start waiting
1   graphical.target       start waiting
2   multi-user.target      start waiting