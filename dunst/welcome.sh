#!/bin/bash

# SECTION 1 — Qtile log errors
LOGFILE="$HOME/.local/share/qtile/qtile.log"
if [ -f "$LOGFILE" ]; then
    count=$(grep -cE "ERROR|WARNING" "$LOGFILE")
    if [ "$count" -eq 0 ]; then
        qtile_status="Qtile: No errors on load"
    else
        qtile_status="Qtile: $count errors detected on load"
    fi
else
    qtile_status="Qtile: Log file not found"
fi

# SECTION 2 — Package updates
count=$(yay -Qu --noconfirm 2>/dev/null | wc -l)
if [ "$count" -eq 0 ]; then
    updates="Packages: System up to date"
else
    updates="Packages: $count updates available"
fi

# SECTION 3 — Disk usage
disk_status=""
warning_found=false
while read -r line; do
    percent=$(echo "$line" | awk '{print $1}' | tr -d '%')
    mount=$(echo "$line" | awk '{print $2}')
    if [ "$percent" -gt 70 ]; then
        if [ -z "$disk_status" ]; then
            disk_status="Disk: $mount at $percent%"
        else
            disk_status="$disk_status\nDisk: $mount at $percent%"
        fi
        warning_found=true
    fi
done < <(df -h --output=pcent,target | tail -n +2)

if [ "$warning_found" = false ]; then
    disk_status="Disk: All partitions OK"
fi

# SECTION 4 — Last login
last_info=$(last -2 "$USER" | head -n 2 | tail -n 1)
if [[ -z "$last_info" ]] || [[ "$last_info" == wtmp* ]]; then
    last_login="Last login: No previous session found"
else
    # Format as Last login: <day> <date> <time> on <tty>
    # Typical 'last' output for a session:
    # user     tty1         Sat Mar 28 18:22 - 18:24  (00:01)
    day=$(echo "$last_info" | awk '{print $3}')
    month=$(echo "$last_info" | awk '{print $4}')
    date=$(echo "$last_info" | awk '{print $5}')
    time=$(echo "$last_info" | awk '{print $6}')
    tty=$(echo "$last_info" | awk '{print $2}')
    last_login="Last login: $day $month $date $time on $tty"
fi

# ASSEMBLING AND SENDING
message="$qtile_status\n$updates\n$disk_status\n$last_login"
urgency="normal"
if [[ "$qtile_status" == *"errors detected"* ]] || [ "$warning_found" = true ]; then
    urgency="critical"
fi

notify-send "System Ready" "$message" \
    --urgency=$urgency \
    --timeout=10000 \
    --app-name="Qtile"
