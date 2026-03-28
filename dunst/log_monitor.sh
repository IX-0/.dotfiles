#!/bin/bash

LOGFILE="$HOME/.local/share/qtile/qtile.log"
INTERVAL=300

# Wait until log file exists before starting
while [ ! -f "$LOGFILE" ]; do
    sleep 5
done

last_size=$(wc -c < "$LOGFILE")

while true; do
    sleep $INTERVAL

    current_size=$(wc -c < "$LOGFILE" 2>/dev/null || echo 0)

    if [ "$current_size" -gt "$last_size" ]; then
        new_content=$(tail -c +$((last_size + 1)) "$LOGFILE" 2>/dev/null)
        count=$(echo "$new_content" | grep -cE "ERROR|WARNING")

        if [ "$count" -gt 0 ]; then
            notify-send "Qtile Log Alert" "$count new errors/warnings detected" \
                --urgency=critical \
                --app-name="Qtile"
        fi
    fi

    last_size=$current_size
done
